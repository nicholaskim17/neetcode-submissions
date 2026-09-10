class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {} #key: num, val: freq

        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] +=1
            else:
                hm[nums[i]] = 1
            
        arr = []

        for i in range(len(nums)):
            arr.append([])

        for key, value in hm.items():
            arr[value - 1].append(key)

        fin = []

        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                fin.append(num)
                if len(fin) == k:
                    return fin








        

        
            
        

        
            