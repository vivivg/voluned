from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context, Template
import os


BASEPATH="/mainapp/"
emptyContext = Context({})


def index(request):
    maincontent = Template("""
        <div class="header-content" id="inicio">
            <div class="header-content-inner">
                <h1 id="homeHeading">Your Favorite Source of Free Bootstrap Themes</h1>
                <hr>
                <p>Start Bootstrap can help you build better websites using the Bootstrap CSS framework! Just download your template and start going, no strings attached!</p>
                <a href="#about" class="btn btn-primary btn-xl page-scroll">Find Out More</a>
            </div>
        </div>
    """).render(emptyContext)
    section_content = get_template("mainapp/inicio.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list()
    context["sections"].append(section_content)
    return render(request, 'mainapp/index.html', context)


def mantenimientousuarios (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/user_mantenimiento.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def calendario (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/calendario.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def eventos (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/eventos.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def reporteasistencia (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/reporte_asistencia.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def viaticos (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/viaticos.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def retrospectiva (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/retrospectiva.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)

def registroestudiantes (request):
    maincontent = Template("""
    """).render(emptyContext)
    section_content = get_template("mainapp/registro_estudiantes.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    context["sections"].append(section_content)
    return render(request,'mainapp/index.html', context)
