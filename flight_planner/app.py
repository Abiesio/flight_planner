from flask import Flask
from flight_planner.routes import register_routes
from flight_planner.services import InMemoryStore, FileStore, SQLStore

def select_data_store():
    data_store = os.getenv('DATA_STORE', 'inmemory').lower()
    if data_store == 'file':
        return FileStore()
    elif data_store == 'sql':
        return SQLStore()
    else:
        return InMemoryStore()

def create_app():
    app = Flask(__name__)
    store = select_data_store()  # Избира хранилището
    app.config['DATA_STORE'] = store  # Запазва хранилището в конфигурацията
    register_routes(app, store)  # Предава на маршрутизацията
    return app
    
    

def main():
    app = create_app()
    app.run(debug=True)

if __name__ == '__main__':
    main()