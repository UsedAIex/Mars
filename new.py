from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/<title>")
def name_of_operation(title):
   return render_template('first.html', title=title)


# @app.route("/list_prof/<list_type>")
# def profs(list_type):
#
#    return render_template('prof_list.html', title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
