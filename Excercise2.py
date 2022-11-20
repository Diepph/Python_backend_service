"""
Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format.
The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
"""


from flask import Flask
import mysql.connector

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game2',
         user='root',
         password='manager',
         autocommit=True
         )


app = Flask(__name__)
@app.route('/airport/<icao_code>')
def airport(icao_code):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident ='" + icao_code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            airport_name = row[1]
            location = row[2]

    response = {
        "ICAO": icao_code,
        "Name": airport_name,
        "Location": location
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)