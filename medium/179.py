class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #convert ints to strs
        array = list(map(str, nums))
        array.sort(key = lambda x: x*10, reverse = True) #compare two strings a and b by checking a + b vs b + a if a + b larger a come first

        if array[0] == "0":
            return "0"
        
        ans = ''.join(array)

        return ans