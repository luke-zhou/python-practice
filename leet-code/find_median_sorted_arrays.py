class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len==0:
            return self.get_median(nums2)
        elif nums2_len==0:
            return self.get_median(nums1)
        else:
            nums1_median = self.get_median(nums1)
            nums2_median = self.get_median(nums2)
            if nums1_median == nums2_median:
                return nums1_median
            
            if nums1_len < nums2_len:
                remove_len = int(nums1_len/2)
                if nums1_len%2==0:
                    remove_len -=1
            else:
                remove_len = int(nums2_len/2)
                if nums2_len%2==0:
                    remove_len -=1
            
            if remove_len==0:
                return self.merge_get_median(nums1, nums2)

            if nums1_median < nums2_median:
                new_nums1 = nums1[remove_len:]
                new_nums2 = nums2[:-remove_len]
                print(new_nums1)
                print(new_nums2)
                print('1 less 2')
                return self.find_median_sorted_arrays(new_nums1, new_nums2)
            else:
                new_nums1 = nums1[:-remove_len]
                new_nums2 = nums2[remove_len:]
                print(new_nums1)
                print(new_nums2)
                print('2 less 1')
                return self.find_median_sorted_arrays(new_nums1, new_nums2)

                    
                
           
    def get_median(self, list):
        length = len(list)
        halfLength = int(length/2)
        if length%2==0:
            median = (list[halfLength]+list[halfLength-1])/2
        else:
            median = list[halfLength] 
        return median
    
    def merge_get_median(self, nums1, nums2):
        i = 0
        j = 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i +=1
            else:
                nums.append(nums2[j])
                j +=1

        if i < len(nums1):
            nums.extend(nums1[i:])
        elif j < len(nums2):
            nums.extend(nums2[j:])
        return self.get_median(nums)

if __name__ == '__main__':
    nums1=[1, 2, 6, 7]
    nums2=[3, 4, 5, 8]
    result = Solution().find_median_sorted_arrays(nums1, nums2)
    print(result)