import numpy as np
import sounddevice as sd

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz (must be > 50KHz for 25KHz signal, but most sound cards max out at 44.1KHz)
FREQ = 25000  # 25kHz

# Generate one second of the waveform
DURATION = 1
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
signal = 0.9 * np.sin(2 * np.pi * FREQ * t).astype(np.float32)  # Float32 is enough

print("Starting continuous 25kHz tone... Press Ctrl+C to stop.")

try:
    sd.play(signal, samplerate=SAMPLE_RATE, loop=True)
    input()  # Keep the script alive until Enter is pressed or interrupted
except KeyboardInterrupt:
    print("Stopping...")
finally:
    sd.stop()