from flask import Flask, render_template, request, redirect, session, flash
from service.endpoints import Endpoints


app = Flask(__name__)
app.secret_key = 'app-hotel'

titulo = 'Hotel - Hospedagem Amiga'
endpoints_admin = Endpoints()
endpoints_usuario = Endpoints(admin=False)

@app.route('/')
def pagina_inicial():
    session['admin_logado'] = None
    return render_template(
        'pagina_inicial.html', titulo=titulo)
        # 'template.html', titulo=titulo)



if __name__ == "__main__":  # Para poder executar quando o arquivo não for importado
    app.run(debug=True)     # Para ir atualizando as modificações que o codigo faz no site