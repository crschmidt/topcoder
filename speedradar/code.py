# http://community.topcoder.com/stat?c=problem_statement&pm=6474

class SpeedRadar:
    def averageSpeed(self, min, max, readings):
        """
        >>> s = SpeedRadar()
        >>> s.averageSpeed(1,50,[45,40,50])
        45.0
        >>> s.averageSpeed(1,50,[42,43,44,45,46,47,48,49,50,51])
        46.0
        >>> s.averageSpeed(1,50,[42,46,48,50,52])
        0.0
        >>> s.averageSpeed(20,60,[25,45,45,43,24,9,51,55,60,34,61,23,40,40,47,49,33,23,47,54,54])
        41.68421052631579
        >>> s.averageSpeed(47, 68, [63, 67, 66, 68, 51, 61, 51, 52, 60, 57, 62, 68, 65, 68, 49, 50, 48, 60, 66, 59, 64, 49, 53, 48, 67, 47, 60, 55, 66, 65, 47, 59, 61, 47, 48, 52, 49, 67, 67, 54, 67, 63, 54, 47, 53, 56, 49, 52, 46, 49])
        57.265306122448976
        >>> s.averageSpeed(1, 1, [1, 1, 1, 2, 2, 2])
        0.0
        """
        failed = len(filter(lambda x: x<min or x>max, readings))
        if float(failed) / len(readings) > .1:
            return 0.0
        else:
            inlimit = filter(lambda x: x>=min and x<=max, readings)
            return float(sum(inlimit))/len(inlimit)
            
import doctest
doctest.testmod()            