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
"""
赤外線を送信するサンプル。
"adafruit_irremote.py"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。

CPXのボードの中心にある赤外線送信機を使います。
「赤外線を受信しよう」のサンプルといっしょにうごきます。
Aボタンをおすと、送信機は赤く点灯します。赤外線受信機がうけとると白く光ります。
Bボタンをおすと、送信機は赤く点灯します。赤外線受信機がうけとるとオレンジに光ります。
"""
import time
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx

# Create a 'pulseio' output, to send infrared signals from the IR transmitter
pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)
# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500],
                                            one=[550, 550],
                                            zero=[550, 1700], trail=0)
# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3

while True:
    if cpx.button_a:
        # 2～4も光らせてみよう
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (255, 0, 0)
        cpx.red_led = True
        # 好きな音にかえてみよう
        cpx.play_file("dip.wav")
        encoder.transmit(pulseout, [66, 84, 78, 65])
        cpx.red_led = False
        # 送信がおわったら光をけしてみよう
        # wait so the receiver can get the full message
        time.sleep(0.2)
    if cpx.button_b:
        # 6～8も光らせてみよう
        cpx.pixels[5] = (255, 0, 0)
        cpx.pixels[9] = (255, 0, 0)
        cpx.red_led = True
        # 好きな音にかえてみよう
        cpx.play_file("rise.wav")
        encoder.transmit(pulseout, [66, 84, 78, 64])
        cpx.red_led = False
        # 送信がおわったら光をけしてみよう
        time.sleep(0.2)
