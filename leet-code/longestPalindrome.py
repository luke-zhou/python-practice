class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if length==0:
            return s
        longest_str=""
        len_longest_str=0
        if self.isEven(length):
            start_index=[int(length/2)-1, int(length/2)]
            start_index_list=[[start_index[0]],[start_index[1]]]
        else:
            start_index=[int(length/2)]
            start_index_list=[[start_index[0]-1, start_index[0]],[start_index[0], start_index[0]+1]]
        
        longest_str = self.findLongest(s, start_index)
        len_longest_str = len(longest_str)
        
        while self.inRange(start_index_list):
            result1 = self.findLongest(s, start_index_list[0])
            result2 = self.findLongest(s, start_index_list[1])
            if len(result1)> len_longest_str:
                len_longest_str= len(result1)
                longest_str=result1
            if len(result2)> len_longest_str:
                len_longest_str= len(result2)
                longest_str=result2
            start_index_list = self.expand(start_index_list)
        
        return longest_str
            
    def expand(self, start_index_list) -> list:
        new_list =[[],[]]
        if len(start_index_list[0])==1:
            new_list[0]=[start_index_list[0][0]-1, start_index_list[0][0]]
            new_list[1]=[start_index_list[1][0], start_index_list[1][0]+1]
        else:
            new_list[0]=[start_index_list[0][0]]
            new_list[1]=[start_index_list[1][1]]
        return new_list
    
    def inRange(self, start_index_list) -> bool:
        return start_index_list[0][0]>=0
    
    def findLongest(self, s:str, index:list) -> str:
        left = index[0]
        right = index[-1]

        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                return s[left+1:right]
            left-=1
            right+=1

        min_len = min(index[0], len(s)-1-index[-1])
        
        return s[index[0]-min_len:index[-1]+min_len+1]
        
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
    
    def manacher(self, s0 : str) -> list:
        T = '$#' + '#'.join(s0) + '#@'
        l = len(T)
        P = [0] * l
        R, C = 0, 0
        for i in range(1,l-1):
            if i < R:
                P[i] = min(P[2 * C - i], R - i)
            
            while T[i+(P[i]+1)] == T[i-(P[i]+1)]:
                P[i] += 1
            
            if P[i] + i > R:
                R = P[i] + i
                C = i
        return P

if __name__=='__main__':
    result = Solution().manacher("ecaacd")
    print(list('$#' + '#'.join("ecaacd") + '#@'))
    result_str=[str(i) for i in result]
    print(result_str)