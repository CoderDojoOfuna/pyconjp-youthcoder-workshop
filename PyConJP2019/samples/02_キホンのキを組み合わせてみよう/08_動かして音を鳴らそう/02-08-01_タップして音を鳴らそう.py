"""
タップして音を鳴らすサンプル。
"dip.wav"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 1

while True:
    if cpx.tapped:
        # タップした
        # 音を鳴らす
        cpx.play_file("dip.wav")
