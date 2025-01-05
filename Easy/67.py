#Adds binary numbers together and return the sum back in binary

def addBinary(self, a, b):
    a_int = int(a, 2)
    b_int = int(b, 2)
    sum = a_int + b_int
    return bin(sum)[2:]