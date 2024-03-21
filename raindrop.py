n = int(input())
if n%3 == 0 and n%5 == 0 and n%7 == 0:
    print("plingplangplong")
elif n%3 == 0 and n%5 == 0:
    print("plingplang")
elif n%3 == 0 and n%7 == 0:
    print("plingplong")
elif n%5 == 0 and n%7 == 0:
    print("plangplong")
elif n%3 == 0:
    print("pling")
elif n%5 == 0:
    print("plang")
elif n%7 == 0:
    print("plong")
else:
    print(n)