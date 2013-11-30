# http://community.topcoder.com/stat?c=problem_statement&pm=3075


class HiddenNumbers:
    def findNums(self, text):
        """
        >>> h = HiddenNumbers()
        >>> h.findNums("12 abc3 4 17")
        ['12', '3', '4', '17']
        >>> h.findNums("098m03r9f80239802389f0m9KDKLKLJDKLJm0983m890DMOm03dlkfj3hljf4h3klhl  4j4 444 44  rjhkrrkr34534539893 390804980498409480 dkldjkl djkl djkl d00000002998")
        ['098', '03', '9', '80239802389', '0', '9', '0983', '890', '03', '3', '4', '3', '4', '4', '444', '44', '34534539893', '390804980498409480', '00000002998']
        """
        nums = []
        cur_num = []
        digits = "0123456789"
        for char in text:
            if char in digits:
                cur_num.append(char)
            elif cur_num:
                nums.append("".join(cur_num))
                cur_num = []
        if cur_num:
            nums.append("".join(cur_num))        
        return nums
    
    def leadingZeros(self, num):
        zeros = 0
        if num[0] != "0":
            return zeros
        else:
            while num[zeros] == "0" and len(num) > (zeros+1) :
                zeros += 1
        return zeros            
    
    def findAll(self, text):
        """
        >>> h = HiddenNumbers()
        >>> h.findAll(["098m03r9f80239802389f0m9KDKLKLJDKLJm0983m890DMOm03","dlkfj3hljf4h3klhl  4j4 444 44  rjhkrrkr34534539893", " 390804980498409480 dkldjkl djkl djkl d00000002998"])
        ['9', '44', '098', '444', '890', '0983', '00000002998', '34534539893', '80239802389', '390804980498409480']
        >>> h.findAll(["39 000220 30 skldjdije939939slkk 3090 2912kjdk3949","dlkjd dkljsl098 dkd3 23kdkdkl 0000002222kdjdie9000"])
        ['0000002222', '2912', '3090', '3949', '9000', '939939']
        >>> h.findAll([])
        []
        >>> h.findAll(["0022 22k00022a022"])
        ['0022', '00022']
        """
        text = "".join(text)
        nums = self.findNums(text)
        sortable_nums = []
        for i in nums:
            sortable_nums.append((int(i), self.leadingZeros(i), i))
        sort = list(reversed(sorted(sortable_nums)))
        total = len(sort)
        ret = total / 2 + (total % 2)
        return list(reversed([s[2] for s in sort[0:ret]]))
        
import doctest
doctest.testmod()        