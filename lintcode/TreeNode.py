class TreeNode:
    # def __init__(self, val):
    #     self.val = val
    #     self.left, self.right = None, None

    def __init__(self, val, left, right):
        self.val = val
        self.left, self.right = left, right


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
