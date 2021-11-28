from flask import Blueprint, json, render_template, jsonify, request

cli = Blueprint('cli', __name__, template_folder="static")

@cli.route('/', methods=['GET', 'POST'])
def input_form():
    if request.method == 'GET':
        return render_template("input_form.html")
    else:
        print("POST Received")
        #print(request.values)
        for v in request.values:
            print(v)

        return render_template("input_form.html")