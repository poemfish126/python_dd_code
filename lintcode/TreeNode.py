import collections


class TreeNode:
    # def __init__(self, val):
    #     self.val = val
    #     self.left, self.right = None, None

    def __init__(self, val=1, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

    def deserialize(self, data):
        # None or ""
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != '#' else None
            for val in data.split(',')
        ]
        root = bfs_order[0]
        fast_index = 1

        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root

    def serialize(self, root):
        if not root:
            return "{}"

        queue = collections.deque()
        queue.append(root)
        result = ""
        while queue:
            node = queue.popleft()
            if node:
                result += str(node.val) + ","
                queue.append(node.left)
                queue.append(node.right)
            else:
                result += "#,"

        result = "{" + result[:-1] + "}"
        # print(result)
        return result


node123 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
node1023 = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
node1235 = TreeNode(1, TreeNode(2, None, TreeNode(5, None, None)), TreeNode(3, None, None))
node12345 = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))
node5492810 = TreeNode(5, TreeNode(4, TreeNode(2, None, None), None),
                       TreeNode(9, TreeNode(8, None, None), TreeNode(10, None, None)))
node596 = TreeNode(1, TreeNode(-5, TreeNode(1, None, None), TreeNode(2, None, None)),
                   TreeNode(2, TreeNode(-4, None, None), TreeNode(-5, None, None)))
leaf5 = TreeNode(5, None, None)
leaf3 = TreeNode(3, None, None)
leaf6 = TreeNode(6, None, None)
node88 = TreeNode(4, leaf3, TreeNode(7, leaf5, leaf6))
#
# print(node123.serialize(node88))
node88 = TreeNode().deserialize("4,3,7,#,#,5,6,#,#,#,#")
# print(node88)
