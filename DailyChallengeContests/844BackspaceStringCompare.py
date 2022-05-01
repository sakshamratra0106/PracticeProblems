class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        TC : O(N)
        SC : O(N)
        """
        sList = []
        sLen = 0
        tList = []
        tLen = 0

        for element in s:
            if element != "#":
                sList.append(element)
                sLen += 1
            elif sLen > 0:
                sList.pop()
                sLen -= 1

        for element in t:
            if element != "#":
                tList.append(element)
                tLen += 1
            elif tLen > 0:
                tList.pop()
                tLen -= 1

        print(sList, sLen, tList, tLen)

        if sLen != tLen:
            return False

        while sLen > 0:
            if tList[sLen - 1] != sList[sLen - 1]:
                return False

            sLen -= 1

        return True


    backSpace = '#'

    # Returns the index after backspace
    def getIndexAfterBackSpace(self, str, index):
        backSpaceCount = 0
        while (index >= 0):
            if (str[index] == self.backSpace):
                backSpaceCount += 1
            elif (backSpaceCount > 0):
                backSpaceCount -= 1
            else:
                break
            index -= 1
        return index

    def backspaceCompare(self, s: str, t: str) -> bool:
        """

        :param s:
        :param t:
        :return:

        TC : O(N)
        SC : O(1)
        """
        p1, p2 = len(s) - 1, len(t) - 1

        while (p1 >= 0 and p2 >= 0):
            p1 = self.getIndexAfterBackSpace(s, p1)
            p2 = self.getIndexAfterBackSpace(t, p2)
            if (p1 < 0 or p2 < 0):   break
            if (s[p1] != t[p2]): return False
            p1 -= 1
            p2 -= 1

        # Checking if Still any backspace charecter left, for case. s = "", t = "a#"
        p1 = self.getIndexAfterBackSpace(s, p1)
        p2 = self.getIndexAfterBackSpace(t, p2)

        if (p1 != p2):   return False
        return True