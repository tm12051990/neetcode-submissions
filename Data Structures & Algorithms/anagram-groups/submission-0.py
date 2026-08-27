class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in wordMap:
                wordMap[key].append(word)
            else:
                wordMap[key] = []
                wordMap[key].append(word)
        
        result = list(wordMap.values())

        return result