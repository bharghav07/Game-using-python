import random
AI=random.choice([-1,0,1])
player=input("Enter your choice:")
dict={"r":1,"p":-1,"s":0}
reversedict={1:"rock",-1:"paper",0:"scissor"}
play=dict[player]
print(f"Player choice {reversedict[play]} \nComputer choice {reversedict[AI]}")
if(AI==play):
    print('Its draw..')
else:
    if(AI==1 and play==-1):
        print('Player wins.. :)')
    elif(AI==1 and play==0):
        print('Computer wins.. :(')
    elif(AI==0 and play==1):
        print('Player wins.. :)')
    elif(AI==0 and play==-1):
        print('Computer wins.. :(')
    elif(AI==-1 and play==0):
        print('Player wins.. :)')
    elif(AI==-1 and play==1):
        print('Computer wins.. :(')
    else:
        print('Something went wrong')

