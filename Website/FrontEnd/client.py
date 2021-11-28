from flask import Blueprint, json, render_template, request, flash
from BackEnd import server

cli = Blueprint('cli', __name__, template_folder="static")

@cli.route('/', methods=['GET', 'POST'])
def input_form():
    input_values = ['mdvp_fo_hz', 'mdvp_fhi_hz', 'mdvp_flo_hz', 'mdvp_jitter_percent', 'mdvp_jitter_abs', 'mdvp_rap', 'mdvp_ppq', 'jitter_ddp', 'mdvp_shimmer', 'mdvp_shimmer_db', 'shimmer_apq3', 'shimmer_apq5', 'mdvp_apq', 'shimmer_dda', 'nhr', 'hnr', 'rpde', 'dfa', 'spread1', 'spread2', 'd2', 'ppe']
    if request.method == 'GET':
        return render_template("input_form.html", input_values = input_values)
    else:
        input = []

        for para in input_values:
            input.append(float(request.values.get(para)))

        output = server.get_outputs(input)
        if output['overall'] == 1:
            flash("Parkinson's Disease Detected", category='error')
        else:
            flash("Parkinson's Disease Not Detected", category='success')
        return render_template("input_form.html", input_values = input_values, output = output)