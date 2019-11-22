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
