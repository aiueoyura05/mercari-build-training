def pattern_match_with_hashmap(p, s):
    pattern_length = len(p)
    words = s.split()
    words_length = len(words)
    
    if pattern_length != words_length:
        return False
    
    pattern_hashmap = {}
    for i in range(pattern_length):
        if p[i] not in pattern_hashmap:
            pattern_hashmap[p[i]] = words[i]
        elif pattern_hashmap[p[i]] != words[i]:
            return False
    
    return True


print(pattern_match_with_hashmap("abba", "dog cat cat dog")) 
print(pattern_match_with_hashmap("abba", "dog cat cat fish")) 

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()
#         word_dict = {}
#         word_inversed_dict = {}

#         if len(pattern) != len(words):
#             return False
#         for i ,p in enumerate(pattern):
#             if p not in word_dict and words[i] not in word_inversed_dict:
#                 word_dict[p] = words[i]
#                 word_inversed_dict[words[i]] = p
#             elif p in word_dict and word_dict[p] == words[i]:
#                 if word_dict[p] != words[i]:
#                     return False
#             else:
#                 return False
            
#         return True