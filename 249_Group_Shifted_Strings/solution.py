# Approach: Hash Map
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapHashToList = collections.defaultdict(list)

        def shift_letter(c, shift): 
            return chr((ord(c) - shift) % 26 + ord('a'))

        for string in strings: 
            shift = ord(string[0])
            hash_key = ''.join(shift_letter(c, shift) for c in string)

            mapHashToList[hash_key].append(string) 
        
        return list(mapHashToList.values())
