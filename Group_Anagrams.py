class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map=defaultdict(list)
        print(map)
        for word in strs:
            sorted_string=''.join(sorted(word)) # to get a string to use as key
            # print(sorted_string)
            map[sorted_string].append(word)
        output=list(map.values())
        return output
        # print(output)

        
