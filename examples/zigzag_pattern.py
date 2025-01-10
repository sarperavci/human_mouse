from human_mouse import MouseController
import time

mouse = MouseController(always_zigzag=True)

print("Moving with zigzag pattern...")
mouse.move(500, 300)
time.sleep(1)

points = [(100, 100), (500, 100), (500, 500), (100, 500)]
for x, y in points:
    print(f"Moving to ({x}, {y})...")
    mouse.move(x, y)
    time.sleep(1) 