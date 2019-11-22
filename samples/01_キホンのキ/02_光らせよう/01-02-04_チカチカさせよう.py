"""
ネオピクセルをチカチカ光らせるサンプル。
"""

from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
flag = 0
while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    if flag == 0:
        cpx.pixels[0] = (0, 255, 0)
        cpx.pixels[1] = (0, 0, 255)
        flag = 1
    else:
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        flag = 0
