# Code used to compute a payment, related to working hours,
# using 40 hour as weekly limit. Above that, the rate is multiplied
# by 1,5.

def computepay(hours, rate):
    hourThreshold = 40
    if hours <= hourThreshold:
        return hours * rate
    else:
        return (hourThreshold * rate) + (hours - hourThreshold) * 1.5 * rate

hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
print("Pay", computepay(float(hrs), float(rate)))
