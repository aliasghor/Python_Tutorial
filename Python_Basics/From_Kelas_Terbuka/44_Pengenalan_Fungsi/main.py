"""
    Fungsi secara singkat adalah membuat program secara singkat.dan sebuah fungsi bisa membikin program kita untuk tidak melakukan DRY(Do not Repeat Yourself)

"""

# Contoh fungsi DRY(Do not Repeat Yourself)
def sum(x: int, y: int) -> int:
    return x + y

x = 5
y = 5
sum(x,y)

x = 10
y = 12
sum(x,y)

def hallo():
    print("Hallo")

hallo()
hallo()
hallo()

# Contoh fungsi membuat program menjadi singkat
def factorial(num):
    if num == 1:
        print(num,'=',end=' ')
        return 1
    else:
        print(num,"*",end=' ')
        return num * factorial(num - 1)

num = 5
print(factorial(num))