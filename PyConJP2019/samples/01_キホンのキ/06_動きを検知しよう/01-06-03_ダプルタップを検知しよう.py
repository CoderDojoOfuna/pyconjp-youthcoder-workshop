"""
ダブルタップも検知するサンプル。
シングルタップするとMuエディターのシリアルに文字が表示されます
次にダブルタップするとMuエディターのシリアルに文字が表示されます
"""
from adafruit_circuitplayground.express import cpx

# シングルタップを検知するための設定
cpx.detect_taps = 1
tap_count = 0

# 動かす前にシングルタップしてみよう
while tap_count < 2:
    if cpx.tapped:
        tap_count += 1
        print("single-tap!")

# ダブルタップを検知するための設定に変更
tap_count = 0
cpx.detect_taps = 2

# 動かす前にダブルタップしてみよう
while tap_count < 2:
    if cpx.tapped:
        tap_count += 1
        print("double-tap!")
print("Done.")
