---
title: Advent of Code 2024 - Day 7
date: 2024-12-07
tags:
  - AOC
draft: "false"
---
Day 7 of #AdventOfCode 2024 was a complex problem set in a jungle, involving engineers calibrating a rope bridge and sneaky elephants. The challenge, **"Bridge Repair,"** required determining whether equations could be made true by inserting a combination of operators (+, \*, and the new ||) into a series of numbers. While the problem itself was intriguing, it also introduced significant computational challenges, particularly with handling permutations and optimizing the process for large inputs.

***

### 🧩 The Challenge: Complex Equations and Permutations

Each equation in the puzzle came with a test value, and I had to figure out if inserting any combination of +, \*, or the new **concatenation (**||) operator between numbers could produce that test value.

**Part 1:** I focused on equations with + and \*, evaluated left-to-right. For each equation, I checked all possible permutations of the operators between the numbers to see if the equation could match the test value.

**Part 2:** The introduction of the **concatenation (**||) operator in Part 2 added more complexity. Now, not only did I have to handle the combinations of + and \*, but I also had to incorporate the new operator into the permutations, further increasing the number of possible configurations to test.

***

### 💻 Optimizing Permutations with CuPy and Multithreading

The complexity of evaluating permutations across multiple operators was evident, especially as the input size increased. To optimize my solution, I used **CuPy**, a GPU-accelerated library for numerical computation, to speed up calculations, and I also implemented **multithreading** to parallelize the processing of multiple equations.

By using **CuPy** for matrix manipulations and number crunching, I was able to harness the power of the GPU to significantly reduce computation time. Additionally, **multithreading** allowed me to handle multiple equations simultaneously, further speeding up the process.

Here’s how I approached this optimization:

1.  **CuPy for Faster Calculations:** CuPy is a GPU-backed alternative to NumPy, which can accelerate array operations. I used it to handle large matrix calculations for evaluating permutations efficiently.

```python
import cupy as cp
# Advent of Code 2024 - Day 7
array = cp.array(terms)
# Perform element-wise operations
result = cp.multiply(array\[0\], array\[1\]) + array\[2\]
```

2. **Multithreading for Parallel Processing:** I used **Python's** concurrent.futures to parallelize the processing of multiple equations. By distributing the workload across multiple threads, I could process equations faster, particularly when dealing with larger datasets.

```python
from concurrent.futures import ThreadPoolExecutor

def evaluate\_equation(eq):
    # Perform the evaluation logic
    return result

with ThreadPoolExecutor() as executor:
    results = list(executor.map(evaluate\_equation, equations)) 
```

These optimizations allowed me to handle the increased complexity of testing permutations and make the computation process more efficient.

***

### 🔑 Key Takeaways:

1.  **Working with Permutations:** The problem was complicated by the need to test multiple permutations of operators. This introduced significant computational overhead, particularly for larger inputs.
2.  **Optimizing with CuPy:** Using CuPy allowed me to take advantage of GPU acceleration, speeding up the evaluation of equations and matrix operations.
3.  **Multithreading for Efficiency:** Implementing multithreading ensured that I could process multiple equations in parallel, making the solution scalable even with larger datasets.
4.  **Handling Complexity:** The combination of different operators (+, \*, ||) required dynamically adjusting my approach to evaluate the equations. This reinforced the importance of flexibility in algorithm design.

***

### 🚀 Reflections on "Bridge Repair"

Day 7 was a fantastic exercise in both algorithmic problem-solving and performance optimization. While the challenge was primarily about parsing and validating equations, the real fun came from tackling the permutations and optimizing the computation process to handle large numbers of equations quickly. **CuPy** and **multithreading** were indispensable in speeding up the process, and I enjoyed the opportunity to apply these tools to real-world problems.

***

### 📣 Looking Ahead

Day 7 provided a deep dive into performance optimization, but there’s no slowing down as we approach Day 8! I’m looking forward to tackling even more complex puzzles and applying new techniques to optimize performance.

How did you approach Day 7? Did you face similar challenges with permutations and performance? Let me know in the comments—let's share our solutions and ideas!

You can check out my solution on GitHub: [Day 7 Solutions](https://github.com/SixFiveMil/Advent_of_Code/tree/main/2024/Day%207)