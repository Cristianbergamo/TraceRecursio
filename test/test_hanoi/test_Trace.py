from TraceRecursio.tracer import Trace


class Hanoi:
    def __init__(self, disks, source, helper, destination):
        self.disks = disks
        self.source = source
        self.helper = helper
        self.destination = destination

    def __call__(self):
        self.hanoi(self.disks, self.source, self.helper, self.destination)

    @Trace
    def hanoi(self, disks, source, helper, destination):
        if disks == 1:
            print(f"disk {disks} goes from {source} to {destination}")
            return

        self.hanoi(disks - 1, source, destination, helper)
        print(f"disk {disks} goes from {source} to {destination}")
        self.hanoi(disks - 1, helper, source, destination)


@Trace
def hanoi_2(disks, source, helper, destination):
    if disks == 1:
        print(f"disk {disks} goes from {source} to {destination}")
        return

    hanoi_2(disks - 1, source, destination, helper)
    print(f"disk {disks} goes from {source} to {destination}")
    hanoi_2(disks - 1, helper, source, destination)


if __name__ == "__main__":
    # Driver code
    # disks = int(input("Number of disks to be displaced: "))
    """
    Tower names passed as arguments:
    Source: A
    Helper: B
    Destination: C
    """
    # Actual function call
    hanoi = Hanoi(4, "A", "B", "C")
    hanoi()
    hanoi_2(4, "A", "B", "C")
    Trace.get_graph("hanoi_2")
    Trace.get_graph("hanoi")
