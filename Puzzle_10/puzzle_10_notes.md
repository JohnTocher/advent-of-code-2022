# Advent of Code - Puzzle 10 notes

[Official link](https://adventofcode.com/2022/day/10) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_10-part_1_jmt.py)

This one isn't overly complicated, but does introduce the likelihood of one of the most common problems in 
software development, the "off-by-oe" error.

The problem talks about things happening at the start of a cycle, where they are during a cycle, and what 
happens at the end of a cycle.  None of this is rocket surgery, but if you don't kepe track of it carefully 
it's easy to be out by a little bit.

I also wasted a bucket load of time on this thinking that the longer example on the web page was the same as 
the actual puzzle input.  They are about the same size, but not the same.


Run with:
```python puzzle_10-part_1_jmt.py```

## Part 2

The wording on this one was a little inconsistent, and again the off-by-one possibilities are many! 
Pixel positions are discussed as zero-based, while the first cycle is 1, not zero.

Also see my notes on the range statement I was used to check the bounds of the sprite.
Once I sorted that out, the algorihm worked as expected, and the display rendered nicely.

[my solution](puzzle_10-part_2_jmt.py)

Run with:
```python puzzle_10-part_2_jmt.py```

## Gotchas

My initial check for the pixel position being inside the sprite was to check: 
pixel_pos in range(register -1, register +1)

for example with a register value of 5, the sprite cover positiosn 4,5,6
so a pixel position of 6 should be covered, but for python, the range(4,6) is doesn't include the 
boundary value of 6, much like in a for loop. It might be just me, but this is the first time a range 
statement threw me like that.

TBA

# Raw text from web site

TBA
