import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from config import BASE_GREEN, STEP, MIN_GREEN

def next_times(right: int, bottom: int) -> tuple[int, int]:
    diff = right - bottom
    return max(MIN_GREEN, BASE_GREEN + diff * STEP), max(MIN_GREEN, BASE_GREEN - diff * STEP)