class library:
  def __init__(self,book):
    self.book_list = book
  def show(self):
    print(*self.book_list)
  def lend_book(self,book_name):
    if book_name in self.book_list:
      self.book_list.remove(book_name)
      print('Thankyou, Book issued ')
      return True
    else:
      print("This book is not availabe ")
      return False

class customer:
  def __init__(self):
    self.bookList = []
  def add_book(self,book_name):
    self.bookList.append(book_name)
  def show(self):
    print(self.bookList)
  def request_book(self):
    print('Enter the book ')
    self.book = input()
    return self.book

lib_cbe = library(['book1','book2','book3','book4','book5','book2'])
sandeep = customer()

while True:
  print('-----------------------------------------------------------------------------')
  print("select the option below ")
  print("1 - Show the list of books \n2 - Lend a book \n3 Customer borrowed books \n0 - exit")
  option = int(input())
  if option == 1:
    lib_cbe.show()
  elif option == 2:
    requested_book = sandeep.request_book()
    status = lib_cbe.lend_book(requested_book)
    if status == True:
      sandeep.add_book(requested_book)
  elif option == 3:
    sandeep.show()

  elif option == 0:
    break

