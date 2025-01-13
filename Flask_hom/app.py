from flask import Flask
from views.shoe_views import shoe_views
from views.recipe_views import recipe_views

app = Flask(__name__)

app.register_blueprint(shoe_views, url_prefix='/api/shoes')
app.register_blueprint(recipe_views, url_prefix='/api/recipes')

if __name__ == '__main__':
    app.run(debug=True)
