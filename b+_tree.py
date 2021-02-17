import bisect 
import sys
order = 3
class Node:
    def __init__(self,flag):
        self.isLeaf = flag
        self.parent = 0
        self.keys = []
        self.ptr = [None]
class BTree:
    def __init__(self,N):
        #max number of keys in a node 
        self.N = N - 1
        self.root = Node(True)

    def search(self,x):
        node = self.root
        ind=0
        flag = False
        while(1):
            ind = 0
            for i in range(len(node.keys)):
                # if x==node.keys[i]:
                #     ind+=1
                if x>=node.keys[i]:
                    ind+=1
                elif x<=node.keys[i]:
                    break
            if node.isLeaf:
                break
            else:
                node = node.ptr[ind]
        return node

    def count(self,x):
        node = self.search(x)
        res = 0
        flag = True
        while node is not None and flag:
            for i in range(len(node.keys)):
                if node.keys[i] == x:
                    res += 1
                else:
                    flag = False
            node = node.ptr[0]
        return res
    
    def find(self, x):
        node = self.search(x)
        if x in node.keys:
            return True
        else:
            return False
    
    def range(self,x,y):
        node = self.search(x)
        res = 0
        flag = True
        while node is not None and flag:
            for i in range(len(node.keys)):
                if node.keys[i]>=x and node.keys[i]<=y:
                    res+=1
                elif node.keys[i]>y:
                    flag=False
                    break
            node = node.ptr[0]
        return res
        
    def insert(self,x):
        node = self.search(x)
        bisect.insort(node.keys, x)
        if len(node.keys)>self.N:
            self.split_leaf(node)
        
    def split_leaf(self,node):
        n = self.N
        l = int((n+1)/2) # number of keys in left split
        r = n-l          #number of keys in right split
        temp = Node(True) #create a new node (right split)
        
        # insert last r keys of node into right node &
        #       remove them from original node
        for i in range(l,len(node.keys)):
            temp.keys.append(node.keys[i])
        del node.keys[l:]

        #leaf pointer updating
        temp.ptr[0] = node.ptr[0]
        node.ptr[0] = temp

        #if the node being split is a root, create new root
        if node.parent == 0:
            root = Node(False)
            root.keys.append(temp.keys[0])
            root.ptr[0] = node
            root.ptr.append(temp)
            node.parent = root
            temp.parent = root
            self.root = root
        else:
            self.insert_nonleaf(node.parent,temp.keys[0],temp)
        
    def split_nonleaf(self,node):
        n = self.N
        l = int((n+1)/2)
        r = n-l
        temp = Node(False)
        temp.ptr.clear()
        for i in range(l+1,len(node.keys)):
            temp.keys.append(node.keys[i])
            temp.ptr.append(node.ptr[i])
            node.ptr[i].parent = temp
        temp.ptr.append(node.ptr[-1])
        node.ptr[-1].parent = temp
        if node.parent == 0:
            root = Node(False)
            root.keys.append(node.keys[l])
            root.ptr[0] = node #first child
            root.ptr.append(temp) #second child
            temp.parent = root
            node.parent = root
            self.root = root
        else:
            self.insert_nonleaf(node.parent,node.keys[l],temp)
        
        del node.keys[l:]    
        del node.ptr[l+1:]
        
    def display(self,node,s=""):
        print(s,node.keys)
        if not (node.isLeaf):
            for i in range(len(node.ptr)):
                self.display(node.ptr[i],s+"  ")
          
    def insert_nonleaf(self,node,x,r_ptr):
        r_ptr.parent = node
        bisect.insort(node.keys, x)
        for i in range(len(node.keys)):
            if node.keys[i]==x:
                node.ptr.insert(i+1,r_ptr)
        if len(node.keys)>self.N:
            self.split_nonleaf(node)

            
def display(node,s=""):
    print(s,node.keys)
    if not (node.isLeaf):
        for i in range(len(node.ptr)):
            display(node.ptr[i],s+"  ")

def error(msg):
    print(msg)
    exit(0)

def main():
    if len(sys.argv)!=2:
        error("Wrong number of arguments")
    tree = BTree(order)
    fname = sys.argv[1]
    try:
        f = open(fname,'r')
    except OSError:
        error ("Could not open/read file:"+ fname)
    for line in f:
        try:
            print("\n"+line.strip())
            line = line.strip().lower()
            if "insert" in line:
                x = line.split()[1]
                tree.insert(int(x))
            
            elif "find" in line:
                x = line.split()[1]
                if tree.find(int(x)):
                    print("Yes")
                else:
                    print("No")
            elif "count" in line:
                x = line.split()[1]
                print(tree.count(int(x)))
            elif "range" in line:
                x,y = line.split()[1:]
                print(tree.range(int(x),int(y)))
            else:
                error("invalid query")
        except :
            error("invalid query")
    print("\nTree:")
    tree.display(tree.root)
if __name__ == "__main__":
    main()

# tree = BTree(4)
# tree.insert(8)
# tree.insert(5)
# tree.insert(6)
# tree.insert(7)
# tree.insert(9)
# tree.insert(10)
# tree.insert(11)
# tree.insert(12)
# tree.insert(13)
# print("Tree:")
# tree.display(tree.root)
# print("count(7) :",tree.count(7))
# print("range(1,7) :",tree.range(1,7))
