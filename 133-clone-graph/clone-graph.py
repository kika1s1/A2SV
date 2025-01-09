"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        visited = set()
        stack = [node]
        old_to_new = {}
        
        while stack:
            nod = stack.pop()
            if nod not in visited:
                visited.add(nod)
                old_to_new[nod] = Node(nod.val)
                for neighbor in nod.neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        for old_node, new_node in old_to_new.items():
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(old_to_new[neighbor])
        
        return old_to_new[start]
