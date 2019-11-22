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

CPXのボードの中心にある赤外線受信機を使います。
「赤外線を送信しよう」のサンプルといっしょにうごきます。
送信機のAボタンをおして、赤外線をうけとると白く光ります。
送信機のBボタンをおして、赤外線をうけとるとオレンジに光ります。
"""
import time
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx

kazu = 0

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

while True:
    cpx.red_led = True
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        print("IRNECRepeatException")
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted
        print("IRDecodeException")
        continue

    print("Infrared code received: ", received_code)
    if received_code == [66, 84, 78, 65]:
        print("Button A signal")
        cpx.pixels.fill((100, 0, 155))
        cpx.play_file("se_chime14.wav")
        time.sleep(0.2)
        kazu = kazu + 1
        cpx.pixels.fill((0, 0, 0))
    if received_code == [66, 84, 78, 64]:
        print("Button B Signal")
        cpx.pixels.fill((210, 45, 0))
        cpx.play_file("se_chime07.wav")
        time.sleep(0.2)
        cpx.pixels.fill((0, 0, 0))
    if kazu >= 5:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 255)
        cpx.pixels[3] = (255, 255, 0)
        cpx.pixels[4] = (255, 0, 255)
        cpx.pixels[5] = (0, 255, 255)
        cpx.pixels[6] = (255, 128, 0)
        cpx.pixels[7] = (0, 255, 128)
        cpx.pixels[8] = (128, 0, 255)
        cpx.pixels[9] = (64, 128, 255)
    if not cpx.switch:
        kazu = 0
