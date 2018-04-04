import flask
from flask import Flask
from flask import render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from setup_db import db, comments, app, responses
from  sqlalchemy.sql.expression import func, select
import random



@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_comment_text = request.form.get('comment_input')
        if len(new_comment_text) > 300:
                comments_quer = db.session.query(comments).all()

                responses_quer = []
                length_responses_inputs = db.session.query(responses).count()
                for response in range(0, len(comments_quer)):
                    rand = random.randrange(0, length_responses_inputs)
                    resp = db.session.query(responses)[rand]
                    responses_quer.append(resp)
                comm_range_in = range(0, len(comments_quer))

                return render_template('calc.html', comments = comments_quer, responses = responses_quer, comm_range = comm_range_in, error = 'Input Too Long')

        new_comment_obj = comments(text = new_comment_text)
        db.session.add(new_comment_obj)
        db.session.commit()

    comments_quer = db.session.query(comments).all()

    responses_quer = []
    length_responses_inputs = db.session.query(responses).count()
    for response in range(0, len(comments_quer)):
        rand = random.randrange(0, length_responses_inputs)
        resp = db.session.query(responses)[rand]
        responses_quer.append(resp)
    comm_range_in = range(0, len(comments_quer))

    return render_template('calc.html', comments = comments_quer, responses = responses_quer, comm_range = comm_range_in)

if __name__ == '__main__':
    app.run(debug = True)
