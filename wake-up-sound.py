import numpy as np
import sounddevice as sd
import time

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz (must be > 50KHz for 25KHz signal, but most sound cards max out at 44.1KHz)
FREQ = 25000  # Frequency of the tone in Hz
DURATION = 10000  # Duration of the tone in seconds

# Generate the waveform
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
signal = 0.9 * np.sin(2 * np.pi * FREQ * t)  # 0.9 to prevent clipping

print("Starting 25KHz sound generator...")

try:
    while True:
        sd.play(signal, samplerate=SAMPLE_RATE)
        sd.wait()
except KeyboardInterrupt:
    print("Sound generation stopped.")