import docx2txt
import re
import os


def extract_keywords_text(text):
    skills = ""
    roles = ""
    softskills = ""
    lines = text.split('\n')
    i = 0
    for line in lines:
        print(line)

        i = i + 1
        if "Technical skill set:- " in line:
            start = line.find("Technical skill set:- ") + len("Technical skill set:- ")
            end = len(line)
            substring = line[start:end]
            skills = skills + (substring)

        if "Compete skill set:- " in line:
            start = line.find("Compete skill set:- ") + len("Compete skill set:- ")
            end = len(line)
            substring = line[start:end]
            softskills = softskills + (substring)

        if "Role: -" in line:
            start = line.find("Role: -") + len("Role: -")
            end = len(line)
            substring = line[start:end]
            roles = roles + substring

    return roles, skills, softskills


def flatten(l):
    try:
        return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
    except IndexError:
        return []

def create_knowledge_base(path):

    jd = []
    for r, d, f in os.walk(path):
        for file in f:
            if 'JD' in file:
                jd.append(os.path.join(r, file))

    role, technical, compete = [],[],[]
    jd =  flatten(jd)
    for jd_file in jd:
        #print(jd_file)
        text = docx2txt.process(jd_file)
        rl, t_skill, s_skill = extract_keywords_text(text)
        role.append(rl)
        technical.append(t_skill.split(','))
        compete.append(s_skill.split(','))

    return role, technical, compete



r,t,c = create_knowledge_base("resumes")
print(r)
print("-----")
print(t)
print("---------")
print(c)