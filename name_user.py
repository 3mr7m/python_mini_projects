# This is the first project by 'Amr' About ' ask users about thier names '

print ('welcome back')
name = input('what is your name? ') 

# Remove whitespace from string
name = name.strip()

# First litter in just first Name users capitalize
name = name.capitalize()

# first litter every name users capitalize
name = name.title()

# you can add all thesa together
name = name.strip().title()   # this is bretty code 
#-----------------------------------------------------
# you can have the best code frome first like this:
# name = input("What is your name? ").strip().title()

# split first name into first name and last name:
# first , last = name.split(" ")  # To say hello for just first name
#-----------------------------------------------------
# Say hello to user 
print('Hello ',name)

# Use  variable 'name' with format and print it
print (f'We miss you so much {name} welcome back to our')
#----------------------------------------------------------------
# define function
# def hello():
#     name = input("what's your name? ")
#     print (f'hi {name}')
# hello()

# # Add len() to project and what can he do??
# # to tell user num of his name name_len => bla bla
