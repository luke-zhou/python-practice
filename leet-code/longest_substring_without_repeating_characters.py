def lengthOfLongestSubstring(s:str):
    max = len(set(s))
            
    end = 1
    start = 0
    longest = 0
    while end-start<=max and start<len(s) and end<=len(s):
        test_string = s[start:end]
        print(end)
        print(start)
        print(test_string)
        if len(test_string)>len(set(test_string)):
            start += 1
            end += 1
        else:
            longest = end-start
            end += 1
    
    return longest    

if __name__=='__main__':
    print(lengthOfLongestSubstring('pwwkew'))