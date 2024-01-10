# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        infected = []
        prev_infected = set()
        def fillParents(root, parent=None):
            if root == None:
                return
            if parent != None:
                parents[root.val] = parent
            if root.val == start:
                infected.append(root)
            fillParents(root.left, root)
            fillParents(root.right, root)
        fillParents(root)

        mins = 0
        while len(infected):
            infected_ints = [i.val for i in infected]
            current_infected = infected[:]
            infected = []
            while len(current_infected):
                e = current_infected.pop(0)
                if e not in prev_infected:
                    prev_infected.add(e)
                    if e.left and e.left not in prev_infected:
                        infected.append(e.left)
                    if e.right and e.right not in prev_infected:
                        infected.append(e.right)
                    if e.val in parents:
                        if parents[e.val] not in prev_infected:
                            infected.append(parents[e.val])
            mins += 1
        return mins - 1

