def primer_4a(a):
    a = int(a)
    global x
    x = a / 2
    return(x)

def primer_4b(b):
    b = int(b)
    return(b * 4)

primer_4a(2)
primer_4b(x)
