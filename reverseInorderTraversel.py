class Solution:

    def populateNext(self, root):
        
        def populate_Next(root, prev):
            if not root:
                return prev
                
            prev = populate_Next(root.right, prev)
            root.next = prev
            prev = root
            
            return populate_Next(root.left, prev)
        populate_Next(root, None)
        return 