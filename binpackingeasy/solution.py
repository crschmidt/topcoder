# http://community.topcoder.com/stat?c=problem_statement&pm=12862

class BinPackingEasy:
    def minBins(self, items):
        """
        >>> bpe = BinPackingEasy()
        >>> bpe.minBins([150, 150, 150, 150, 150])
        3
        >>> bpe.minBins([130, 140, 150, 160])
        2
        >>> bpe.minBins([101, 101, 101, 101, 101, 101, 101, 101, 101])
        5
        >>> bpe.minBins([101, 200, 101, 101, 101, 101, 200, 101, 200])
        6
        >>> bpe.minBins([123, 145, 167, 213, 245, 267, 289, 132, 154, 176, 198])
        8
        >>> bpe.minBins([100, 200, 100, 100, 100, 100, 200, 100, 200])
        4
        >>> bpe.minBins([100, 100, 100, 100, 100, 100, 100, 100, 100])
        3
        """
        bins = []
        items.sort()
        items.reverse()
        while items:
            biggest = items.pop(0)
            for i, b in enumerate(bins):
                if b + biggest <= 300:
                    bins[i] = b+biggest
                    break
            else:
                bins.append(biggest)

        return len(bins)

import doctest
doctest.testmod()
