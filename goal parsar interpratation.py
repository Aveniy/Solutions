class Solution:
    def interpret(self, command: str) -> str:
        interprator = {'G':'G',
                    '()': 'o',
                    '(al)':'al' }
        empty = ''
        final = ''
        for letter in command:
            empty+=letter
            if empty in interprator:
                final += interprator.get(empty)
                empty=''
        return final

        



        
