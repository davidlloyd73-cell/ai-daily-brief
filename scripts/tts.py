#!/usr/bin/env python3
"""
Generate audio/<date>.mp3 from audio/scripts/<date>.txt.

Usage: python3 scripts/tts.py 2026-06-12

Engine preference:
  1. OpenAI TTS      (if OPENAI_API_KEY set)
  2. ElevenLabs      (if ELEVENLABS_API_KEY set)
  3. edge-tts        (free, no key; pip install edge-tts)
"""
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDGE_VOICE = "en-GB-RyanNeural"
EDGE_RATE = "-5%"  # a touch slower than default; calm narration


def openai_tts(text, out):
    body = json.dumps({
        "model": "gpt-4o-mini-tts",
        "voice": "ash",
        "input": text,
        "instructions": "Calm, measured British radio narration. Unhurried, warm, no hype.",
        "response_format": "mp3",
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech", data=body,
        headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        out.write_bytes(r.read())


def elevenlabs_tts(text, out):
    voice_id = os.environ.get("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")  # George (British)
    body = json.dumps({"text": text, "model_id": "eleven_multilingual_v2"}).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_64",
        data=body,
        headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"],
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        out.write_bytes(r.read())


def edge(script_path, out):
    subprocess.run(
        [sys.executable, "-m", "edge_tts", "--voice", EDGE_VOICE, f"--rate={EDGE_RATE}",
         "--file", str(script_path), "--write-media", str(out)],
        check=True, timeout=300)


def main():
    date = sys.argv[1]
    script_path = ROOT / "audio" / "scripts" / f"{date}.txt"
    if not script_path.exists():
        sys.exit(f"No script at {script_path}")
    text = script_path.read_text()
    out = ROOT / "audio" / f"{date}.mp3"
    out.parent.mkdir(parents=True, exist_ok=True)

    for name, fn, key in (("openai", lambda: openai_tts(text, out), "OPENAI_API_KEY"),
                          ("elevenlabs", lambda: elevenlabs_tts(text, out), "ELEVENLABS_API_KEY")):
        if os.environ.get(key):
            try:
                fn()
                print(f"Generated {out.name} via {name}")
                return
            except Exception as e:  # fall through to next engine
                print(f"{name} TTS failed ({e}); falling back")
    edge(script_path, out)
    print(f"Generated {out.name} via edge-tts ({EDGE_VOICE})")


if __name__ == "__main__":
    main()
