from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de exemplo de usuários para login
usuarios = {
    'miguelpinxs@gmail.com': '@Batatas123',
    '1@1' : '1'
}

# Rota para exibir o formulário de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para exibir o formulário de criação de conta (você pode implementar a criação de usuários aqui)
@app.route('/criar')
def criar():
    return render_template('criar.conta.html')

@app.route('/perfil')
def perfil ():
    return render_template('perfil.html')


# Rota para verificar o login
@app.route('/verificar_login', methods=['POST'])
def verificar_senha():
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Debug para verificar o que está chegando
    print(f"Email: {email}, Senha: {senha}")
    
    # Verifica se o e-mail e senha estão corretos
    if email in usuarios:
        if usuarios[email] == senha:
            return redirect(url_for('perfil'))
        else:
            print(f'Senha incorreta para o usuário: {email}')
            return 'Senha incorreta', 400  # Senha incorreta
    else:
        print(f'Email não encontrado: {email}')
        return 'Email não encontrado', 400  # Email não encontrado

@app.route('/paginainicial')
def paginainicial():
    return render_template('pagina_inicial.html')

@app.route('/pagina_inicial', methods=['POST'])
def trocarpagina():
    return redirect(url_for('paginainicial'))  

if __name__ == '__main__':
    app.run(debug=True)
