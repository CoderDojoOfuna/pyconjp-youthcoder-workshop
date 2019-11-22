"""
光を検知するサンプル
光の大きさがMuエディターのシリアルに文字が表示されます
プロッターにも光の大きさが表示されます
"""
import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Light:", cpx.light)
    print((cpx.light,))
    time.sleep(1)
