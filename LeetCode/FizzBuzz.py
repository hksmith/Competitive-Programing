class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        soln = []
        i = 1
        while n > 0:
            if i % 3 == 0 and i % 5 == 0:
                soln.append("FizzBuzz")
            elif i % 3 == 0:
                soln.append("Fizz")
            elif i % 5 == 0:
                soln.append("Buzz")
            else:
                soln.append(str(i))
            n -= 1
            i += 1
        return soln