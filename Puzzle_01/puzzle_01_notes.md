# Advent of Code - Puzzle 01 notes

[Official link](https://adventofcode.com/2022/day/1)
[Main page](../readme.md)

## Part 1
[my solution])(puzzle_01-part_1_jmt.py)

This is a straightwforward exercise in reading some text from a long list in a file.
There are 2224 lines, and there is only one piece of information on each line, and its a number made ip of 1-5 digits
We read each line, and add it the total for the current elf
There are blank lines separating the groups of numbers belonging to each elf
We treat the blank lines as our cue to see if the current "total" is bigger than any we've seen before

```python puzzle_01-part_1_jmt.py```

## Part 2
[my solution](puzzle_01-part_2_jmt.py)

This part requires us to find the top three totals, so we can no longer keep a single total.
Here we introduce the idea of a list.  Python lists can contain all sorts of things, here they will just be integers.
One of the great things about lists is that they can be sorted.
So we modify the code to add each total to a list, sort the list from biggest to smallest, and then grab the first three
Lists items are accessed by their number, in square brackets.  
Indexes start with 0, to the first item is the_list[0], the second the_list[2]

```python puzzle_01-part_2_jmt.py```

## Gotchas

Some gotchas to think about for more real world examples:
It relies on a blank line being present after the last entry, or we might not check the final group
We aren't doing any error checking on the existence of the file
We're assuming that any line with text in it can be safely converted to an integer

# Raw text from web site

--- Day 1: Calorie Counting ---

Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Your puzzle answer was 74711.

--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

Your puzzle answer was 209481.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Shareon Twitter Mastodon] this puzzle.
