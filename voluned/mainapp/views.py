from django.shortcuts import render
from django.template.loader import get_template
import os


BASEPATH="/mainapp/"
fsbasepath=os.path.dirname(os.path.abspath(__file__))

# Create your views here.
def index(request):
    maincontent = """
        <div class="header-content" id="inicio">
            <div class="header-content-inner">
                <h1 id="homeHeading">Your Favorite Source of Free Bootstrap Themes</h1>
                <hr>
                <p>Start Bootstrap can help you build better websites using the Bootstrap CSS framework! Just download your template and start going, no strings attached!</p>
                <a href="#about" class="btn btn-primary btn-xl page-scroll">Find Out More</a>
            </div>
        </div>
    """
    section_content = get_template("inicio.html")
    #with open (os.path.join(fsbasepath, "templates/mainapp/inicio.html")) as f:
    #    section_content = f.read()
    context = dict()
    context["BASEPATH"] = BASEPATH
    context["maincontent"] = maincontent
    context["sections"] = list()
    context["sections"].append(section_content)
    return render(request, 'mainapp/index.html', context)
