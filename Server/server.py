from flask import render_template

from app import app

if __name__ == '__main__':
    @app.route('/')
    def index():
        return render_template('index.html')

    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
