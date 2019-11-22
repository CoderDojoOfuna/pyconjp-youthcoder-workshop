"""
赤外線を送信するサンプル。
"adafruit_irremote.py"ファイルをCIRCUITPYフォルダにドラッグ&ドロップしましょう。

CPXのボードの中心にある赤外線受信機を使います。
「赤外線を送信しよう」のサンプルといっしょにうごきます。
送信機のAボタンをおして、赤外線をうけとると白く光ります。
送信機のBボタンをおして、赤外線をうけとるとオレンジに光ります。
"""
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

while True:
    cpx.red_led = True
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        print("IRNECRepeatException")
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted
        print("IRDecodeException")
        continue

    print("Infrared code received: ", received_code)
    if received_code == [66, 84, 78, 65]:
        print("Button A signal")
        cpx.pixels.fill((100, 0, 155))
    if received_code == [66, 84, 78, 64]:
        print("Button B Signal")
        cpx.pixels.fill((210, 45, 0))
