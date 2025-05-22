sum = int(input("pulni kiriting: "))
on = sum //10000
b =sum-(on* 10000)
c = b //5000
d = b - (c * 5000)
e = d //1000
f = d - (e * 1000)
g = f //500
h = f - (g * 500)
i = h //100
print(f"pulingizda {on} ta 10000 so'm, {c} ta 5000 so'm, {e} ta 1000 so'm, {g} ta 500 so'm, {i} ta 100 so'm bor")