"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0, 0 # longest path, longest diameter
            longest_child_diameter = 0
            longest_child_path, second_longest_child_path = 0, 0
            for child in root.children:
                path, diameter = helper(child)
                if path > longest_child_path:
                    second_longest_child_path = longest_child_path
                    longest_child_path = path
                elif path > second_longest_child_path:
                    second_longest_child_path = path
                longest_child_diameter = max(longest_child_diameter, diameter)
            
            longest_child_diameter = max(longest_child_diameter, 1 + longest_child_path + second_longest_child_path)
            longest_child_path += 1
            return longest_child_path, longest_child_diameter
        path, diameter = helper(root)
        return diameter - 1


            
