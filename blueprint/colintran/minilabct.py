from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/BubbleSort', methods=['POST'])
def BubbleSort:
    # import user input
    strnum = request.form['strnum']
    strarr = strnum.split()
    intlist = map(int, strarr)
    n = len(intlist)

# Filter through array
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Filter the array from 0 to n-i-1
            # Swap if the number found is greater than the next number
            if intlist[j] > intlist[j + 1]:
                intlist[j], intlist[j + 1] = intlist[j + 1], intlist[j]

    # Numbers to be sorted, including user inputted number
    arr = [strnum]

    # sort
    BubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])

    # return home
    return render_template("testing.html")