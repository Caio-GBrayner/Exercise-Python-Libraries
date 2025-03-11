class Service:
    def __init__(self):
        self.lendings = []
        self.bookings = []

    def lending_book(self, book, member):
        if book.available:
            book.available = False
            self.lendings.append({"book": book, "member": member})
            return f"Book '{book.title}' borrowed for {member.name}."
        else:
            return f"'{book.title}'book is not available for loan."

    def return_book(self, book):
        for lending in self.lendings:
            if lending["book"] == book:
                book.available = True
                self.lendings.remove(lending)
                return f"{book.title} book was returned."
            return f"{book.title} book was not found in loan list."

    def booking_book(self, book, member):
        if book.available:
            return f"'{book.title}' is available for loan, no reservation is necessary."
        else:
            self.lendings.append({"livro": book, "member": member})
            return f"'{book.title}' book was reserved for the member {member.name}."

    def booking_cancel(self, book, member):
        for booking in self.bookings:
            if booking["book"] == book and booking["member"] == member:
                self.bookings.remove(booking)
                return f"'{book.title}' book reservation for member '{member.name}' has been cancelled."
            return f"'{book.title}' book reservation for '{member.name}' has not found."

    def list_loans(self):
        if not self.lendings:
            return "no loans at the moment"
        return "\n".join([f"Book: {l['book'].title}, Member:{l['member'].name}" for l in self.lendings])

    def list_bookings(self):
        if not self.bookings:
            return "no bookings at the moment"
        return "\n".join([f"Book: {b['book'].title}, Member:{b['member'].name}" for b in self.bookings])
