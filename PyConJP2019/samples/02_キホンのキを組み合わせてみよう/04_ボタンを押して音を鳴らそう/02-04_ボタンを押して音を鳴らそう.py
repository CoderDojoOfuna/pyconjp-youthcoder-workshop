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
ボタンを押して光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    if cpx.button_a:
        # Aボタンが押された
        cpx.pixels[0] = (0, 0, 255)
        cpx.pixels[1] = (255, 255, 0)
    else:
        # Aボタンからはなれた
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)

    if cpx.button_b:
        # Bボタンが押された
        cpx.pixels[5] = (255, 0, 255)
        cpx.pixels[6] = (0, 255, 255)
    else:
        # Bボタンからはなれた
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
