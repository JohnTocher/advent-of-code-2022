# Advent of Code - Puzzle 03 notes

[Official link](https://adventofcode.com/2022/day/3) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_03-part_1_jmt.py)  

This problem revolves around comparing the members of two groups of letters and finding the common elements.  
The first task is to split each line into two.  
If we iterate through the items in the first half, and look for it to ocurr in the second half. We have been told that this will only ocurr once for each sack (line of text) so we need only look for that first case.  
In my code, I split the contents of the rucksack into two, assuming that there are an even number of components.  
I haven't done so here, but I would normally introduce an assertion here to confirm this is true.  

Run with:  
```python puzzle_03-part_1_jmt.py```

## Part 2

[my solution](puzzle_03-part_2_jmt.py)  

TBA

Run with:  
```python puzzle_03-part_2_jmt.py```

## Gotchas

# Raw text from web site

--- Day 3: Rucksack Reorganization ---
