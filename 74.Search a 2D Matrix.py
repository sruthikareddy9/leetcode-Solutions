class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=n*m-1
        while(low<=high):
            mid=(low+high)//2
            row=mid//m
            column=mid%m
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                low=mid+1
            else:
                high=mid-1
        return False
