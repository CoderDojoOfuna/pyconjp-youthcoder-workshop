"""
温度の大きさによって光を変えるサンプル。
CPXの温度計の横にあるセンサーをつかいます。
センサーを指で触ったりすると温度が変わります。
温度はMuエディターのシリアルに表示されます。
"""
from adafruit_circuitplayground.express import cpx
# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3
while True:
    print("Temperature C:", cpx.temperature)
    # (あかいろのこさ、みどりいろのこさ, あおいろのこさ)
    # 0〜255
    if cpx.temperature > 33:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 255)
        cpx.pixels[3] = (255, 255, 0)
    elif cpx.temperature > 32:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 255)
        cpx.pixels[3] = (0, 0, 0)
    elif cpx.temperature > 31:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 255, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
    elif cpx.temperature > 30:
        cpx.pixels[0] = (255, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
    else:
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
