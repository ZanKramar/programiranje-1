from functools import lru_cache

test_matrix =  [
     [1 , 2 , 0 ],
     [ 2 , 4 , 5 ],
     [ 7 , 0 , 1 ]
     ]


def max_sir(matrika):
    a = len(matrika)
    try:
        b = len(matrika[0])
    except:
        IndexError
        return 0
    @lru_cache()
    def max_index(i, j):
        if i == a or j == b:
            return 0
        return matrika[i][j] + max(
            matrika[i+1][j],
            matrika[i][j+1]
        )
    return max_index(0,0)

print(max_sir(test_matrix))
import sys 
sys.setrecursionlimit(10**9)
print(max_sir([[j for j in range(2000)] for _ in range (20)]))

            
    