# Data Structures & Algorithms Quiz Answers

## Conceptual Questions

1. **What is the time complexity of reversing a singly linked list iteratively?**
   - **Answer:** O(n). The key operations are traversing the list once and reversing the pointers.

2. **Explain the difference between BFS and DFS in terms of their data structures and search order.**
   - **Answer:** BFS uses a queue and explores nodes level by level. DFS uses a stack (or recursion) and explores as far as possible along each branch before backtracking. BFS is preferable for finding the shortest path, while DFS is useful for exploring all possible paths.

3. **Describe how a hash map helps solve the two-sum problem in O(n) time.**
   - **Answer:** A hash map stores the complement of each number as we iterate through the list. This allows for O(1) average-time lookups to check if the complement exists. The trade-off is the additional space used by the hash map.

4. **What is the worst-case scenario for quicksort, and why does it happen?**
   - **Answer:** The worst-case scenario is O(n^2) and occurs when the pivot selection consistently results in the most unbalanced partitions (e.g., always picking the smallest or largest element as the pivot). This can be mitigated by using randomized pivot selection or the median-of-three method.

5. **For a binary tree with n nodes, what is the maximum possible height?**
   - **Answer:** The maximum possible height is n-1, which occurs in a degenerate (or skewed) tree where each node has only one child. The minimum possible height is log2(n) in a perfectly balanced tree.

## Code Analysis

6. **Review the following linked list reversal code. Is it correct? If not, identify and fix the issues:**

```python
def reverse_linked_list(head):
    prev = None
    curr = head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr  # This line was missing in the original code
        curr = temp
    
    return prev
```

7. **What will be the output of the following BFS traversal code on this tree?**

``` text
    1
   / \
  2   3
 / \   \
4   5   6
```

```python
def bfs(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

- **Answer:** [1, 2, 3, 4, 5, 6]

8. **Analyze the time and space complexity of the following two-sum implementation:**

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

- **Answer:** Time complexity is O(n) because we iterate through the list once. Space complexity is O(n) because we store up to n elements in the hash map.

## Coding Challenges

9. **Implement a function to check if a linked list has a cycle (returns to a previously visited node).**

```python
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

10. **Write a function that takes a binary tree and returns the maximum sum path from root to leaf.**

```python
def max_sum_path(root):
    if not root:
        return 0
    
    left_sum = max_sum_path(root.left)
    right_sum = max_sum_path(root.right)
    
    return root.val + max(left_sum, right_sum)
```

11. **Implement a function to find the k-th largest element in an unsorted array.**

```python
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

12. **Design a data structure that supports the following operations in O(1) time:**

```python
import random

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.index_map = {}
    
    def insert(self, val):
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.data)
        self.data.append(val)
        return True
    
    def remove(self, val):
        if val not in self.index_map:
            return False
        last_element = self.data[-1]
        idx = self.index_map[val]
        self.data[idx] = last_element
        self.index_map[last_element] = idx
        self.data.pop()
        del self.index_map[val]
        return True
    
    def get_random(self):
        return random.choice(self.data)
```

## Application Questions

13. **As an SRE, how might you use BFS or DFS when troubleshooting a service dependency issue?**

- **Answer:** BFS can be used to find the shortest path to a failing service, identifying the quickest route to the root cause. DFS can be used to explore all dependencies of a service to ensure all potential issues are identified.

14. **Describe a situation where understanding algorithm complexity would be important for system performance in an SRE context.**

- **Answer:** When diagnosing performance issues, understanding algorithm complexity helps identify inefficient code that may be causing bottlenecks. For example, an O(n^2) algorithm in a critical path can significantly degrade performance as data size grows.

15. **Explain how you would design an efficient caching system using the data structures we've discussed.**

- **Answer:** An efficient caching system can be designed using a hash map for O(1) lookups and a doubly linked list to maintain the order of access for implementing an LRU (Least Recently Used) eviction policy. This ensures quick access and efficient eviction of the least recently used items.