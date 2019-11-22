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
ダブルタップも検知するサンプル。
シングルタップするとMuエディターのシリアルに文字が表示されます
次にダブルタップするとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

# シングルタップを検知するための設定
cpx.detect_taps = 1
tap_count = 0

# 動かす前にシングルタップしてみよう
while tap_count < 2:
    if cpx.tapped:
        tap_count += 1
        print("single-tap!")

# ダブルタップを検知するための設定に変更
tap_count = 0
cpx.detect_taps = 2

# 動かす前にダブルタップしてみよう
while tap_count < 2:
    if cpx.tapped:
        tap_count += 1
        print("double-tap!")
print("Done.")
