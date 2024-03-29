class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "1234567890"
        window_size = len(str(low))
        max_size = len(str(high))
        result = []
        within_range = True
        i = 0
        while window_size<=max_size:
            i = window_size
            while i < 10:
                val = int(nums[i-window_size:i])
                if low <= val <= high:
                    result.append(val)
                i+=1
            window_size+=1
        return result
