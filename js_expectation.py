import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def get_expectation(decknum):
    #decknum must be even
    s = 0
    for n in range(1,decknum/2):
        if n % 2 == 0 :
            summation = sum([ ncr(n,i) for i in range(max(0,n-decknum/2/2),min(decknum/2/2,n)+1) ])*2**(decknum/2-n)
            s += ncr(decknum/2, n)*summation*(2*n-decknum/2)
    return 1.0*s/ncr(decknum, decknum/2)




if __name__ == '__main__':
    print get_expectation(52)