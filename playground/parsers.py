import commands
import os

def buildAndRun(lang, code):
    if lang == 'GO':
        return buildAndRunGo(code)
    elif lang == 'PYTHON':
        return buildAndRunPython(code)
    elif lang == 'JAVA':
        return buildAndRunJava(code)
    else:
        return {'result': 'FAIL', 'msg': 'Error: Language %s is not supported' % lang}


def buildAndRunGo(code):
    result = {}

    fo = open("code.go", "wb")
    fo.write(code)
    fo.close()

    cmd = 'go run code.go'
    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        result['result'] = 'PASS'
    else:
        #print cmd, status, output
        result['result'] = 'FAIL'

    result['msg'] = output

    os.remove("code.go")

    return result


def buildAndRunPython(code):
    result = {}

    fo = open("code.py", "wb")
    fo.write(code)
    fo.close()

    cmd = 'python code.py'
    status, output = commands.getstatusoutput(cmd)

    if status == 0:
        result['result'] = 'PASS'
    else:
        #print cmd, status, output
        result['result'] = 'FAIL'

    result['msg'] = output

    os.remove("code.py")

    return result


def buildAndRunJava(code):
    result = {}

    fo = open("Hello.java", "wb")
    fo.write(code)
    fo.close()

    comp_cmd = 'javac Hello.java'
    comp_status, comp_output = commands.getstatusoutput(comp_cmd)

    if comp_status == 0:
        run_cmd = 'java Hello'
        run_status, run_output = commands.getstatusoutput(run_cmd)
        if run_status == 0:
            result['result'] = 'PASS'
        else:
            result['result'] = 'FAIL'
        result['msg'] = run_output
    else:
        result['result'] = 'COMPILE_FAIL'
        result['msg'] = comp_output

    os.remove("Hello.java")
    os.remove("Hello.class")

    return result