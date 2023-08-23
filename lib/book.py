#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

# The following code is necessary for the tests to work properly
if __name__ == "__main__":
    book = Book("And Then There Were None", 272)
    print(book.page_count)
    print(book.title)
    book.page_count = "not an integer"
    book.turn_page()

   
    
        