def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

print(
    "Enter as many # as you want.\n Any positive #.\nLeave a space between each one."
)
numbers = input()
items = [int(num) for num in numbers.split() if num.isdigit()]
our_list = items
bubble_sort(our_list)



print(our_list)

# def niharbb():
#
#     if request.method == 'POST':
#         form = request.form
#         def bubble_sort(our_list):
#             # We go through the list as many times as there are elements
#             for i in range(len(our_list)):
#                 # We want the last pair of adjacent elements to be (n-2, n-1)
#                 for j in range(len(our_list) - 1):
#                     if our_list[j] > our_list[j+1]:
#                         # Swap
#                         our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
#
#         print(
#             "Enter as many # as you want.\n Any positive #.\nLeave a space between each one."
#         )
#         numbers = input()
#         items = [int(num) for num in numbers.split() if num.isdigit()]
#         our_list = items
#         bubble_sort(our_list)
#
#
#
#         nbbb = print(our_list)
#         return render_template("niharbb.html", display = nbbb)
