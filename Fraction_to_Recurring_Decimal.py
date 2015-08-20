class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        a, b = numerator, denominator
        d = float(a) / b
        ret = str(abs(int(d)))
        if d < 0:
            a = abs(a)
            b = abs(b)
            ret = '-' + ret

        a = a % b
        if not a:
            return ret

        ret += '.'
        result = []
        index = 0
        mod = {}
        while True:
            p = a % b
            a = p * 10
            if not a:
                for c in result:
                    ret += str(c)
                return ret
            result.append(a / b)

            if p not in mod:
                mod[p] = index
            else:
                for i in range(mod[p]):
                    ret += str(result[i])
                ret += '('
                for i in range(mod[p], index):
                    ret += str(result[i])
                ret += ')'
                return ret

            index += 1