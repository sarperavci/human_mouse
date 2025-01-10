# Human Mouse

A Python package that generates realistic, human-like mouse movements using spline interpolation and natural movement patterns.

## Features

- Realistic mouse movements using Spline interpolation
- Movement patterns and Random trajectories
- Zigzag and Smooth movements
- Natural consistent clicks, double-clicks, and right-clicks:
- Virtual Display support on Linux based systems
- Adjustable speed & movement pattern easily using

## Installation

```bash
pip install human-mouse
```

## Quick Start

```python
from human_mouse import MouseController

# Create a mouse controller
mouse = MouseController()

# Move to specific coordinates
mouse.move(500, 300)  # Move to x=500, y=300

# Perform clicks
mouse.perform_click()  # Click at current position
mouse.perform_click(200, 300)  # Move and click at position

# Double click
mouse.perform_double_click(300, 400)  # Move and double click

# Right click
mouse.perform_context_click()  # Right click at current position

# Random movement
mouse.move_random()  # Move to random screen position

# Create zigzag-focused movement patterns
zigzag_mouse = MouseController(always_zigzag=True)
zigzag_mouse.move(500, 300)
```

## Advanced Usage

### Virtual Display Support

For Linux systems with virtual displays:

```python
mouse = MouseController(is_virtual=True)
```

### Movement Customization

```python
# Adjust movement speed (lower value = faster)
mouse.move(500, 300, speed_factor=0.5)  # Faster movement
mouse.move(500, 300, speed_factor=2.0)  # Slower movement
```

## Requirements

- Python 3.10+
- numpy
- pyautogui
- scipy
- python-xlib (optional, for Linux virtual display support)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
