class Solution(object):
    def removeElements(self,nums,val):
        k=0
        for i in range (len(nums)):
            if nums[i]!= val:
                nums[k] = nums[i]
                k +=1
                return k
            
solution = Solution()
nums=[0,1,2,2,3,0,4,2]
k=solution.removeElements(nums,2)
print(k)
            
