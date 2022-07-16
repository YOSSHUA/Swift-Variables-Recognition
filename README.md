## Project 1 (Swift Statement Recognition). 

## Members:

- Yosshua Cisneros 
- Mariano Franco Gómez 
- Anairam Mar Cuevas 


## Steps to run the statement classifier


Create a txt file with swift code. You must have the Python interpreter to execute the source code.

Execute the following command from the terminal:

```
python -u <path to file>project.py <path to file>test_file.txt
```


Where test_file.txt is the file from which you want to get the classification.
To run the sample file run `python -u project.py tester.txt`.

## Requirements

- Total number of declared variables.
- Total number of types used in the declarations found.
- Total number of declared variables of each type.
- Total number of initialized variables.
- Total number of array type variables.
- Sorting of all variable names by declared type.


## Processing

We decided to divide the classification into several regular expressions to make it more understandable, although some are very long because of the different cases that were considered.


We divide the text to be processed into lines separated by the regular expression "`\nlet |nvar `". 

Then, for each line we searched for all the substrings that were accepted by the regular expression for each type of variable and replaced it with an empty string to facilitate the recognition of the subsequent ones and to decrease the size of the string after a match. 


Since we sorted all the variables, we stored the results in a dictionary to print the results.

### Notes

Two additional files(`regexListStrInit.txt`,`regexStrInit.txt`) are included that contain some regular expressions that were altered when we tried to assign them directly to python variables.