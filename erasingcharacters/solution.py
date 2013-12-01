# http://community.topcoder.com/stat?c=problem_statement&pm=12863

class ErasingCharacters:
    def simulate(self, s):
        """
        >>> ec = ErasingCharacters()
        >>> ec.simulate("cieeilll")
        'cl'
        >>> ec.simulate("topcoder")
        'topcoder'
        >>> ec.simulate("abcdefghijklmnopqrstuvwxyyxwvutsrqponmlkjihgfedcba")
        ''
        >>> ec.simulate("bacaabaccbaaccabbcabbacabcbba")
        'bacbaca'
        >>> ec.simulate("eel")
        'l'
        """
        while True:
            for i, char in enumerate(s[:-1]):
                if s[i+1]==char:
                    s = "%s%s" % (s[0:i], s[i+2:])
                    break
            else:
                return s
                
import doctest
doctest.testmod()                