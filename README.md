# vvpd5
## merge sort
The **Merge Sort**  uses a recursive algorithm to achieve its results. The divide-and-conquer algorithm breaks down a big problem into smaller, more manageable pieces that look similar to the initial problem. It then solves these subproblems recursively and puts their solutions together to solve the original problem.
### **advatages of merge sorting:**
+ *merge sort can efficiently sort a list in $`O(n*log(n))`$ time;*
+ *merge sort can be used with linked lists without taking up any more space;*
+ *merge sort algorithm is used to count the number of inversions in the list;*
+ *merge sort is employed in external sorting*
### Here you can see how does the merge sort algorithm work
![merge sort](https://cdn.educba.com/academy/wp-content/uploads/2021/06/7.png)
### what is the use of merge sort?
- [x] Thus, whenever data stability is a priority, consider using merge sort
---
### **Let's see how does the algorithm look like in python**
```
def merge_two_arrays(list_1, list_2):
    res = []
    while len(list_1) != 0 and len(list_2) != 0:
        res.append(min(list_1[0], list_2[0]))
        if list_1[0] <= list_2[0]:
            list_1.pop(0)
        else:
            list_2.pop(0)
    if len(list_1) != 0:
        res.extend(list_1)
    else:
        res.extend(list_2)
    return res
    
def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[:(len(array)//2)])
    right = merge_sort(array[(len(array)//2):])
    return merge_two_arrays(left, right)
```
---
To understand better how the algorithm works you may watch *[this video](https://www.youtube.com/watch?v=JSceec-wEyw&t=51s)*


