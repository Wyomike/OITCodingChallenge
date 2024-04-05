External depencies - only used argparse, as specified in requirements.txt
To run executable - requires -s ROMAN_STRING -d INTEGER, with the string in all caps.

Thought process - I first thought to make some representative variables to make switching easier. I first started on the roman to decimal converter. I tried a for loop at first,
but realized with the requirement of considering the next character, it might be easier with a while loop. I also realized that due to checking the next character I'd need to add 
on some logic at the end to handle the final character. I started doing the conversion to roman logic in the function but decomposed it to its own function to adhere a bit better
to single responsibility and to reduce code replication. I eventually figured out how to handle subtraction by taking in two characters at a time and comparing their values, 
subtracting if one is less than the other. I didn't consider the case where you pass in a weird numeral that might have been like IC. I interpreted the description in the assignment
as givens rather than as test cases. It was due to subtraction that I also had to figure out some logic on timing to polish the end result.
Next I worked on the decimal to roman converter. First, I worked on just getting the most basic possible representation from decimal. I decided to use casting to a string to make it
easy to track where in the number I am. I took each digit and passed it into my single converter function as it's long form. Next, I added logic to handle when the value is 5*10^n.
I eventually just implemented handling 4s and 9s by checking for specific values. Ithen just had to polish my logic to avoid repetitions and order the numerals well. 
Honestly probably the hardest part was just getting the code compiled into a good executable due to my laptop having a messed up python environment from my first forays in cs 236.
The challenge didn't specify if the rules were held to with the input numerals or not, but considering the hypothetical source, I assumed the roman numerals were formatted correctly 
I spent 1 hour and 21 minutes completing the coding challenge.
