a = int(input("1-tomonni kiriting: "))
b = int(input("2-tomonni kiriting: "))
c = int(input("3-tomonni kiriting: "))
s = (a + b + c) / 2
S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Uchburchakning yuzi:", S)
