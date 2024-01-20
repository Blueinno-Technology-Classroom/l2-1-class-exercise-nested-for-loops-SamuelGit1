##################################################
'''
Q1: 
'''

for i in range(7):
    for j in range(i + 1):
        print(j, end=" ")
    print("")
print("")

##################################################
'''
Q2:
'''

for i in range(6):
    for j in range(1, i + 2):
        print(j, end=" ")
    print("")
print("")

##################################################
'''
Q3:
'''

for i in range(9, 0, -1):
    for j in range(5):
        print(i, end="")
print("\n")

##################################################
'''
Q4:
'''

for i in range(9, 0, -1):
    for j in range(i):
        print(i, end="")
print("\n")

##################################################
'''
Q5:
'''

for i in range(5):
    for j in range(5, i - 1, -1):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print(i * 2 + 1, end="")
    print("")
print("")

##################################################
'''
Q6:
'''

for i in range(5):
    for j in range(5, i - 1, -1):
        print(" ", end="")
    print(int("1" * (i + 1)) ** 2)

##################################################
'''
Challenge
'''

def draw_cake(segments, top_width, height):
    for i in range(segments):
        for j in range(height):
            print(" " * ((segments - i) * 4), end="")
            print("*" * (top_width + i * 8))

##################################################