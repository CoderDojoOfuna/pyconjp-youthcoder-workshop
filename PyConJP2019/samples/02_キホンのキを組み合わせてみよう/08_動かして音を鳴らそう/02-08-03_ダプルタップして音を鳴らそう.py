"""
ダブルタップして音を鳴らすサンプル。
"dip.wav"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

# ダブルタップを知るための設定
cpx.detect_taps = 2

# ダブルタップしてみよう
while True:
    if cpx.tapped:
        # ダブルタップされた
        # 音を鳴らす
        cpx.play_file("dip.wav")
