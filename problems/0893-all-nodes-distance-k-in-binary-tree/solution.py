# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def parenthood(_root):
            if _root == None:
                return
            if _root.left:
                parent[_root.left] = _root
                parenthood(_root.left)
            if _root.right:
                parent[_root.right] = _root
                parenthood(_root.right)
        
        def dfs(_root, target):
            if _root == None:
                return None
            if _root.val == target.val:
                return _root
            return dfs(_root.left, target) or dfs(_root.right, target)
        
        parenthood(root)
        node = dfs(root, target)
        
        places = []
        visited = set()
        def travel(node, distance_remaining):
            if node in visited:
                return
            if node == None:
                return
            if distance_remaining == 0:
                places.append(node.val)
                return
            visited.add(node)
            travel(node.left, distance_remaining - 1)
            travel(node.right, distance_remaining - 1)
            if node in parent:
                travel(parent[node], distance_remaining - 1)
        travel(node, k)
        return places


