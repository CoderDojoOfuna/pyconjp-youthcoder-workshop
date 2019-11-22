"""
シェイクを検知するサンプル。
シェイクするとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake(shake_threshold=20):
        print("Shake")
