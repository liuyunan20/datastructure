from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        dict2 = {}
        result_index = len(list1) + len(list2)
        result_name = []
        for i, name in enumerate(list1):
            dict1[name] = i
        for i, name in enumerate(list2):
            dict2[name] = i
        for key in dict1:
            if dict2.get(key) is not None:
                if dict1[key] + dict2[key] == result_index:
                    result_name.append(key)
                if dict1[key] + dict2[key] < result_index:
                    result_index = dict1[key] + dict2[key]
                    result_name.clear()
                    result_name.append(key)
        return result_name
