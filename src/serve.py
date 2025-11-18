from waitress import serve
from app.wsgi import application  # замените 'app' на имя вашего Django проекта

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8000)
