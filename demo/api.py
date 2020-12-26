import flask
from flask import request, jsonify
import db_connection

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resource/subject/all', methods=['GET'])
def get_subject():
    db = db_connection.db_connection()
    data = db.query("SELECT * FROM Subject")
    header = ["id", "name"]
    rr = []
    for i in data:
        rt = {}
        for j in range(len(header)):
            rt[header[j]] = i[j]
        rr.append(rt)
    return jsonify(rr)

@app.route('/api/v1/resource/Score/all', methods=['GET'])
def get_score():
    db = db_connection.db_connection()
    data = db.query("SELECT student.student_id, student.student_name, Exam.subject_id, subject.subject_name, Exam.exam_id, exam_name, exam_heso, exam_score, exam_date FROM Student, student_subject, subject, Exam WHERE student.student_id = student_subject.student_id and student_subject.subject_id = Subject.subject_id and subject.subject_id = Exam.subject_id")
    header = ["student_id", "student_name", "subject_id", "subject_name", "exam_id", "exam_name", "exam_heso", "exam_score", "exam_date"]
    rr = []
    for i in data:
        rt = {}
        for j in range(len(header)):
            rt[header[j]] = i[j]
        rr.append(rt)
    return jsonify(rr)


app.run()