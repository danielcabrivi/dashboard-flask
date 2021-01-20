from flask import Flask, render_template
import processamento

app = Flask(__name__)

@app.route('/')
def home():
    describe = processamento.getDescribe()
    list_temp = processamento.getListTemp()
    list_date = processamento.getListDate()
    head_data = processamento.getHead(10)

    lista_dados = [describe,list_temp,list_date,head_data]
    return render_template('dashboard.html', dados=lista_dados)

app.run(port=5200, debug=True)