import time
from decimal import *

print("Python Pi Calculator")
print("<------------------>")
time.sleep(1)
places = int(input("Approximate to how many decimal places? (Recommended: 10-30)"))
getcontext().prec = places
pause = float(input("Seconds between iterations? (Recommended: 0-1)"))

x = Decimal(3)
y = Decimal(4) - Decimal(4)/Decimal(x)
time.sleep(1)
print(Decimal(y))

while True:
    x += Decimal(2)
    y += Decimal(4)/Decimal(x)
    time.sleep(pause)
    print(Decimal(y))
    x += Decimal(2)
    y -= Decimal(4)/Decimal(x)
    time.sleep(pause)
    print(Decimal(y))