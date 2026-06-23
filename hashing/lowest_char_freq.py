#find minimum character frequency. 

class Solution:
    def low_freq(self, s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] =1 
        
        #min_frequecy if set 0 here it will always return 0.
        #so it shld be set infinity
        min_freq = float("inf")
        min_char = ""

        for key, value in freq.items():
            if value < min_freq:
                min_freq = value
                min_char = key 
        
        return min_char, min_freq 
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.low_freq(s="radhesham"))
    print(obj.low_freq(s="lifeisunfair"))