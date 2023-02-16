patch = [8,9,10]
patch.insert(2,17)
for i in range(len(patch)):
    print(patch[i])
print("\n")
patch.append(4)
patch.append(5)
patch.append(6)
for i in range(len(patch)):
    print(patch[i])
print("\n")
patch.sort()
for i in range(len(patch)):
    print(patch[i])
print("\n")
final_list = patch + patch
print(final_list)
patch.insert(3,25)
print("\n")
for i in range(len(patch)):
    print(patch[i])
    