# Book own list 
books_own = []
# ask user to input first book that he own
book_own1 = input("Enter The name of the book you own: ")
# add first book to books library own
books_own.append(book_own1)
# Do the same thing for book two
book_own2 = input("Enter The name of another book you own:\nor press 'Enter' to skip..")
books_own.append(book_own2)
# print full list user books own
print(f"Your books own: {[books_own]}")
# book wish list
books_wish = []
# ask user to input first book that he wish
book_wish1 = input ("Enter The name of the book you wish to have in the future: ")
# add first book to books library wish
books_wish.append(book_wish1)
# Do the same thing for book two
book_wish2 = input("Enter the name of another book you wish to have in the future\nor press enter to skip..")
books_wish.append(book_wish2)
# print full list user books wish
print(f"Your wish list: {[books_wish]}")
# if user got any book from his wishlist
have_wish = input ("Enter the name from your wish list that you have it\nor press enter to skip..")
# remove it from wishlist
if have_wish in books_wish:
    books_wish.remove(have_wish)
# Print finally result 
print(f"Update Book Own: {[books_own]}")
print(f"Update Book Wish: {[books_wish]}")
# if user give book for free to someone
for_free = input("Enter the name of book you give for free to someone:\nor press enter to skip..")
# remove it
books_own.remove(for_free)
# finally reult
print(f"Finally you books own is: {[books_own]}\nand your books wish is: {[books_wish]}")
# Print finally result 
print(f"Update Book Own: {[books_own]}")
print(f"Update Book Wish: {[books_wish]}")
# if user give book for free to someone
for_free = input("Enter the name of book you give for free to someone:\nor press enter to skip..")
# remove it
books_own.remove(for_free)
# finally reult
print(f"Finally you books own is: {[books_own]}\nand your books wish is: {[books_wish]}")
