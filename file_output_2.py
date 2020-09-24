
f = open("myfile.out", "w")
mylist = range(5) 
f.write("List")
for i in mylist:
    line = str(i) + "\n"
    f.writelines(line)
f.close()


