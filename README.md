# Keyboard Layout Status

Calculates the number of finger movements required to type something using
different keyboard layouts

I was obsessed with different keyboard layouts. Like everyone else, I wanted to
find the ULTIMATE keyboard layout. Well, It's not that easy, so I wrote a Python
script which takes multiple lines of characters and calculate the finger
movements to that is required to type it.

Supported keyboard layouts are

* qwerty
* dvorak
* colemak
* workman

## Prerequisites

* Python 3

## How to use (on Linux)
I have no idea how to use this on other platforms. I will let you figure out
that XD

* Clone the project or download `kbstatus.py` file
* Run the script on text

```bash
echo hello | python kbstatus.py
```

* On Linux, if you want to run the status on multiple file content, pipe the
  lines to the file. If you want to get the status from one of your JavaScript
  projects, use following.

 ```bash
cat <path to project root>/**/*.js | python kbstatus.py
 ```
## Sample outout
```
-------------QWERTY-------------
No Movements        9786
Finger Movements    32852
Same Finger Use     3198
Up                  18583
Down                4434
Left                685
Right               1148
Top Right           3651
Top Left            638
Bottom Right        883
Bottom Left         2830

-------------DVORAK-------------
No Movements        21754
Finger Movements    20884
Same Finger Use     2105
Up                  10014
Down                3216
Left                1268
Right               3597
Top Right           638
Top Left            773
Bottom Right        495
Bottom Left         883

-------------WORKMAN-------------
No Movements        23961
Finger Movements    18677
Same Finger Use     2062
Up                  9288
Down                5534
Left                638
Right               1148
Top Right           883
Top Left            142
Bottom Right        888
Bottom Left         156

-------------COLEMAK-------------
No Movements        26739
Finger Movements    15899
Same Finger Use     1471
Up                  7183
Down                4434
Left                685
Right               1268
Top Right           1148
Top Left            142
Bottom Right        883
Bottom Left         156
```
