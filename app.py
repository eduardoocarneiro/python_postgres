from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Função para criar uma nova conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="flask",
        user="postgres",
        password="QPbtc2C5J2KBBpeyMARz1fNLDJzKaj5y"
    )
    return conn

# Rota principal para exibir a lista de pessoas
@app.route('/')
def index():
    order_by = request.args.get('order_by', 'nome')  # Parâmetro de ordenação padrão
    order_direction = request.args.get('order_direction', 'asc')  # Direção de ordenação padrão

    # Definindo a direção de ordenação
    if order_direction not in ['asc', 'desc']:
        order_direction = 'asc'

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM flask.pessoas ORDER BY {order_by} {order_direction}")
    pessoas = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('pessoas.html', pessoas=pessoas, order_by=order_by, order_direction=order_direction)

# Rota para adicionar uma nova pessoa
@app.route('/add', methods=['POST'])
def add_pessoa():
    nome = request.form['nome']
    idade = request.form['idade']
    sexo = request.form['sexo']
    apelido = request.form['apelido']
    endereco = request.form['endereco']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO flask.pessoas (nome, idade, sexo, apelido, endereco) VALUES (%s, %s, %s, %s, %s)",
                (nome, idade, sexo, apelido, endereco))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

# Rota para excluir uma pessoa
@app.route('/delete/<nome>', methods=['POST'])
def delete_pessoa(nome):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM flask.pessoas WHERE nome = %s", (nome,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

# Rota para editar uma pessoa
@app.route('/edit/<nome>', methods=['POST'])
def edit_pessoa(nome):
    # Pegando os novos dados do formulário
    new_nome = request.form['nome']
    new_idade = request.form['idade']
    new_sexo = request.form['sexo']
    new_apelido = request.form['apelido']
    new_endereco = request.form['endereco']
    
    # Atualizando a pessoa no banco de dados
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE flask.pessoas 
        SET nome = %s, idade = %s, sexo = %s, apelido = %s, endereco = %s 
        WHERE nome = %s
    """, (new_nome, new_idade, new_sexo, new_apelido, new_endereco, nome))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
