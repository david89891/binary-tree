class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def recur_inorder(self):
        if self is None:
            return
        if self.left:
            self.left.recur_inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.recur_inorder()

    def recur_preorder(self):
        if not self:
            return
        print(self.val, end=" ")
        if self.left:
            self.left.recur_preorder()
        if self.right:
            self.right.recur_preorder()

    def recur_postorder(self):
        if not self:
            return
        if self.left:
            self.left.recur_postorder()
        if self.right:
            self.right.recur_postorder()
        print(self.val, end=" ")

    def bfs_search(self) -> list:
        order, all_node = [self.val], [self]
        for node in all_node:
            if node.left:
                all_node.append(node.left)
                order.append(node.left.val)
            if node.right:
                all_node.append(node.right)
                order.append(node.right.val)
        print(order)
        return all_node


def insert(node, new_node):
    if not node:
        node = new_node
        return node
    if node.val < new_node.val:
        insert(node.right, new_node)
    elif node.val > new_node.val:
        insert(node.left, new_node)
    else:
        print("Error")


def iter_search(node, target: int) -> bool:
    while node:
        if target > node.val:
            node = node.right
        elif target < node.val:
            node = node.left
        else:
            return True
    return False


def inorder_list(tree_root) -> list:
    stack, order = list(), list()
    node = tree_root
    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left
        pop_node = stack.pop()
        order.append(pop_node.val)
        node = pop_node.right
    return order


def postorder_list(tree_root):
    stack, order = list(), list()
    node = tree_root
    while node or len(stack):
        while node:
            stack.append(node)
            node = node.left
        node = stack[-1].right
        if node and node.val not in order:
            stack.append(node)
        else:
            order.append(stack.pop().val)
            node = stack[-1].right
            if node.val in order:
                order.append(stack.pop().val)
                node = stack[-1].right
        if root.right.val in order:
            order.append(root.val)
            break
    return order


def preorder_list(tree_root):
    stack, order = list(), list()
    node = tree_root
    while node or len(stack):
        while node:
            order.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop().right
    return order


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)


    root.recur_postorder()
    print(postorder_list(root))
