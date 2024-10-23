import time
import board
import neopixel
import analogio
import simpleio

# Initialize NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()
light = analogio.AnalogIn(board.LIGHT)
start_time = time.monotonic()

def get_elapsed_time():
    global start_time
    elapsed_seconds = time.monotonic() - start_time

    if elapsed_seconds >= 86400:
        start_time = time.monotonic()  
        elapsed_seconds = 0 

    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}" 

while True:
    
    light_value = light.value
    timestamp = get_elapsed_time()
    print(f"{timestamp},{light_value}")
    peak = simpleio.map_range(light_value, 2000, 62000, 0, 9)

    for i in range(10):
        if i <= peak:
            pixels[i] = (0, 255, 0)
        else:
            pixels[i] = (0, 0, 0)
    pixels.show()

    # Delay for stability
    time.sleep(60)  # Delay to reduce output frequency

