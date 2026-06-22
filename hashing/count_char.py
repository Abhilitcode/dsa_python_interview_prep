#hashing for character 

class Solution():
    def count_char(self, s):
        char_freq = {}

        for char in s:
            if char in char_freq:
                char_freq[char] +=1
            else:
                char_freq[char] =1 
        
        return char_freq 

if __name__ == "__main__":
    obj = Solution()
    print(obj.count_char(s="abbcccdd"))