from human_mouse import MouseController
import time

mouse = MouseController()

print("Moving to coordinates (500, 300)...")
mouse.move(500, 300)
time.sleep(1)

print("Performing click...")
mouse.perform_click(500, 300)
time.sleep(1)

print("Moving to random position...")
mouse.move_random()
time.sleep(1)

print("Performing double click...")
mouse.perform_double_click(500, 300)