import time


def create_delay(interval: int) -> None:
    """Create a timing delay."""
    for _ in range(interval):
        time.sleep(0.001)