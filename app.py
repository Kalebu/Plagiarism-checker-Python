import os
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load the spacy model that you have installed
nlp = spacy.load('en_core_web_md')


student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_files.remove("requirements.txt")
student_notes = [open(_file, encoding='utf-8').read() for _file in student_files]


def preprocess(text):
    # Remove stop words
    stop_words = set(spacy.lang.en.stop_words.STOP_WORDS)
    return ' '.join([token.text.lower() for token in nlp(text) if not token.is_stop])


def vectorize(Text):
    vectors = [preprocess(text) for text in Text]
    return TfidfVectorizer().fit_transform(vectors).toarray()


def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])


vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))
plagiarism_results = set()


def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    return plagiarism_results


for data in check_plagiarism():
    print(data)
