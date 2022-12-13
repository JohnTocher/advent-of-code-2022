# Advent of Code - Puzzle 07 notes

[Official link](https://adventofcode.com/2022/day/7) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_07-part_1_jmt.py)

In my opinion, this puzzle bumps up the complexity quite a bit, in terms of general problem solving. 
There are comments in the code, but discussing the overall flow would be best done on a white board 
or something along those lines.

The first task is to build a record of the file system folders based on the system input provided

Once we've built up the input, we need to build a recursive function to calculte the size of a folder 
meaning the size of the file contained directly within it, as well as the sum of the sizes for all of
the subfolders

Once we have that ability we can answer the question fairly easily.

Run with:
```python puzzle_07-part_1_jmt.py```

## Part 2

TBA

[my solution](puzzle_07-part_2_jmt.py)

Run with:
```python puzzle_07-part_2_jmt.py```

## Gotchas

This problem doesn't guarantee anything about the actual file system, we are only acting on 
the results provided by manually traversing bits of the file system and getting listings. 
There is no guarantee that this would actually cover the entire file system, although that 
isn't the actual problem in this case.


# Raw text from web site

TBA
