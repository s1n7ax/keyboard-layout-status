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

## How to use

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
