from operator import truediv
import random
def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Computer's Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
else:
    comp = 's'
you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?\n")

print("Computer chose: " + comp)
print("You chose: " + you)
a = game(comp, you)

if a==None:
    print("Its a tie!")
elif a==True:
    print("You win!")
elif a==False:
    print("You lose!")
