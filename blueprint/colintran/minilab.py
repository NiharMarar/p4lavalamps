class BubbleSort:

#
    def BubbleSort(self):
        changes = passes = 0
        last = len(self)
        swapped = True

        while swapped:
            swapped = False
            passes += 1
            for j in range(1, last):
                if self[j - 1] > self[j]:
                    self[j], self[j - 1] = self[j - 1], self[j]  # Swap
                    changes += 1
                    swapped = True
                    last = j

        print(self)

    print("Bubble Sort")

    while True:
        print("Enter a list with spaces between each number.\nClick return when finished.")
        numbers = input()
        items = [int(num) for num in numbers.split() if num.isdigit()]
        if items: BubbleSort()
