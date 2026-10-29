class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        master = []
        for num in nums:
            master.append([])
        hm = {} #k: num v: freq

        for num in nums:

            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        for num, freq in hm.items():
            master[freq - 1].append(num)

        
        final = []
        a = len(nums) - 1
        while len(final)!=k:

            if master[a] == []:
                a-=1
            else:
                final.append(master[a][-1])
                master[a].pop()

        return final
            


            






