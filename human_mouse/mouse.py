from typing import Optional, Tuple
import numpy as np
from numpy.typing import NDArray
import pyautogui
import random
from scipy import interpolate
import platform
from .utils import create_delay

class MouseController:
    """Simulates organic cursor movements using spline interpolation and variance."""
    
    def __init__(self, is_virtual: bool = False, always_zigzag: bool = False):
        self.is_virtual = is_virtual
        self.always_zigzag = always_zigzag
        if self.is_virtual:
            self._enable_virtual_display()
        

    def _enable_virtual_display(self) -> None:
        """Enable virtual display support for Linux systems."""
        if platform.system() != 'Linux':
            return
            
        try:
            import os
            import Xlib.display
            pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ.get('DISPLAY', ':0'))
        except ImportError:
            print("Warning: Virtual display support requires python-xlib package")
        except Exception as e:
            print(f"Warning: Failed to initialize virtual display: {e}")

    def move(self, target_x: int, target_y: int, speed_factor: float = 1.0) -> None:
        """Navigate cursor to target coordinates with organic movement patterns."""
        nodes = self._calculate_path_nodes()
        curve_x, curve_y = self._generate_path_coordinates(nodes, target_x, target_y)
        trajectory = self._compute_trajectory(nodes, curve_x, curve_y)
        interval = self._calculate_movement_interval(curve_x, curve_y, speed_factor)
        self._perform_movement(trajectory, interval)
    
    def move_random(self, speed_factor: float = 1.0) -> None:
        """Navigate cursor to random coordinates with organic movement patterns."""
         
        target_x = random.randint(0, pyautogui.size()[0])
        target_y = random.randint(0, pyautogui.size()[1])
        self.move(target_x, target_y, speed_factor)

    def _calculate_path_nodes(self) -> int:
        base = random.randint(2, 7)
        ceiling = random.randint(10, 15)
        return random.randint(base, ceiling)

    def _generate_path_coordinates(self, nodes: int, target_x: int, target_y: int) -> Tuple[NDArray, NDArray]:
        start_x, start_y = pyautogui.position()
        distance = ((target_x - start_x)**2 + (target_y - start_y)**2)**0.5
        
        if random.random() < 0.75 or self.always_zigzag:
            return self._generate_zigzag_path(nodes, start_x, start_y, target_x, target_y, distance)
        
        base_x, base_y = self._create_base_coordinates(nodes, start_x, start_y, target_x, target_y)
        variance = random.randint(7, 12)
        return self._apply_coordinate_variance(variance, nodes, base_x, base_y)

    def _generate_zigzag_path(self, nodes: int, start_x: int, start_y: int, 
                             target_x: int, target_y: int, distance: float) -> Tuple[NDArray, NDArray]:
        nodes = max(2, nodes)
        
        path_x = np.linspace(start_x, target_x, nodes)
        path_y = np.linspace(start_y, target_y, nodes)
        
        variance = min(distance * 0.15, 100)
        
        return self._apply_coordinate_variance(variance, nodes, path_x, path_y)

    def _create_base_coordinates(self, nodes: int, x1: int, y1: int, x2: int, y2: int) -> Tuple[NDArray, NDArray]:
        coord_x = np.linspace(x1, x2, num=nodes, dtype='int')
        coord_y = np.linspace(y1, y2, num=nodes, dtype='int')
        return coord_x, coord_y

    def _apply_coordinate_variance(self, variance: float, num_points: int, 
                                 path_x: NDArray, path_y: NDArray) -> Tuple[NDArray, NDArray]:
        if num_points < 2:
            return np.array([path_x[0], path_x[-1]]), np.array([path_y[0], path_y[-1]])
        
        offset_x = np.random.normal(0, variance, num_points)
        offset_y = np.random.normal(0, variance, num_points)
        
        offset_x[0] = offset_y[0] = offset_x[-1] = offset_y[-1] = 0
        
        return path_x + offset_x, path_y + offset_y

    def _compute_trajectory(self, nodes: int, x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
        unique_mask = np.ones(len(x), dtype=bool)
        for i in range(1, len(x)):
            if x[i] == x[i-1] and y[i] == y[i-1]:
                unique_mask[i] = False
        x = x[unique_mask]
        y = y[unique_mask]
        
        if len(x) < 4:
            t_points = np.linspace(0, 1, num=max(pyautogui.size()))
            x_interp = np.interp(t_points, np.linspace(0, 1, len(x)), x)
            y_interp = np.interp(t_points, np.linspace(0, 1, len(y)), y)
            return x_interp, y_interp
        
        try:
            curve_degree = min(3, len(x) - 1)
            spline_params, _ = interpolate.splprep([x, y], k=curve_degree, s=0)
            t_points = np.linspace(0, 1, num=max(pyautogui.size()))
            return interpolate.splev(t_points, spline_params)
        except ValueError:
            t_points = np.linspace(0, 1, num=max(pyautogui.size()))
            x_interp = np.interp(t_points, np.linspace(0, 1, len(x)), x)
            y_interp = np.interp(t_points, np.linspace(0, 1, len(y)), y)
            return x_interp, y_interp

    def _calculate_movement_interval(self, x_coords: NDArray, y_coords: NDArray, speed_factor: float) -> int:
        delta_x = ((x_coords[0]-x_coords[-1])**2)**0.5
        delta_y = ((y_coords[0]-y_coords[-1])**2)**0.5
        distance = delta_x + delta_y
        
        is_zigzag = len(x_coords) < 10  
        
        exponent = round(random.uniform(1.1,1.75), 5)
        adjustment = round(random.uniform(1.1,1.75), 5)
        
        interval = int((((distance)**exponent)/adjustment)*speed_factor)
        
        if is_zigzag:
            interval = interval // 10
            
        return interval

    def _perform_movement(self, trajectory: Tuple[NDArray, NDArray], interval: int) -> None:
        for coords in zip(*(axis.astype(int) for axis in trajectory)):
            pos_x = int(coords[0])
            pos_y = int(coords[1])
            pyautogui.platformModule._moveTo(pos_x, pos_y)
            create_delay(interval)

    def perform_click(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """Execute single click at specified or current position."""
        self._prepare_click_position(x, y)
        pyautogui.click()

    def perform_double_click(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """Execute double click with randomized interval."""
        self._prepare_click_position(x, y)
        delay = random.randint(1, 499)/1000
        pyautogui.click(clicks=2, interval=delay)

    def perform_context_click(self, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """Execute right-click at specified or current position."""
        self._prepare_click_position(x, y)
        pyautogui.click(button='right')

    def _prepare_click_position(self, x: Optional[int], y: Optional[int]) -> None:
        current_x, current_y = pyautogui.position()
        if x is None and y is None:
            self.move(current_x, current_y)
        elif x is None:
            self.move(current_x, y)
        elif y is None:
            self.move(x, current_y)
        else:
            self.move(x, y)