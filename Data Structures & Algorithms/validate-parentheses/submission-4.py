class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        dict1 = {"]":"[", ")":"(", "}":"{"}
        for x in s:
            if x == "[" or x == "(" or x == "{":
                list1.append(x)

            elif x == "]" or x == "}" or x == ")":
                if list1 == []:
                    return False
                if dict1[x] == list1[-1]:
                    print(dict1[x])
                    print(list1[-1])
                    list1.pop(-1)
                else:
                    return False
        if list1 != []:
            return False
        return True