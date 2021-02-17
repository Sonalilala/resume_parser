import nltk

from pdfminer.high_level import extract_text

import re


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# usecase = 5 years’ experience data engineer having expertise in Java, Scala, Python”


# B.A can add them or we can scrap them from data
skills_db = ['Word', 'Excel', 'Powerpoint', 'Outlook', 'Access', 'OneNote',
             'HTML', 'CSS', 'Javascript', 'WordPress', 'Content Management Systems',
             'C#', 'SQL', 'Java', 'C++', 'HTML', 'JavaScript', 'XML', 'C',
             'Perl', 'Python', 'PHP', 'Objective-C', 'AJAX', 'ASP.NET', 'Ruby',
             ]


# job roles - more data can be added
role = ['software engineer', 'data engineer']


# extracts job role/designation
def extract_designation(input_text):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove stop words
    filtered_text = [w for w in word_tokens if w not in stopwords]

    # remove punctuation
    filtered_tokens = [w for w in filtered_text if w.isalpha()]

    # generate bigrams and tigrams (business analyst)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2,3)))



    role_designation = ""
    # we search bigram and trigram in our job database
    for token in bigrams_trigrams:
        if token.lower() in role:
            role_designation = token

        return role_designation

def extract_skills(input_text):
    stopwords = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove stop words
    filtered_text = [w for w in word_tokens if w not in stopwords]

    # remove punctuation
    filtered_tokens = [w for w in word_tokens  if w.isalpha()]

    # generate bigrams and tigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2,3)))

    # we search for each token in our skills database
    found_skills = set()

    # we search bigram and trigram in our skills database
    for token in filtered_tokens:
        if token.lower() in skills_db:
            found_skills.add(token)

        return  found_skills


def extract_experience(input_text):
    return re.search("\d+\syears", input_text).group(0)


def main():
    text = extract_text_from_pdf("C:\\Users\\acer-pc\\PycharmProjects\\Bis\\challenges_usecases\\resume_parse\\resumes\\Accounts Receiveable\\Profiles\\HIMANSHUDHALL[8_0].pdf")
    skills = extract_skills(text)
    experience = extract_experience(text)
    role = extract_designation(text)
    skills = ",".join(skills)
    print(role + "  experience "+experience +" specialized in "+skills)


if __name__ == '__main__':
    main()



