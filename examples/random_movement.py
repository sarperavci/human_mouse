from human_mouse import MouseController

mouse = MouseController(always_zigzag=True)
while True:
    mouse.move_random(speed_factor=2)
    
