---
title: Advent of Code 2024 - Day 5
date: 2024-12-05
tags:
  - AOC
draft: "false"
---

Day 5 of #AdventOfCode 2024 involved helping the North Pole printing department solve a crucial issue with the sleigh launch safety manual updates. The puzzle, **"Print Queue,"** required us to ensure that the pages were printed in the correct order based on a set of dependencies, and then find the middle page number for correctly ordered updates. In Part 2, the task was to reorder any incorrect updates and compute the middle page numbers for those.

### 🧩 The Challenge: Page Ordering

The problem was divided into two parts:

**Part 1:** We needed to check whether each update’s pages followed the specified ordering rules. If the pages were in the correct order, we would identify the middle page of each valid update and calculate the sum of these middle page numbers.

**Part 2:** For updates that weren’t in the correct order, we had to reorder the pages using the rules, and then compute the middle page for each of these reordered updates. The final step was to sum up the middle page numbers for these corrected updates.

***

### 💻 My Approach: Parsing the Input and Solving the Problem

You can find my complete solutions here:

*   [Part 1 Solution](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%205/y2024-d05-pt1.py)
*   [Part 2 Solution](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%205/y2024-d05-pt2.py)

**Part 1: Verifying Order**

For the first part, the solution involved the following steps:

1.  **Input Parsing:** The input consists of two parts: ordering rules (which specify the dependencies between pages) and the page updates. I parsed these into lists of rules and updates.
2.  **Checking Page Order:** I wrote a function that verifies if each update respects the ordering rules by comparing the positions of the pages in the update against the given rules.
3.  **Finding the Middle Page:** Once I verified the updates, I calculated the middle page number by finding the page in the middle of each valid update list.

Here's a simplified code snippet from **Part 1**, where I check if an update respects the rules:

def is\_update\_valid(update, rules):
    rule\_set = {(x, y) for x, y in rules if x in update and y in update}
    positions = {page: i for i, page in enumerate(update)}
    return all(positions\[x\] < positions\[y\] for x, y in rule\_set) 

**Part 2: Reordering Incorrect Updates**

For the second part, I used **topological sorting** to reorder the updates that did not respect the page ordering rules:

1.  **Input Parsing:** I reused the input parsing function from Part 1.
2.  **Topological Sorting:** For each incorrect update, I built a graph based on the page ordering rules, then applied topological sorting to reorder the pages.
3.  **Finding the Middle Page:** Once the update was reordered, I computed the middle page number and summed them for all reordered updates.

Here’s the code snippet for **Part 2**, where I reorder the pages using topological sorting:

```python
def reorder\_update(update, rules):
    graph = defaultdict(list)
    in\_degree = defaultdict(int)
    
    applicable\_rules = \[(x, y) for x, y in rules if x in update and y in update\]
    for x, y in applicable\_rules:
        graph\[x\].append(y)
        in\_degree\[y\] += 1
        in\_degree.setdefault(x, 0)
    
    queue = deque(\[node for node in update if in\_degree\[node\] == 0\])
    ordered\_update = \[\]
    while queue:
        node = queue.popleft()
        ordered\_update.append(node)
        for neighbor in graph\[node\]:
            in\_degree\[neighbor\] -= 1
            if in\_degree\[neighbor\] == 0:
                queue.append(neighbor)
    
    return ordered\_update 
```

### 🔑 Key Takeaways:

1.  **Topological Sorting for Dependency Resolution:** Part 2 required me to implement topological sorting, which was a crucial step in ensuring that pages were reordered correctly according to the rules.
2.  **Efficient Input Parsing:** Parsing the input effectively allowed me to handle both rules and updates with ease.
3.  **Middle Page Calculation:** Finding the middle page number involved handling the edge cases when the number of pages in an update was odd or even.

***

### 🚀 Reflections on "Print Queue"

Day 5's challenge was a fantastic exercise in dependency management and sorting. The real fun came from handling the rules and ensuring that pages were printed in the correct order. It was a great opportunity to apply topological sorting and see how it could be used to solve practical problems.

I particularly enjoyed the progression from Part 1 (verifying the order) to Part 2 (reordering the updates). Both parts were highly rewarding and reinforced the importance of clear input handling and algorithmic thinking.

***

### 📣 Looking Ahead

With Day 5 wrapped up, I’m eager to tackle Day 6! These puzzles continue to challenge me and push my understanding of algorithms and problem-solving.

How did you approach today’s challenge? Share your solutions, strategies, or any insights in the comments—I’d love to hear from you!

Follow my progress on GitHub: Day 5 Solutions