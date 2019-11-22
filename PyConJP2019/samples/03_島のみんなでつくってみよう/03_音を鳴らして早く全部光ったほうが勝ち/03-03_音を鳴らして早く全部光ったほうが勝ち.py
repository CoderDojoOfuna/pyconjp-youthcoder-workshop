"""
Copyright 2019 CoderDojo Ofuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
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

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3

# 音のセンサーの設定
mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                       sample_rate=16000, bit_depth=16)

samples = array.array('H', [0] * 160)
mic.record(samples, len(samples))
input_floor = normalized_rms(samples) + 10

# Lower number means more sensitive - more LEDs will light up with less sound.
sensitivity = 500
input_ceiling = input_floor + sensitivity

peak = 0
pika = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    if cpx.switch:
        mic.record(samples, len(samples))
        magnitude = normalized_rms(samples)
        # ネオピクセルは全部光ったかな？
        # 光らない場合はどこがおかしいんだろう？
        if 0 <= magnitude < 100:
            cpx.pixels[0] = (255, 0, 0)
            pika[0] = 1
        elif 100 <= magnitude < 200:
            cpx.pixels[1] = (0, 255, 0)
            pika[1] = 1
        elif 200 <= magnitude < 300:
            cpx.pixels[2] = (0, 0, 255)
            pika[2] = 1
        elif 300 <= magnitude < 400:
            cpx.pixels[3] = (255, 255, 0)
            pika[3] = 1
        elif 400 <= magnitude < 500:
            cpx.pixels[4] = (255, 0, 255)
            pika[4] = 1
        elif 500 <= magnitude < 600:
            cpx.pixels[5] = (0, 255, 255)
            pika[5] = 1
        elif 600 <= magnitude < 700:
            cpx.pixels[6] = (255, 128, 0)
            pika[6] = 1
        elif 700 <= magnitude < 800:
            cpx.pixels[7] = (0, 255, 128)
            pika[7] = 1
        elif 800 <= magnitude < 900:
            cpx.pixels[8] = (128, 0, 255)
            pika[8] = 1
        elif 900000 <= magnitude:
            pika[9] = 1
        kati = 1
        for i in range(10):
            if pika[i] == 0:
                kati = 0
        if kati == 1:
            cpx.play_file("laugh.wav")
    else:
        # スイッチをかえたら全部のネオピクセルの光はきえたかな？
        for i in range(10):
            pika[i] = 0
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
        cpx.pixels[7] = (0, 0, 0)
        cpx.pixels[8] = (0, 0, 0)
        cpx.pixels[9] = (0, 0, 0)
