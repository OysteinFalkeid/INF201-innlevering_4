# innlevering 4

# Group members:

# Oystein Falkeid
# e-mail: oystein.falkeid@nmbu.no

# Eirik Mentyjaervi
# e-mail: eirik.mentyjarvi@nmbu.no

import sys
from pathlib import Path

#printer til fil i stedenfor terminal
file = Path('.') / Path('terminal.txt')
sys.stdout = open(file, 'w')

print('innlevering 4')
print()

# How to work on this exercise
# Work on this exercise together with your partner. 
# Do not share your code with other groups. 
# Use VSCode, virtual environments, and a "requirements.txt" file to install and document packages. 
# Only one persontest
# in the group hands in the assignment. 
# Send a screenshot of the submission notification so that both of you know the exercise has been submitted. 
# Indicate both your names and NMBU email addresses on top of your .py file or your notebook. 
# Only share code with your project partner. 
# Persons who hand in alone will not receive points unless we see that they have actively tried to find a partner 
# by adding their name to the Padlet (https://padlet.com/jonaskusch1/exerciseteams2024Links to an external site.) 
# before Tuesday, October 1st.  
# Use the concepts learned in this course to solve the assignment.
#
# Upload your solution before Monday at 2 pm as a Python file or Jupyter Notebook. 
# In addition, if you are using a .py file, upload a .txt file with the output of your code. 
# In case you are using a Jupyter Notebook, generate an output pdf and hand it in. 
# Your points will then be uploaded to Canvas. You cannot submit this exercise multiple times. 
# Exercises that give 0 points are meant to help you or provide a deeper understanding. 
# Since they do not give points, you do not have to solve them, but they will help you become a good programmer. 
# Especially this week's challenge exercise will help you better understand the next lectures and exercises.
#
# This week's exercise involves a non-trivial task description. 
# You will have to generate folders given specific rules, 
# and you will first have to understand how these rules work to start with the implementation. 
# This is supposed to prepare you for the project exercises, 
# where understanding the non-trivial problem you are supposed to solve is part of the programming process 
# and something you should learn in this course. It might help to take notes and discuss with your partner.

#-------------------------------------------------------------------------------------------------------------------
print('Group members:')
print()
# Group members

print('Oystein Falkeid')
print('e-mail: oystein.falkeid@nmbu.no')
print()
print('Eirik Mentyjaervi')
print('e-mail: eirik.mentyjarvi@nmbu.no')   
print()                  

#-------------------------------------------------------------------------------------------------------------------

# Task 0: Warmup exercise (0 points)
# You are tasked with managing directories for a simple project. 
# You will create a project folder, check if certain subdirectories exist, and create them if they don't. 
# You will also learn how to work with both local and global paths.

# 1. Create a function to set up a project directory in the current working directory. 
#   The project name is specified as input to the function.
# 2. Inside the project folder, the function creates two subdirectories:
#----------
# data    -
# output  -
#----------
# 3. Always check if a directory already exists. If it does, print a warning and abort.

# 4. The function should create a file inside the data folder named data.txt.
# 5. After calling the function, check that all directories have been created, and if so, print out their global path.

# Requirements:

# Use Path.cwd() for the current working directory.
# Use Path.mkdir() to create directories and handle exceptions if they already exist.
# Use Path.exists() to check if a folder exists.
# Use Path.touch() to create an empty file.

# If you want to check your solution or run into trouble, watch this video.

#-------------------------------------------------------------------------------------------------------------------
print('Task 0: Warmup exercise (0 points)')
print()

from pathlib import Path 

def create_project_folder(project_name: str = 'No name deffined') -> None:
    print(f'project name is set to \"{project_name}\"')
    print()
    project_dir = Path('.') / Path(project_name)
    
    if not project_dir.is_dir(): #tests if directory exists
        project_dir.mkdir()
        print(f'\"{project_name}\" created')
        print()
        
        data_dir = project_dir / Path('data')
        data_dir.mkdir()
        output_dir = project_dir / Path('output')
        output_dir.mkdir()
        
        with open((data_dir / Path('data.txt')), 'w', encoding='utf_8') as f: #creates an empty txt file.
            pass
        
        directories = list(project_dir.glob('*'))
        
        print('Directories created:')
        for dir in directories:
            print(dir)
        print()
            
        files = list(project_dir.glob('*/*'))
        
        print('Files created:')
        for file in files:
            print(file)
        print()
        
    else: # Aborts if the directory exists
        print(f'A directory with name \"{project_name}\" already exists')

print('enter project name: ', end='')
name = input()
print()
create_project_folder(name)

print()

#-------------------------------------------------------------------------------------------------------------------

# Task 1: Exercise folder creation (5 points)

# Write a program that creates folders from a list of exercises and a list of students. 
# In the following, the folder structure is explained:

# 1 The list of exercises incorporates simple assignments followed by project assignments
# with a part "a" and a part "b". Write a function that generates this list for a given 
# variable project_assignments_start (the number of the exercise at which the project 
# assignments start) and a given total number of exercises. Use list comprehensions to 
# generate this list compactly.

# As an example, if the project assignments start at exercise 3 and there is a total 
# number of 4 exercises, the list of exercises which is returned by the function call 
# exercises = create_exercises(total_number=4, project_assignments_start=3) takes the form

#----------------------------------------------
# exercises = ["1","2","3a","3b","4a","4b"]   -
#----------------------------------------------

# 2 Assume that you are given a list of students and the exercise list described above in (1.). 
# Then, your program should create a folder for each exercise, and the program should 
# create a folder for each student. Your program should create the exercise folders in 
# a parent folder "projects". Folders for exercise X should have the format "exercise_X". 
# Hence, the folder structure should be "projects/exercise_X/Y/", where X is the exercise, 
# and Y is the student's name. That is, given the student list

#-----------------------------------------------
# students = ["Ole", "Sarah"]                  -
#-----------------------------------------------

# and a total number of 4 exercises where the project assignments start at exercise 3, 
# your program should generate the folders

#-----------------------------------------------
# projects/exercise_1/Ole                      -
# projects/exercise_1/Sarah                    -
# projects/exercise_2/Ole                      -
# projects/exercise_2/Sarah                    -
# projects/exercise_3a/Ole                     -
# projects/exercise_3b/Ole                     -
# projects/exercise_3a/Sarah                   -
# projects/exercise_3b/Sarah                   -
# projects/exercise_4a/Ole                     -
# projects/exercise_4b/Ole                     -
# projects/exercise_4a/Sarah                   -
# projects/exercise_4b/Sarah                   -
#-----------------------------------------------

# Note that your program should work for a general list of students, 
# a general number of exercises, and a general variable project_assignments_start. 

# Work on this task as follows:

# 1 Write a function that generates the exercise list. 
# Use list comprehensions to ensure the code of your function 
# (including the function header) does not exceed four lines.

# 2 Create a list of students. You can start with the list that is provided in the example.

# 3 Use the concepts learned in the lecture to create the specified file structure. 
# Ensure that your code works even if the folders already exist.

# 4 Print out the generated file structure with the glob function.

#-------------------------------------------------------------------------------------------------------------------

print('Task 1: Exercise folder creation (5 points)')
print()


from pathlib import Path # imports Path to be used in the creation of directories

def create_exercises(total_number: int = 0, project_assignments_start: int = 0) -> list[str]: # returns a list of exercises that confines to the spesified perameters
    return [f'{i+1}' 
            if i < project_assignments_start else f'{i+1}{chr(65 + j)}' 
            for i in range(total_number) 
            for j in (range(2) if i >= project_assignments_start else [0])] # en linje

projects_dir = Path('.') / Path('projects') # the directori to be filled with exercises
exercises = create_exercises(4, 2) # the exercises spessified
students = ['Ole', 'Sarah'] # the students spesified

if not projects_dir.is_dir(): # tests if the directory exitsts
    projects_dir.mkdir()

for exercise in exercises: # a for loop to test for and create if directories not exixts
    exercise_dir = projects_dir / Path('exercise_' + exercise)
    if not exercise_dir.is_dir(): # tests if the directory exitsts
        exercise_dir.mkdir()
    for student in students:
        student_dir = exercise_dir / Path(student)
        if not student_dir.is_dir(): # tests if the directory exitsts
            student_dir.mkdir()

directories = list(projects_dir.glob('*/*')) # glob to list all directories in project

print('these directories are created:')
for dir in directories:
    print(dir)
    
print()
    
#-------------------------------------------------------------------------------------------------------------------

# Task 2: Challenge Exercise (0 points)

# In this task, you will implement a function to compute the matrix-vector product using two different approaches:

# 1 A custom implementation using a list of lists (your own data format).
# 2 A NumPy implementation.


# Proceed as follows:

# 1 Implement a Custom Matrix-Vector Product Function:
# Define a function matrix_vector_product(matrix, vector) that takes a matrix (as a list of lists) and a vector (as a list) and returns the resulting vector. Try to implement this function as efficiently as possible.

# 2 Implement a NumPy Matrix-Vector Product Function:
# Use NumPy to create a function numpy_matrix_vector_product(matrix, vector) that performs the same operation, but uses the numpy.dot function.

# 3 Timing the Implementations:
# Use the time module to measure and compare the execution time of both implementations. Generate a random matrix and vector for testing.
# Check that the results of your method and numpy match. You can use the np.allclose function. 

#-------------------------------------------------------------------------------------------------------------------

from typing import Union
import numpy
import time
 
print('Task 2: Challenge Exercise (0 points)')
print()

dimentions = 10000

matrix = numpy.random.randint(0, 100, size=(dimentions, dimentions)).tolist()
vector = numpy.random.randint(0, 100, size=dimentions).tolist()


def matrix_vector_product(matrix: list[list[Union[float,int]]], vector: list[list[Union[float, int]]]) -> list:
    dot_product = [ 0 for j in vector]
    shape = len(matrix)
    range_of_shape = range(shape)
    for i in range_of_shape:
        for j in range_of_shape:
            dot_product[i] += matrix[i][j] * vector[j]    
    return dot_product

def numpy_matrix_vector_product(matrix: Union[list[list[float]], numpy.ndarray], vector: Union[list[list[float]], numpy.ndarray]) -> numpy.ndarray:
    return numpy.dot(numpy.asarray(matrix), numpy.asarray(vector))



python_start_time = time.time()

dot_python = matrix_vector_product(matrix=matrix, vector=vector)

numpy_start_time = time.time()

dot_numpy = numpy_matrix_vector_product(matrix=matrix, vector=vector)

end_time = time.time()


print(f'true if the dot product is equal: {numpy.allclose(numpy.asarray(dot_python), dot_numpy)}')
print(f'python used {round((numpy_start_time - python_start_time)*100)/100}s')
print(f'numpy used {round((end_time - numpy_start_time)*100)/100}s')










