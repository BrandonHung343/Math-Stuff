''' Lagrange's polynomial interpolation
    you can approximate the polynomial by setting
    p(x) = L1(x)y1 + L2(x)y2 + ... LN(x)yn
    Lk(x) = ((x-x1)(x-x2)...(x-xn)) / ((xk-x1)(xk-x2)...(xk-xn))
    for a set of points ((x1, y1)...(xn, yn))

    Let's talk basic intuition about the polynomial. First thing, we want to assume the 
    number of points we have is going to guide the degree of the polynomial. In other
    words, we want to say that the degree of the polynomial is going to be n-1.

    Secondly, to fit the point to our polynomial, we want to force the polynomial. In other
    words, for a given point (xk, yk), we want that 

    p(xk) = yk

    We enforce this for ALL POINTS by using a forcing term. for Lk(x), we want that Lk(xk) = 1
    and forall j != k, Lj(xk) = 0. This way, we have the non-xk terms go to 0 and the 
    Lk(xk)yk = 1*yk = yk.

    The easiest way to construct this is simple to have (xk - xk) be in every single numerator 
    EXCEPT the numerator Lk(x). So we do this for each Lk(x) by excluding the (x - xk) term for 
    said value of k. 

    Now we need to normalize it. How do we do that? We need to divide the whole thing by the terms 
    we don't care about. Since for our non-zero Lk(x), we have (xk-x1)(xk-x2)...(xk-xn) missing term
    (xk - xk), then we simply divide by this and are done.
 
    '''



import matplotlib.pyplot as plt
from functools import *

def lagrange(points, n):
    X = [point[0] for point in points]
    Y = [point[1] for point in points]
    # print("X", X)
    # print("Y", Y)
    if n in X:
    	return Y[X.index(n)]

    subtraction = lambda a, b: a - b
    mult = lambda a, b: a * b
    add = lambda a, b: a + b

    Lks = []
    for xk in X:
        noXk = list(filter(lambda x: x != xk, X))

        ns = [n] * len(noXk)
        numerList = list(map(subtraction, ns, noXk))
        numer = reduce(mult, numerList)
        # print("Numerater", numer)

        xks = [xk] * len(noXk)
        denomList = list(map(subtraction, xks, noXk))
        # print("DenomList", denomList)
        nonZeroDenomList = list(filter(lambda x: x != 0, denomList))
        
        denom = reduce(mult, nonZeroDenomList)
        Lks.append(numer / denom)
    products = list(map(mult, Lks, Y))
    # print("Products", products)
    p = reduce(add, products)
    # print("Lks", Lks)
    # print("p", p)
    return p



def main():
    points = [[-1, 1], [1, 1], [0,0]]#, [-25, 6], [0, 6]]
    calcYs = []
    calcXs = []
    for i in range(-10, 11):
	    calcXs.append(i)
	    calcYs.append(lagrange(points, i))
    plt.plot(calcXs, calcYs)
    plt.show()

if __name__ == '__main__':
	main()






        






