class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        new_list = []
        word= set(words[0])
        for letter in word:
            freq = min([word.count(letter) for word in words])
            new_list+=[letter]*freq
        return new_list
