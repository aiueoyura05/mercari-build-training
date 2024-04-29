class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        test = {}
        for i in range(1, len(nums)+1):  
            test[i] = 0
        for i in nums:
            test[i] += 1
        result = []
        for key, val in test.items():
            if val == 0:
                result.append(key)
        return result
    
