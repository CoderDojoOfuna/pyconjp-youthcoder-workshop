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
ボタンを押して音を鳴らすサンプル。
"dip.wav"ファイルと"rise.wav"をCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.play_file("dip.wav")
    if cpx.button_b:
        cpx.play_file("rise.wav")
