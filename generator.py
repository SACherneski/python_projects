import random

# generates random names from a list of predefined names

# Generate a random number between 0 and whatever the length of your list is.  In this case it should be a random number between 0 and 6.
# You will need to import a python module called "random". A function inside this module called "randint" will generate a random number.
# use the random number to identify which name in the all_names list that will be selected. You will pull out the name that matches the index.
# For instance, if you randomly generated a 2, your program should pull "Erin" from the list.
# put the name you pulled out of the all_names list into the new list called "selected_names".
# Do this two more times until you have 3 total names inside the list.  This should look something like ["Erin", "Joe", "Stephen"] or any combination of three names.

# after you have three names in the selected_names list, we need to split the names into smaller sections so we can jumble them together to create a new "random" name.
# Think of a good way to do this. The solution should work for very long names, as well as very short names.
# the pseudo-logic for this could be something like, "if the length of the name is less than 4 characters, do nothing and skip to the next name"
# After you have successfully split each name, add them to a new variable called split_names containing the split strings should look something like ["Er", "in", "Joe", "Ste", "phen"]

# The next step should be similar to the first step.  Again you will want to generate a random number from 0 to the length of the new split_names variable (so in this case, a random number from 0 through 4)
# pull out a random piece of a name and put it into a new variable, called combined_name.  This could look something like ["Joe", "Er", "phen"]
# do this 2 or 3 more times depending on how long you want the generated name to be

# Final steps:
# you want first to combine all pieces of the name together into one string and set this to a new variable.. ["JoeErphen"]
# Lowercase the entire string, and then uppercase the first letter in the string
# Print the completed string to the screen.  "Your random name is: "


def main():
    all_names = ["Stephen", "Misha", "Erin", "Leslie", "Jared", "Joe", "Justin"]

    # sample three random numbers
    rand_nums = random.sample(range(len(all_names)), 3)

    # get the names at each index in all_names that correspond to the rand_nums
    rand_names = [all_names[i] for i in rand_nums]

    split_names = [rand]

    print("Welcome to the Python Name Generator!\n")

main()
