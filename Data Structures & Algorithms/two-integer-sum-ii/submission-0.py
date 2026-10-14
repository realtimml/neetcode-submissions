class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if (sum := numbers[i] + numbers[j]) == target:
                break
            elif sum > target:
                j -= 1
            else:
                i += 1
            # print(sum, i, j + 1)
        
        return [i + 1, j + 1]