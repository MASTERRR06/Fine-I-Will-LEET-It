class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i]=arr[i]+arr[i-1]
        return(arr)