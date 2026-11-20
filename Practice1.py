def findLowest(arr):
    if not arr:
        return None
    minVal = arr[0]
    for num in arr:
        if num < minVal:
            minVal = num
    return minVal

numbers = [15, 3, 27, 8, 12]
print(findLowest(numbers))


def isPalindrome(string):
    string = string.lower()
    return string == string[::-1]

print(isPalindrome("Hello World!"))
print(isPalindrome("ollo"))


def printArr(arr):
    print(*arr)

arr = [54, 43, 2, 1, 5]
printArr(arr)


def printArr1(arr1):
    for n in arr1:
        print(n, end=" ")

arr1 = [324, 5, 2, 2]
printArr1(arr1)


a = int(input())
b = int(input())
c = input().strip()
print(f"{str(a) * a}{c}{str(b) * b}")


def relation(n, m):
    if n > m:
        print("greater")
    elif n == m:
        print("equal")
    elif n < m:
        print("less")
    else:
        print("NAN")
relation(9, 3)


def multTable(n):
    print("\n", end="")
    for i in range(1, 11):
        print(n * i, end=" ")

multTable(11)
print("\n", end="")


def evenCharacs(s):
    print(s[1::2])

evenCharacs("Penelope")
evenCharacs("pneumonoultramicroscopicsilicovolcanoconiosis")


def evenCharacs(*words):
    for s in words:
        print(s[1::2])

evenCharacs("Penelope", "pneumonoultramicroscopicsilicovolcanoconiosis", "DoctorPhenomenal")


def serialNos(n):
    i = 0
    while i <= n:
        print(i)
        i += 1

serialNos(10)


s = "Antelope"
n = 29
f = 11.9
print(s, n, int(f))


def separator():
    s1 = str(input())
    s2 = str(input())
    sep = input()
    print(s1 + sep + s2)
separator()


def arithOp(x, y):
    s = x / y
    t = x // y
    u = x % y
    return s, t, u

print(arithOp(1, 2))


def logicOp(x, y):
    a = x & y
    b = x | y
    c = not x
    d = not y
    return a, b, c, d

print(logicOp(True, False))
print(*logicOp(True, False))

a = 4
b = 5
c = 6
d = a ^ a
e = c ^ b
f = a & b
g = ~e
print(d, e, f, g)

d = 10.23
print(int(d))

n = "31"
N = int(n)
print(N * 2)

a = 2
b = 1
a, b = b, a
print(a, b)


def geomProg(a, r, n):
    nth_term = a * (r ** (n - 1))
    print(nth_term)

geomProg(2, 2, 5)


def gfgNTimes(n):
    n = "GFG"
    print(n * 3, end=" ")

gfgNTimes(3) 
