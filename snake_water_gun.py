import random

def gamewin(comp,a):
    if comp=='s' and a =='w':
        print('comp win')
    elif comp=='g' and a == 's':
        print('comp win')
    elif comp=='w' and a=='g':
        print('comp win')
    elif comp =='w' and a=='w':
        if comp =='s' and a=='s':
            if comp=='g' and a=='g':
                print('The game is tie ')
    else:
        print('player win')

a = input('player turn :- snake(s) or water(w) or gun(g)')
print("comp turn : snake(s) or water(w) or gun(g)")
randno = random.randint(1,3)
if randno==1:
    comp = 's'
elif randno==2:
    comp = 'w'
elif randno==3:
    comp = 'g'



c = gamewin(comp,a)
print(f'comp choose {comp}')
print(f"the player choose {a}")

