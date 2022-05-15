import json

PATH = "candidates.json"

def load_data(path=PATH):
    """Загружает список кандидатов из файла"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data

def candidates_list():
    """Получает список всех кандидатов"""
    data = load_data()
    return data

def candidates_by_id(id):
    """Получает кандидата по id"""
    candidates = load_data()
    for candidate in candidates:
        if candidate["id"] == id:
            return candidate

def candidates_by_skills(skill_name):
    """Получает кандидата по его навыкам(skill_name)"""

    skill_candidates = []
    skill_lower = skill_name.lower()

    candidates = load_data()
    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_lower in skills:
            skill_candidates.append(candidate)
            continue

    return skill_candidates

def html_for_one_candidate(candidate):

    code_for_candidate = ""

    code_for_candidate += f"<img scr=\"{candidate['picture']}\">\n"
    code_for_candidate += f"{candidate['name']}\n"
    code_for_candidate += f"{candidate['position']}\n"
    code_for_candidate += f"{candidate['skills']}\n"
    code_for_candidate += "\n"

    return f"<pre>{code_for_candidate}<pre>"