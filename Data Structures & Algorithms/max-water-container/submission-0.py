class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = []
        left = 0 
        right = len(heights) - 1
        while left < right:
            length = right - left
            area = length * min([heights[left],heights[right]])
            output.append(area)
            if heights[left] <= heights[right]:
                left += 1 
            else :
                right -= 1 
        return max(output)
            
            
           
        
        
                 


    
