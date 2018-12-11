import csv
import os

from os.path import expanduser

output_path = expanduser("~")



selection = [0,0,0]

with open(output_path + '/output.csv', "a") as csvfile:
    outputwriter = csv.writer(csvfile)
    outputwriter.writerow(selection)