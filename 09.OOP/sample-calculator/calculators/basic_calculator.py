import numpy as np


class BasicCalculator:
    def add(self, x: float, y: float) -> float:
        return np.add(x, y)

    def subtract(self, x: float, y: float) -> float:
        return np.subtract(x, y)

    def multiply(self, x: float, y: float) -> float:
        return np.multiply(x, y)

    def divide(self, x: float, y: float) -> float:
        return np.divide(x, y)

    def power(self, x: float, y: float) -> float:
        return np.power(x, y)
