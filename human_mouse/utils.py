import time


def create_delay(interval: int) -> None:
    """Create a timing delay."""
    time.sleep(interval*0.001)