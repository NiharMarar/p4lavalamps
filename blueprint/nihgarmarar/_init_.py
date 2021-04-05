from flask import Blueprint, render_template
from flask import request
from francislim.minilab_FL import Books

francislim_bp = Blueprint('francislim', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')

@francislim_bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        a = int(request.form.get("series"))
        bookrecs = Books(a/a)
        return render_template("select-book.html", bookrecs=Books(int(request.form.get("series"))))
    return render_template("select-book.html", bookrecs=Books(1))




    #coder_francislim_bp = Blueprint('coder_francislim', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')


#@coder_francislim_bp.route('/')
#def index():
#return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/cspcbproject")