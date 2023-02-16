list = []
list_length = 6
for i in range (list_length):
    number = eval(input("Enter value"))
    list.append(number)
print(list)
print(list[-1]) 
list.reverse()
print(list)
