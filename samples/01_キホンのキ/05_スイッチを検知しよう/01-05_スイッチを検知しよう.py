"""
スイッチを検知するサンプル。
スイッチをオンまたはオフにするとMuエディターのシリアルに文字が表示されます

"""
from adafruit_circuitplayground.express import cpx
import time

# This code is written to be readable versus being Pylint compliant.
# pylint: disable=simplifiable-if-statement

while True:
    if cpx.switch:
        print("ON")
    else:
        print("OFF")
    time.sleep(0.3)
