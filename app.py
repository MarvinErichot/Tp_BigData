from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

db_config = {
    'dbname': 'postgres',
    'user': 'admin',
    'password': 'adminadmin',
    'host': 'localhost',
    'port': '5432'
}

@app.route('/films', methods=['GET'])
def get_films():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM film")
        films = cursor.fetchall()
        cursor.close()
        conn.close()
        film_list = [{"id": film[0], "name": film[1], "description": film[2]} for film in films]
        return jsonify({"films": film_list})

    except psycopg2.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

@app.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()
    movie_name = data.get('name')
    movie_description = data.get('description')

    return jsonify({"message": "Film added successfully"})

@app.route('/films/<film_id>', methods=['GET'])
def get_film(film_id):
    return jsonify({"film": {}})

if __name__ == '__main__':
    app.run(debug=True, port=80)