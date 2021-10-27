class Device:
    def __init__(self, name: str, connect_by):
        self.name = name
        self.connected_by = connect_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.disconnected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


printer1 = Printer("Printer", "USB", 500)

print(printer1)
printer1.disconnected()

printer1.print(450)
