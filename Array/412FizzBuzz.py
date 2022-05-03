# https://leetcode.com/problems/fizz-buzz/

# All sol has O(N) TC
# Each one is optimized in less conditions and keeping future complexity in mind

from typing import List


class Solution:
    def fizzBuzz0(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n + 1)]
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i - 1] = "Fizz"
            elif i % 5 == 0:
                answer[i - 1] = "Buzz"

        return answer

    def fizzBuzz1(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ""

            if divisible_by_3:
                num_ans_str += "Fizz"
            if divisible_by_5:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str = str(num)

            ans.append(num_ans_str)

        return ans

    def fizzBuzz2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n + 1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)

        return ans
