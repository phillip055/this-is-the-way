class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        myDict = {}
    
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    myDict[list1[i]] = i+j

        #print(myDict)

        minkey = min(myDict, key=myDict.get)

        #print(minkey)

        minvalue = myDict[minkey]

        #print(minvalue)

        retList = []

        for key, value in myDict.items():
            if value == minvalue:
                retList.append(key)

        #print(retList)

        return retList
