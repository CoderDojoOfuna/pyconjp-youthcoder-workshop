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
Aボタンがおされたことを検知するサンプル。
AボタンがおされるとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        print("A")
