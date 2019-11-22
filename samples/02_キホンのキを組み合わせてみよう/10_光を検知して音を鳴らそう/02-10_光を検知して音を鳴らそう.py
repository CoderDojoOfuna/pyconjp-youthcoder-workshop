"""
光を検知して音を鳴らすサンプル
"dip.wav"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.light > 50:
        cpx.play_file("dip.wav")
