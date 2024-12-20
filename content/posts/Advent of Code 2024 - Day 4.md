---
title: Advent of Code 2024 - Day 4
date: 2024-12-04 00:00:00
lastmod: 2024-12-20 09:46:20
categories: 
tags:
  - AOC
aliases: 
share: false
draft: "false"
---

Day 4 of #AdventOfCode 2024 took us to the Ceres monitoring station, where the challenge revolved around an intriguing word search puzzle. Titled **"Ceres Search,"** this task tested spatial reasoning, pattern matching, and efficient coding techniques. Let’s dive into the details of the puzzle and how I approached it.

***

## 🧩 The Challenge: Word Searches and Hidden Patterns

The Elf at the Ceres monitoring station presented us with a word search puzzle containing two parts:

**Part 1:** Find all occurrences of the word XMAS in the grid. Words could appear horizontally, vertically, diagonally, forwards, or backwards—overlapping characters were fair game.

**Part 2:** Instead of searching for XMAS, the goal shifted to finding a pattern where the word MAS appeared twice, forming an "X" shape within a 3x3 sub grid.

***

## 💻 My Approach: Breaking Down the Problem

You can find my complete solutions on GitHub here:

- [Part 1 Solution](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%204/y2024-d04-pt1.py)
- [Part 2 Solution](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%204/y2024-d04-pt2.py)

Here’s how I tackled each part:

***

**Part 1:**

- **Goal:** Count all occurrences of XMAS in all eight possible directions (horizontal, vertical, diagonal).
- **Approach:** Defined eight directional vectors for movement across the grid. Wrote a recursive function to search for the word, starting from every grid cell containing the letter X. Ensured bounds checking for valid positions while matching characters.

**Key Functionality:** The recursive search function was the heart of this solution. It handled boundary checks and matched the word letter-by-letter in the specified direction. The overall solution efficiently identified all occurrences of XMAS.

Here’s a snippet from my solution:

```python
def search(x, y, index, dx, dy):
        """Recursive search for the word."""
        if index == len(word):  # Found the complete word
            return 1
        if not is\_valid(x, y) or grid\[x\]\[y\] != word\[index\]:  # Out of bounds or mismatch
            return 0
        return search(x + dx, y + dy, index + 1, dx, dy)
```

***

**Part 2:**

- **Goal:** Identify 3x3 subgrids where two occurrences of MAS formed an "X" shape.
- **Approach:** Converted the word search into a 2D NumPy array for efficient slicing. Iterated over all possible 3x3 subgrids in the array. Validated each subgrid to check if it matched the specified "X-MAS" pattern.

**Key Functionality:** A helper function was used to check each subgrid. By leveraging NumPy's capabilities, I kept the logic concise and the execution fast.

Here’s a snippet from my solution:

```python
def check\_subarray(subarray):
    check = \["MAS", "SAM"\]
    s1 = "".join(subarray.ravel()\[\[0, 4, 8\]\])
    s2 = "".join(subarray.ravel()\[\[2, 4, 6\]\])
    return (s1 in check) and (s2 in check)
```

***

## 🔑 Key Takeaways: Lessons From Day 4

1. **Direction Handling:** The key to solving Part 1 efficiently was clearly defining the eight possible directions and systematically applying them.
2. **Grid Manipulation with NumPy:** For Part 2, using NumPy simplified the process of extracting and analyzing subgrids, saving both time and effort.
3. **Iterative Refinement:** Part 2 required revisiting and refining my approach to ensure edge cases and overlaps were correctly handled.
4. **Debugging Patterns:** Visualizing grids and patterns proved invaluable for understanding mismatches during debugging.

***

## 🚀 Reflections on "Ceres Search"

This puzzle highlighted the importance of modular code design and effective use of libraries like NumPy. Tackling both parts required a mix of spatial reasoning and programming, making this one of the most satisfying challenges so far.

I particularly enjoyed the problem’s transition from a straightforward search in Part 1 to a more intricate pattern-matching exercise in Part 2. It’s these progressive layers of complexity that make Advent of Code such an engaging experience.

***

## 📣 What’s Next?

Day 4 was a blast, and I can’t wait to see what Day 5 brings! How did you approach today’s challenge? Did you use similar strategies, or did you take a completely different route? Share your thoughts and solutions in the comments—I’d love to hear from you!

For those following along, you can explore my code for Day 4 here:

- [Part 1](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%204/y2024-d04-pt1.py)
- [Part 2](https://github.com/SixFiveMil/Advent_of_Code/blob/main/2024/Day%204/y2024-d04-pt2.py)

Let’s keep learning and solving together. 🎄💻

#AdventOfCode2024 #CodingChallenges #ProblemSolving #Python #NumPy