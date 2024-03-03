import time 
import math

def aft(num, ms):
    time.sleep(ms / 1000)
    print("Square root of", num, "after", ms, "millisecond is", math.sqrt(num))

number = int(input())
millisecond = int(input())
aft(number, millisecond)

#BuiltInFunctions: sleep(), int(), sqrt()