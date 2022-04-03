from typing import List
from collections import OrderedDict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        for match in matches:

            firstTeam = match[0]
            secondTeam = match[1]

            # Count for Winners
            if firstTeam in hashMap:
                hashMap[firstTeam][0] += 1
            else:
                hashMap[firstTeam] = [1, 0]

            # Count for losers
            if secondTeam in hashMap:
                hashMap[secondTeam][1] += 1
            else:
                hashMap[secondTeam] = [0, 1]

        # Sorting Dictionary
        hashMap = OrderedDict(sorted(hashMap.items()))

        lostNoMatch = []
        lostOneMatch = []
        print(hashMap)
        for team in hashMap:
            if hashMap[team][1] == 0:
                lostNoMatch.append(team)
            elif hashMap[team][1] == 1:
                lostOneMatch.append(team)

        return [lostNoMatch, lostOneMatch]


if __name__ == "__main__":
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    print("1. From matches {} teams with zero loss and one loss are {}.".format(
        matches, Solution().findWinners(matches)
    ))
