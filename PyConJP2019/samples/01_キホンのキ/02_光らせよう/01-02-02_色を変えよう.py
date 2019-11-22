"""
0番目のネオピクセルを光らせるサンプル。
みどりいろに光ります。
"""
from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3

while True:
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
#    cpx.pixels[0] = (255, 0, 0)
    cpx.pixels[0] = (0, 255, 0)
