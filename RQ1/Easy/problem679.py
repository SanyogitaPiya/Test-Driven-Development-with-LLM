class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        EPSILON = 1e-6
        
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = []
                        for k in range(len(nums)):
                            if k != i and k != j:
                                next_nums.append(nums[k])
                        
                        for op in range(4):
                            if op < 2 and j > i:
                                continue
                            if op == 0:
                                next_nums.append(nums[i] + nums[j])
                            elif op == 1:
                                next_nums.append(nums[i] * nums[j])
                            elif op == 2:
                                next_nums.append(nums[i] - nums[j])
                            else:
                                if abs(nums[j]) < EPSILON:
                                    continue
                                next_nums.append(nums[i] / nums[j])
                            
                            if dfs(next_nums):
                                return True
                            
                            next_nums.pop()
            
            return False
        
        nums = [float(num) for num in cards]
        return dfs(nums)
