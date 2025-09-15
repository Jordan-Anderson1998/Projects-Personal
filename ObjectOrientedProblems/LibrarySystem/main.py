import datetime
from random import randint

"""

Create classes for Book, Member, and Library. Implement methods to:
- Add/remove books
- Register members
- Allow members to borrow and return books
- Track which books are currently borrowed and by whom

The library object will be responsible for managing the inventory of books and lending/returning of books. The library
should also implement a system for keeping track of members and their status of:
- Books borrowed
- Number of books taken out 
"""


class Book:

    def __init__(self):
        self.book_info = {}

    def __str__(self) -> str:
        return str(self.book_info)

    def add_book_info(self, title: str, author: str, isbn: str, genre: str) -> None:

        self.book_info['Title'] = title
        self.book_info['Author'] = author
        self.book_info['ISBN'] = isbn
        self.book_info['Genre'] = genre

    def push_book(self) -> dict:

        return self.book_info


class Member:

    def __init__(self):

        self.members_info = None
        self.library_id = None
        self.outstanding_balance = 0
        self.has_outstanding_balance = False
        self.granted_membership = False

    def __str__(self):

        return str(self.members_info)

    def register_member(self, name: str, address: str, date_of_birth: str, phone_number: str) -> str:

        if not self.has_outstanding_balance:

            current_date = datetime.datetime.now().isoformat()
            formatted_date = current_date.replace('T', ' ')

            member_info = {'Name': name, 'Address': address, 'Date of Birth': date_of_birth, 'Phone Number': phone_number,
                           'Date of Registry': formatted_date}

            self.members_info = member_info

            self.granted_membership = True

            return 'Success'

        print(f"""Sorry: {name}, we cannot accept any new members who have outstanding fees owing to this library. \n
                  Please pay the amount of {self.outstanding_balance} before applying for a membership.
                
            """)

        return 'Rejected'

    def pay_outstanding_balance(self) -> None:

        print(f'Your balance is : {self.outstanding_balance}')

        payment = int(input('Please enter amount to pay: '))

        self.outstanding_balance -= payment

        if self.outstanding_balance <= 0:
            self.has_outstanding_balance = False

        print(f'Your new balance after payment of {payment} is: {self.outstanding_balance}')

    def get_library_card_id(self) -> int|str:

        if self.granted_membership:
            id_number = randint(100000, 500000)
            self.library_id = id_number
            self.members_info['Id Number'] = id_number
            return id_number

        print('Cannot process request, Error1: not a member')
        return 'Error'


class Library:

    def __init__(self):
        self.members = []
        self.books_in_stock = []
        self.book_borrows = []

    def sign_in_member(self, __member_object, name: str):

        if __member_object.library_id is not None:

            print(f'Member: {name} was signed in successfully.')
            self.members.append(__member_object.members_info)

    def add_book(self, __book_object):

        self.books_in_stock.append(__book_object.push_book())

    def remove_book(self, book_name):

        book_to_remove = None

        for book in self.books_in_stock:
            if book['Name'] == book_name:
                book_to_remove = book

        self.books_in_stock.remove(book_to_remove)
        return book_to_remove

    def list_book_inventory(self):

        return self.books_in_stock

    def get_number_of_books_in_stock(self):

        return len(self.books_in_stock)

    def borrow_book(self, book_to_borrow: str, library_card: int, member_name: str, access: bool=False):

        # check if valid member
        for member in self.members:

            if member['Id Number'] == library_card:
                print(f'Found: {member['Name']}, {member['Id Number']}')
                access = True

        # check if any outstanding fees
        if jordan.has_outstanding_balance:
            print(f'Sorry {member_name} you can not borrow a book from the library until all dues have been payed.')

        if access:

            book_name_to_borrow = None

            for book in self.books_in_stock:
                if book['Title'] == book_to_borrow:
                    book_name_to_borrow = book

            if book_name_to_borrow is not None:

                self.books_in_stock.remove(book_name_to_borrow)

            book_checkout_date = datetime.date.today()
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            book_return_due_date = None

            if month < 12:
                book_return_due_date = datetime.date(2025, month + 1, day)
            else:
                book_return_due_date = datetime.date(2026, 1, day)

            print(f'You took out book: {book_to_borrow} on {book_checkout_date}. The book will be due on {book_return_due_date}')

            book_burrow_info = {'Book Name': book_to_borrow, 'Member': member_name, 'Transaction Date': book_checkout_date,
                                'Transaction Number': randint(1000, 100000)}
            self.book_borrows.append(book_burrow_info)

            return tuple([book_checkout_date, book_return_due_date])

        return 'Access Denied'

    def return_book(self, returned_on_time: bool, library_card: int):

        member_info = None

        for member in self.members:
            if member['Id Number'] == library_card:
                member_info = member

        if returned_on_time:
            print(f'Thank you for returning your book on time.')
            return 'Success'

        # if late return of book
        member_info['outstanding_balance'] += 5


if __name__ == '__main__':

    harry_potter = Book()
    harry_potter.add_book_info(title='Harry Potter and the Deathly Hallows', author='J.K. Rowling',
                               isbn='978-1-4028-9462-6', genre='Fantasy/Fiction')

    hamlet = Book()
    hamlet.add_book_info(title='Hamlet', author='William Shakespeare', isbn='N/A', genre='Play/Tragedy')

    pragmatic_programmer = Book()
    pragmatic_programmer.add_book_info(title='The Pragmatic Programmer 20 Year Anniversary', author='David Thomas/Andrew Hunt',
                                       isbn='9780135957059', genre='Technology/Software Engineering/Non Fiction')

    jordan = Member()
    jordan.register_member(name='Jordan Anderson', address='123 Blueberru Avenue', date_of_birth='1998-06-12', phone_number='666-666-666')
    jordan.get_library_card_id()

    julia = Member()
    julia.register_member(name='Julia Hertz', address='456 NukeTown', date_of_birth='1967-09-13', phone_number='999-999-999')
    julia.get_library_card_id()

    library = Library()
    library.sign_in_member(jordan, 'Jordan Anderson')
    library.sign_in_member(julia, name='Julia Hertz')

    library.add_book(hamlet)
    library.add_book(harry_potter)
    library.add_book(pragmatic_programmer)

    print(library.books_in_stock)
    library.borrow_book(book_to_borrow='Hamlet', library_card=jordan.library_id, member_name='Jordan Anderson')

    # hamlet should now be removed
    print(library.books_in_stock)

    print(library.book_borrows)

    library.borrow_book(book_to_borrow='Harry Potter and the Deathly Hollows', library_card=julia.library_id, member_name='Julia Hertz')

    print(library.books_in_stock)
    print(library.book_borrows)

    library.return_book(returned_on_time=True, library_card=jordan.members_info)

    print(library.books_in_stock)
    print(library.book_borrows)

    # library.return_book(returned_on_time=False, library_card=julia.members_info)