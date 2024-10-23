import random
def gamewin(comp,me):
    if comp==me:
        return None
    elif comp=='R':
        if me=='S':
            return False
        elif me=='P':
            return True
    elif comp=='P':
        if me=='R':
            return False
        elif me=='S':
            return True
    elif comp=='S':
        if me=='P':
            return False
        elif me=='R':
            return True
comp=("comp turn:rock(R),Paper(P),Sizer(S)")
randno=random.randint(1,3)
if randno==1:
    comp='R'
elif randno==2:
    comp='P'
elif randno==3:
    comp="S"

me=input("your turn:rock(R),Paper(P),Sizer(S): ")
a=gamewin(comp,me)

print("computer choose",comp)
print("me choose",me)
if comp==me:
    print("TIE")
elif comp!=me:
    print("yoU LOOSE")
else:
    print("WIN")
