#Created by: Catelyn Joy M.Morco from BSCPE 1-4
#Assignment 3 
#Write a Python program that read a file containing the name of 20 
#students together with their GWA. 
#The program will outputs the name of the student who got the highest GWA (including the GWA).


#Imports necessary elements
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

#Creates reference for printing
highest_line=''

#Creates Method For Printing student with highest gwa
def process():
    #Allows other def to access the variable
    global highest_line

    #sets the lowest value for gwa
    highest_gwa=5
    highest_student=''

    #opens students_gwa.txt
    with open ("students_gwa.txt") as initial_file:

        #separates each line into name and gwa
        for line in initial_file:
            lines=line.split('-')
            students_name= lines[0]
            students_gwa= float(lines [1])

            #checks if the gwa is higher than the current highest gwa and replaces the values within the variables
            if students_gwa< highest_gwa:
                highest_gwa=students_gwa
                highest_student=students_name

    #Joins all the variables together
    highest_line="The student with the Highest Score: \n" + highest_student + " GWA OF : {:.2f}".format(highest_gwa)


#calls the method
process()

#Prints and animates the final output
def input(screen):
    effects = [
        Cycle(screen,
              FigletText(highest_line, font= 'big'),
              int(screen.height / 2-8)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects,500)])
Screen.wrapper(input)