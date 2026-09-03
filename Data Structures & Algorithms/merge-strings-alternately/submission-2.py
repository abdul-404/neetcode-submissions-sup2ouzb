class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b, word = 0, 0, 1
        S = []

        while A > a and B > b:
            if word == 1:
                S.append(word1[a])
                a += 1
                word = 2
            else:
                S.append(word2[b])
                b += 1
                word = 1
        
        while A > a:
            S.append(word1[a])
            a += 1
            
        while B > b:
            S.append(word2[b])
            b += 1

        return ''.join(S)