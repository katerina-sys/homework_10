import utils
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_candidates():
    candidates = utils.candidates_list()
    all_condidates = ""

    for candidate in candidates:
        all_condidates += f"{candidate['name']}\n"
        all_condidates += f"{candidate['position']}\n"
        all_condidates += f"{candidate['skills']}\n"
        all_condidates +="\n"

    return f"<pre>{all_condidates}<pre>"

@app.route("/candidate/<int:id>")
def page_candidate_by_id(id):
    candidate = utils.candidates_by_id(id)
    html_code = utils.html_for_one_candidate(candidate)

    return html_code

@app.route("/skills/<skill_name>")
def page_skills(skill_name):
    candidates = utils.candidates_by_skills(skill_name)
    all_condidates = ""

    for candidate in candidates:
        all_condidates += f"{candidate['name']}\n"
        all_condidates += f"{candidate['position']}\n"
        all_condidates += f"{candidate['skills']}\n"
        all_condidates += "\n"
    return f"<pre>{all_condidates}<pre>"


if __name__ == '__main__':
    app.run(port=8000)