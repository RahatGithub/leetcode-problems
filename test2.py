class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []

        for i in range(len(nums1)) : 
                
            for j in range(len(nums2)) : 
                if nums1[i] == nums2[j] : 
                    res.append(nums2[j])
                    del nums2[j]
                    break
        
        return res