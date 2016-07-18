from pysound.wavetable import saw_wave
from pysound.soundfile import write_wav

wave = saw_wave(frequency=400, amplitude=1)
write_wav(source=wave, filename='saw-wave.wav')
