from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/bubble', methods=['POST'])
def bubbleSort(arr):
    # import user input
    bubble = request.form['bubble']
    n = len(arr)

    # Filter through array
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Filter the array from 0 to n-i-1
            # Swap if the number found is greater than the next number
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Numbers to be sorted, including user inputted number
    arr = [64, 34, 25, 12, 22, 11, 90, bubble]

    # sort
    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])

    # return home
    return render_template("bfsort.html")