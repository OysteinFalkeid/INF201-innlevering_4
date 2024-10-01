print('innlevering 4')
print()

# How to work on this exercise
# Work on this exercise together with your partner. 
# Do not share your code with other groups. 
# Use VSCode, virtual environments, and a "requirements.txt" file to install and document packages. 
# Only one person in the group hands in the assignment. 
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
print('Group members')
print()
# Group members

print('Øystein Falkeid')
print('e-mail: oystein.falkeid@nmbu.no')
print()
print('Eirik Mentyjærvi')
print('e-mail: ')   
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
    path = Path.cwd()
    project_dir = path / Path(project_name)
    
    if not project_dir.is_dir(): #tests if directory exists
        project_dir.mkdir()
        print(f'\"{project_name}\" created')
        
        sub_dir_1 = project_dir / Path('data')
        sub_dir_1.mkdir()
        sub_dir_2 = project_dir / Path('output')
        sub_dir_2.mkdir()
        
    else: # Aborts if the directory exists
        print(f'A directory with name \"{project_name}\" already exists')

print('enter project name: ', end='')
create_project_folder(input())
print()







