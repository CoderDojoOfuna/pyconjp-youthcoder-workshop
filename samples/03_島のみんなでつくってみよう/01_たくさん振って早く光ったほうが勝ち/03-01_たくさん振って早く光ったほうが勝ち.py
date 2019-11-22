from adafruit_circuitplayground.express import cpx

# 光のつよさ
# 0.0 〜1.0
cpx.pixels.brightness = 0.3

kazu = 0
shake = 0
while True:
    if cpx.switch:
        print("ON")
        if cpx.shake(shake_threshold=20):
            # ネオピクセルは全部光ったかな？
            shake = shake + 1
            if shake == 0:
                print("0")
            elif shake == 1:
                cpx.pixels[0] = (255, 0, 0)
            elif shake == 2:
                cpx.pixels[0] = (0, 255, 0)
            elif shake == 3:
                cpx.pixels[2] = (0, 0, 255)
            elif shake == 4:
                cpx.pixels[3] = (255, 255, 0)
            elif shake == 5:
                cpx.pixels[4] = (255, 0, 255)
            elif shake == 6:
                cpx.pixels[5] = (0, 255, 255)
            elif shake == 7:
                cpx.pixels[6] = (255, 128, 0)
            elif shake == 8:
                cpx.pixels[7] = (0, 255, 128)
            elif shake == 9:
                cpx.pixels[8] = (128, 0, 255)
            else:
                cpx.pixels[9] = (64, 128, 255)
        if shake >= 10:
            cpx.play_file("laugh.wav")
    else:
        # ネオピクセルの光は全部消えたかな？
        kazu = 0
        shake = 0
        cpx.pixels[0] = (0, 0, 0)
        cpx.pixels[1] = (0, 0, 0)
        cpx.pixels[2] = (0, 0, 0)
        cpx.pixels[3] = (0, 0, 0)
        cpx.pixels[4] = (0, 0, 0)
        cpx.pixels[5] = (0, 0, 0)
        cpx.pixels[6] = (0, 0, 0)
        cpx.pixels[7] = (0, 0, 0)
        cpx.pixels[8] = (0, 0, 0)
        cpx.pixels[8] = (0, 0, 0)
        print("OFF")
