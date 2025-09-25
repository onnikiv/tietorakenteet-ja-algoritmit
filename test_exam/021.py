def tower_of_hanoi(count, stacks=None, source=0, auxiliary=1, destination=2, moves=0):
    if not stacks:
        stacks = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] for i in range(count-1, -1, -1)], [], []]
        moves = 1
        print(stacks)
    # COMPLETE FROM HERE
   
    
    print(stacks[destination])
    print(stacks[auxiliary])
    print(stacks[source])

    stacks[destination] = stacks[source].pop(0)
    
    
    print(stacks)
    return moves
    

    
print(tower_of_hanoi(3))