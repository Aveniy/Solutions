class Solution:
    def sortSentence(self, s: str) -> str:
        new = s[::-1].split()
        new.sort()
        new_list = []

        for word in new:
            new_list.append(word[1:][::-1])
        return ' '.join(new_list)
            




        
        
