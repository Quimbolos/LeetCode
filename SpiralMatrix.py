'''
Given an m x n matrix, return all elements of the matrix in spiral order.

https://leetcode.com/problems/spiral-matrix/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix) # rows
        n = len(matrix[0]) # columns
        
        result = []

        length_matrix = m*n

        if m == n:

            while len(result) <= (length_matrix):

                if not matrix:
                    break

                if m*n == 1:
                    result.append(matrix[0][0])
                    break

                # Right scan -->
                for i in range(n):
                    result.append(matrix[0][i])
                del matrix[0]

                if not matrix:
                    break

                if m*n == 1:
                    result.append(matrix[0][0])
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns



                # Down scan 
                for i in range(m):
                    result.append(matrix[i][-1])
                    del matrix[i][-1]

                if not matrix[0]:
                    break


                if m*n == 1:
                    result.append(matrix[0][0])
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns



                # Left scan <--
                for i in range(n):
                    result.append(matrix[-1][-1*(i+1)])
                del matrix[-1]

                if not matrix:
                    break


                if m*n == 1:
                    result.append(matrix[0][0])
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns



                # Up Scan ^
                for i in range(m):
                    result.append(matrix[-1*(i+1)][0])
                    del matrix[-1*(i+1)][0]

                if m*n == 1:
                    result.append(matrix[0][0])
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns


        elif m != n:

            while len(result) <= (length_matrix):
                
                if not matrix[0]:
                    break
                    
                # Right scan -->
                for i in range(n):
                    result.append(matrix[0][i])
                del matrix[0]

                if not matrix:
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns

                # Down scan 
                for i in range(m):
                    result.append(matrix[i][-1])
                    del matrix[i][-1]

                if not matrix[0]:
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns


                # Left scan <--
                for i in range(n):
                    result.append(matrix[-1][-1*(i+1)])
                del matrix[-1]

                if not matrix:
                    break

                m = len(matrix) # rows
                n = len(matrix[0]) # columns

                # Up Scan ^
                for i in range(m):
                    result.append(matrix[-1*(i+1)][0])
                    del matrix[-1*(i+1)][0]

                m = len(matrix) # rows
                n = len(matrix[0]) # columns    
                
        return(result)
