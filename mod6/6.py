from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "About Page"

@app.errorhandler(404)
def page_not_found(e):
    # Get the list of all available routes
    routes = [str(route) for route in app.url_map.iter_rules() if route.endpoint != 'static']
    
    # Render a template that displays all available routes
    return render_template('404.html', routes=routes), 404

if __name__ == "__main__":
    app.run(debug=True)
