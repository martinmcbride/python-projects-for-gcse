from pysound.wavetable import sine_wave
from pysound.soundfile import write_wav

wave = sine_wave(frequency=400, amplitude=1)
write_wav(source=wave, filename='sine-wave.wav')
