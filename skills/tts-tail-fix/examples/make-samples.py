"""make-samples.py - write two tiny practice clips (synthetic noise, NOT speech) into the folder you pass.

  python make-samples.py practice

chopped.wav   noise that stops abruptly while still loud (what a chopped TTS ending looks like)
sentinel.wav  the same noise, a 0.3 s pause, then a short extra burst (stands in for the throw-away sentinel word)
Needs: pip install numpy soundfile
"""
import os
import sys

import numpy as np
import soundfile as sf

out = sys.argv[1] if len(sys.argv) > 1 else "practice"
os.makedirs(out, exist_ok=True)
sr = 24000
rng = np.random.default_rng(0)


def burst(seconds):
    t = np.arange(int(seconds * sr)) / sr
    return 0.08 * rng.standard_normal(len(t)) * (0.6 + 0.4 * np.sin(2 * np.pi * 4 * t))


sf.write(os.path.join(out, "chopped.wav"),
         np.concatenate([np.zeros(2400), burst(1.5), np.zeros(4800)]), sr)
sf.write(os.path.join(out, "sentinel.wav"),
         np.concatenate([np.zeros(2400), burst(1.5), np.zeros(int(0.3 * sr)), burst(0.25), np.zeros(2400)]), sr)
print(f"wrote {out}/chopped.wav and {out}/sentinel.wav")