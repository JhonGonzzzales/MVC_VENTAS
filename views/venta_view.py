from flask import render_template

def list(ventas):
    return render_template('ventas/index.html', ventas = ventas)

def create(clientes, productos):
    # SE REQUIERE PRODUCTOS Y CLIENTES
    return render_template('ventas/create.html', clientes=clientes, productos=productos)

def edit(venta, clientes, productos):
    # SE REQUIERE PRODUCTOS Y CLIENTES
    return render_template('ventas/edit.html', venta = venta, clientes=clientes, productos=productos)
