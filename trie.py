class Trie(object):
    """
    Uncompressed trie that supports exact as well as longest prefix matching. 
    
    Lookups are O(N) in the worst case where N is the length of the longest 
    string in the trie. Space is O(W) worst case where W is combined size of 
    all strings in the trie.
    """
    def __init__(self):
        """
        Create the trie.
        """
        self.root = [None, {}]

    def get(self, key):
        """
        Returns the value if key exists, None otherwise.
        """
        cur = self.root
        for c in key:
            try:
                cur = cur[1][c]
            except KeyError:
                return None
        return cur[0]

    def lpm(self, key):
        """ 
        Returns the key in the trie that shares the longest prefix with
        the given key. Returns None if no key shares a prefix.
        """
        best = None
        prefix = ""
        cur = self.root
        for c in key:
            prefix += c
            try:
                cur = cur[1][c]
            except KeyError:
                return best
            if cur[0]:
                best = prefix
        return best

    def remove(self, key):
        """
        Removes the key if it exists and returns its value, returns None otherwise.
        """
        cur = self.root
        # tracks the root of the one-way branch (if any) to the key node
        branch_root = None
        # tracks the direction of the one-way branch from the root
        branch_char = None
        for c in key:
            if len(cur[1]) > 1:
                branch_root = branch_char = None
            elif not branch_root:
                branch_root = cur
                branch_char = c

            try:
                cur = cur[1][c]
            except KeyError:
                return None

        old_val = cur[0]
        # delete all nodes along the one-way branch
        if branch_root:
            node = branch_root[1].pop(branch_char)
            while node[1]:
                (key, node) = node[1].popitem()
        else:
            cur[0] = None
        return old_val

    def add(self, key, value):
        """
        Adds the key with the given value. 
        Returns old value associated with the key if present, None otherwise.
        """
        cur = self.root
        for c in key:
            cur = cur[1].setdefault(c, [None, {}])
        ret = cur[0] 
        cur[0] = value
        return ret

