from flask import Flask, render_template, request, url_for, flash
import mysql.connector

app=Flask(__name__)
app.secret_key = 'reincarnation@0'

conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Jamon123",
    database="apis"
)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/add')
def agregar():
    return render_template('add.html')

@app.route('/del')
def eliminar():
    return render_template('del.html')

@app.route('/inv')
def inventario():
    cursor=conexion.cursor(dictionary=True)
    query="SELECT * FROM PRODUCTOS"
    cursor.execute(query)
    productos=cursor.fetchall()
    cursor.close()
    return render_template('inv.html', productos=productos)

#FUNCIONES
@app.route('/add_prod', methods=["POST"])
def add_sql():
    id=request.form['id']
    nombre=request.form['nombre']
    cantidad=request.form['cantidad']
    precio=request.form['precio']
    query=f"INSERT INTO PRODUCTOS (IdProducto, Nombre, Precio, Cantidad) VALUES ({id},'{nombre}', '{cantidad}', '{precio}');"
    cursor=conexion.cursor()
    cursor.execute(query)
    cursor.close()
    conexion.commit()
    return render_template('add.html')

@app.route('/del_prod', methods=["POST"])
def del_sql():
    id=request.form['id']
    query=f"DELETE FROM PRODUCTOS WHERE IdProducto={id}"
    cursor=conexion.cursor()
    cursor.execute(query)
    cursor.close()
    conexion.commit()
    return render_template('del.html')

if __name__ == '__main__':
    app.run(debug=True)