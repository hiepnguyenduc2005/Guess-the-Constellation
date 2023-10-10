# GUESS THE CONSTELLATION
#### Video Demo:  https://youtu.be/Df76YbEyi3o
#### Description:

I created a game called **GUESS THE CONSTELLATION** as the final project of CS50P and since I am a big fan of the mysterious night sky.

This game allows participants to guess the **constellation** that contains one of the top brightest stars randomly chosen from the list. The player can have _three_ chances to guess before the correct answer is given. If the user types the correct answer, the game ends immediately and prints _'Correct'_. Otherwise, the game will print _'Incorrect'_ or _'Invalid input'_ and ask for another prompt.

In the **project.py** file, besides the **main** function, here are four top-level functions: **get_star** (generate a random bright star),**get_constellation** (get the user's input for the answer), **compare_pair** (to validate the answer), and **final_result** (to show the answer for the final response). The list of stars is provided in the **bright_star.csv** (in this sample there are 10 brightest ones), while the list of 88 IAU constellations is typed in **constellation.txt**. If the user's input is not in the constellation list, the system will respond _'Invalid input'_.

In the  **test_project.py** file, the three last functions are tested, and all pass. I also try to raise an error to test the **get_constellation** function.

I try to use my knowledge of Conditionals, Loops, Exceptions, Libraries, Unit tests, and File I/O to finish this project. I would like to improve this project later with classes and regular expressions or allow participants to prompt in abbreviations or more bright stars.  
