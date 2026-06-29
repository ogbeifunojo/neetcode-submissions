class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        list2 = []
        for i in s.lower():
            if i.isalnum():
                list1.append(i)
        s_reversed = s[::-1]
        for j in s_reversed.lower():
            if j.isalnum():
                list2.append(j)
        if list1 == list2:
            return True
        else:
            return False
        
        


        