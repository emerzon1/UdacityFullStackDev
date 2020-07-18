import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def add_cors_headers(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PUT, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        res = {}
        for i in categories:
            res[i.id] = i.type
        return jsonify({'categories': res})
    '''
  @TODO:
  Create an endpoint to handle GET requests for questions,
  including pagination (every 10 questions).
  This endpoint should return a list of questions,
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions.
  '''
    def question_get_return(page, cID=None, sTerm=None):
      if cID:
        questions = Question.query.filter(Question.category==cID).paginate(page=page, max_per_page=QUESTIONS_PER_PAGE)
        category = Category.query.get(cID)
        if(not category):
          abort(404)
        category_type=category.type
      elif sTerm:
        questions = Question.query.filter(func.lower(Question.question).contains(sTerm.lower())).paginate(max_per_page=QUESTIONS_PER_PAGE, page=page)
        category_type = ' '
      else:
        questions = Question.query.paginate(
          max_per_page=QUESTIONS_PER_PAGE, page=page)
        category_type = ' '
      questions = [dict(question.format()) for question in questions.items]
      categories = Category.query.all()

      c_res = {}
      for category in categories:
        c_res[category.id] = category.type
      result = {
        "questions": questions,
        "total_questions": len(questions),
        "current_category": category_type,
        'categories': c_res
      }
      return result

    @app.route('/questions', methods=['GET'])
    def get_questions():
      page = request.args.get('page', 1, type=int)

      result = question_get_return(page)

      if len(result) == 0:
        abort(400)

      return jsonify(result)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
      question = Question.query.get(question_id)
      if not question:
        abort(404)
      try:
        question.delete()
      except Exception:
        abort(500)
      return jsonify({'message' : 'Delete Successful'})

  
    @app.route('/questions',methods=['POST'])
    def add_question():
      data = request.json
      if ((data.get('question') == '') or (data.get('answer') == '') or (data.get('category') == '') or (data.get('difficulty') == '')):
        abort(422)
      try:
        q = Question(question=data.get('question', ''), answer=data.get('answer'), category=data.get('category'), difficulty=data.get('difficulty'))
        q.insert()
      except Exception:
        abort(422)
      return jsonify({'message' : 'success'})

    @app.route('/questions/search', methods=['POST'])
    def search():
      sTerm = request.json.get('searchTerm', '')
      res = question_get_return(1, sTerm = sTerm)
      if not res.get('questions'):
        abort(404)
      return jsonify(res)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_q_by_c(category_id):
      res = question_get_return(1, cID=category_id)
      if not res.get('questions'):
        abort(404)
      return jsonify(res)

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
      data = request.json
      prev_list = data.get('previous_questions')
      quiz_cat = data.get('quiz_category')
      if not quiz_cat:
        abort(422)
      question = Question.query.filter(Question.category == quiz_cat.get('id')).filter(Question.id.notin_(prev_list)).order_by(func.random()).limit(1).all()
      if question:
        question = dict(question[0].format())
      return jsonfiy({'question' : question})

    @app.errorhandler(404)
    def not_found(error):
      return jsonify({
        'error': 404,
        'message': 'Not Found'
      }), 404

    @app.errorhandler(422)
    def unprocessable(error):
      return jsonify({
        'error': 422,
        'message': 'Unprocessable'
      }), 422

    @app.errorhandler(400)
    def bad_request(error):
      return jsonify({
        'error': 400,
        'message': 'Bad Request'
      }), 400

    @app.errorhandler(500)
    def sever_error(error):
      return jsonify({
        'error': 500,
        'message': 'Sever Error'
      }), 500
    return app
