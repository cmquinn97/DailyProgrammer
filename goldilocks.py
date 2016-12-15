#Once upon a time, there lived an adventurous little girl called Goldilocks. She explored the world with abandon, having a lot of fun.
#During her latest foray into the woods, she found another bear home -- though this one is home to many more bears.
#Having learned from her previous experiences, Goldilocks knows that trial and error is not an efficient way of finding the right chair and porridge to help herself to.
#The task falls to you: given descriptions of Goldilocks' needs and of the available porridge/chairs at the dinner table,
#tell Goldilocks which chair to sit in so the chair does not break, and the porridge is at an edible temperature.

#If weight is 100 and temp is 80, seats 1 and 3, in the options list, she can sit in. (0 and 2 in programmer language)


weight = int(input("What is the weight of Goldilocks: "))
temp = int(input("What temperature porridge can she handle: "))

def possible(x, y):
    if x > weight:
        if y < temp:
            return 1
    else:
        return 0

options = [possible(30, 50), possible(130, 75), possible(90, 60), possible(150, 85), possible(120, 70), possible(200, 200), possible(110, 100)]

for check in range(len(options)):
    if options[check] == 1:
        print(check + 1)
