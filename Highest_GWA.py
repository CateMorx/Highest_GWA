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

    #opens students_gwa.txt
    with open ("students_gwa.txt") as initial_file:
    #checks if the gwa is higher than the current highest gwa and replaces the values within the variables


#calls the method
#Prints and animates the final output