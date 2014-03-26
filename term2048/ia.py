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
                newBoard.move(m,add_tile=True)
                
                score = AI.evaluate(newBoard)
                if depth != 0:
                    my_m,my_s = AI.nextMoveRecur(newBoard,depth-1,maxDepth)
                    score += my_s*pow(base,maxDepth-depth+1)
                    
                if(score > bestScore):
                    bestMove = m
                    bestScore = score
        return (bestMove,bestScore);

    @staticmethod
    def evaluate(board,commonRatio=0.25):
        linearWeightedVal = 0
        invert = False
        weight = 1.
        malus = 0
        for y in range(0,board.size()):
            for x in range(0,board.size()):
                b_x = x
                if invert:
                    b_x = board.size() - 1 - x
                #linearW
                currVal=board.getCell(b_x,y)
                linearWeightedVal += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        linearWeightedVal2 = 0
        invert = False
        weight = 1.
        malus = 0
        for x in range(0,board.size()):
            for y in range(0,board.size()):
                b_y = y
                if invert:
                    b_y = board.size() - 1 - y
                #linearW
                currVal=board.getCell(x,b_y)
                linearWeightedVal2 += currVal*weight
                weight *= commonRatio
            invert = not invert
            
        return max(linearWeightedVal,linearWeightedVal2)
        