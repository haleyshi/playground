import commands
import re

def buildAndRun(lang, code):
    if lang == 'GO':
        return buildAndRunGo(code)
    elif lang == 'PYTHON':
        return buildAndRunPython(code)
    else:
        return {'result': 'FAIL', 'msg': 'Error: Language %s is not supported' % lang}


def buildAndRunGo(code):
    return {}


def buildAndRunPython(code):

    result = {}

    # TODO: Create the temp file code.py & Write code to it

    cmd = 'python code.py'
    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        result['result'] = 'PASS'
    else:
        print cmd, status, output
        result['result'] = 'FAIL'

    result['msg'] = output

    # TODO delete the file code.py

    return result