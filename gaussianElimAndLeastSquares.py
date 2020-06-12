# M is an mxn 2d list representing a matrix
import copy
import math
import matplotlib.pyplot as plt
from functools import reduce

def prettyPrint(s, M):
    if s != "":
        print(s)
    print("[", end="")
    for row in M:
        print("%-.3f " * len(row) % tuple(row))
    print("]")

def swapRows(M, r1, r2):
    temp = copy.deepcopy(M[r2])
    for i in range(len(M[r1])):
        M[r2][i] = M[r1][i]
    # print(M[r2])
    # print(temp)
    for j in range(len(temp)):
        M[r1][j] = temp[j]
    return M

def gaussianElimination(M, stopCol=0):
    m = len(M) # number of rows 
    n = len(M[0])
    # n = len(M[0]) # number of columns
    i = 0
    j = 0
    if stopCol == 0:
        stopCol = n

    while (i < m and j < stopCol):
        col = [(M[x][j], x) for x in range(i, m)]
        compare = lambda a,b: a if abs(a[0]) > abs(b[0]) else b
        pivot = reduce(compare, col)
        if (pivot[0] == 0):
            # go to next column
            # print("no good")
            j += 1
        else:
            pivotRow = pivot[1]
            #  print("")
            # print("i", i)
            # print("pivrow", pivotRow)
            # print("")

            M = swapRows(M, pivotRow, i)
            for a in range(i+1, m):
                # reduce the subsequent rows of the matrix by the max
                # cancelling the first value of each row below
                multiplyFactor = M[a][j] / M[i][j]
                M[a][j] = 0
                # print("mf:", multiplyFactor)
                # subtract from the rest of the items
                for b in range(j+1, n):
                    M[a][b] = M[a][b] - multiplyFactor * M[i][b]
                print("\nMF:", multiplyFactor)
                prettyPrint("At this step:", M)
            i += 1
            j += 1
            # print("i", i)
            # print("j", j)
    return M 

# naive matrix multiplication algorithm
def matMul(A, B, scalarA):
    if (scalarA):
        for row in range(len(B)):
            for col in range(len(B[0])):
                B[row][col] = A * B[row][col]
        return B

    if (len(A[0]) != len(B)):
        print(len(A[0]))
        print(len(B))
        return None

    Q = [[0 for i in range(len(B[0]))] for j in range(len(A))]

    for row in range(len(A)):
        for col in range(len(B[0])):
            for i in range(len(B)):
                # print(A[row][i])
                # print(B[i][col])
                Q[row][col] += A[row][i] * B[i][col]
    return Q
# assumes the augmented matrix
def backSub(M):
    m = len(M)
    n = len(M[0])
    xs = [0] * (n - 1)
    # print(xs)
    pivots = []

    # identify pivot variables
    for row in range(len(M)):
        for col in range(len(M[0])):
            if (M[row][col] != 0):
                pivots.append(col)
                break

    # all frees, just set to 0
    if len(pivots) == 0:
        return xs
    # sets to final pivot column if taller than wide
    i = max(pivots)
    # if square or wide, then start from last col
    if (m < n-1):
        i = m-1
    j = n-2
    # print("Pivots", pivots)
    # print("i", i)
    while (i >= 0 and j >= 0):
        # if its a free var, go back a column
        if j not in pivots:
            j -= 1 
            continue
        # find y value of augmented matrix
        yi = M[i][n-1]
        # get the x value by dividing its coefficient
        xi = yi / M[i][j] 
        # insert into list of xs
        xs[j] = xi
        # update the upper parts of the matrix using newfound xi
        for k in range(i-1, -1, -1):
            M[k][n-1] = M[k][n-1] - M[k][j]*xi
        i -= 1
        j -= 1
    return xs

def transpose(M):
    Mt = [[0 for i in range(len(M))] for j in range(len(M[0]))]
    for row in range(len(M)):
        for col in range(len(M[0])):
            Mt[col][row] = M[row][col]
    return Mt
    


def leastSquares(points, degree=1):
    A = [[0 for i in range(degree+1)] for j in range(len(points))]
    x = []
    y = [[p[1]] for p in points] 
    for row in range(len(A)):
        for col in range(len(A[0])):
            xp = points[row][0]
            if col == 0:
                A[row][col] = 1
            else:
                A[row][col] = math.pow(xp, col)
    At = transpose(A)
    # prettyPrint("", At)
    # prettyPrint("\n", y)
    AtA = matMul(At, A, False)
    # prettyPrint("Before transform", AtA)
    Atb = matMul(At, y, False)
    # print(Atb)
    for i in range(len(Atb)):
        AtA[i].append(Atb[i][0])
    # prettyPrint("After transform", AtA)
    AtA = gaussianElimination(AtA)
    xhat = backSub(AtA)

    return xhat



def main():
    M = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    M = gaussianElimination(M)
    prettyPrint("\n", M)
    M = [[ 2,  1, -1, 8],
         [-3, -1,  2, -11],
         [-2,  1,  2, -2]]
    M = gaussianElimination(M, 2)
    prettyPrint("\n", M)
    N = backSub(M)
    print(N)
    M = [[2, 4, -2, 8, 4, 6],
         [3, 6, 1, 12, -2, 1],
         [9, 18, 1, 36, 38, 0]]
    M = gaussianElimination(M, 4)
    N = backSub(M)
    print(N)
    prettyPrint("\n", M)
    M = [[1, 0, 3, 8],
         [0, 1, 7, 9],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    M = gaussianElimination(M, 3)
    N = backSub(M)
    print(N)
    prettyPrint("\n", M)

    A = [[1, -3, 5],
         [9, -11, -1]]
    prettyPrint("transpose", transpose(A))
    M = gaussianElimination(A, 2)
    prettyPrint("A", M)
    print(backSub(M))
    points = [[0, 1],
              [2, 4],
              [-1, 2],
              [1, 3]]
    xhat = leastSquares(points, degree=4)
    xstart = -5
    xend = 6
    graphX = []
    graphY = []
    for i in range(xstart, xend):
        totalY = 0
        for j in range(len(xhat)):
            totalY += xhat[j] * math.pow(i, j)
        graphX.append(i)  
        graphY.append(totalY)
    plt.xkcd()
    plt.plot(graphX, graphY)
    xPoints = [p[0] for p in points]
    yPoints = [p[1] for p in points]
    plt.scatter(xPoints, yPoints, color='red')
    plt.show()

    # prettyPrint("\n", Q)


if __name__ == '__main__':
    main()





        


 



