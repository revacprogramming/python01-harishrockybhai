# Files

#filename = "dataset/mbox-short.txt"

fname=input("enter the file name")
fh=open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    t=line.find("0")
    number=float(line[t:])
    total=total+number
    count=count+1
average=total/count
print("average spam confidence",average)        
