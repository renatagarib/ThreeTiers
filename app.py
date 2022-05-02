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


@app.route("/students", methods=["POST"])
def create():
    body = request.get_json()
    print(body)

    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='nilmar21',
                                database='mydb')

    with connection:
        with connection.cursor() as cursor:
            try:
                sql = 'INSERT INTO `aluno` (`CPF`, `nome`, `idade`, `email`, `media`, `historico`, `id_turma`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql, (body['CPF'], body['nome'], body['idade'], body['email'], body['media'], body['historico'], body['id_turma']))
                connection.commit()
                return create_response(201, "student", to_json([body['CPF'], body['nome'], body['idade'], body['email'], body['media'], body['historico'], body['id_turma']]), "Criado com sucesso")
            except Exception as e:
                print('Erro', e)
                return create_response(400, "usuario", {}, "Erro ao cadastrar")

@app.route('/students/<id>', methods=["PUT"])
def update(id):

    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='nilmar21',
                                database='mydb')
    
    body = request.get_json()

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `aluno` WHERE `CPF`=%s"
            cursor.execute(sql, id)
            result = list(cursor.fetchone())

            try:
                if 'nome' in body:
                    result[1] = body['nome']
                if 'idade' in body:
                    result[2] = body['idade']
                if 'email' in body:
                    result[3] = body['email']
                if 'media' in body:
                    result[4] = body['media']
                if 'historico' in body:
                    result[5] = body['historico']
                if 'id_turma' in body:
                    result[6] = body['id_turma']
            
                sql = 'UPDATE aluno SET nome = %s, idade = %s, email = %s, media = %s, historico = %s, id_turma = %s WHERE CPF = %s'
                cursor.execute(sql, (result[1], result[2], result[3], result[4], result[5], result[6], id))
                connection.commit()
                return create_response(200, "student", to_json([id, result[1], result[2], result[3], result[4], result[5], result[6]]), "Atualizado com sucesso")
            except Exception as e:
                print('Erro', e)
                return create_response(400, "usuario", {}, "Erro ao atualizar")


@app.route('/students/<id>', methods=["DELETE"])
def delete(id):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='nilmar21',
                                database='mydb')
    
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `aluno` WHERE `CPF`=%s"
                cursor.execute(sql, id)
                result = cursor.fetchall()
                result_jason = [to_json(student) for student in result]

                sql = 'DELETE FROM aluno WHERE CPF = %s'
                cursor.execute(sql, id)
                connection.commit()
                return create_response(200, "student", result_jason, "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return create_response(400, "usuario", {}, "Erro ao deletar")



def create_response(status, content_name, content, message=False):
    body = {}
    body[content_name] = content

    if (message):
        body['message'] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
