---
title: Advent of Code 2024 - Day 2
date: 2024-12-02 00:00:00
lastmod: 2024-12-20 09:42:58
categories: []
tags:
  - AOC
aliases: 
share: false
draft: "false"
---

# Advent of Code 2024 - Day 2

Recently, I tackled **Day 2 of the Advent of Code 2024**—a coding challenge with a fascinating twist on data analysis and optimization. The task involved analyzing lists of numbers to determine if they were "safe" based on specific rules, with an additional complexity introduced in Part Two.

## The Challenge

The puzzle required checking if:

1. The numbers were either all increasing or all decreasing.
2. Adjacent differences were between 1 and 3 (inclusive).

In Part Two, we could "tolerate a single bad level" by imagining one number removed, potentially transforming an unsafe report into a safe one.

Here's a simplified example of the rules:

- 7 6 4 2 1: Safe, decreasing by 1 or 2.
- 1 2 7 8 9: Unsafe due to a jump of 5.
- 1 3 2 4 5: Unsafe due to changing directions.

## My Approach

1. **Initial Implementation**: I began by writing the safe function to check the basic conditions of sorted order and adjacency differences. This was straightforward but didn't account for Part Two's "single removal" scenario.
2. **Refining for Part Two**: I extended the logic to test all possibilities:
3. **Balancing Optimization and Clarity**: While exploring performance optimizations, I chose readability over premature micro-optimizations. The code's intent needed to remain clear for anyone reviewing it.

Here's the Python function that handled this:

```python
def safe(f):

    if is_safe_list(f):

        ld = largest_adjacent_distance(f)

        return (1, "is Safe distance", ld)

    # Test by removing one element at a time
    for i in range(len(f)):
        modified_list = f[:i] + f[i+1:]
        if is_safe_list(modified_list):
            ld = largest_adjacent_distance(modified_list)
            return (1, "is Safe distance after removing element", ld)

    ld = largest_adjacent_distance(f)
    return (0, "is unsafe", ld)
```

## Key Takeaways

- **Iterative Problem-Solving**: Tackling this challenge reminded me of the importance of breaking problems into manageable steps.
- **Code Readability**: While optimization is important, clarity should always take precedence when others might review your work—or when you revisit it after some time.
- **Learning from Fun**: Advent of Code isn't just a puzzle; it's a chance to explore algorithms, reflect on code design, and grow as a developer.

## Why Share This?

Participating in events like **Advent of Code** is an excellent way to practice and showcase your coding skills. It's not just about solving puzzles but about refining your problem-solving techniques, learning from others, and building community connections.

What are your thoughts on balancing readability and optimization in coding challenges? Let’s discuss! 👇
