#!/usr/bin/python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=-1):
        if item == -1:
            res = super().pop()
        else:
            res = super().pop(item)
        print(f"Removed [{res}] from the list.")
