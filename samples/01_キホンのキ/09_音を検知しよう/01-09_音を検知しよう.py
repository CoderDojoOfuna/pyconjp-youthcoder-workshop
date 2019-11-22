"""
音を検知するサンプル。
CPXの耳の絵の横にあるセンサーを使います。
CPXに話しかけるとMuエディタのプロッターに音の強さが表示されます。
"""
import array
import math
import audiobusio
import board
from adafruit_circuitplayground.express import cpx

def normalized_rms(values):
    minbuf = int(sum(values) / len(values))
    return math.sqrt(sum(float(sample - minbuf) *
                         (sample - minbuf) for sample in values) / len(values))


mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       sample_rate=16000, bit_depth=16)

samples = array.array('H', [0] * 160)
mic.record(samples, len(samples))
input_floor = normalized_rms(samples) + 10

# Lower number means more sensitive - more LEDs will light up with less sound.
sensitivity = 500
input_ceiling = input_floor + sensitivity

peak = 0
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print((magnitude,))
