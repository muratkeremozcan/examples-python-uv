# ===== PREFERRED PATTERNS =====
# 1. Use dateutil.tz.gettz('Region/City') for timezone objects (handles DST)
# 2. Use astimezone() to convert between timezones (handles DST automatically)
# 3. For current time: datetime.now(tz=timezone_obj)

# ===== USE WITH CAUTION =====
# - replace(tzinfo=) - Doesn't convert time, just changes the label
# - timezone(timedelta()) - Fixed offset, no DST handling
# - Naive datetimes (without timezone)

from datetime import datetime, timedelta, timezone

# ⚠️ Fixed offset (no DST) - only for simple cases
CT = timezone(timedelta(hours=-6))
dt = datetime(2022, 1, 1, 15, 23, 25, tzinfo=CT)
print("timezone-aware datetime CT:", dt, dt.isoformat())

# ✅ Preferred: Get timezone with DST support
from dateutil import tz

et = tz.gettz("US/Eastern")
ct = tz.gettz("US/Central")
utc_time = tz.gettz("UTC")

# Example of proper timezone conversion
ny_time = datetime(2023, 1, 1, 12, 0, tzinfo=et)
london_time = ny_time.astimezone(tz.gettz("Europe/London"))

# ⚠️ Common pitfall: replace() vs astimezone()
print("✅ Correct conversion:", ny_time.astimezone(timezone.utc))  # Right
print("❌ Just changes label:", ny_time.replace(tzinfo=timezone.utc))  # Wrong

# Working with timezone-naive datetimes (avoid when possible)
naive_dt = datetime(2023, 1, 1, 12, 0)
# ⚠️ Better to start with timezone-aware datetimes
aware_dt = naive_dt.replace(tzinfo=et)  # Assumes naive_dt is in ET

# DST-aware calculations
# Start just before DST transition (March 12, 2017 00:00 EST)
start = datetime(2017, 3, 12, tzinfo=et)
end = start + timedelta(hours=6)  # Crosses DST boundary

print(f"Local time: {start.isoformat()} to {end.isoformat()}")
print(f"Wall clock hours: {(end-start).total_seconds()/3600}")  # 6 hours
print(
    f"UTC hours: {(end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds()/3600}"
)  # 5 hours

# Best practice: Convert to UTC for storage/calculations
utc_time = datetime.now(tz=timezone.utc)
local_time = utc_time.astimezone(et)  # Convert to local only for display

##########

# ===== HANDLING AMBIGUOUS TIMES (DST) =====
# During DST transitions, some local times occur twice
# Use tz.datetime_ambiguous() to detect and tz.enfold() to handle them

# During DST "fall back", the same local time occurs twice
# Example: 1:30 AM happens twice when clocks go from 2 AM back to 1 AM

# Without fold:
dt = datetime(2023, 11, 5, 1, 30, tzinfo=et)  # Which 1:30 AM is this?

# With fold:
first = tz.enfold(dt, fold=0)  # First occurrence (before DST transition)
second = tz.enfold(dt, fold=1)  # Second occurrence (after DST transition)

# They look the same but represent different moments in time
print(first == second)  # True (same local time)
print(first == second)  # False (different UTC times)


# Example: Nov 5, 2023 1:30 AM happens twice when clocks fall back
dst_time = datetime(2023, 11, 5, 1, 30, tzinfo=et)
if tz.datetime_ambiguous(dst_time):
    # Handle both possible times (before/after DST transition)
    first = tz.enfold(dst_time, fold=0)  # First occurrence (before DST)
    second = tz.enfold(dst_time, fold=1)  # Second occurrence (after DST)
    print(f"Ambiguous time! Could be {first} or {second}")


# Check for ambiguous times in data

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
]

for trip in onebike_datetimes:
    # Make times timezone-aware first
    start = trip["start"].replace(tzinfo=et)  # Assuming Eastern Time
    end = trip["end"].replace(tzinfo=et)

    # Handle DST transitions
    if start > end:
        end = tz.enfold(
            end, fold=1
        )  # ensures that if an end time appears to be before its start due to DST, it's interpreted as the later occurrence

    # Convert to UTC
    start_utc = start.astimezone(timezone.utc)
    end_utc = end.astimezone(timezone.utc)
