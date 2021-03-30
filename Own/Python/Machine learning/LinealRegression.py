π = 3.141592
#Δ  π
def range2(start, stop, step=1):
    l = []
    while stop >= start:
        l.append(start)
        start += step
    return l

range