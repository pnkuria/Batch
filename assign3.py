string = input("Enter string")
def paracheck(seq):
    if "()" in seq:
        seq = ()
    elif "[]" in seq:
        seq = seq.replace("[]","")
    elif "{}" in seq:
        seq = seq.replace("{}","")
    else:
        print("false")
paracheck("seq")
