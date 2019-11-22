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
温度の大きさによって音を変えるサンプル。
CPXの温度計の横にあるセンサーをつかいます。
センサーを指で触ったりすると温度が変わります。
温度はMuエディターのシリアルに表示されます。
"""
from adafruit_circuitplayground.express import cpx
while True:
    print("Temperature C:", cpx.temperature)
    if cpx.temperature > 32.5:
        cpx.play_file("dip.wav")
    elif cpx.temperature > 32:
        cpx.play_file("rise.wav")
