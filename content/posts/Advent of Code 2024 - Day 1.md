---
title: Advent of Code 2024 - Day 1
date: 2024-12-01
lastmod: 2024-12-20 09:42:58
categories: 
tags:
  - AOC
aliases: 
share: false
draft: "false"
---
The 2024 #AdventOfCode kicked off with a fascinating problem set that combined sorting, pairing, and computational efficiency. Titled **"Historian Hysteria,"** Day 1 tasked us with reconciling two lists of location IDs to help The Historians track down the Chief Historian. With both Part 1 and Part 2 complete, here’s a detailed breakdown of the challenge, my solutions, and key takeaways.

---

#### 🧩 **The Challenge: Reconciling Location Lists**

**Part 1:**  
The goal was to determine the total distance between two lists of location IDs by pairing numbers in sorted order and summing up their absolute differences. The challenge was to efficiently sort the lists and compute the distances, ensuring scalability as the size of the input increased.

For example:

- Pairing the smallest numbers in each list, calculate the absolute difference, then move to the next smallest, and so on.
- Add up these differences to find the total distance.

**Part 2:**  
The second part introduced a new task: calculate a similarity score by determining how often each number in the left list appears in the right list, then multiplying the number by its frequency and summing up the results. This part emphasized the importance of efficiently counting occurrences in the right list.

---

#### 💻 **My Approach: Sorting and Frequency Counting**

You can view my full solutions here:  
➡️ [Day 1 GitHub Repo](https://github.com/SixFiveMil/Advent_of_Code/tree/main/2024/Day%201)

**Part 1: Calculating Total Distance**

1. **Input Parsing:** The first step was to read the input data and separate it into two lists (left and right).
2. **Sorting the Lists:** Using Python’s efficient built-in sorting function (`sorted()`), I arranged both lists in ascending order.
3. **Calculating Distances:** I paired corresponding elements in the sorted lists, calculated the absolute difference, and summed up the results.

Here’s a snippet of my solution for **Part 1**:

python

Copy code

```python
def calculate_total_distance(left, right):
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    return sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

```


**Part 2: Calculating Similarity Score**

1. **Counting Frequencies:** I used Python’s `collections.Counter` to efficiently count the occurrences of each number in the right list.
2. **Calculating Similarity:** For each number in the left list, I multiplied the number by its frequency in the right list and added the results to find the similarity score.

Here’s a snippet of my solution for **Part 2**:


```python
from collections import Counter

def calculate_similarity_score(left, right):
    right_counts = Counter(right)
    return sum(num * right_counts[num] for num in left)

```
---

#### 🔑 **Key Takeaways**

1. **Sorting Efficiency:** Sorting both lists was crucial in Part 1. Python’s `sorted()` function is based on Timsort, which has an average time complexity of O(nlog⁡n)O(n \log n)O(nlogn), making it highly efficient for this task.
2. **Frequency Counting with `Counter`:** Part 2 emphasized the power of `Counter` for fast frequency lookups, which helped reduce computational overhead when handling large datasets.
3. **Scalability:** Both parts were designed with scalability in mind, ensuring the solution could handle larger inputs without significant performance degradation.
4. **Clear Problem Decomposition:** Breaking the problem into logical sub-tasks (parsing, sorting, pairing, counting) made it easier to implement and debug.

---

#### 🚀 **Reflections on Day 1**

Day 1 of Advent of Code set the stage beautifully for the challenges ahead. The problems were accessible yet thought-provoking, offering an excellent opportunity to revisit fundamental concepts like sorting and frequency counting while emphasizing efficiency.

Both parts demonstrated how small tweaks in problem constraints (e.g., switching from absolute differences to frequency-based scores) could lead to entirely new computational challenges. It was a great start to this year’s journey!

---

#### 📣 **Looking Ahead**

With the first day completed, I’m excited to tackle Day 2 and see how the puzzles evolve. The progression from sorting to frequency-based calculations was a smooth one, and I can’t wait to see what new twists await.

How did you approach Day 1? Let’s discuss strategies and insights in the comments below!

Check out my full solution and code here:  
➡️ [Day 1 GitHub Repo](https://github.com/SixFiveMil/Advent_of_Code/tree/main/2024/Day%201)

#AdventOfCode2024 #CodingChallenges #ProblemSolving #Python #Efficiency