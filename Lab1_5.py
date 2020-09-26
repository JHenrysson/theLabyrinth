# coding=utf-8
print(
    '''
    You have been placed in a pitch-black labyrinth, without knowing if there is a way out or not.
    Maybe there are traps? The only option available is to walk in a random direction and hope 
    for the best, hope that you do not walk into a wall, or even worse,that you walk in circles. 
    But hurry up, you only have so many moves…''')
print(
    '''
    To move around use:
    w = up 
    a = left 
    s = down 
    d = right 
    '''
)

# the map using a 2d array
# 0 = wall
# 1 = walkable
# 2 = Power
# 3 = return to start
# 4 = exit
#User Input
# w=up, a=left, s=down, and d=right)


map = {}
map[0] = {0,0,0,0,0,0,0,0,0,0}
map[1] = {1,1,1,0,2,1,3,0,4,0}
map[2] = {1,0,1,0,0,1,0,0,1,3}
map[3] = {1,0,1,1,1,1,1,0,1,0}
map[4] = {1,0,1,0,1,0,1,0,1,1}
map[5] = {1,0,1,0,1,0,1,0,0,1}
map[6] = {1,0,1,0,1,0,1,0,2,1}
map[7] = {1,0,1,1,1,0,1,0,0,1}
map[8] = {1,0,0,0,0,0,1,1,1,1}
map[9] = {1,1,1,3,0,0,0,0,0,0}

start_point = [7,2]
user = start_point
user_moves = 2

while user_moves > 0:
    user_moves -= 1
    direction = input("Enter direction: ")
    if direction == "w":
      user[0]-=1
    if direction == "s":
        user[0] +=1
    if direction == "d":
        user[1]+=1
    if direction == "a":
        user[1] -=1

        # this uses the values for location based on user input 
    new_value = map[user[0]][user[1]]


