"""
タッチして音を鳴らすサンプル。
"dip.wav"ファイルと"rise.wav"をCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A1:
        cpx.play_file("dip.wav")
    if cpx.touch_A7:
        cpx.play_file("rise.wav")
