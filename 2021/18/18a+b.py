#!/usr/bin/python3
 
import sys

debug = False

class Node:
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.value = value
        self.left = None
        self.right = None
        if left != None:
            self.left = left
            self.left.parent = self
        if right != None:
            self.right = right
            self.right.parent = self
        self.parent = parent
 
    def __str__(self): 
        return str(self.value) if self.value != None else '[' + str(self.left) + ',' + str(self.right) + ']'
 
    # return (exploded, node) where exploded = True/False if node has more than four levels of nesting
    def explode_loop(self, p, level):
        if p.value == None:
            if level < 4:
                (exploded, node) = self.explode_loop(p.left, level+1)
                if exploded:
                    return (exploded, node)
                (exploded, node) = self.explode_loop(p.right, level+1)
                if exploded:
                    return (exploded, node)
                return (False, None)
            else:
                return (True, p)
        else:
            return (False, None)
 
    def find_explode_start(self):
        return self.explode_loop(self, 0)
 
    # add number to rightmost node in left subtree
    def add_to_left(self, node, number):
        while True:
            if node.parent == None:
                return
            if node == node.parent.right:
                self.add_rightmost(node.parent.left, number)
                return
            else:
                node = node.parent
 
    # add number to leftmost node in right subtree
    def add_to_right(self, node, number):
        while True:
            if node.parent == None:
                return
            if node == node.parent.left:
                self.add_leftmost(node.parent.right, number)
                return
            else:
                node = node.parent
 
    def add_leftmost(self, node, number):
        while node.left:
            node = node.left
        node.value += number
 
    def add_rightmost(self, node, number):
        while node.right:
            node = node.right
        node.value += number
 
    # replace node with 0, the distribute left/right values
    def explode(self, node):
        left = node.left.value
        right = node.right.value
        node.left = None
        node.right = None
        node.value = 0
        self.add_to_left(node, left)
        self.add_to_right(node, right)
 
    # look for nodes that needs to be split, return first one that matches
    def split_loop(self, node):
        if node.value != None:
            return (True, node) if node.value > 9 else (False, node)
        else:
            split, split_node = self.split_loop(node.left)
            if split:
                return (split, split_node)
            split, split_node = self.split_loop(node.right)
            if split:
                return (split, split_node)
            return (False, None)
 
    def find_split_start(self):
        return self.split_loop(self)
 
    def split(self, node):
        import math
        node.left = Node(node, None, None, math.floor(node.value/2))
        node.right = Node(node, None, None, math.ceil(node.value/2))
        node.value = None
 
    def reduce(self):
        while True:
            exploded, node = self.find_explode_start()
            if exploded:
                if debug:
                    print("Explode  :", self)
                self.explode(node)
                if debug:
                    print("Explode =>", self)
                continue
            split, node = self.find_split_start()
            if split:
                if debug:
                    print("Split    :", self)
                self.split(node)
                if debug:
                    print("Split   =>", self)
                continue
            return
 
    def magnitude(self):
        return self.value if self.value != None else 3*self.left.magnitude() + 2*self.right.magnitude()

# Turn list into tree, recursively
def parse_loop(p, data):
    if type(data) == list:
        [left, right] = data
        p.left = Node()
        parse_loop(p.left, left)
        p.left.parent = p
        p.right = Node()
        parse_loop(p.right, right)
        p.right.parent = p
    else:
        p.value = data
 
# Using same syntax as Python for lists
def parse(line):
    p = Node()
    parse_loop(p, eval(line))   
    return p
 
# Sum all input.
# No identity for + so use None to detect first term
def sum(lines):
    sum = None
    for line in lines:
        p = parse(line)
        p.reduce()
        if sum is None:         
            sum = p
        else:
            sum = Node(left=sum, right=p)
        sum.reduce()
        if debug:
            print(sum)
    return sum.magnitude()
 
def sum_two(lines):
    sums = []
    for line in lines:
        p = parse(line)
        p.reduce()
        sums.append(p)
 
    max_magnitude = 0
    for i in range(len(sums)):
        for j in range(len(sums)):
            if i != j:
                sum = Node(left=sums[i], right=sums[j]) 
                sum.reduce()
                magnitude = sum.magnitude()
                if magnitude > max_magnitude:
                    max_magnitude = magnitude
    return max_magnitude
 
if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        print('sum of all lines -->', sum(lines))
        print('max sum of two lines -->', sum_two(lines))
