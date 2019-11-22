"""
スイッチを変えて音を鳴らす。
"dip.wav"ファイルと"rise.wav"をCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.switch:
        cpx.play_file("dip.wav")
    else:
        cpx.play_file("rise.wav")
