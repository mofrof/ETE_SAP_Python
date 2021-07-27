from flask import Flask

webApp = Flask(__name__)

@webApp.route('/inicio')
def ola():
    html = '<h1>Olá mundo</h1>'
    return html

webApp.run()