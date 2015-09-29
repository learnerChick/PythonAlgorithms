"""
1) Move n-1 disk from source to aux
2) Move disk #n from source to dest
3) Move n-1 disk from aux to dest
"""

def tower_of_hanoi(disks, source, dest, aux):
    # if number of disks are greater than 1
    if disks >= 1:
        tower_of_hanoi(disks - 1, source, aux, dest)
        move(source, dest)
        tower_of_hanoi(disks - 1, aux, dest, source)


def move(source, dest):
    print("Moving disk from", source, "to", dest)


tower_of_hanoi(3, "A", "B", "C")
tower_of_hanoi(5, "A", "B", "C")
