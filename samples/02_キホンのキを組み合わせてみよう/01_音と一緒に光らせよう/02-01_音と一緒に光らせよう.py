"""
音と一緒に光らせるサンプル。
"dip.wav"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。
"""
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    cpx.pixels[0] = (0, 255, 0)
    cpx.pixels[1] = (0, 0, 255)
    cpx.play_file("dip.wav")
