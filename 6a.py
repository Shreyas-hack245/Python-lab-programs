file1 = open("file1.txt", "w")
file1.write("VTU")
file1.close()

file2 = open("file2.txt", "w")
file2.write("UNIVERSITY")
file2.close()


file1 = open("file1.txt", "r")
c1 = file1.read()
print(c1)

file2 = open("file2.txt", "r")
c2 = file2.read()
print(c2)


file3 = open("file3.txt", "w")
file3.write(c1 + " " + c2)
file3.close()


file3 = open("file3.txt", "r")
print(file3.read())