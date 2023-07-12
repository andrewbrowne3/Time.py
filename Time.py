
from datetime import time


x = input("Please enter an early time (HH:MM): ")
early_hours, early_minutes = map(int, x.split(":"))
y = input("Please enter a later time (HH:MM): ")
late_hours, late_minutes = map(int, y.split(":"))

early = time(early_hours, early_minutes)
late = time(late_hours, late_minutes)
print(early)
late_time_in_seconds = (late.hour*3600+late.minute*60)
early_time_in_seconds = (early.hour*3600 + early.minute*60)
difference_in_seconds = late_time_in_seconds -early_time_in_seconds
if late_time_in_seconds < early_time_in_seconds:
    print("Incorrect order of times :/")
else:
    print(difference_in_seconds,"seconds difference",difference_in_seconds/60,"minutes difference")