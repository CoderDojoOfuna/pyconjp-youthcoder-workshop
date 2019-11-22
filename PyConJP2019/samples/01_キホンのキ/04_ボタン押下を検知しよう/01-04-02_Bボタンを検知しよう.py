"""
Bボタンがおされたことも検知するサンプル。
AボタンまたはBボタンがおされるとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        print("A")
    if cpx.button_b:
        print("B")
