'''
Given a roman numeral, convert it to an integer.

https://leetcode.com/problems/roman-to-integer/
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0

        for i in range(0,len(s)):

            if i+1 <= (len(s)-1):

                if s[i] == "C" and s[i+1] == "M":
                    number = number + 1000 - 100
                elif s[i] == "M":
                    if i >= 1 and s[i-1] == "C":
                        continue
                    else:
                        number = number + 1000

                elif s[i] == "C" and s[i+1] == "D":
                    number = number + 500 - 100
                elif s[i] == "D":
                    if i >= 1 and s[i-1] == 'C':
                        continue
                    else:
                        number = number + 500

                elif s[i] == "X" and s[i+1] == "C":
                    number = number + 100 - 10  
                elif s[i] == "C":
                    if i >= 1 and s[i-1] == 'X':
                        continue
                    else:
                        number = number + 100

                elif s[i] == "X" and s[i+1] == "L":
                    number = number + 50 - 10 
                elif s[i] == "L":
                    if i >= 1 and s[i-1] == 'X':
                        continue 
                    else:
                        number = number + 50

                elif s[i] == "I" and s[i+1] == "X":
                    number = number + 10 - 1                
                elif s[i] == "X":
                    if i >= 1 and s[i-1] == 'I':
                        continue 
                    else:
                        number = number + 10
                elif s[i] == "I" and s[i+1] == "V":
                    number = number + 5 - 1         
                elif s[i] == "V":
                    if i >= 1 and s[i-1] == 'I':
                        continue 
                    else:
                        number = number + 5

                elif s[i] == "I":
                    number = number + 1

            if i+1 > (len(s)-1):

                if s[i] == "M":
                    if i >= 1 and s[i-1] == "C":
                        continue
                    else:
                        number = number + 1000

                elif s[i] == "D":
                    if i >= 1 and s[i-1] == 'C':
                        continue
                    else:
                        number = number + 500          

                elif s[i] == "C":
                    if i >= 1 and s[i-1] == 'X':
                        continue
                    else:
                        number = number + 100

                elif s[i] == "L":
                    if i >= 1 and s[i-1] == 'X':
                        continue
                    else:
                        number = number + 50

                elif s[i] == "X":
                    if i >= 1 and s[i-1] == 'I':
                        continue
                    else:
                        number = number + 10

                elif s[i] == "V":
                    if i >= 1 and s[i-1] == 'I':
                        continue
                    else:
                        number = number + 5

                elif s[i] == "I":
                    number = number + 1

                break

        return(number)
