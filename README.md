# miniature-tribble-counter.py
A practical Python guide to collections.Counter, demonstrating frequency counting for lists, strings, and dictionaries alongside methods like .update(), .elements(), .most_common(), and .subtract().

# 🐍 Python `collections.Counter`: Frequency Counting & Methods

A hands-on Python reference script exploring `Counter` from the built-in `collections` module to count hashable objects and manipulate frequency distributions[cite: 1]. This is the fourth installment in a Python learning repository.

## 📌 Topics Covered

The script (`Counter.py`) is organized into 5 commented sections for step-by-step execution[cite: 1]:

1. **Counting List Elements** – Initializing a `Counter` from a list of integers to automatically tally occurrences (noting the capitalized `Counter` syntax)[cite: 1].
2. **Initializing from Dictionaries & Strings** – Creating `Counter` objects directly from key-value mappings and character sequences[cite: 1].
3. **Accessing Element Counts** – Querying individual item frequencies by key (`a[1]`, `a[2]`, etc.)[cite: 1].
4. **Core `Counter` Methods** – Adding counts with `.update()`, expanding items back into an iterable with `.elements()`, and finding top frequencies using `.most_common(n)`[cite: 1].
5. **In-Place Adjustments & Subtraction** – Incrementing specific element counts directly (`+=`) and reducing counts using `.subtract()`[cite: 1].

## 🚀 How to Run

1. Ensure you have **Python 3.x** installed (no external libraries required—`collections` is part of the Python standard library).
2. Open `Counter.py` in your editor, uncomment the section (`''' ... '''`) you want to test[cite: 1], and run:
   ```bash
   python Counter.py


   from collections import Counter

a = Counter([1, 2, 3, 2, 3])
a.update([4, 5, 6])

print(list(a.elements()))
Output: [1, 2, 2, 3, 3, 4, 5, 6]

print(a.most_common(3))
Output: [(2, 2), (3, 2), (1, 1)]
