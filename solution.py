class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child = 0  # Pointer for children
        cookie = 0  # Pointer for cookies
        
        # Try to assign cookies to children
        while child < len(g) and cookie < len(s):
            # If current cookie can satisfy current child
            if s[cookie] >= g[child]:
                child += 1  # Move to next child (this child is content)
            cookie += 1  # Move to next cookie regardless
        
        return child  # Number of content children
