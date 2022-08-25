# Sierpinski's Triangle by Anatoliy Kushnir

## How it works

To add triangles click on any of the three buttons on the 
top-right corner.
The first two triangles are always the same, coloured white.
The next triangles created are coloured red, to make it clear
where you are within the triangle.
You can click Reset to start over.

## My approach
I saw a visualisation of Sierpinski's triangle and I thought
it would be an interesting project to code. After completing an assignment for a company involving Pygame, I took the liberty to practice scripting further and develop my own version. My first focus was to be able to add tringles repeatedly on each side of the triangle separately.

The trick is to use only one side of the previous triangle 
when constructing the next. In this way you are able
to add triangles repeatedly in any of the three sides.

After being able to add triangles on all three sides I had to
keep track of the user's choices, which I simply stored in an
array.

In order to make the program easily maintainable and allow other 
programmers to edit/improve the code, it follows the MVC design pattern.

##### UI can become unresponsive if window is resized in certain sizes

## How to run
Made in Python 3.9.7
You need: 
Python, Pygame

To download python paste this link in your browser:
https://www.python.org/downloads/

##### To download Pygame:
In your terminal, type:
python3 -m pip install -U pygame
This will download pygame globally.
If you want Pygame only on your current user type:
python3 -m pip install -U pygame --user

Once you have both dependencies installed, make sure you are in the
"triangles" directory in your terminal and type:
#### python Start.py
