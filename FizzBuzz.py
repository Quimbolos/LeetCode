'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


https://leetcode.com/problems/fizz-buzz/
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        customarray = []
        
        for i in range(1,n+1):
            customarray.append(i)
            
        for i in range(0,len(customarray)):
            
            
            if (customarray[i] % 3 == 0) and (customarray[i] % 5 == 0):
                answer.append("FizzBuzz")
            
            elif customarray[i] % 3 == 0:
                answer.append("Fizz")
                
            elif customarray[i] % 5 == 0:
                answer.append("Buzz")
                
            else:
                answer.append(str(customarray[i]))
            
        return(answer)
            
            
