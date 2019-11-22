"""
タッチして光らせるサンプル。
"""
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    if cpx.touch_A1:
        # A1をタッチした
        # 0と1を光らせる
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
    else:
        # A1からはなれた
        # 0と1を光らせない
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
    if cpx.touch_A7:
        # A7をタッチした
        # 5と6を光らせる
        cpx.pixels[5] = (255, 0, 0)
        cpx.pixels[6] = (0, 255, 0)
    else:
        # A7からはなれた
        # 5と6を光らせない
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
