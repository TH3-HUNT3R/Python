ip = open("input.txt",'r')
lst = ip.readlines()
print(lst)
lst.reverse()
print(lst)
ip.close()

op=open("fileOP.txt",'w')
op.write("".join(lst))
op.close()