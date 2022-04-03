"""You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59.
The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.


Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations."""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        timeIncrement = [1, 5, 15, 60]

        if current == correct:
            return 0

        # Calculate time difference
        current = current.split(":")
        correct = correct.split(":")

        difference = (int(correct[0]) - int(current[0])) * 60 + (int(correct[1]) - int(current[1]))

        print(difference)

        if difference < 0:
            return -1

        # steps required
        minSteps = 0
        divisionBy = len(timeIncrement) - 1
        while difference > 0 and divisionBy > -1:
            if difference >= timeIncrement[divisionBy]:
                minSteps += int(difference / timeIncrement[divisionBy])
                difference = difference % timeIncrement[divisionBy]
            print("1  .here ")
            print(minSteps, "--",difference, "--", timeIncrement[divisionBy], "--",  timeIncrement[divisionBy] >= difference)

            while timeIncrement[divisionBy] > difference and divisionBy > -1:
                divisionBy -= 1
                print("2 .here ")
        return int(minSteps)


if __name__ == "__main__":
    current = "02:30"
    correct = "04:35"
    print("1. From Current {} and Correct {} can be achieved in min steps {}.".format(
        current, correct, Solution().convertTime(current, correct)
    ))

    current = "11:00"
    correct = "11:01"
    print("2. From Current {} and Correct {} can be achieved in min steps {}.".format(
        current, correct, Solution().convertTime(current, correct)
    ))

    current = "00:00"
    correct = "23:59"
    print("2. From Current {} and Correct {} can be achieved in min steps {}.".format(
        current, correct, Solution().convertTime(current, correct)
    ))