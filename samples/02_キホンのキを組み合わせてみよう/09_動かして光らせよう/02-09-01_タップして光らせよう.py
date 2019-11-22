"""
タップして光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 1

while True:
    if cpx.tapped:
        # タップした
        # 0と1を光らせる
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
    else:
        # タップがおわった
        # 0と1を光らせない
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
