import sys
w = input("First wire color: ")
x = input("Second wire color: ")
y = input("Third wire color: ")
z = input("Fourth wire color: ")



def check(wire1, wire2):
    if wire1 == 'white':
        if wire2 == "white" or wire2 == "black":
            print("boom")
            sys.exit(0)
    if wire1 == "red":
         if wire2 != "green":
             print("boom")
             sys.exit(0)
    if wire1 == "black":
         if wire2 == "white" or wire2 == "green" or wire2 == "orange":
             print("boom")
             sys.exit(0)
    if wire1 == "orange":
         if  not(wire2 == "red" or wire2 == "black") :
             print("boom")
             sys.exit(0)
    if wire1 == "green":
         if not( wire2 == "orange" or wire2 == "white"):
             print("boom")
             sys.exit(0)
    if wire1 == "purple":
         if wire2 != "red":
             print("boom")
             sys.exit(0)

check(w, x)

check(x, y)

check(y, z)

print("Bomb Defused")
