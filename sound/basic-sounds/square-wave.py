from pysound.wavetable import square_wave
from pysound.soundfile import write_wav

wave = square_wave(frequency=400, amplitude=0.9)
write_wav(source=wave, filename='square-wave.wav')
