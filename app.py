from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta de la página de bienvenida
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de información básica
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        age = request.form['age']
        height = request.form['height']
        gender = request.form['gender']
        skin_tone = request.form['skin_tone']
        return redirect(url_for('result', skin_tone=skin_tone))
    
    return render_template('form.html')

# Ruta para la página de resultados
@app.route('/result/<skin_tone>')
def result(skin_tone):
    return render_template('result.html', skin_tone=skin_tone)

# Ruta para la página de "Sobre Nosotros"
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para la página de "Productos"
@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)

