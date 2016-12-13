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
    customhead =  Template("""
            <link rel='stylesheet' href='/static/css/fullcalendar.min.css' />
            <script src="/static/vendor/jquery/jquery.min.js"></script>
            <script src='/static/js/moment.min.js'></script>
            <script src="/static/vendor/jquery/jquery.min.js"></script>
            <script src='/static/js/fullcalendar.min.js'></script>
            <script> $(document).ready(function() {            
                $(document).ready(function() {
                    $('#calendar').fullCalendar({
                        header: {
                            left: 'prev,next today',
                            center: 'title',
                            right: 'month,basicWeek,basicDay'
                        },
                        defaultDate: '2016-12-12',
                        navLinks: true, // can click day/week names to navigate views
                        editable: true,
                        eventLimit: true, // allow "more" link when too many events
                        events: [
                            {
                                title: 'All Day Event',
                                start: '2016-12-01'
                            },
                            {
                                title: 'Long Event',
                                start: '2016-12-07',
                                end: '2016-12-10'
                            },
                            {
                                id: 999,
                                title: 'Repeating Event',
                                start: '2016-12-09T16:00:00'
                            },
                            {
                                id: 999,
                                title: 'Repeating Event',
                                start: '2016-12-16T16:00:00'
                            },
                            {
                                title: 'Conference',
                                start: '2016-12-11',
                                end: '2016-12-13'
                            },
                            {
                                title: 'Meeting',
                                start: '2016-12-12T10:30:00',
                                end: '2016-12-12T12:30:00'
                            },
                            {
                                title: 'Lunch',
                                start: '2016-12-12T12:00:00'
                            },
                            {
                                title: 'Meeting',
                                start: '2016-12-12T14:30:00'
                            },
                            {
                                title: 'Happy Hour',
                                start: '2016-12-12T17:30:00'
                            },
                            {
                                title: 'Dinner',
                                start: '2016-12-12T20:00:00'
                            },
                            {
                                title: 'Birthday Party',
                                start: '2016-12-13T07:00:00'
                            },
                            {
                                title: 'Click for Google',
                                url: 'http://google.com/',
                                start: '2016-12-28'
                            }
                        ]
                    });
                    
                });
    """).render(emptyContext)
    maincontent = get_template("mainapp/calendario.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["CUSTOM_HEAD"] = customhead
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def eventos (request):
    maincontent = get_template("mainapp/eventos.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
    return render(request,'mainapp/index.html', context)

def reporteasistencia (request):
    maincontent = get_template("mainapp/reporte_asistencia.html").render()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list ()
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
