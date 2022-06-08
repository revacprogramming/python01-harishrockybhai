# Lists


fname=input("enter file name :")
fh=open(fname)
lst=list()
for line in fh:
    word=line.rstrip().strip()
    for element in word:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)