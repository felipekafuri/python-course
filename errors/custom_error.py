class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You have attempted to read {pages} pages, but you only have {self.page_count - self.pages_read} pages left."
            )
        self.pages_read += pages
        print(
            f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 100)

try:
    python101.read(10)
    python101.read(99)
except TooManyPagesReadError as e:
    print(e)
