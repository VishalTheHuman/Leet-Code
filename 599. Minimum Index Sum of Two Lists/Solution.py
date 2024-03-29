class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dt = {}
        for i in range(len(list1)):
            j = list2.index(list1[i]) if list1[i] in list2 else -1
            if j!=-1:
                dt[i+j] = dt.get(i+j,[]) + [list1[i]]
        return dt[min(dt.keys())]

