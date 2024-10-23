import time
import board
import neopixel
import analogio
import simpleio

# Initialize NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Initialize Light Sensor
light = analogio.AnalogIn(board.LIGHT)

# Store start time
start_time = time.monotonic()

def get_elapsed_time():
    global start_time
    elapsed_seconds = time.monotonic() - start_time

    # Reset timer every 24 hours (86400 seconds)
    if elapsed_seconds >= 86400:
        start_time = time.monotonic()  # Reset start time
        elapsed_seconds = 0  # Reset elapsed time

    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = int(elapsed_seconds % 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"  # Format as HH:MM:SS

while True:
    # Read light sensor value
    light_value = light.value

    # Get the elapsed time as a formatted string
    timestamp = get_elapsed_time()

    # Print light value with timestamp for Plotter
    print(f"{timestamp},{light_value}")

    # Map the light value to pixel position
    peak = simpleio.map_range(light_value, 2000, 62000, 0, 9)

    # Update NeoPixels
    for i in range(10):
        if i <= peak:
            pixels[i] = (0, 255, 0)
        else:
            pixels[i] = (0, 0, 0)
    pixels.show()

    # Delay for stability
    time.sleep(60)  # Delay to reduce output frequency

