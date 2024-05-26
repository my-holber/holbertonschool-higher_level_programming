#!/usr/bin/python3x
class MyList(list):
    def print_sorted(self):
        """Выводит отсортированный список (по возрастанию)."""
        print(sorted(self))
