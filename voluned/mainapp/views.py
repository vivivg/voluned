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
                <h1 id="homeHeading">Tu puedes hacer el CAMBIO<br />EN LA VIDA<br />DE NUESTRO PLANETA<br /></h1>
                <hr>
                <a href="/static/img/voluntariado/fullsize/voluhuerto.jpg" class="portfolio-box">
                    <img src="/static/img/voluntariado/thumbnails/voluhuerto.jpg" class="img-responsive" alt="">
                    <div class="portfolio-box-caption">
                        <div class="portfolio-box-caption-content">
                            <div class="project-category text-faded">
                                Voluntariado
                            </div>
                            <div class="project-name">
                                en huertos
                            </div>
                        </div>
                    </div>
                </a>
                <br />
                <p><a href="#contactenos" class="btn btn-primary btn-xl page-scroll">Contactenos</a></p>
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
    maincontent = get_template("mainapp/user_mantenimiento.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def calendario (request):
    maincontent  = get_template("mainapp/calendario.html"    ).render()
    customheader = get_template("mainapp/calendario_hdr.html").render()
    customfooter = get_template("mainapp/calendario_ftr.html").render()
    context                  = dict()
    context["BASEPATH"]      = BASEPATH
    context["maincontent"]   = maincontent
    context["CUSTOM_HEAD"]   = customheader
    context["CUSTOM_FOOTER"] = customfooter
    context["sections"]      = list ()
    return render(request,'mainapp/index.html', context)

def eventos (request):
    maincontent = get_template("mainapp/eventos.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def reporteasistencia (request):
    maincontent  = get_template("mainapp/reporte_asistencia.html"    ).render()
    customheader = get_template("mainapp/reporte_asistencia_hdr.html").render()
    customfooter = get_template("mainapp/reporte_asistencia_ftr.html").render()
    context                  = dict()
    context["BASEPATH"]      = BASEPATH
    context["maincontent"]   = maincontent
    context["CUSTOM_HEAD"]   = customheader
    context["CUSTOM_FOOTER"] = customfooter
    context["sections"]      = list ()
    return render(request,'mainapp/index.html', context)

def viaticos (request):
    maincontent = get_template("mainapp/viaticos.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def retrospectiva (request):
    maincontent = get_template("mainapp/retrospectiva.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def registroestudiantes (request):
    maincontent = get_template("mainapp/registro_estudiantes.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)
