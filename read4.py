'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times. 
'''
#实际上这个read4是读取4个单词 并存到我们提供的tempbuff 里面 ， 我们需要将这个tempbuff转存到目标buff 里面， 每一次读取的时候若有多余的需要记录并提供给下次的read使用
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.last = []
        self.cnt = 0 
    def read(self, buf, n):
        # print buf, n
        if len(buf) == 0 or n <= 0:
            return 0
            
        else:
            ans = 0
            if self.cnt > 0:
                step = min(self.cnt, n)
                buf[:step] = self.last[:step]
                ans += step
                n -= step
                self.cnt -= step
                if self.cnt == 0:
                    self.last = []
                else:
                    for _ in xrange(step):
                        self.last.pop(0)
            if n <= 0:
                return ans
            else:
                while n > 0:
                    tmpBuff = [""] * 4
                    tmp = read4(tmpBuff)
                    # print tmpBuff
                    step = min(n , tmp)
                    # print "step is" , step
                    for index in xrange(step):
                        buf[ans+index] = tmpBuff[index]
                    ans += step
                    n -= step
                    if step < 4:
                        for index in xrange(step,tmp):
                            # print index, len(tmpBuff)
                            self.last.append(tmpBuff[index])
                            self.cnt += 1
                        break
            return ans
            
            
            
            
            
            
                 
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
