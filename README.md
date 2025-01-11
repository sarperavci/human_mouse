# Human Mouse 🖱️

🎯 Human-like mouse movements powered by bezier curves and spline interpolation. Ultra-realistic cursor automation.

[![PyPI version](https://badge.fury.io/py/human-mouse.svg)](https://badge.fury.io/py/human-mouse)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Human Mouse is a sophisticated Python package that generates ultra-realistic mouse movements by implementing advanced mathematical algorithms. It uses a combination of bezier curves and spline interpolation to create smooth, natural-looking cursor trajectories that closely mimic human behavior.

## Installation

```bash
pip install human-mouse
```

## Core Functions & Examples

### Basic Movement

Move cursor to specific coordinates with natural trajectory

```python
mouse = MouseController()
mouse.move(500, 300)  # Move to coordinates
mouse.move(800, 600, speed_factor=0.5)  # Move faster
```

### Random Movement

Move to a random screen position using human-like patterns

```python
mouse.move_random()  # Move to random position
mouse.move_random(speed_factor=2.0)  # Slower random movement
```

### Click Operations
    
Execute a single click

```python
mouse.perform_click(500, 300)  # Move and click
```

Natural double click
```python
mouse.perform_double_click(500, 300)  # Move and double click
```

Right-click action
```python
mouse.perform_context_click(500, 300)  # Move and right click
```

### Movement Patterns

Enable zigzag movements for more natural patterns
```python
zigzag_mouse = MouseController(always_zigzag=True)
zigzag_mouse.move(500, 300)
```

### Virtual Display Support

Linux virtual display support
```python
virtual_mouse = MouseController(is_virtual=True)
virtual_mouse.move(500, 300)
```

## Advanced Features

### Movement Patterns
- Bezier curve interpolation for smooth trajectories
- Spline-based path generation
- Randomized movement variance
- Natural acceleration/deceleration
- Configurable zigzag patterns

### Platform Support
- Windows: Full native support
- macOS: Full native support
- Linux: Supports both native and virtual displays

## Complete Example

```python
from human_mouse import MouseController
import time

# Initialize controller
mouse = MouseController(always_zigzag=True)

# Perform series of actions
mouse.move(500, 300)  # Move to position
time.sleep(0.5)  # Wait briefly
mouse.perform_click()  # Click
time.sleep(0.5)  # Wait briefly
mouse.move_random()  # Move to random position
mouse.perform_double_click()  # Double click
```

## Technical Requirements

- Python 3.10+
- Dependencies:
  - numpy
  - pyautogui
  - scipy
  - python-xlib (optional, for Linux virtual display)

## Contributing

We welcome contributions! Please feel free to submit pull requests.

## License

MIT License - see the LICENSE file for details.

## Support

- Issues: [GitHub Issues](https://github.com/sarperavci/human_mouse/issues)

## Random Move Demo

https://github.com/user-attachments/assets/fa5b900b-01c3-4312-819c-1f558005b54e