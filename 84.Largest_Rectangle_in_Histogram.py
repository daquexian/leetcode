import sys

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s, res, heights = [], 0, [0] + heights + [0] # add the first 0 to let s[-1] be always avaliable, add the last 0 to calculate when meeting the end
        for i, height in enumerate(heights):
            if len(s) > 0:
                while height < heights[s[-1]]:
                    top = s.pop()
                    # The stack must have such feature: if items after "top" are lower than heights[top], heights[top] will be poped; the items between s[-1] (not including) and top are obviously taller than heights[top] (because heights[s[-1]] is the heightest between all items lower than heights[top], so all items between s[-1] and i (both not including) are heighter than s[top]
                    res = max(res, heights[top] * (i - s[-1] - 1))
                #res = max(res, height * (i - s[-1]))
            s.append(i)
        return res

heights = eval(sys.argv[1])
print(Solution().largestRectangleArea(heights))
