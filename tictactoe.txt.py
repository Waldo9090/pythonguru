board = [0,1,2,3,4,5,6,7,8]
print(board[0] , '|' , board[1] , '|' , board[2])
print('_________')
print(board[3] , '|' , board[4] , '|' , board[5])
print('_________')
print(board[6] , '|' , board[7] , '|' , board[8])
while True:
    p1 = input('Player 1, enter a spot')
    p1 = int(p1)
    if board[p1] != 'o':
        board[p1] = 'x'
    if board[p1] == 'o':
        p1w = input('Choose a diffrent spot , this spot is taken :')
        p1w = int(p1w)
        board[p1w] = 'x'
    
    print(board[0] , '|' , board[1] , '|' , board[2])
    print('_________')
    print(board[3] , '|' , board[4] , '|' , board[5])
    print('_________')
    print(board[6] , '|' , board[7] , '|' , board[8])
    p2 = input('Player 2, enter a spot')
    p2 = int(p2)
    if board[p2] != 'x':
        board[p2] = 'o'
    if board[p2] == 'x':
        p2w = input('Choose a diffrent spot , this spot is taken :')
        p2w = int(p2w)
        board[p2w] = 'o'
    print(board[0] , '|' , board[1] , '|' , board[2])
    print('_________')
    print(board[3] , '|' , board[4] , '|' , board[5])
    print('_________')
    print(board[6] , '|' , board[7] , '|' , board[8])
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x':
        print('X wins')
        break
    if board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        print('X wins')
        break
    if board[6] == 'x' and board[6] == 'x' and board[8] == 'x':
        print('X wins')
        break
       
    
    
    if board[0] == 'x' and board[4] == 'x' and board[8] == 'x':
        print('X wins')
        break
    if board[6] == 'x' and board[4] == 'x' and board[2] == 'x':
        print('X wins')
        break
    
    
    
    
    if board[0] == 'x' and board[3] == 'x' and board[6] == 'x':
        print('X wins')
        break
    if board[4] == 'x' and board[1] == 'x' and board[7] == 'x':
        print('X wins')
        break
    if board[8] == 'x' and board[5] == 'x' and board[2] == 'x':
        print('X wins')
        break
    
    
    
    
    
    
    if board[0] == 'o' and board[1] == 'o' and board[2] == 'o':
        print('O wins')
        break
    if board[3] == 'o' and board[4] == 'o' and board[5] == 'o':
        print('O wins')
        break
    if board[6] == 'o' and board[6] == 'o' and board[8] == 'o':
        print('O wins')
        break
       
    
    
    if board[0] == 'o' and board[4] == 'o' and board[8] == 'o':
        print('X wins')
        break
    if board[6] == 'o' and board[4] == 'o' and board[2] == 'o':
        print('X wins')
        break
    
    
    
    
    if board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        print('O wins')
        break
    if board[4] == 'o' and board[1] == 'o' and board[7] == 'o':
        print('O wins')
        break
    if board[8] == 'o' and board[5] == 'o' and board[2] == 'o':
        print('O wins')
        break
    
    
    
    
    #if board[0] == 'x' or 'o' and board[1] == 'x' or 'o' and board[2] == 'x' or 'o' and board[3] == 'x' or 'o' and board[4] == 'x' or 'o' and board[5] == 'x' or 'o' and board[6] == 'x' or 'o'and board[7] == 'x' or 'o' and board[8] == 'x' or 'o':
    if board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8:      
   
        print('tie, no one wins')
        break