file = open('file.txt', 'r')
# read all lines
# print(file.readlines())


for x in file:
    print(x)
x = open('file.txt', 'a')
x.write("\n Pro coder")    
with open("file.txt", "r") as file:
    data =file.readlines()
    for line in data:
        x =line.split()
        print(x)    