def kwadraten_som(grondgetallen):
    uitkomst = 0
    for grondgetal in grondgetallen:
        if type(grondgetal) == int:
            if grondgetal >= 0:
                uitkomst += grondgetal**2
        else:
            return -1
    return uitkomst
print(kwadraten_som([4, 5, 3, -81]))
