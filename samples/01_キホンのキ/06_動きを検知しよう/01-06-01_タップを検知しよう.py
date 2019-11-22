"""
タップを検知するサンプル。
タップするとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 1

while True:
    if cpx.tapped:
        print("tap")
