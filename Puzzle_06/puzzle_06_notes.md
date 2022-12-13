# Advent of Code - Puzzle 06 notes

[Official link](https://adventofcode.com/2022/day/6) or back to [main readme](../readme.md)

## Part 1

[my solution](puzzle_06-part_1_jmt.py)  

This time the puzzle input is a single stream of charaters, with no separators.
We don't need to handle this much differently, only that we will only get one "line" when we 
read the input as we have in the past.  We can then loop over the indidual characters in the 
line in much the same way.

The solution is pretty straightforward, add each character to an ever growing list, once the 
list has grown to 4 or more characters, take the last 4 (using list slicing) and put those into 
a set.  A set can contain only unique chacters, duplicates are discarded, so the length of the
set (the number of elements in it) is the number of unique characters in a row we've had.

This isn't a particularly efficient solution, we're keep ean ever-growing list for no good reason, 
and checking that it's greater than 4 is a lot of overhead (other than the first three times!), but  \
we're not aiming for maximum efficiency just yet.

Run with:  
```python puzzle_06-part_1_jmt.py```

## Part 2

The only thing that changed about this part was the number of unique strings required.
As such, all I had to change was three instances of "4" to "14", which is a little unusual. 
I'm wondering why the change was so minor, perhaps the creator was expecting people to use a 
different algorithm which would require more re-work.

[my solution](puzzle_06-part_2_jmt.py)  

Run with:  
```python puzzle_06-part_2_jmt.py```

## Gotchas

Nothing springs to mind, although this puzzle would be a good strting point to talk about differnt 
serial buffer implementations, or other ways you could optimmise this solution.  

# Raw text from web site

--- Day 6: Tuning Trouble ---

The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward the star fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a handheld device. He says that it has many fancy features, but the most important one to set up right now is the communication system.

However, because he's heard you have significant experience dealing with signal-based systems, he convinced the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few colorful sparks.

To be able to communicate with the Elves, the device needs to lock on to their signal. The signal is a series of seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.

For example, suppose you receive the following datastream buffer:

mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.

The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

How many characters need to be processed before the first start-of-packet marker is detected?

Your puzzle answer was 1356.

--- Part Two ---

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?

Your puzzle answer was 2564.
