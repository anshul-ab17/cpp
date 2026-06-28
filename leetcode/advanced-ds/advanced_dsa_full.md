# Advanced Data Structures

## Topics
1. Ordered Set / TreeMap
2. Treap
3. Skip List
4. B-Tree / B+ Tree
5. Sparse Table
6. Heavy Light Decomposition (HLD)
7. Euler Tour Technique
8. Mo's Algorithm
9. Order Statistic Tree
10. Rope Data Structure

---

# 1. Ordered Set / TreeMap

Used for:
- predecessor/successor
- kth smallest
- range queries

Python:
Important Problems:
- LC 220
- LC 363
- LC 729
- LC 732

---

# 2. Treap

BST + Heap.

Operations:
- Insert O(log N)
- Delete O(log N)
- Search O(log N)

Template:
Used in:
- Order statistics
- Dynamic ordered set

---

# 3. Skip List

Average:
- Search O(log N)
- Insert O(log N)
- Delete O(log N)

Used heavily in:
- Redis
- RocksDB
- LevelDB

LC:
- LC 1206 Design Skiplist
---

# 4. B Tree / B+ Tree

## B Tree
- Keys + data in internal nodes.
- Used for disks.

## B+ Tree
- Data only in leaves.
- Leaves linked together.

Used in:
- MySQL InnoDB
- PostgreSQL indexes
- Filesystems

Complexity:
- Search O(log N)
- Insert O(log N)

Interview Topics:
- Why DBs use B+ Trees instead of BST.
- B Tree vs B+ Tree.

---

# 5. Sparse Table

Static RMQ.

Build: O(N log N)
Query: O(1)
LC:
- LC 1483 Kth Ancestor

---

# 6. Euler Tour Technique

Convert tree into array.

DFS:
Used for:
- subtree queries
- flatten tree
- HLD

---

# 7. Heavy Light Decomposition

Supports:
- path queries
- subtree queries

Complexities:
- Update O(log²N)
- Query O(log²N)

Common combination:
- HLD + Segment Tree

Problems:
- CSES Path Queries
- QTREE SPOJ

---

# 8. Mo's Algorithm

Offline range queries.

Complexity:
O((N + Q) * sqrt(N))

Sort queries:
Used in:
- Distinct values in range
- Frequency queries

---

# 9. Order Statistic Tree

Supports:
- kth smallest
- rank of element

Operations:
- insert
- erase
- kth(k)
- rank(x)

Implemented using:
- Treap
- AVL
- Red Black Tree

LC:
- LC 315 Count Smaller After Self

---

# 10. Rope Data Structure

Efficient string editing.

Operations:
- concatenate
- split
- insert
- erase

Complexities:
O(log N)

Used in:
- text editors
- IDEs

---

# Recommended For Trading Systems

Must Know:
1. B+ Tree
2. Skip List
3. Segment Tree
4. Treap
5. Order Statistic Tree

Infrastructure:
1. Consistent Hashing
2. Bloom Filter
3. HyperLogLog
4. LSM Tree
5. Merkle Tree

---

# Infrastructure Data Structures

## Bloom Filter

Membership testing.

False positives possible.

Used by:
- Redis
- Cassandra

## HyperLogLog

Approximate cardinality.

Memory efficient.

Used by:
- Redis PFCOUNT

## Consistent Hashing

Used by:
- Cassandra
- DynamoDB
- Redis Cluster

## Merkle Tree

Used by:
- Blockchain
- Cassandra

## LSM Tree

Used by:
- RocksDB
- LevelDB
- Cassandra
