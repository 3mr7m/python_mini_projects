# ------------------------------------------
# Data Structure 
# List []
# Variable [-1] or [0]
# append in list[]
# extend in list[]
# remove in list[]
# ------------------------------------------

books = [ "laws", "improving", "reading", "English"]
print(books[0]) # => "laws"
print(books[1]) # => "improving"
print(books[2]) # => "reading"
print(books[3]) # => "English"
print(books[-1]) # => "English"
print(books[-2]) # => "reading"
print(books[-3]) # => "improving"
print(f"The best books That i love to read is {books[1]} and The worst book that i read is {books[-1]}")
books[-2] = "raeding books in python"
print(books[-2]) # => "reading books in python"
books.append("french books")
print(books[-1]) # => "french books"

#-------------------------------------------------
add_list = input ("Add the first color do you like: ")
colors =[]
colors.append(add_list)
ask_user = input("Do you want to add another color? yes or no: ").lower()
if ask_user =="yes":
    add_list = input ("Add the sconed color do you like: ")
    colors.append(add_list)
    print(f"Here is your list {[colors]}")
elif ask_user == "no":
    print(f"Ok Here is your list {[colors]}")
else:
    print("try later")
# --------------------------------------------------
class_a = ["ahmed", "hafez", "sayed", "osama", "osman", "amr"]
class_b = ["esraa", "soaad", "mervt", "abrar", "noraa", "shrouk"]
new_class =[]
new_class.extend(class_a)
new_class.extend(class_b) 
# you can use this: new_class = class_a + class_b
print(new_class)
print(class_a)
# --------------------------------------------------
num=[1,2,3,4,5,6,7,7,8,89,9]
num.remove(89) # => Will remove 89
print(num)
# --------------------------------------------------
