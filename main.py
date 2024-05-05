from flask import Flask, request, render_template
import mysql.connector
import re

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Crear Base de Datos</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Crear Base de Datos MySQL</h1>
        <form action="/crear-base-de-datos" method="POST">
            <input type="text" name="nombre_db" placeholder="Nombre de la Base de Datos" class="input-field">
            <button type="submit" class="btn">Crear Base de Datos</button>
        </form>
        {% if message %}
            <p>{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/crear-base-de-datos', methods=['POST'])
def create_database():
    dbname = request.form['nombre_db']
    message = ""

    # Validar el nombre de la base de datos
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', dbname):
        message = "El nombre de la base de datos debe comenzar con una letra y solo puede contener letras, números, guiones bajos (_) y guiones (-)."
        return render_template('index.html', message=message)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Reemplaza con tu nombre de usuario de MySQL
            password=""  # Reemplaza con tu contraseña de MySQL
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {dbname};")
        message = "Se creó exitosamente la base de datos."
    except mysql.connector.Error as error:
        message = f"No se pudo crear la base de datos: {error}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)