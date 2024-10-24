## Pycalc - A multi-platform Python modules pack for calcs

### What is that thing?
Pycalc is a Python **modules set** that aim to bring back on various *programming* calculators' *MicroPython* ports some *modules* and *functions* from the *standard library* .  

By the way, it's and ooold project, but I've decided to take a look on it  again since more and more **programming calculators** have a **built-in Python support**.
##


### Why?

A lot of manufacturers don't really care (and sometimes the hardware is not well chosen) about a wider support.
Then a lot of beginners are always asking why their scripts doesn't work:

> *If I run it on my calc it crashes , but on my pc it runs idk whyyyy*

And the only solution is to rewrite yourself the function, which breaks completely the user experience... so that's the main target of this project.
##

### How?

So far, it plans to include multiple functions and classes from:

 - `math` → (`comb`, `factorial`, `gcd`, ...)
 - `random`	→ (`choice`, `sample`, `shuffle`, ...)
 - `stat`	→ (`mean`, `median`, `mode`, ...)
 - `itertools` → (`chain`, `count`, `repeat`, ...)
 - `and maybe some other ones`

#### Keep in mind that those librairies are written in Python only, mainly because 95% of the current implementations are closed to contributions and not open-source at all. 

##

### Usage

All you've to do is just download those files  and to import them (with `from x import *` or `import x`) in your scripts. 

##


Feel free to fork and contribute to that project ^^ 
