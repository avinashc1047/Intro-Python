class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        1. cut of certain strings that do not have repeating chars
        2. place all the cut string in a list
        3. loop over list to check the length
        4. return the highest length
        '''
        # list of cut strings
        cutStrings = []
        
        # word holder
        word = ''
        
        for char in s:
            if (char in word):
                if (char == word[0]):
                    word.replace('char', '')
                    word += char
                elif (char == word[-1]):
                    cutStrings.append(word)
                    word = char
            else:
                word += char
        
        max = 0
        
        for string in cutStrings:
            if (len(string) >= max):
                max = len(string)

        return max
    
print(Solution.lengthOfLongestSubstring("adbanceebfghijjls"))