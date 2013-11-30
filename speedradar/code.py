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
        """
        failed = len(filter(lambda x: x<min or x>max, readings))
        if float(failed) / len(readings) > .1:
            return 0.0
        else:
            inlimit = filter(lambda x: x>=min and x<=max, readings)
            return float(sum(inlimit))/len(inlimit)
            
import doctest
doctest.testmod()            