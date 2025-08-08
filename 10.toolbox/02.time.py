# we can specify the time together with the date
# there is a expanded format, and we can .replace() to change a property
# we can access the properties with .year, .month, .day, .hour, .minute, .second

# Time differences between datetime objects return timedelta objects
# Use .total_seconds() to get duration in seconds as a float
# datetime objects are comparable and support min()/max() operations
# datetime arithmetic (subtraction) returns a timedelta object

from datetime import datetime

dt = datetime(2022, 1, 1, 15, 23, 25)
# you can also use expanded format
dt2 = datetime(year=2022, month=1, day=1, hour=15, minute=23, second=25)
print(dt.isoformat())
print(dt2.isoformat())

# Replace the year with 1917
dt_old = dt.replace(year=1917)

print(dt_old)


#######
onebike_datetimes = [
    {
        "start": datetime(2017, 10, 1, 15, 23, 25),
        "end": datetime(2017, 10, 1, 15, 26, 26),
    },
    {
        "start": datetime(2017, 10, 1, 15, 42, 57),
        "end": datetime(2017, 10, 1, 17, 49, 59),
    },
    {
        "start": datetime(2017, 10, 2, 6, 37, 10),
        "end": datetime(2017, 10, 2, 6, 42, 53),
    },
    {"start": datetime(2017, 10, 2, 8, 56, 45), "end": datetime(2017, 10, 2, 9, 18, 3)},
    {
        "start": datetime(2017, 10, 2, 18, 23, 48),
        "end": datetime(2017, 10, 2, 18, 45, 5),
    },
    {
        "start": datetime(2017, 10, 2, 18, 48, 8),
        "end": datetime(2017, 10, 2, 19, 10, 54),
    },
    {
        "start": datetime(2017, 10, 2, 19, 18, 10),
        "end": datetime(2017, 10, 2, 19, 31, 45),
    },
    {
        "start": datetime(2017, 10, 2, 19, 37, 32),
        "end": datetime(2017, 10, 2, 19, 46, 37),
    },
    {
        "start": datetime(2017, 10, 3, 8, 24, 16),
        "end": datetime(2017, 10, 3, 8, 32, 27),
    },
    {
        "start": datetime(2017, 10, 3, 18, 17, 7),
        "end": datetime(2017, 10, 3, 18, 27, 46),
    },
    {
        "start": datetime(2017, 10, 3, 19, 24, 10),
        "end": datetime(2017, 10, 3, 19, 52, 8),
    },
    {
        "start": datetime(2017, 10, 3, 20, 17, 6),
        "end": datetime(2017, 10, 3, 20, 23, 52),
    },
    {
        "start": datetime(2017, 10, 3, 20, 45, 21),
        "end": datetime(2017, 10, 3, 20, 57, 10),
    },
    {"start": datetime(2017, 10, 4, 7, 4, 57), "end": datetime(2017, 10, 4, 7, 13, 31)},
    {
        "start": datetime(2017, 10, 4, 7, 13, 42),
        "end": datetime(2017, 10, 4, 7, 21, 54),
    },
    {"start": datetime(2017, 10, 4, 14, 22, 12), "end": datetime(2017, 10, 4, 14, 50)},
    {
        "start": datetime(2017, 10, 4, 15, 7, 27),
        "end": datetime(2017, 10, 4, 15, 44, 49),
    },
    {
        "start": datetime(2017, 10, 4, 15, 46, 41),
        "end": datetime(2017, 10, 4, 16, 32, 33),
    },
    {
        "start": datetime(2017, 10, 4, 16, 34, 44),
        "end": datetime(2017, 10, 4, 16, 46, 59),
    },
    {
        "start": datetime(2017, 10, 4, 17, 26, 6),
        "end": datetime(2017, 10, 4, 17, 31, 36),
    },
    {
        "start": datetime(2017, 10, 4, 17, 42, 3),
        "end": datetime(2017, 10, 4, 17, 50, 41),
    },
    {"start": datetime(2017, 10, 5, 7, 49, 2), "end": datetime(2017, 10, 5, 8, 12, 55)},
    {
        "start": datetime(2017, 10, 5, 8, 26, 21),
        "end": datetime(2017, 10, 5, 8, 29, 45),
    },
    {
        "start": datetime(2017, 10, 5, 8, 33, 27),
        "end": datetime(2017, 10, 5, 8, 38, 31),
    },
    {
        "start": datetime(2017, 10, 5, 16, 35, 35),
        "end": datetime(2017, 10, 5, 16, 51, 52),
    },
    {
        "start": datetime(2017, 10, 5, 17, 53, 31),
        "end": datetime(2017, 10, 5, 18, 16, 50),
    },
    {"start": datetime(2017, 10, 6, 8, 17, 17), "end": datetime(2017, 10, 6, 8, 38, 1)},
    {
        "start": datetime(2017, 10, 6, 11, 39, 40),
        "end": datetime(2017, 10, 6, 11, 50, 38),
    },
    {
        "start": datetime(2017, 10, 6, 12, 59, 54),
        "end": datetime(2017, 10, 6, 13, 13, 14),
    },
    {
        "start": datetime(2017, 10, 6, 13, 43, 5),
        "end": datetime(2017, 10, 6, 14, 14, 56),
    },
    {
        "start": datetime(2017, 10, 6, 14, 28, 15),
        "end": datetime(2017, 10, 6, 15, 9, 26),
    },
    {
        "start": datetime(2017, 10, 6, 15, 50, 10),
        "end": datetime(2017, 10, 6, 16, 12, 34),
    },
    {
        "start": datetime(2017, 10, 6, 16, 32, 16),
        "end": datetime(2017, 10, 6, 16, 39, 31),
    },
    {
        "start": datetime(2017, 10, 6, 16, 44, 8),
        "end": datetime(2017, 10, 6, 16, 48, 39),
    },
    {
        "start": datetime(2017, 10, 6, 16, 53, 43),
        "end": datetime(2017, 10, 6, 17, 9, 3),
    },
    {
        "start": datetime(2017, 10, 7, 11, 38, 55),
        "end": datetime(2017, 10, 7, 11, 53, 6),
    },
    {"start": datetime(2017, 10, 7, 14, 3, 36), "end": datetime(2017, 10, 7, 14, 7, 5)},
    {
        "start": datetime(2017, 10, 7, 14, 20, 3),
        "end": datetime(2017, 10, 7, 14, 27, 36),
    },
    {
        "start": datetime(2017, 10, 7, 14, 30, 50),
        "end": datetime(2017, 10, 7, 14, 44, 51),
    },
    {
        "start": datetime(2017, 10, 8, 0, 28, 26),
        "end": datetime(2017, 10, 8, 0, 30, 48),
    },
    {
        "start": datetime(2017, 10, 8, 11, 16, 21),
        "end": datetime(2017, 10, 8, 11, 33, 24),
    },
    {
        "start": datetime(2017, 10, 8, 12, 37, 3),
        "end": datetime(2017, 10, 8, 13, 1, 29),
    },
    {
        "start": datetime(2017, 10, 8, 13, 30, 37),
        "end": datetime(2017, 10, 8, 13, 57, 53),
    },
    {
        "start": datetime(2017, 10, 8, 14, 16, 40),
        "end": datetime(2017, 10, 8, 15, 7, 19),
    },
    {
        "start": datetime(2017, 10, 8, 15, 23, 50),
        "end": datetime(2017, 10, 8, 15, 50, 1),
    },
    {
        "start": datetime(2017, 10, 8, 15, 54, 12),
        "end": datetime(2017, 10, 8, 16, 17, 42),
    },
    {
        "start": datetime(2017, 10, 8, 16, 28, 52),
        "end": datetime(2017, 10, 8, 16, 35, 18),
    },
    {
        "start": datetime(2017, 10, 8, 23, 8, 14),
        "end": datetime(2017, 10, 8, 23, 33, 41),
    },
    {
        "start": datetime(2017, 10, 8, 23, 34, 49),
        "end": datetime(2017, 10, 8, 23, 45, 11),
    },
    {
        "start": datetime(2017, 10, 8, 23, 46, 47),
        "end": datetime(2017, 10, 9, 0, 10, 57),
    },
    {
        "start": datetime(2017, 10, 9, 0, 12, 58),
        "end": datetime(2017, 10, 9, 0, 36, 40),
    },
    {"start": datetime(2017, 10, 9, 0, 37, 2), "end": datetime(2017, 10, 9, 0, 53, 33)},
    {
        "start": datetime(2017, 10, 9, 1, 23, 29),
        "end": datetime(2017, 10, 9, 1, 48, 13),
    },
    {
        "start": datetime(2017, 10, 9, 1, 49, 25),
        "end": datetime(2017, 10, 9, 2, 13, 35),
    },
    {
        "start": datetime(2017, 10, 9, 2, 14, 11),
        "end": datetime(2017, 10, 9, 2, 29, 40),
    },
    {
        "start": datetime(2017, 10, 9, 13, 4, 32),
        "end": datetime(2017, 10, 9, 13, 13, 25),
    },
    {
        "start": datetime(2017, 10, 9, 14, 30, 10),
        "end": datetime(2017, 10, 9, 14, 38, 55),
    },
    {
        "start": datetime(2017, 10, 9, 15, 6, 47),
        "end": datetime(2017, 10, 9, 15, 11, 30),
    },
    {
        "start": datetime(2017, 10, 9, 16, 43, 25),
        "end": datetime(2017, 10, 9, 16, 45, 38),
    },
    {
        "start": datetime(2017, 10, 10, 15, 32, 58),
        "end": datetime(2017, 10, 10, 15, 51, 24),
    },
    {
        "start": datetime(2017, 10, 10, 16, 47, 55),
        "end": datetime(2017, 10, 10, 17, 3, 47),
    },
    {
        "start": datetime(2017, 10, 10, 17, 51, 5),
        "end": datetime(2017, 10, 10, 18, 0, 18),
    },
    {
        "start": datetime(2017, 10, 10, 18, 8, 12),
        "end": datetime(2017, 10, 10, 18, 19, 11),
    },
    {
        "start": datetime(2017, 10, 10, 19, 9, 35),
        "end": datetime(2017, 10, 10, 19, 14, 32),
    },
    {
        "start": datetime(2017, 10, 10, 19, 17, 11),
        "end": datetime(2017, 10, 10, 19, 23, 8),
    },
    {
        "start": datetime(2017, 10, 10, 19, 28, 11),
        "end": datetime(2017, 10, 10, 19, 44, 40),
    },
    {
        "start": datetime(2017, 10, 10, 19, 55, 35),
        "end": datetime(2017, 10, 10, 20, 11, 54),
    },
    {
        "start": datetime(2017, 10, 10, 22, 20, 43),
        "end": datetime(2017, 10, 10, 22, 33, 23),
    },
    {
        "start": datetime(2017, 10, 11, 4, 40, 52),
        "end": datetime(2017, 10, 11, 4, 59, 22),
    },
    {
        "start": datetime(2017, 10, 11, 6, 28, 58),
        "end": datetime(2017, 10, 11, 6, 40, 13),
    },
    {
        "start": datetime(2017, 10, 11, 16, 41, 7),
        "end": datetime(2017, 10, 11, 17, 1, 14),
    },
    {
        "start": datetime(2017, 10, 12, 8, 8, 30),
        "end": datetime(2017, 10, 12, 8, 35, 3),
    },
    {
        "start": datetime(2017, 10, 12, 8, 47, 2),
        "end": datetime(2017, 10, 12, 8, 59, 50),
    },
    {
        "start": datetime(2017, 10, 12, 13, 13, 39),
        "end": datetime(2017, 10, 12, 13, 37, 45),
    },
    {
        "start": datetime(2017, 10, 12, 13, 40, 12),
        "end": datetime(2017, 10, 12, 13, 48, 17),
    },
    {
        "start": datetime(2017, 10, 12, 13, 49, 56),
        "end": datetime(2017, 10, 12, 13, 53, 16),
    },
    {
        "start": datetime(2017, 10, 12, 14, 33, 18),
        "end": datetime(2017, 10, 12, 14, 39, 57),
    },
    {
        "start": datetime(2017, 10, 13, 15, 55, 39),
        "end": datetime(2017, 10, 13, 15, 59, 41),
    },
    {
        "start": datetime(2017, 10, 17, 17, 58, 48),
        "end": datetime(2017, 10, 17, 18, 1, 38),
    },
    {
        "start": datetime(2017, 10, 19, 20, 21, 45),
        "end": datetime(2017, 10, 19, 20, 29, 15),
    },
    {
        "start": datetime(2017, 10, 19, 21, 11, 39),
        "end": datetime(2017, 10, 19, 21, 29, 37),
    },
    {
        "start": datetime(2017, 10, 19, 21, 30, 1),
        "end": datetime(2017, 10, 19, 21, 47, 23),
    },
    {
        "start": datetime(2017, 10, 19, 21, 47, 34),
        "end": datetime(2017, 10, 19, 21, 57, 7),
    },
    {
        "start": datetime(2017, 10, 19, 21, 57, 24),
        "end": datetime(2017, 10, 19, 22, 9, 52),
    },
    {
        "start": datetime(2017, 10, 21, 12, 24, 9),
        "end": datetime(2017, 10, 21, 12, 36, 24),
    },
    {
        "start": datetime(2017, 10, 21, 12, 36, 37),
        "end": datetime(2017, 10, 21, 12, 42, 13),
    },
    {
        "start": datetime(2017, 10, 21, 13, 47, 43),
        "end": datetime(2017, 10, 22, 11, 9, 36),
    },
    {
        "start": datetime(2017, 10, 22, 13, 28, 53),
        "end": datetime(2017, 10, 22, 13, 31, 44),
    },
    {
        "start": datetime(2017, 10, 22, 13, 47, 5),
        "end": datetime(2017, 10, 22, 13, 56, 33),
    },
    {
        "start": datetime(2017, 10, 22, 14, 26, 41),
        "end": datetime(2017, 10, 22, 14, 32, 39),
    },
    {
        "start": datetime(2017, 10, 22, 14, 54, 41),
        "end": datetime(2017, 10, 22, 15, 9, 58),
    },
    {
        "start": datetime(2017, 10, 22, 16, 40, 29),
        "end": datetime(2017, 10, 22, 16, 51, 40),
    },
    {
        "start": datetime(2017, 10, 22, 17, 58, 46),
        "end": datetime(2017, 10, 22, 18, 28, 37),
    },
    {
        "start": datetime(2017, 10, 22, 18, 45, 16),
        "end": datetime(2017, 10, 22, 18, 50, 34),
    },
    {
        "start": datetime(2017, 10, 22, 18, 56, 22),
        "end": datetime(2017, 10, 22, 19, 11, 10),
    },
    {
        "start": datetime(2017, 10, 23, 10, 14, 8),
        "end": datetime(2017, 10, 23, 10, 35, 32),
    },
    {
        "start": datetime(2017, 10, 23, 11, 29, 36),
        "end": datetime(2017, 10, 23, 14, 38, 34),
    },
    {
        "start": datetime(2017, 10, 23, 15, 4, 52),
        "end": datetime(2017, 10, 23, 15, 32, 58),
    },
    {
        "start": datetime(2017, 10, 23, 15, 33, 48),
        "end": datetime(2017, 10, 23, 17, 6, 47),
    },
    {
        "start": datetime(2017, 10, 23, 17, 13, 16),
        "end": datetime(2017, 10, 23, 19, 31, 26),
    },
    {
        "start": datetime(2017, 10, 23, 19, 55, 3),
        "end": datetime(2017, 10, 23, 20, 25, 53),
    },
    {
        "start": datetime(2017, 10, 23, 21, 47, 54),
        "end": datetime(2017, 10, 23, 22, 18, 4),
    },
    {
        "start": datetime(2017, 10, 23, 22, 34, 12),
        "end": datetime(2017, 10, 23, 22, 48, 42),
    },
    {
        "start": datetime(2017, 10, 24, 6, 55, 1),
        "end": datetime(2017, 10, 24, 7, 2, 17),
    },
    {
        "start": datetime(2017, 10, 24, 14, 56, 7),
        "end": datetime(2017, 10, 24, 15, 3, 16),
    },
    {
        "start": datetime(2017, 10, 24, 15, 51, 36),
        "end": datetime(2017, 10, 24, 15, 59, 50),
    },
    {
        "start": datetime(2017, 10, 24, 16, 31, 10),
        "end": datetime(2017, 10, 24, 16, 55, 9),
    },
    {
        "start": datetime(2017, 10, 28, 14, 26, 14),
        "end": datetime(2017, 10, 28, 14, 32, 34),
    },
    {
        "start": datetime(2017, 11, 1, 9, 41, 54),
        "end": datetime(2017, 11, 1, 9, 52, 23),
    },
    {
        "start": datetime(2017, 11, 1, 20, 16, 11),
        "end": datetime(2017, 11, 1, 20, 32, 13),
    },
    {
        "start": datetime(2017, 11, 2, 19, 44, 29),
        "end": datetime(2017, 11, 2, 19, 50, 56),
    },
    {
        "start": datetime(2017, 11, 2, 20, 14, 37),
        "end": datetime(2017, 11, 2, 20, 30, 29),
    },
    {
        "start": datetime(2017, 11, 2, 21, 35, 47),
        "end": datetime(2017, 11, 2, 21, 38, 57),
    },
    {
        "start": datetime(2017, 11, 3, 9, 59, 27),
        "end": datetime(2017, 11, 3, 10, 11, 46),
    },
    {
        "start": datetime(2017, 11, 3, 10, 13, 22),
        "end": datetime(2017, 11, 3, 10, 32, 2),
    },
    {
        "start": datetime(2017, 11, 3, 10, 44, 25),
        "end": datetime(2017, 11, 3, 10, 50, 34),
    },
    {
        "start": datetime(2017, 11, 3, 16, 6, 43),
        "end": datetime(2017, 11, 3, 16, 44, 38),
    },
    {
        "start": datetime(2017, 11, 3, 16, 45, 54),
        "end": datetime(2017, 11, 3, 17, 0, 27),
    },
    {
        "start": datetime(2017, 11, 3, 17, 7, 15),
        "end": datetime(2017, 11, 3, 17, 35, 5),
    },
    {
        "start": datetime(2017, 11, 3, 17, 36, 5),
        "end": datetime(2017, 11, 3, 17, 46, 48),
    },
    {
        "start": datetime(2017, 11, 3, 17, 50, 31),
        "end": datetime(2017, 11, 3, 18, 0, 3),
    },
    {
        "start": datetime(2017, 11, 3, 19, 22, 56),
        "end": datetime(2017, 11, 3, 19, 45, 51),
    },
    {
        "start": datetime(2017, 11, 4, 13, 14, 10),
        "end": datetime(2017, 11, 4, 13, 26, 15),
    },
    {
        "start": datetime(2017, 11, 4, 14, 18, 37),
        "end": datetime(2017, 11, 4, 14, 30, 5),
    },
    {
        "start": datetime(2017, 11, 4, 14, 45, 59),
        "end": datetime(2017, 11, 4, 15, 3, 20),
    },
    {
        "start": datetime(2017, 11, 4, 15, 16, 3),
        "end": datetime(2017, 11, 4, 15, 44, 30),
    },
    {
        "start": datetime(2017, 11, 4, 16, 37, 46),
        "end": datetime(2017, 11, 4, 16, 58, 22),
    },
    {
        "start": datetime(2017, 11, 4, 17, 13, 19),
        "end": datetime(2017, 11, 4, 17, 34, 50),
    },
    {
        "start": datetime(2017, 11, 4, 18, 10, 34),
        "end": datetime(2017, 11, 4, 18, 58, 44),
    },
    {"start": datetime(2017, 11, 5, 1, 56, 50), "end": datetime(2017, 11, 5, 1, 1, 4)},
    {
        "start": datetime(2017, 11, 5, 8, 33, 33),
        "end": datetime(2017, 11, 5, 8, 53, 46),
    },
    {"start": datetime(2017, 11, 5, 8, 58, 8), "end": datetime(2017, 11, 5, 9, 3, 39)},
    {"start": datetime(2017, 11, 5, 11, 5, 8), "end": datetime(2017, 11, 5, 11, 30, 5)},
    {"start": datetime(2017, 11, 6, 8, 50, 18), "end": datetime(2017, 11, 6, 8, 59, 5)},
    {"start": datetime(2017, 11, 6, 9, 4, 3), "end": datetime(2017, 11, 6, 9, 13, 47)},
    {
        "start": datetime(2017, 11, 6, 16, 19, 36),
        "end": datetime(2017, 11, 6, 17, 2, 55),
    },
    {
        "start": datetime(2017, 11, 6, 17, 21, 27),
        "end": datetime(2017, 11, 6, 17, 34, 6),
    },
    {
        "start": datetime(2017, 11, 6, 17, 36, 1),
        "end": datetime(2017, 11, 6, 17, 57, 32),
    },
    {
        "start": datetime(2017, 11, 6, 17, 59, 52),
        "end": datetime(2017, 11, 6, 18, 15, 8),
    },
    {
        "start": datetime(2017, 11, 6, 18, 18, 36),
        "end": datetime(2017, 11, 6, 18, 21, 17),
    },
    {
        "start": datetime(2017, 11, 6, 19, 24, 31),
        "end": datetime(2017, 11, 6, 19, 37, 57),
    },
    {
        "start": datetime(2017, 11, 6, 19, 49, 16),
        "end": datetime(2017, 11, 6, 20, 3, 14),
    },
    {"start": datetime(2017, 11, 7, 7, 50, 48), "end": datetime(2017, 11, 7, 8, 1, 32)},
    {
        "start": datetime(2017, 11, 8, 13, 11, 51),
        "end": datetime(2017, 11, 8, 13, 18, 5),
    },
    {
        "start": datetime(2017, 11, 8, 21, 34, 47),
        "end": datetime(2017, 11, 8, 21, 46, 5),
    },
    {
        "start": datetime(2017, 11, 8, 22, 2, 30),
        "end": datetime(2017, 11, 8, 22, 4, 47),
    },
    {"start": datetime(2017, 11, 9, 7, 1, 11), "end": datetime(2017, 11, 9, 7, 12, 10)},
    {"start": datetime(2017, 11, 9, 8, 2, 2), "end": datetime(2017, 11, 9, 8, 8, 28)},
    {
        "start": datetime(2017, 11, 9, 8, 19, 59),
        "end": datetime(2017, 11, 9, 8, 32, 24),
    },
    {
        "start": datetime(2017, 11, 9, 8, 41, 31),
        "end": datetime(2017, 11, 9, 8, 48, 59),
    },
    {"start": datetime(2017, 11, 9, 9, 0, 6), "end": datetime(2017, 11, 9, 9, 9, 24)},
    {"start": datetime(2017, 11, 9, 9, 9, 37), "end": datetime(2017, 11, 9, 9, 24, 25)},
    {
        "start": datetime(2017, 11, 9, 13, 14, 37),
        "end": datetime(2017, 11, 9, 13, 25, 39),
    },
    {
        "start": datetime(2017, 11, 9, 15, 20, 7),
        "end": datetime(2017, 11, 9, 15, 31, 10),
    },
    {
        "start": datetime(2017, 11, 9, 18, 47, 8),
        "end": datetime(2017, 11, 9, 18, 53, 10),
    },
    {
        "start": datetime(2017, 11, 9, 23, 35, 2),
        "end": datetime(2017, 11, 9, 23, 43, 35),
    },
    {
        "start": datetime(2017, 11, 10, 7, 51, 33),
        "end": datetime(2017, 11, 10, 8, 2, 28),
    },
    {
        "start": datetime(2017, 11, 10, 8, 38, 28),
        "end": datetime(2017, 11, 10, 8, 42, 9),
    },
    {
        "start": datetime(2017, 11, 11, 18, 5, 25),
        "end": datetime(2017, 11, 11, 18, 13, 14),
    },
    {
        "start": datetime(2017, 11, 11, 19, 39, 12),
        "end": datetime(2017, 11, 11, 19, 46, 22),
    },
    {
        "start": datetime(2017, 11, 11, 21, 13, 19),
        "end": datetime(2017, 11, 11, 21, 16, 31),
    },
    {
        "start": datetime(2017, 11, 12, 9, 46, 19),
        "end": datetime(2017, 11, 12, 9, 51, 43),
    },
    {
        "start": datetime(2017, 11, 13, 13, 33, 42),
        "end": datetime(2017, 11, 13, 13, 54, 15),
    },
    {
        "start": datetime(2017, 11, 14, 8, 40, 29),
        "end": datetime(2017, 11, 14, 8, 55, 52),
    },
    {
        "start": datetime(2017, 11, 15, 6, 14, 5),
        "end": datetime(2017, 11, 15, 6, 30, 6),
    },
    {
        "start": datetime(2017, 11, 15, 8, 14, 59),
        "end": datetime(2017, 11, 15, 8, 23, 44),
    },
    {
        "start": datetime(2017, 11, 15, 10, 16, 44),
        "end": datetime(2017, 11, 15, 10, 33, 41),
    },
    {
        "start": datetime(2017, 11, 15, 10, 33, 58),
        "end": datetime(2017, 11, 15, 10, 54, 14),
    },
    {
        "start": datetime(2017, 11, 15, 11, 2, 15),
        "end": datetime(2017, 11, 15, 11, 14, 42),
    },
    {
        "start": datetime(2017, 11, 16, 9, 27, 41),
        "end": datetime(2017, 11, 16, 9, 38, 49),
    },
    {"start": datetime(2017, 11, 16, 9, 57, 41), "end": datetime(2017, 11, 16, 10, 18)},
    {
        "start": datetime(2017, 11, 16, 17, 25, 5),
        "end": datetime(2017, 11, 16, 17, 44, 47),
    },
    {
        "start": datetime(2017, 11, 17, 13, 45, 54),
        "end": datetime(2017, 11, 17, 16, 36, 56),
    },
    {
        "start": datetime(2017, 11, 17, 19, 12, 49),
        "end": datetime(2017, 11, 17, 19, 31, 15),
    },
    {
        "start": datetime(2017, 11, 18, 10, 49, 6),
        "end": datetime(2017, 11, 18, 10, 55, 45),
    },
    {
        "start": datetime(2017, 11, 18, 11, 32, 12),
        "end": datetime(2017, 11, 18, 11, 44, 16),
    },
    {
        "start": datetime(2017, 11, 18, 18, 9, 1),
        "end": datetime(2017, 11, 18, 18, 14, 31),
    },
    {
        "start": datetime(2017, 11, 18, 18, 53, 10),
        "end": datetime(2017, 11, 18, 19, 1, 29),
    },
    {
        "start": datetime(2017, 11, 19, 14, 15, 41),
        "end": datetime(2017, 11, 19, 14, 31, 49),
    },
    {
        "start": datetime(2017, 11, 20, 21, 19, 19),
        "end": datetime(2017, 11, 20, 21, 41, 9),
    },
    {
        "start": datetime(2017, 11, 20, 22, 39, 48),
        "end": datetime(2017, 11, 20, 23, 23, 37),
    },
    {
        "start": datetime(2017, 11, 21, 17, 44, 25),
        "end": datetime(2017, 11, 21, 17, 51, 32),
    },
    {
        "start": datetime(2017, 11, 21, 18, 20, 52),
        "end": datetime(2017, 11, 21, 18, 34, 51),
    },
    {
        "start": datetime(2017, 11, 21, 18, 47, 32),
        "end": datetime(2017, 11, 21, 18, 51, 50),
    },
    {
        "start": datetime(2017, 11, 21, 19, 7, 57),
        "end": datetime(2017, 11, 21, 19, 14, 33),
    },
    {
        "start": datetime(2017, 11, 21, 20, 4, 56),
        "end": datetime(2017, 11, 21, 20, 8, 54),
    },
    {
        "start": datetime(2017, 11, 21, 21, 55, 47),
        "end": datetime(2017, 11, 21, 22, 8, 12),
    },
    {
        "start": datetime(2017, 11, 23, 23, 47, 43),
        "end": datetime(2017, 11, 23, 23, 57, 56),
    },
    {
        "start": datetime(2017, 11, 24, 6, 41, 25),
        "end": datetime(2017, 11, 24, 6, 53, 15),
    },
    {
        "start": datetime(2017, 11, 24, 6, 58, 56),
        "end": datetime(2017, 11, 24, 7, 33, 24),
    },
    {
        "start": datetime(2017, 11, 26, 12, 25, 49),
        "end": datetime(2017, 11, 26, 12, 41, 36),
    },
    {
        "start": datetime(2017, 11, 27, 5, 29, 4),
        "end": datetime(2017, 11, 27, 5, 54, 13),
    },
    {
        "start": datetime(2017, 11, 27, 6, 6, 47),
        "end": datetime(2017, 11, 27, 6, 11, 1),
    },
    {
        "start": datetime(2017, 11, 27, 6, 45, 14),
        "end": datetime(2017, 11, 27, 6, 55, 39),
    },
    {
        "start": datetime(2017, 11, 27, 9, 39, 44),
        "end": datetime(2017, 11, 27, 9, 47, 43),
    },
    {
        "start": datetime(2017, 11, 27, 11, 9, 18),
        "end": datetime(2017, 11, 27, 11, 20, 46),
    },
    {
        "start": datetime(2017, 11, 27, 11, 31, 46),
        "end": datetime(2017, 11, 27, 11, 35, 44),
    },
    {
        "start": datetime(2017, 11, 27, 12, 7, 14),
        "end": datetime(2017, 11, 27, 12, 12, 36),
    },
    {
        "start": datetime(2017, 11, 27, 12, 21, 40),
        "end": datetime(2017, 11, 27, 12, 26, 44),
    },
    {
        "start": datetime(2017, 11, 27, 17, 26, 31),
        "end": datetime(2017, 11, 27, 17, 36, 7),
    },
    {
        "start": datetime(2017, 11, 27, 18, 11, 49),
        "end": datetime(2017, 11, 27, 18, 29, 4),
    },
    {
        "start": datetime(2017, 11, 27, 19, 36, 16),
        "end": datetime(2017, 11, 27, 19, 47, 17),
    },
    {
        "start": datetime(2017, 11, 27, 20, 12, 57),
        "end": datetime(2017, 11, 27, 20, 17, 33),
    },
    {
        "start": datetime(2017, 11, 28, 8, 18, 6),
        "end": datetime(2017, 11, 28, 8, 41, 53),
    },
    {
        "start": datetime(2017, 11, 28, 19, 17, 23),
        "end": datetime(2017, 11, 28, 19, 34, 1),
    },
    {
        "start": datetime(2017, 11, 28, 19, 34, 15),
        "end": datetime(2017, 11, 28, 19, 46, 24),
    },
    {
        "start": datetime(2017, 11, 28, 21, 27, 29),
        "end": datetime(2017, 11, 28, 21, 39, 32),
    },
    {
        "start": datetime(2017, 11, 29, 7, 47, 38),
        "end": datetime(2017, 11, 29, 7, 51, 18),
    },
    {
        "start": datetime(2017, 11, 29, 9, 50, 12),
        "end": datetime(2017, 11, 29, 9, 53, 44),
    },
    {
        "start": datetime(2017, 11, 29, 17, 3, 42),
        "end": datetime(2017, 11, 29, 17, 16, 21),
    },
    {
        "start": datetime(2017, 11, 29, 18, 19, 15),
        "end": datetime(2017, 11, 29, 18, 23, 43),
    },
    {
        "start": datetime(2017, 12, 1, 17, 3, 58),
        "end": datetime(2017, 12, 1, 17, 10, 12),
    },
    {"start": datetime(2017, 12, 2, 7, 55, 56), "end": datetime(2017, 12, 2, 8, 1, 1)},
    {
        "start": datetime(2017, 12, 2, 9, 16, 14),
        "end": datetime(2017, 12, 2, 9, 21, 18),
    },
    {
        "start": datetime(2017, 12, 2, 19, 48, 29),
        "end": datetime(2017, 12, 2, 19, 53, 18),
    },
    {
        "start": datetime(2017, 12, 3, 14, 36, 29),
        "end": datetime(2017, 12, 3, 15, 20, 9),
    },
    {
        "start": datetime(2017, 12, 3, 16, 4, 2),
        "end": datetime(2017, 12, 3, 16, 25, 30),
    },
    {
        "start": datetime(2017, 12, 3, 16, 40, 26),
        "end": datetime(2017, 12, 3, 16, 43, 58),
    },
    {
        "start": datetime(2017, 12, 3, 17, 20, 17),
        "end": datetime(2017, 12, 3, 18, 4, 33),
    },
    {"start": datetime(2017, 12, 4, 8, 34, 24), "end": datetime(2017, 12, 4, 8, 51)},
    {
        "start": datetime(2017, 12, 4, 17, 49, 26),
        "end": datetime(2017, 12, 4, 17, 53, 57),
    },
    {
        "start": datetime(2017, 12, 4, 18, 38, 52),
        "end": datetime(2017, 12, 4, 18, 50, 33),
    },
    {
        "start": datetime(2017, 12, 4, 21, 39, 20),
        "end": datetime(2017, 12, 4, 21, 46, 58),
    },
    {
        "start": datetime(2017, 12, 4, 21, 54, 21),
        "end": datetime(2017, 12, 4, 21, 56, 17),
    },
    {
        "start": datetime(2017, 12, 5, 8, 50, 50),
        "end": datetime(2017, 12, 5, 8, 52, 54),
    },
    {
        "start": datetime(2017, 12, 6, 8, 19, 38),
        "end": datetime(2017, 12, 6, 8, 24, 14),
    },
    {
        "start": datetime(2017, 12, 6, 18, 19, 19),
        "end": datetime(2017, 12, 6, 18, 28, 11),
    },
    {
        "start": datetime(2017, 12, 6, 18, 28, 55),
        "end": datetime(2017, 12, 6, 18, 33, 12),
    },
    {
        "start": datetime(2017, 12, 6, 20, 3, 29),
        "end": datetime(2017, 12, 6, 20, 21, 38),
    },
    {
        "start": datetime(2017, 12, 6, 20, 36, 42),
        "end": datetime(2017, 12, 6, 20, 39, 57),
    },
    {"start": datetime(2017, 12, 7, 5, 54, 51), "end": datetime(2017, 12, 7, 6, 1, 15)},
    {
        "start": datetime(2017, 12, 8, 16, 47, 18),
        "end": datetime(2017, 12, 8, 16, 55, 49),
    },
    {
        "start": datetime(2017, 12, 8, 19, 15, 2),
        "end": datetime(2017, 12, 8, 19, 29, 12),
    },
    {
        "start": datetime(2017, 12, 9, 22, 39, 37),
        "end": datetime(2017, 12, 9, 22, 47, 19),
    },
    {
        "start": datetime(2017, 12, 9, 23, 0, 10),
        "end": datetime(2017, 12, 9, 23, 5, 32),
    },
    {
        "start": datetime(2017, 12, 10, 0, 39, 24),
        "end": datetime(2017, 12, 10, 0, 56, 2),
    },
    {"start": datetime(2017, 12, 10, 1, 2, 42), "end": datetime(2017, 12, 10, 1, 8, 9)},
    {
        "start": datetime(2017, 12, 10, 1, 8, 57),
        "end": datetime(2017, 12, 10, 1, 11, 30),
    },
    {
        "start": datetime(2017, 12, 10, 13, 49, 9),
        "end": datetime(2017, 12, 10, 13, 51, 41),
    },
    {
        "start": datetime(2017, 12, 10, 15, 14, 29),
        "end": datetime(2017, 12, 10, 15, 18, 19),
    },
    {
        "start": datetime(2017, 12, 10, 15, 31, 7),
        "end": datetime(2017, 12, 10, 15, 36, 28),
    },
    {
        "start": datetime(2017, 12, 10, 16, 20, 6),
        "end": datetime(2017, 12, 10, 16, 30, 31),
    },
    {
        "start": datetime(2017, 12, 10, 17, 7, 54),
        "end": datetime(2017, 12, 10, 17, 14, 25),
    },
    {
        "start": datetime(2017, 12, 10, 17, 23, 47),
        "end": datetime(2017, 12, 10, 17, 45, 25),
    },
    {
        "start": datetime(2017, 12, 11, 6, 17, 6),
        "end": datetime(2017, 12, 11, 6, 34, 4),
    },
    {
        "start": datetime(2017, 12, 11, 9, 8, 41),
        "end": datetime(2017, 12, 11, 9, 12, 21),
    },
    {
        "start": datetime(2017, 12, 11, 9, 15, 41),
        "end": datetime(2017, 12, 11, 9, 20, 18),
    },
    {
        "start": datetime(2017, 12, 12, 8, 55, 53),
        "end": datetime(2017, 12, 12, 8, 59, 34),
    },
    {
        "start": datetime(2017, 12, 13, 17, 14, 56),
        "end": datetime(2017, 12, 13, 17, 18, 32),
    },
    {
        "start": datetime(2017, 12, 13, 18, 52, 16),
        "end": datetime(2017, 12, 13, 19, 0, 45),
    },
    {
        "start": datetime(2017, 12, 14, 9, 1, 10),
        "end": datetime(2017, 12, 14, 9, 11, 6),
    },
    {
        "start": datetime(2017, 12, 14, 9, 12, 59),
        "end": datetime(2017, 12, 14, 9, 19, 6),
    },
    {"start": datetime(2017, 12, 14, 11, 54, 33), "end": datetime(2017, 12, 14, 12, 2)},
    {
        "start": datetime(2017, 12, 14, 14, 40, 23),
        "end": datetime(2017, 12, 14, 14, 44, 40),
    },
    {
        "start": datetime(2017, 12, 14, 15, 8, 55),
        "end": datetime(2017, 12, 14, 15, 26, 24),
    },
    {
        "start": datetime(2017, 12, 14, 17, 46, 17),
        "end": datetime(2017, 12, 14, 18, 9, 4),
    },
    {
        "start": datetime(2017, 12, 15, 9, 8, 12),
        "end": datetime(2017, 12, 15, 9, 23, 45),
    },
    {
        "start": datetime(2017, 12, 16, 9, 33, 46),
        "end": datetime(2017, 12, 16, 9, 36, 17),
    },
    {
        "start": datetime(2017, 12, 16, 11, 2, 31),
        "end": datetime(2017, 12, 16, 11, 5, 4),
    },
    {
        "start": datetime(2017, 12, 17, 10, 9, 47),
        "end": datetime(2017, 12, 17, 10, 32, 3),
    },
    {
        "start": datetime(2017, 12, 18, 8, 2, 36),
        "end": datetime(2017, 12, 18, 8, 7, 34),
    },
    {"start": datetime(2017, 12, 18, 16, 3), "end": datetime(2017, 12, 18, 16, 9, 20)},
    {
        "start": datetime(2017, 12, 18, 16, 30, 7),
        "end": datetime(2017, 12, 18, 16, 53, 12),
    },
    {
        "start": datetime(2017, 12, 18, 19, 18, 23),
        "end": datetime(2017, 12, 18, 19, 22, 8),
    },
    {
        "start": datetime(2017, 12, 18, 20, 14, 46),
        "end": datetime(2017, 12, 18, 20, 17, 47),
    },
    {
        "start": datetime(2017, 12, 19, 19, 14, 8),
        "end": datetime(2017, 12, 19, 19, 23, 49),
    },
    {
        "start": datetime(2017, 12, 19, 19, 39, 36),
        "end": datetime(2017, 12, 19, 19, 43, 46),
    },
    {
        "start": datetime(2017, 12, 20, 8, 5, 14),
        "end": datetime(2017, 12, 20, 8, 10, 46),
    },
    {
        "start": datetime(2017, 12, 20, 8, 15, 45),
        "end": datetime(2017, 12, 20, 8, 29, 50),
    },
    {
        "start": datetime(2017, 12, 20, 8, 33, 32),
        "end": datetime(2017, 12, 20, 8, 38, 9),
    },
    {
        "start": datetime(2017, 12, 20, 13, 43, 36),
        "end": datetime(2017, 12, 20, 13, 54, 39),
    },
    {
        "start": datetime(2017, 12, 20, 18, 57, 53),
        "end": datetime(2017, 12, 20, 19, 6, 54),
    },
    {
        "start": datetime(2017, 12, 21, 7, 21, 11),
        "end": datetime(2017, 12, 21, 7, 32, 3),
    },
    {
        "start": datetime(2017, 12, 21, 8, 1, 58),
        "end": datetime(2017, 12, 21, 8, 6, 15),
    },
    {
        "start": datetime(2017, 12, 21, 13, 20, 54),
        "end": datetime(2017, 12, 21, 13, 33, 49),
    },
    {
        "start": datetime(2017, 12, 21, 15, 26, 8),
        "end": datetime(2017, 12, 21, 15, 34, 27),
    },
    {
        "start": datetime(2017, 12, 21, 18, 9, 46),
        "end": datetime(2017, 12, 21, 18, 38, 50),
    },
    {
        "start": datetime(2017, 12, 22, 16, 14, 21),
        "end": datetime(2017, 12, 22, 16, 21, 46),
    },
    {
        "start": datetime(2017, 12, 22, 16, 29, 17),
        "end": datetime(2017, 12, 22, 16, 34, 14),
    },
    {
        "start": datetime(2017, 12, 25, 12, 49, 51),
        "end": datetime(2017, 12, 25, 13, 18, 27),
    },
    {
        "start": datetime(2017, 12, 25, 13, 46, 44),
        "end": datetime(2017, 12, 25, 14, 20, 50),
    },
    {
        "start": datetime(2017, 12, 26, 10, 40, 16),
        "end": datetime(2017, 12, 26, 10, 53, 45),
    },
    {
        "start": datetime(2017, 12, 27, 16, 56, 12),
        "end": datetime(2017, 12, 27, 17, 17, 39),
    },
    {
        "start": datetime(2017, 12, 29, 6, 2, 34),
        "end": datetime(2017, 12, 29, 6, 12, 30),
    },
    {
        "start": datetime(2017, 12, 29, 12, 21, 3),
        "end": datetime(2017, 12, 29, 12, 46, 16),
    },
    {
        "start": datetime(2017, 12, 29, 14, 32, 55),
        "end": datetime(2017, 12, 29, 14, 43, 46),
    },
    {
        "start": datetime(2017, 12, 29, 15, 8, 26),
        "end": datetime(2017, 12, 29, 15, 18, 51),
    },
    {
        "start": datetime(2017, 12, 29, 20, 33, 34),
        "end": datetime(2017, 12, 29, 20, 38, 13),
    },
    {
        "start": datetime(2017, 12, 30, 13, 51, 3),
        "end": datetime(2017, 12, 30, 13, 54, 33),
    },
    {
        "start": datetime(2017, 12, 30, 15, 9, 3),
        "end": datetime(2017, 12, 30, 15, 19, 13),
    },
]

trip_counts = {"AM": 0, "PM": 0}

for trip in onebike_datetimes:
    # check if before noon
    if trip["start"].hour < 12:
        trip_counts["AM"] += 1
    else:
        trip_counts["PM"] += 1

print(trip_counts)


###########

onebike_durations = []

for trip in onebike_datetimes:
    trip_duration = (
        trip["end"] - trip["start"]
    )  # datetime arithmetic (subtraction) returns a timedelta object
    trip_length_seconds = (
        trip_duration.total_seconds()
    )  # Use .total_seconds() to get duration in seconds as a float
    onebike_durations.append(trip_length_seconds)

total_elapsed_time = sum(onebike_durations)
number_of_trips = len(onebike_durations)
print(total_elapsed_time / number_of_trips)

# datetime objects are comparable and support min()/max() operations
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")
