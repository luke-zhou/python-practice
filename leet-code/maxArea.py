class Solution:
    def maxArea(self, height: list) -> int:
        max_value = max(height)
        h = max_value
        max_area = 0;
        left_hash={}
        right_hash={}
        left = 0
        right = len(height)-1
        while h>0 and (max_area/h)<len(height):
            # print(h)
            if h in left_hash:
                left = left_hash[h]
            else:
                while left < right:
                    current_h = height[left]
                    if current_h>=h:
                        break
                    else:
                        if current_h not in left_hash:
                            left_hash[current_h] = left
                        left +=1
                
            # print(left)
            if h in right_hash:
                right = right_hash[h]
            else:
                while right >=left:
                    current_h = height[right]
                    if current_h>=h:
                        break
                    else:
                        if current_h not in right_hash:
                            right_hash[current_h] = right
                        right -=1
            
            # print(right)
            area = h *(right- left)
            if max_area< area:
                max_area = area
            h -=1
        
        return max_area

if __name__ == '__main__':
    print([8,10,14,0,13,10,9,9,11,11])
    result = Solution().maxArea([8,10,14,0,13,10,9,9,11,11])
    print(result)