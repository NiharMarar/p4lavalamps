from flask import Flask, Blueprint, render_template, request, redirect
from bubblesort.bfbubble.bfbubble import BubbleSort
from bubblesort.bfbubble.bfwords import alphabetize
from bubblesort.bfbubble.bfnums import order
bubblesort_bfbubblesort_bp = Blueprint('bfbubblesort', __name__,
                                         template_folder='templates',
                                         static_folder='static', static_url_path='assets')

@bubblesort_bfbubblesort_bp.route('/bf_bubble', methods=["GET", "POST"])
def bfbubblesort():
    if request.method == 'POST':
        form = request.form
        smallestNum = int(form["smallestNum"])
        largestNum = int(form["largestNum"])
        totalNum = int(form["totalNum"])
        return render_template("bfbubble.html", bubblesort=BubbleSort(smallestNum, largestNum, totalNum), word=alphabetize(form["words"]), num=order(form["nums"]))
    return render_template("bfbubble.html", bubblesort=BubbleSort(0, 10, 5))