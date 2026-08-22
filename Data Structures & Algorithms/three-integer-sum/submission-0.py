class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        i=0
        print(nums)
        while i < n-2:
            # while nums[i]==nums[i+2]:
            #     i+=1
            print(i)
            l=i+1
            r=n-1
            while l<r:
                curr_sum = nums[i]+nums[l]+nums[r]
                if curr_sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while nums[l]==nums[l+1] and l<r-1:
                        l+=1
                    while nums[r]==nums[r-1] and l<r:
                        r-=1
                    l+=1
                    r-=1
                    
                elif curr_sum < 0:
                    l+=1
                else:
                    r-=1
            i+=1
            while nums[i]==nums[i-1] and i < n-2:
                i+=1

        return ans