from flask import render_template

from app import app
from app.models.library import LibraryModel
from app.models.user import AdminModel

if __name__ == '__main__':
    @app.route('/')
    def index():
        return render_template('index.html')
    
    LibraryModel.objects(id='test').delete()
    new_library = LibraryModel(id='test', title='멋진 도서관').save()
    
    AdminModel.objects(id='test').delete()
    AdminModel.objects(id='test', pw='test', managing_library=new_library).save()
    
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
