# 📚 Step 1 => Setup
library = []
wishlist = []

# 📚 Step 2 => Adding Individual Books
print("""
   📖 Welcome to Your Personal Library! 📖
   ================================
""")
book_name = input("Enter the name of a book you own: ")
library.append(book_name)

book_name = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book_name:
    library.append(book_name)

print("\n📚 Your Library: ", library)

# 📜 Step 3 => Managing the Wishlist
book_name = input("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(book_name)

book_name = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if book_name:
    wishlist.append(book_name)

print("\n📝 Your Wishlist: ", wishlist)

# 🔄 Step 4 => Merging Wishlist into Library
acquired_book = input("\nEnter the name of a book from your wishlist that you have acquired (or press 'Enter' to skip): ")
if acquired_book in wishlist:
    library.append(acquired_book)
    wishlist.remove(acquired_book)

print("\n📚 Updated Library: ", library)
print("\n📝 Updated Wishlist: ", wishlist)

# 🎁 Step 5 => Donating Books
donated_book = input("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donated_book in library:
    library.remove(donated_book)

print("""
   📚 Final Library: {}
   ================================
   Thank you for managing your books with us! 📖✨
""".format(library))
