#!/usr/bin/python3

'''task_02_verboselist.py
Module that add a subclass to list, and customize its methods'''


class VerboseList(list):
    # Creating a subclass to list, in order to custom it
    def append(self, item):
        # Modification of the append method
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, list_item):
        # Modification of the extend method
        super().extend(list_item)
        print(f"Extended the list with [{len(list_item)}] items.")

    def remove(self, item):
        # Modification of the remove method
        if item < len(self) and item >= 0:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=None):
        # Modification of the pop method
        if item is None:
            print(f"Popped [{self[-1]}] from the list.")
            super().pop()
        elif item < len(self) and item >= 0:
            print(f"Popped [{self[item]}] from the list.")
            super().pop(item)
        else:
            super().pop(item)
