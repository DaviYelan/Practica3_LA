from flask import Blueprint, jsonify, abort, request, render_template, redirect 
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
from controls.exception.linkedEmpty import LinkedEmpty
from controls.tda.linked.binarySearch import BinarySearch
from controls.tda.linked.insercion import Insercion
from controls.tda.linked.burbuja import Burbuja
from controls.tda.linked.linearSearch import LinearSearch
from controls.tda.linked.merge import Merge
from controls.tda.linked.quick import QuickSort
from controls.tda.linked.shell import ShellSort
from controls.tda.linked.linkedList import Linked_List
from models.attention import Attention
from models.server import Server
from datetime import datetime
from controls.ventana.json_utils import save_to_json, load_from_json

router = Blueprint('router', __name__)

# Inicializar servidores
servers = load_from_json()


#GET es para presentar datos
#POST guardar datos, modificar datos y el inicio de sesion
#
@router.route('/')
def home():
    return render_template("template.html")
    
#lista personas
@router.route('/personas')
def lista_personas():
    pd = PersonaDaoControl()
    lista = pd._list()
    array_personas = lista.toArray
    lista.toList(array_personas)
    return render_template("nene/lista.html", lista=lista.toArray)

#Lista personas
@router.route('/personas/ver')
def ver_guardar():
    return render_template("nene/guardar.html")\

#Lista personas
@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos) -1)
    print(nene)
    return render_template("nene/editar.html", data = nene )

#ordenar personas
@router.route('/personas/ordenar', methods=["GET"])
def ordenar_personas():
    sort_method = request.args.get("sortMethod")
    sort_attribute = request.args.get("sortAttribute")
    sort_order = request.args.get("sortOrder")
    descending = True if sort_order == "desc" else False

    pd = PersonaDaoControl()
    lista = pd._list()
    burbuja = Burbuja()
    insercion = Insercion()
    merge = Merge()
    quick = QuickSort()
    shell = ShellSort()


    # Convertimos de lista a array
    array_personas = lista.toArray

    # Metdos de ordenacion
    if sort_method == "burbuja":
        if descending:
            array_personas = burbuja.sort_burbuja_attribute_descendent(array_personas, sort_attribute)
        else:
            array_personas = burbuja.sort_burbuja_attribute_ascendent(array_personas, sort_attribute)
    elif sort_method == "insercion":
        if descending:
            array_personas = insercion.sort_insercion_attribute_descendent(array_personas, sort_attribute)
        else:
            array_personas = insercion.sort_insercion_attribute_ascendent(array_personas, sort_attribute)
    elif sort_method == "merge":
        if descending:
            array_personas = merge.sort_merge_attribute_descendent(array_personas, sort_attribute)
        else:
            array_personas = merge.sort_merge_attribute_ascendent(array_personas, sort_attribute)
    elif sort_method == "quick":
        if descending:
            array_personas = quick.sort_quick_attribute_descendent(array_personas, sort_attribute)
        else:
            array_personas = quick.sort_quick_attribute_ascendent(array_personas, sort_attribute)
    elif sort_method == "shell":
        if descending:
            array_personas = shell.sort_shell_attribute_descendent(array_personas, sort_attribute)
        else:
            array_personas = shell.sort_shell_attribute_ascendent(array_personas, sort_attribute)

    # Convertimos el array a lista
    lista.toList(array_personas)

    return render_template("nene/lista.html", lista=lista.toArray)

#guardar personas
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    #pd._persona._id = data["id"]
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)

@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    nene = pd._list().get(int(data["id"]))
    if not "apellido" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._id = data["id"]
    pd._persona._apellidos = data["apellido"]
    pd._persona._nombres = data["nombre"]
    pd._persona._direccion = data["dir"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["fono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.merge(int(pos) -1)
    return redirect("/personas", code=302)

#Buscar personas
@router.route('/personas/buscar', methods=["GET"])
def buscar_personas():
    query = request.args.get("query")
    search_attribute = request.args.get("searchAttribute")
    search_method = request.args.get("metodo_busqueda")
    starts_with = request.args.get("startsWith") == "true"

    pd = PersonaDaoControl()
    lista = pd._list()
    array_personas = lista.toArray

    result = []
    if search_method == "binario":
        result = BinarySearch.search(array_personas, search_attribute, query, starts_with)
    elif search_method == "lineal":
        result = LinearSearch.search(array_personas, search_attribute, query, starts_with)
    else:
        return "Método de búsqueda no válido"

    return render_template('nene/lista.html', lista=result)


#Ventanilla
@router.route('/atenciones/registrar/<person_id>', methods=["GET", "POST"])
def registrar_atencion(person_id):
    if request.method == "GET":
        return render_template("nene/registrar_atencion.html", person_id=person_id)

    if request.method == "POST":
        data = request.form
        server_id = int(data["server_id"])
        rating = data["rating"]
        time_taken = float(data["time_taken"])
        date = datetime.now()

        attention = Attention(person_id, server_id, rating, date, time_taken)
        servers[server_id - 1].add_attention(attention)

        save_to_json(servers)  # Guardar en el JSON

        return redirect("/personas", code=302)

@router.route('/atenciones/lista')
def lista_atenciones():
    atenciones = []
    for server in servers:
        atenciones.extend(server.attentions)
    return render_template("nene/lista_atenciones.html", atenciones=atenciones)