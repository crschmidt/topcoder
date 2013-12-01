# http://community.topcoder.com/stat?c=problem_statement&pm=12816

import doctest

class GoodNumbers:
    def count(self, a, b, N):
        """
        >>> gn = GoodNumbers()
        >>> gn.count([4],[3],20)
        4
        >>> gn.count([3,2],[2,3], 9)
        5
        >>> gn.count([5,15,5,15],[4,4,2,2],50)
        8
        >>> gn.count([1],[1],1000)
        0
        >>> gn.count([168120222,756,408,194,681,856,964,677,250,845], [809,652,204,532,420,10,640688057,55,174076738,318], 1000000000)
        16328141
        """
        total = 0
        for i in xrange(1, N+1):
            for j in xrange(len(a)):
                if i%a[j] == 0 and not i% b[j]==0:
                    total += 1
                    break
        return total
        
doctest.testmod()        