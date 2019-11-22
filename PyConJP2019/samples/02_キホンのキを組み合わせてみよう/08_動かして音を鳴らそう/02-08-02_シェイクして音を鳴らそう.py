"""
シェイクして音を鳴らすサンプル。
"rise.wav"をCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake(shake_threshold=20):
        # シェイクした
        # 音を鳴らす
        cpx.play_file("rise.wav")
