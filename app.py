from flask import Flask, Response, request
import pymysql
import json

app = Flask(__name__)

def to_json(list):
    return {'CPF': list[0], 
            'nome': list[1], 
            'idade': list[2], 
            'email': list[3], 
            'media': list[4], 
            'historico': list[5], 
            'id_turma': list[6]}

@app.route("/students", methods=["GET"])
def read_all():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='nilmar21',
                                database='mydb')

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `aluno`"
            cursor.execute(sql)
            result = cursor.fetchall()
            result_jason = [to_json(student) for student in result]
            print(result_jason)
            return create_response(200, 'students', result_jason)

@app.route('/students/<id>', methods=['GET'])
def read_one(id):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='nilmar21',
                                database='mydb')

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `aluno` WHERE `CPF`=%s"
            cursor.execute(sql, id)
            result = cursor.fetchall()
            result_jason = [to_json(student) for student in result]
            print(result_jason)
            return create_response(200, 'students', result_jason)


def create_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if (message):
        body['message'] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
