---
title: Advent of Code 2024 - Day 3
draft: "false"
date: 2024-12-03
tags:
  - AOC
---
Another day, another coding challenge! Day 3 of #AdventOfCode 2024 brought a unique blend of problem-solving and programming finesse with the puzzle titled **"Mull It Over."** This challenge tested not only my ability to write efficient code but also my skills in managing dynamic logic while parsing tricky input.

### 🧩 The Challenge: Two Parts, One Goal

The premise was simple on the surface but layered with complexity as the puzzle progressed.

**Part 1:** The goal was to extract valid mul(X,Y) instructions from a corrupted memory dump and sum their results. Valid instructions followed a precise format, while corrupted fragments needed to be ignored. For instance, valid instructions like mul(44,46) needed to be identified, whereas invalid ones like mul(6,9! or mul(32,64\] were to be skipped.

**Part 2:** Just as I was getting comfortable with Part 1, Part 2 upped the stakes! Here, new commands, do() and don't(), were introduced to dynamically enable or disable the processing of subsequent mul instructions. This required not just identifying valid instructions but also handling state changes in real-time.

***

### 💻 How I Solved It

You can check out my full solutions on GitHub here: [Day 3 Solutions](https://github.com/SixFiveMil/Advent_of_Code/tree/main/2024/Day%203).

**For Part 1:**

*   I leaned heavily on **Regular Expressions (RegEx)** to filter out valid mul(X,Y) instructions.
*   The challenge here was crafting a pattern robust enough to ignore corrupted fragments while reliably extracting valid instructions. The result was a clean and concise implementation for parsing and summing up the products.

**For Part 2:**

*   Initially, I attempted to adapt my RegEx solution to account for the new do() and don't() commands. However, this approach quickly ran into issues when it came to handling dynamic state changes.
*   My solution pivoted to a more interactive approach:I processed the memory dump line by line.I introduced a state flag that toggled processing based on encountering do() (enabled) or don't() (disabled).When don't() appeared, I paused collecting results, and when do() appeared, I resumed. This inline processing method ensured accurate handling of the conditions without overly complicating the logic.

***

### 🔑 What I Learned

Every Advent of Code challenge offers valuable lessons, and today’s puzzle was no exception. Here are some key takeaways:

1.  **The Power of RegEx:** When dealing with unstructured data, RegEx can be a lifesaver. However, it’s important to know its limits—complex state-based conditions often require complementary approaches.
2.  **Dynamic Problem-Solving:** Part 2 was a reminder that not every problem can (or should) be solved in a single pass. Embracing dynamic, state-driven logic helped me overcome the challenge efficiently.
3.  **Patience and Persistence:** Debugging edge cases with state management can be tedious, but it’s incredibly satisfying when the solution finally clicks.

***

### 🎯 Reflections and Strategies

This challenge wasn’t just about writing code—it was a reminder of why I love puzzles like these. They push me to think critically, adapt to new constraints, and refine my skills in both familiar and unfamiliar areas.

One aspect that stood out today was the importance of **breaking the problem into manageable pieces.** By solving Part 1 independently and then focusing on the additional requirements of Part 2, I was able to avoid overwhelming complexity and maintain clarity in my implementation.

***

### 🚀 Looking Ahead

Day 3’s puzzle was a fun mix of analytical problem-solving and practical coding skills. I’m excited to see what Day 4 has in store—each day feels like a mini-adventure, with new twists to keep us on our toes!

For anyone following along:

*   If you’re struggling with similar problems, remember that pivoting your approach isn’t a setback—it’s part of the process.
*   Share your strategies and experiences! How are you tackling this year’s Advent of Code?

Follow my progress on GitHub ([Day 3 Solutions](https://github.com/SixFiveMil/Advent_of_Code/tree/main/2024/Day%203)) and let’s keep the conversation going.

Here’s to another day of learning, coding, and growing. 🎄💻 #CodingLife #ProblemSolving