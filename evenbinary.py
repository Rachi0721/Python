n = int(input("enter a number: "))
binary = str(bin(n))
even_binary = binary.count("1")
print(binary)
print("the no of one's is",even_binary)
if even_binary%2 == 0:
    print("even")
else:
    print ("odd")


