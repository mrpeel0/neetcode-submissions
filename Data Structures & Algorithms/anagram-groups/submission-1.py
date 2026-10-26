class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputList = []
        iscool = True
        appended = False
        for word in strs:
            appended = False
            for list1 in outputList:
                string2 = list1[0]
                if len(word) != len(string2):
                    continue
                iscool = True
                for letter in word:
                    if string2.find(letter) != -1:
                      string2 = string2[:string2.find(letter)] + string2[string2.find(letter)+1:] 
                    else:
                        iscool = False
                        break
                if iscool:
                    list1.append(word)
                    appended = True
                    break
            if not appended:
                outputList.append([word])
        return outputList