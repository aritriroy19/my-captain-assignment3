
def most_frequent(mississippi):
    d= dict()
    for key in mississippi:
        if key not in d:
            d[key]= 1
        else:
            d[key] += 1
    return d
print (most_frequent('mississippi'))
