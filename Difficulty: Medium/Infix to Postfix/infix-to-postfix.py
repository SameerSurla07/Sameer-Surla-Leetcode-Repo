#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        def precedence(op):
            """Function to return precedence of operators."""
            if op == '^':
                return 3
            elif op == '/' or op == '*':
                return 2
            elif op == '+' or op == '-':
                return 1
            else:
                return 0

        stack = []  # stack to hold operators and parentheses
        result = []  # list to store the postfix expression


        for char in exp:
            if char.isalnum():  # If the character is an operand, add it to the result
                result.append(char)
            elif char == '(':  # If the character is '(', push it to the stack
                stack.append(char)
            elif char == ')':  # If the character is ')', pop until '(' is encountered
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # Pop '(' but do not add to result
            else:  # If an operator is encountered
                while stack and precedence(char) <= precedence(stack[-1]):
                    result.append(stack.pop())
                stack.append(char)

        # Pop all the remaining operators in the stack
        while stack:
            result.append(stack.pop())

        return ''.join(result)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends