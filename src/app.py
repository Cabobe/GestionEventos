from flask import Flask
from config import config
from routes import IndexRoutes

app = Flask(__name__)

#Definicio de pagina no encontrada
def page_not_found(error):
    return "<h1>Pagina no encontrada.</h1>",404

if __name__ =='__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(IndexRoutes.main,url_prefix='/api/routes')
    
#Manejador de excepciones
    app.register_error_handler(404,page_not_found)
    app.run()
