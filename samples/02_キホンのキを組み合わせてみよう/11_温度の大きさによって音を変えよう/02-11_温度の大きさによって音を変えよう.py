"""
温度の大きさによって音を変えるサンプル。
CPXの温度計の横にあるセンサーをつかいます。
センサーを指で触ったりすると温度が変わります。
温度はMuエディターのシリアルに表示されます。
"""
from adafruit_circuitplayground.express import cpx
while True:
    print("Temperature C:", cpx.temperature)
    if cpx.temperature > 32.5:
        cpx.play_file("dip.wav")
    elif cpx.temperature > 32:
        cpx.play_file("rise.wav")
