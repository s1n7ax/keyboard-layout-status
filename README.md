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
-------------QWERTY-------------
No Movements Needed                9786
Finger Movements                   32852
Same Finger Usege                  3198

Finger Up Movement                 18583
Finger Down Movement               4434
Finger Left Movement               685
Finger Right Movement              1148
Finger Top Right Movement          3651
Finger Top Left Movement           638
Finger Bottom Right  Movement      883
Finger Bottom Left Movement        2830

-------------DVORAK-------------
No Movements Needed                21754
Finger Movements                   20884
Same Finger Usege                  2105

Finger Up Movement                 10014
Finger Down Movement               3216
Finger Left Movement               1268
Finger Right Movement              3597
Finger Top Right Movement          638
Finger Top Left Movement           773
Finger Bottom Right  Movement      495
Finger Bottom Left Movement        883

-------------WORKMAN-------------
No Movements Needed                23961
Finger Movements                   18677
Same Finger Usege                  2062

Finger Up Movement                 9288
Finger Down Movement               5534
Finger Left Movement               638
Finger Right Movement              1148
Finger Top Right Movement          883
Finger Top Left Movement           142
Finger Bottom Right  Movement      888
Finger Bottom Left Movement        156

-------------HALMAK-------------
No Movements Needed                23961
Finger Movements                   18677
Same Finger Usege                  2406

Finger Up Movement                 9840
Finger Down Movement               7676
Finger Left Movement               0
Finger Right Movement              0
Finger Top Right Movement          13
Finger Top Left Movement           0
Finger Bottom Right  Movement      0
Finger Bottom Left Movement        1148

-------------COLEMAK-------------
No Movements Needed                26739
Finger Movements                   15899
Same Finger Usege                  1471

Finger Up Movement                 7183
Finger Down Movement               4434
Finger Left Movement               685
Finger Right Movement              1268
Finger Top Right Movement          1148
Finger Top Left Movement           142
Finger Bottom Right  Movement      883
Finger Bottom Left Movement        156
```
