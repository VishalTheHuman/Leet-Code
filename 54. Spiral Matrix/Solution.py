class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_limits = [0, len(matrix[0])-1]
        y_limits = [0, len(matrix)-1]
        result = []
        elements = len(matrix) * len(matrix[0])
        i = j = 0
        count = 0
        while count < elements:
            #####################################
            while j <= x_limits[1]:
                result.append(matrix[i][j])
                count += 1
                j += 1
            j -= 1
            i += 1
            x_limits[1] -= 1
            if (count == elements): break
            #####################################
            while i <= y_limits[1]:
                result.append(matrix[i][j])
                count += 1
                i += 1
            i -= 1
            j -= 1
            y_limits[1] -= 1
            if (count == elements): break
            #####################################
            while j >= y_limits[0]:
                result.append(matrix[i][j])
                count += 1
                j-=1
            j+=1
            i-=1
            y_limits[0] += 1
            if (count == elements): break
            #####################################
            while i > x_limits[0]:
                result.append(matrix[i][j])
                count += 1
                i-=1
            i += 1
            j += 1
            x_limits[0] += 1
            #####################################
        return result
