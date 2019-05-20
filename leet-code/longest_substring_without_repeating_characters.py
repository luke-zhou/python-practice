def lengthOfLongestSubstring(s: str) -> int:
    max = len(set(s))

    end = 1
    start = 0
    longest = 0
    while end-start<=max and start<len(s) and end<=len(s):
        test_string = s[start:end]
        duplicate_index = findDuplicate(test_string)
        if duplicate_index !=-1:
            start += 1 + duplicate_index
            end += 1 + duplicate_index
        else:
            longest = end-start
            end += 1

    return longest     
    
def findDuplicate(s: str) -> int:
    index_dic = {}
    for i, c in enumerate(s):
        if c not in index_dic:
            index_dic[c] =i
        else:
            return index_dic[c]
    
    return -1 

if __name__=='__main__':
    result = lengthOfLongestSubstring('abcadc')
    print(result)
    # result = findDuplicate('pabkww')
    # print(result)