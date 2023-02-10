# rsa-store

This repository is an implementation of (https://blogs.umass.edu/shankarsubra/2023/02/05/accountabstraction/)[https://blogs.umass.edu/shankarsubra/2023/02/05/accountabstraction/] where I try to extend the key generation by also building a RSA tree to store data among different nodes that has a varying generator in the RSA computation along with a varying key for everytime a new "block" is created.

Instead of a blockchain we have a BlockTree, 

and every new block creates a new block layer 

each block layer contains a block leaf with every node in the tree. 

The tree does not grow in width after creation, where the storage tree group is explicitly told the number of nodes that are required for this particular tree. 

Multi Party Computation of the data among the nodes is to be implemented.
