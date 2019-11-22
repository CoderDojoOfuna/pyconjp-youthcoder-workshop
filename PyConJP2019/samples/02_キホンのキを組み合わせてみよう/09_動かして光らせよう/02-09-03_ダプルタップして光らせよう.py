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
ダブルタップして光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

# ダブルタップを知るための設定
cpx.detect_taps = 2

# ダブルタップしてみよう
while True:
    if cpx.tapped:
        # ダブルタップされた
        # 0と1を光らせる
        cpx.pixels[2] = (255, 0, 0)
        cpx.pixels[3] = (0, 255, 0)
    else:
        # ダブルタップがおわった
        # 0と1を光らせない
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
