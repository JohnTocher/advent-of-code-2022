# Advent of Code - Puzzle 08 notes

[Official link](https://adventofcode.com/2022/day/8) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_08-part_1_jmt.py)

This one is interesting, and doesn't seem to complex in general terms.  Nothing revolutionary or 
particularly clever comes to mind.  When that's the case, I tend to start with a brute force 
approach and see if any shrotcuts appear while I'm coding.  Even average comouters are typcially 
so fast now that it's nearly impossible to tell an efficient solution from a weaker one for all but 
the biggest of data sets.

Start coding and see what happens.  If you want to start smaller, I also downloaded the tiny, 5 x 5 
forest grid to practice on.  That's often worth doing just so that your print debug lines are a bit 
more manageble on the screen.  It's called 'puzzle_08_input_tiny.txt'

Ny algorithm was made up of the following:
- Iterate over the row and column indexes, create a tuple (col, row) to use as look up values (keys)  
for the tree_heights data (dictionary)
- For each tree point, traverse up and down, left and right, to the edges and in each case make a list of 
those points.
- Pass the tree coordinates and the list of adjacent co-ordinates to a function which checks visibility and
returns False if the view of the tree from the direction supplied, is blocked.
- Repeat this for the other three directions
- If all four directions show no visibility, then that tree is hidden from all edges.

Run with:
```python puzzle_08-part_1_jmt.py```

## Part 2

This part requires calculating a new metric for each tree, called aa view score, based on how far in each  
direction you can see.  The algorithm chosen for part 1 can be tweaked to achive this.  It;s often worth 
goin back to a simpler test data set when making significant changes, so might want to use the tiny  
text file to confirm you can get the results demonstrated in the puzzle discussion.

At first I thought I might have to modify the algorithm to include the trees on the edges, but the score 
devised is the multiplication of the four view scores, and at least one of them is defined as zero, so  
the product will zero and obviously not our optimal solution.

I also had to tweak the code that built the list of adjacent trees to make sure it worked from the tree 
we are testing, out towards the edge.  For two (right and down) this was already the case. 

[my solution](puzzle_08-part_2_jmt.py)

Run with:
```python puzzle_08-part_2_jmt.py```

## Gotchas

I have assumed the forest is square, calculating the size variable by counting the rows qhwn 
doing the puzzle input read. 
It wouldn't take much to fix it for rectangular forests.

# Raw text from web site

--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

Your puzzle answer was 1679.

--- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390

    Looking up, its view is not blocked; it can see 1 tree (of height 3).
    Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
    Looking right, its view is not blocked; it can see 2 trees.
    Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390

    Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
    Looking left, its view is not blocked; it can see 2 trees.
    Looking down, its view is also not blocked; it can see 1 tree.
    Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?

Your puzzle answer was 536625.
