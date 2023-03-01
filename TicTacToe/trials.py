from copy import deepcopy

EMPTY = None
X = "X"
O = "O"

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

plays = []
plays = [(1, (1,0)), (0, (0,0))]
print(sorted(plays, key=lambda x:x[0], reverse=True))
       




