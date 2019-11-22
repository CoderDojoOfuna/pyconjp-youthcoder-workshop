"""
赤外線を送信するサンプル。
"adafruit_irremote.py"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。

CPXのボードの中心にある赤外線送信機を使います。
「赤外線を受信しよう」のサンプルといっしょにうごきます。
Aボタンをおすと、送信機は赤く点灯します。赤外線受信機がうけとると白く光ります。
Bボタンをおすと、送信機は赤く点灯します。赤外線受信機がうけとるとオレンジに光ります。
"""
import time
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx

# Create a 'pulseio' output, to send infrared signals from the IR transmitter
pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)
# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500],
                                            one=[550, 550],
                                            zero=[550, 1700], trail=0)

while True:
    if cpx.button_a:
        cpx.red_led = True
        encoder.transmit(pulseout, [66, 84, 78, 65])
        cpx.red_led = False
        # wait so the receiver can get the full message
        time.sleep(0.2)
    if cpx.button_b:
        cpx.red_led = True
        encoder.transmit(pulseout, [66, 84, 78, 64])
        cpx.red_led = False
        time.sleep(0.2)
