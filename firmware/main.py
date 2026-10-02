from microbit import *

PROJECT_ID = 1459
THRESHOLD = 640
confirmations = 0

while True:
    reading = pin0.read_analog()
    active = reading >= THRESHOLD
    confirmations = min(confirmations + 1, 5) if active else 0
    output = confirmations >= 5
    pin1.write_digital(1 if output else 0)
    display.show(Image.YES if output else Image.NO)
    print((PROJECT_ID, reading, int(output)))
    sleep(500)
