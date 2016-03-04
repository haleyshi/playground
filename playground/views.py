from django.shortcuts import render
from django.http import JsonResponse
from . import parsers

BUILD_RUN_RESULT = {'PASS': 'PASS', 'FAIL': 'FAIL', 'COMPILE_FAIL': 'COMPILE_FAIL', 'TIMEOUT': 'TIMEOUT'}
LANGS_SUPPORTED = ['PYTHON', 'GO', 'JAVA', 'C', 'CPP']

def index(request):
    context = {}
    return render(request, 'index.html', context)

def html(request):
    context = {}
    return render(request, 'html.html', context)

def script(request):
    context = {}

    if 'lang' in request.GET:
        context['lang'] = request.GET['lang']

    return render(request, 'script.html', context)

def parse(request):

    code = None
    lang = None

    if 'code' in request.GET:
        if 'lang' in request.GET:
            lang = request.GET['lang']
            code = request.GET['code']

    result = {}

    if code is None:
        result['result'] = BUILD_RUN_RESULT['FAIL']
        result['msg'] = 'Error: Invalid Request without code provided!'
    elif len(code) == 0:
        result['result'] = BUILD_RUN_RESULT['FAIL']
        result['msg'] = 'Error: Empty, no code provided!'
    elif lang is None:
        result['result'] = BUILD_RUN_RESULT['FAIL']
        result['msg'] = 'Error: Invalid Request without language provided!'
    elif lang not in LANGS_SUPPORTED:
        result['result'] = BUILD_RUN_RESULT['FAIL']
        result['msg'] = 'Error: Language %s is not supported!' % lang
    else:
        result = parsers.buildAndRun(lang, code)

    return JsonResponse(result, safe=False)