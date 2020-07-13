from hashlib import sha256

class MerkleNode:
    def __init__(self, hash):
        self.hash = hash
        self.parent = None

class MerkleTree:
    def __init__(self, data_chunks):
        leaves = []
        for chunk in data_chunks:
            node = self.hash(chunk)
            leaves.append(MerkleNode(node))
        self.root = self.build_merkle_tree(leaves)
    
    def build_merkle_tree(self, leaves):
        parents = []
        num_leaves = len(leaves)
        if num_leaves == 1:
            return leaves[0]
        
        i = 0
        while i < num_leaves:
            left_child = leaves[i]
            right_child = leaves[i+1] if i+1 < num_leaves else left_child
            parents.append(self.create_parent(left_child, right_child))
            i+=2
        return self.build_merkle_tree(parents)


    def create_parent(self, left_child, right_child):
        parent = MerkleNode(self.hash(left_child.hash + right_child.hash))
        print("Left child: {}, Right child: {}, Parent: {}".format(
            left_child.hash, right_child.hash, parent.hash))
        right_child, left_child = parent, parent
        return parent

    @staticmethod
    def hash(data):
        data = data.encode('utf-8')
        return sha256(data).hexdigest()


if __name__ == "__main__":
    merkle_tree = MerkleTree(["0", "1", "2", "3"])
    print("0: {}".format(merkle_tree.hash("0")))
    print("Root: {}".format(merkle_tree.root.hash))