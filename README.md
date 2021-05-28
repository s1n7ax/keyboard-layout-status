# Keyboard Layout Status

Calculates the number of finger movements required to type something using
different keyboard layouts.

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

No Movements Needed - No movement needed to type the characters because finger already should be on the key
Finger Movements - Need to move the finger before typing
Same Finger Use - Same finger is used to type different letters ("lo" in "hello" with qwerty)


```
|#                   |QWERTY    |DVORAK    |WORKMAN   |HALMAK    |COLEMAK
|No Finger Movements |9786      |21754     |23961     |23961     |26739
|Finger Movements    |32852     |20884     |18677     |18677     |15899
|Same Finger Usage   |3198      |2105      |2062      |2406      |1471
|Up                  |18583     |10014     |9288      |9840      |7183
|Down                |4434      |3216      |5534      |7676      |4434
|Left                |685       |1268      |638       |0         |685
|Right               |1148      |3597      |1148      |0         |1268
|Top Right           |3651      |638       |883       |13        |1148
|Top Left            |638       |773       |142       |0         |142
|Bottom Right        |883       |495       |888       |0         |883
|Bottom Left         |2830      |883       |156       |1148      |156
```
