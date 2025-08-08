import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        elif axis == "origin":
            self.x = -self.x
            self.y = -self.y
        else:
            print("Invalid axis")


p = Point(1, 2)
p.reflect("x")
print(p.x, p.y)
p.reflect("y")
print(p.x, p.y)
p.reflect("origin")  # set it back to the original point
print(p.x, p.y)

p2 = Point(1, 2)
p2.reflect("z")


############

from datetime import datetime

import pandas as pd


class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        # pd.DataFrame.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        # avoid modifying the original dataFrame when adding the created_at column
        # This pattern is common when you want to add metadata for export/serialization without affecting the original object's state.
        temp = self.copy()
        temp["created_at"] = self.created_at
        return pd.DataFrame.to_csv(temp, *args, **kwargs)
        # we can't use super() here because it would call the to_csv method of the parent class, not the pandas DataFrame class
