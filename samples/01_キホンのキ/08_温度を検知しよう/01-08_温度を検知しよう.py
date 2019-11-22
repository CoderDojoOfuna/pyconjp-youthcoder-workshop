"""
温度を検知するサンプル。
CPXの温度計の横にあるセンサーをつかいます。
センサーを指で触ったりすると温度が変わります。
温度はMuエディターのシリアル、またはプロッターに表示されます
"""
import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Temperature C:", cpx.temperature)
    print("Temperature F:", cpx.temperature * 1.8 + 32)
    print((cpx.temperature, cpx.temperature * 1.8 + 32))
    time.sleep(1)
