class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if length==0:
            return s
        longest_str=""
        len_longest_str=0
        if self.isEven(length):
            start_index=[length/2-1, length/2]
        else:
            start_index=[int(length/2)]
        
        result = self.findLongest(s, start_index)
            
            
    def findLongest(self, s:str, index:list) -> str:
        left = index[0]
        right = index[-1]
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                return s[left+1:right]
            left-=1
            right+=1
        return s
        
    def isEven(self, num: int) -> bool:
        return num%2==0
    
    def old_way(self, s: str) -> str:
        length = len(s)
        for i in reversed(range(length)):
            start = 0
            while start+i < length:
                test_string= s[start:start+i+1]
                #print(test_string)
                result = self.isPalindrome(test_string)
                if result:
                    return test_string
                start +=1
        return s  
    
    def isPalindrome(self, s: str) -> bool:
        result = True
        start = 0
        end = len(s)-1
        while end-start>0:
            if s[start] != s[end]:
                result=False
                break
            start +=1
            end -=1
        return result

if __name__=='__main__':
    result = Solution().findLongest("abcbdf", [3,4])
    print(result)