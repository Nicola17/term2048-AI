from term2048.board import Board
import random
import copy

class AI(object):
    def __str__(self, margins={}):
        return ""
        

    @staticmethod
    def randomNextMove(board):
        '''
        It's just a test for the validMove function
        '''
        if board.validMove(Board.UP):
            print ("UP: ok")
        else:
            print ("UP: no")
        if board.validMove(Board.DOWN):
            print ("DOWN: ok")
        else:
            print ("DOWN: no")
        if board.validMove(Board.LEFT):
            print ("LEFT: ok")
        else:
            print ("LEFT: no")
        if board.validMove(Board.RIGHT):
            print ("RIGHT: ok")
        else:
            print ("RIGHT: no")
        rm = random.randrange(1, 5)
        print rm 
        return rm
    
    @staticmethod
    def nextMove(board,recursion_depth=3):
        m,s = AI.nextMoveRecur(board,recursion_depth,recursion_depth)
        return m
        
    @staticmethod
    def nextMoveRecur(board,depth,maxDepth,base=0.9):
        bestScore = -1.
        bestMove = 0
        for m in range(1,5):
            if(board.validMove(m)):
                newBoard = copy.deepcopy(board)
                newBoard.move(m,add_tile=False)
                
                score, critical = AI.evaluate(newBoard)
                newBoard.setCell(critical[0],critical[1],2)
                if depth != 0:
                    my_m,my_s = AI.nextMoveRecur(newBoard,depth-1,maxDepth)
                    score += my_s*pow(base,maxDepth-depth+1)
                
                if(score > bestScore):
                    bestMove = m
                    bestScore = score
        return (bestMove,bestScore);

    #Hey!!! Don't judge me for this awful piece of code!!!
    #It's just a quick test...
    @staticmethod
    def evaluate(board,commonRatio=0.25):
        linearWeightedVal = 0
        invert = False
        weight = 1.
        malus = 0
        criticalTile = (-1,-1)
        for y in range(0,board.size()):
            for x in range(0,board.size()):
                b_x = x
                b_y = y
                if invert:
                    b_x = board.size() - 1 - x
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile == (-1,-1)):
                    criticalTile = (b_x,b_y)
                linearWeightedVal += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        linearWeightedVal2 = 0
        invert = False
        weight = 1.
        malus = 0
        criticalTile2 = (-1,-1)
        for x in range(0,board.size()):
            for y in range(0,board.size()):
                b_x = x
                b_y = y
                if invert:
                    b_y = board.size() - 1 - y
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile2 == (-1,-1)):
                    criticalTile2 = (b_x,b_y)
                linearWeightedVal2 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        
        linearWeightedVal3 = 0
        invert = False
        weight = 1.
        malus = 0
        criticalTile3 = (-1,-1)
        for y in range(0,board.size()):
            for x in range(0,board.size()):
                b_x = x
                b_y = board.size() - 1 - y
                if invert:
                    b_x = board.size() - 1 - x
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile3 == (-1,-1)):
                    criticalTile3 = (b_x,b_y)
                linearWeightedVal3 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        linearWeightedVal4 = 0
        invert = False
        weight = 1.
        malus = 0
        criticalTile4 = (-1,-1)
        for x in range(0,board.size()):
            for y in range(0,board.size()):
                b_x = board.size() - 1 - x
                b_y = y
                if invert:
                    b_y = board.size() - 1 - y
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile4 == (-1,-1)):
                    criticalTile4 = (b_x,b_y)
                linearWeightedVal4 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
            
        linearWeightedVal5 = 0
        invert = True
        weight = 1.
        malus = 0
        criticalTile5 = (-1,-1)
        for y in range(0,board.size()):
            for x in range(0,board.size()):
                b_x = x
                b_y = y
                if invert:
                    b_x = board.size() - 1 - x
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile5 == (-1,-1)):
                    criticalTile5 = (b_x,b_y)
                linearWeightedVal5 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        linearWeightedVal6 = 0
        invert = True
        weight = 1.
        malus = 0
        criticalTile6 = (-1,-1)
        for x in range(0,board.size()):
            for y in range(0,board.size()):
                b_x = x
                b_y = y
                if invert:
                    b_y = board.size() - 1 - y
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile6 == (-1,-1)):
                    criticalTile6 = (b_x,b_y)
                linearWeightedVal6 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        
        linearWeightedVal7 = 0
        invert = True
        weight = 1.
        malus = 0
        criticalTile7 = (-1,-1)
        for y in range(0,board.size()):
            for x in range(0,board.size()):
                b_x = x
                b_y = board.size() - 1 - y
                if invert:
                    b_x = board.size() - 1 - x
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile7 == (-1,-1)):
                    criticalTile7 = (b_x,b_y)
                linearWeightedVal7 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        linearWeightedVal8 = 0
        invert = True
        weight = 1.
        malus = 0
        criticalTile8 = (-1,-1)
        for x in range(0,board.size()):
            for y in range(0,board.size()):
                b_x = board.size() - 1 - x
                b_y = y
                if invert:
                    b_y = board.size() - 1 - y
                #linearW
                currVal=board.getCell(b_x,b_y)
                if(currVal == 0 and criticalTile8 == (-1,-1)):
                    criticalTile8 = (b_x,b_y)
                linearWeightedVal8 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        maxVal = max(linearWeightedVal,linearWeightedVal2,linearWeightedVal3,linearWeightedVal4,linearWeightedVal5,linearWeightedVal6,linearWeightedVal7,linearWeightedVal8)
        if(linearWeightedVal2 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal2
            criticalTile = criticalTile2
        if(linearWeightedVal3 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal3
            criticalTile = criticalTile3
        if(linearWeightedVal4 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal4
            criticalTile = criticalTile4
        if(linearWeightedVal5 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal5
            criticalTile = criticalTile5
        if(linearWeightedVal6 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal6
            criticalTile = criticalTile6
        if(linearWeightedVal7 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal7
            criticalTile = criticalTile7
        if(linearWeightedVal8 > linearWeightedVal):
            linearWeightedVal = linearWeightedVal8
            criticalTile = criticalTile8
        
        return maxVal,criticalTile