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
シェイクして光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake(shake_threshold=20):
        # シェイクした
        # 0と1を光らせる
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
    else:
        # シェイクがおわった
        # 0と1を光らせない
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
