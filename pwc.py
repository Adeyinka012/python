print("Star pattern \n ")
for i in range(1,12):
    for j in range(i):
        print('$', end="")
    print('\n')    
print("Invert Star pattern \n")
for i in range(99,1,-1):
    for j in range(i,1,-1):
        print('%', end="")
    print('\n')    