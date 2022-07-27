#Time Complexity: O(log n)
#Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0;
        high=len(nums)-1;
        if nums[0]<=nums[len(nums)-1]:
            return nums[0];
        while low<=high:
            mid=low+((high-low)//2);
            if nums[mid]>nums[mid+1]:
                return nums[mid+1];
            if nums[low]<=nums[mid]:
                low=mid+1;
            else:
                high=mid-1;
            