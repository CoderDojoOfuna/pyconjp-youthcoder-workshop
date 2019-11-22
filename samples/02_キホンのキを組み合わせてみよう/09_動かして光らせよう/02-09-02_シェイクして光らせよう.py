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
