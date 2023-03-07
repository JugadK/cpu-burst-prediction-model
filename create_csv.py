import csv
import random

f = open("super.txt")

training = open("cpu_burst_training.csv", 'w')
testing = open("cpu_burst_testing.csv", 'w')

data = f.read()

x = data.split("update_curr:")


header = ['pid', 'tid', 'flags', 'start_time', 'start_boottime', 'memory_used', 'total_memory_pages', 'number_of_times_ran', 'run_delay', 'last_arrival', 'last_queued', 'thread_flags', 'thread_status', 'thread_cpu', 'stack_pointer', 'stack_pointer_relative', 'instruction_pointer', 'instruction_pointer_relative']

training_writer = csv.writer(training)
testing_writer = csv.writer(testing)

training_writer.writerow(header)
testing_writer.writerow(header)
# Split the input string into a list of substrings

for str in x: 

    substrings = str.split(", ")

    #    Create a dictionary to store the variable names and their values

    variables = {}

    list = []


    for substring in substrings:


        name, value = substring.split(": ",1)
        # Assign the value to a variable with the name as its key
        list.append(value)

    list[-1] = list[-1].split(" ")[0]

    if random.randint(0, 1) == 0:
        training_writer.writerow(list)
    else:
        testing_writer.writerow(list)

