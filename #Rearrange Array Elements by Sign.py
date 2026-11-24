#Rearrange Array Elements by Sign
nums = [3, 1, -2, -5, 2, -4,-10,10,3,-1,5,6,-7,8,-9,11,-12,13,-14,15]
class Solution:
    def rearrangeArray(self, nums):
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]

        for i in range(min(len(pos), len(neg))):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums

sp = Solution()
print(sp.rearrangeArray(nums))

#optimized solution
print("Optimized solution")

class Solution:
    def rearrangeArray(self, nums):
        result = [0] * len(nums)
        pos_index, neg_index = 0, 1
        for num in nums:
            if num > 0:
                result[pos_index] = num
                pos_index += 2
            else:
                result[neg_index] = num
                neg_index += 2
        return result

sp = Solution()
print(sp.rearrangeArray(nums))