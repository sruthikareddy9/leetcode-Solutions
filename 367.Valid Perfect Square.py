class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 1, num // 2
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return False

        
