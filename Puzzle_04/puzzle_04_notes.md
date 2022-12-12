# Advent of Code - Puzzle 04 notes

[Official link](https://adventofcode.com/2022/day/4) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_04-part_1_jmt.py)  

The source data for this one contains text in two columns separated by a comma,  
and each column is a range from and to, although they could be the same number  
such as "23-23, 18-18" but generally look something like "7-21, 13-16"

We'll split the input using the comma, and then split each one again using the dash,  
to get an upper and lower range.  We have to find the number of pairs where one   
range is completely inside another. For examle 3-5 is completely inside 3-10.  

Run with:  
```python puzzle_04-part_1_jmt.py```

## Part 2

The second part doesn't require any more complicated data processing to get the answers.  
We produce the same sets of lists, only this time I've done it using a list comprehension  
rather than explicitly assigning members of the list.  If you haven't seen this before or  
had a play with list comprehensions, don't stress, we'll look at them elsewhere.

To get the solution this time, we simply have to check if either bound (lower or upper)  
from one pair is "inside" the other.

Again, proper set math would be a little nicer here, but this gets the job done.

[my solution](puzzle_04-part_2_jmt.py)  

Run with:  
```python puzzle_04-part_2_jmt.py``` 

## Gotchas
We're assuming the data is nicely formatted, and that for each pair it looks like [lower, upper] 
Our tests will fail if the ranges are in the other order.  [6, 4] is "inside" [3 ,7] but won't get  
spotted correctly by our current if logics.  Proper set math would fix this.


# Raw text from web site

--- Day 4: Camp Cleanup ---

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

For the first few pairs, this list means:

    Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
    The Elves in the second pair were each assigned two sections.
    The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

Your puzzle answer was 459.

--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

Your puzzle answer was 779.
