"""
ボタンを押して光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    if cpx.button_a:
        # Aボタンが押された
        cpx.pixels[0] = (0, 0, 255)
        cpx.pixels[1] = (255, 255, 0)
    else:
        # Aボタンからはなれた
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)

    if cpx.button_b:
        # Bボタンが押された
        cpx.pixels[5] = (255, 0, 255)
        cpx.pixels[6] = (0, 255, 255)
    else:
        # Bボタンからはなれた
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
