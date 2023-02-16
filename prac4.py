list = []
list = eval(input("Enter a list of numbers between 1 and 12"))
for i in range(len(list)):
    if i >10:
        i=10
        print(i)
print("\n")
for i in range(len(list)):
    print(list[i]) 
