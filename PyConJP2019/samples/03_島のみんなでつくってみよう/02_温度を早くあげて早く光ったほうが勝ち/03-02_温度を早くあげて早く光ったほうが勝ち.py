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
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3

kati = 0
ondo = 0
while True:
    if cpx.switch:
        print("ON")
        ondo = cpx.temperature
        # ネオピクセルは全部光ったかな？
        if ondo < 32:
            cpx.pixels[2] = (0, 0, 255)
            cpx.pixels[7] = (0, 255, 128)
        elif ondo < 32:
            cpx.pixels[1] = (0, 255, 0)
            cpx.pixels[2] = (0, 0, 255)
            cpx.pixels[3] = (255, 255, 0)
            cpx.pixels[6] = (255, 128, 0)
            cpx.pixels[7] = (0, 255, 128)
            cpx.pixels[8] = (128, 0, 255)
        else:
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
            kati = 1
        if kati == 1:
            cpx.play_file("laugh.wav")
    else:
        # ネオピクセルの光はきえたかな？
        ondo = 0
        kati = 0
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[7] = (0, 0, 0)
        cpx.pixels[8] = (0, 0, 0)
        cpx.pixels[9] = (0, 0, 0)
        print("OFF")
