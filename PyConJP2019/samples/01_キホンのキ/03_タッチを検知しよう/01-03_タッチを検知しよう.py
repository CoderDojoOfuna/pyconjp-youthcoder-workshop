"""
タッチを検知するサンプル。
Muエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A1:
        print('A1')
    if cpx.touch_A2:
        print('A2')
    if cpx.touch_A3:
        print('A3')
    if cpx.touch_A4:
        print('A4')
    if cpx.touch_A5:
        print('A5')
    if cpx.touch_A6:
        print('A6')
    if cpx.touch_A7:
        print('A7')
