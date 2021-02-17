# B+ Tree Implementation
- implementation of B+ tree in python to handle following types of queries.
a. INSERT X - insert X into the B+ tree
b. FIND X - print YES if X is already inserted, else NO
c. COUNT X - print number of occurrences of X in B+tree
d. RANGE X Y - print number of elements in range x to y (both x and y included) 

## Execution
> python3 b+_tree.py <input_file>
- <input_file> contains the commands to execute
- output for each command is printed in a seperate line 

## Implementation
#### INSERT x
- Every element is inserted in the leaf node.So get the appropriate leaf node in which the element `x` can be inserted.
- Insert `x` in increasing order. If this operation creates overflow we split the node as follows:
    - first node contains n/2 keys 
    - second node contains remaining keys
    - the smallest key in the second node is copied to the parent node if exists or new node is created and then copying is done. The newly created node is made root. 
    - if parent exists and inserting key in the parent node (internal node) creates overflow, we split that internal node as follows:
        - first node contains n/2 keys
        - last node contains n-1/2 keys
        - remaining one node is inserted into its parent node in the same way as mentioned.
#### FIND x
-  searching is done as if we are inserting the element i.e first we get a appropriate node where `x` could be inserted. 
- For `x` to be present in the tree, it should be present in that particular node.

#### COUNT x
- search for the first leaf node where the element `x`could be present.
- traverse through leaf nodes and keep track of occurances of `x`. We stop iterating when element encountered is greater than `x` or when there are no more leaf nodes in the tree.

#### RANGE x y
- similar to `COUNT` except that here we stop iterating when the element encountered is greater than 'y' or when there are no more leaf nodes.
