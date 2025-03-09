# Data Structures & Algorithms Quiz

## Conceptual Questions

1. **What is the time complexity of reversing a singly linked list iteratively?**
   - Explain your reasoning and identify the key operations that contribute to this complexity.

2. **Explain the difference between BFS and DFS in terms of their data structures and search order.**
   - Provide examples of scenarios where each would be preferable.

3. **Describe how a hash map helps solve the two-sum problem in O(n) time.**
   - What are the trade-offs compared to other approaches?

4. **What is the worst-case scenario for quicksort, and why does it happen?**
   - How can this scenario be mitigated?

5. **For a binary tree with n nodes, what is the maximum possible height?**
   - What is the minimum possible height? Under what conditions do these occur?

## Code Analysis

6. **Review the following linked list reversal code. Is it correct? If not, identify and fix the issues:**

```python
def reverse_linked_list(head):
    prev = None
    curr = head
    
    while curr:
        temp = curr.next
        curr.next = prev
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

## Coding Challenges

9. **Implement a function to check if a linked list has a cycle (returns to a previously visited node).**
   - Your solution should use O(1) extra space.

10. **Write a function that takes a binary tree and returns the maximum sum path from root to leaf.**
    - A path must start at the root and end at a leaf.

11. **Implement a function to find the k-th largest element in an unsorted array.**
    - Try to optimize beyond the obvious O(n log n) sorting solution.

12. **Design a data structure that supports the following operations in O(1) time:**
    - Insert an element
    - Remove an element
    - Get a random element
    - Explain your approach and any trade-offs.

## Application Questions

13. **As an SRE, how might you use BFS or DFS when troubleshooting a service dependency issue?**
    - Give a concrete example of how graph traversal algorithms could help in an operational scenario.

14. **Describe a situation where understanding algorithm complexity would be important for system performance in an SRE context.**
    - How would you identify and address a potential algorithmic bottleneck?

15. **Explain how you would design an efficient caching system using the data structures we've discussed.**
    - What would be your eviction policy and why?