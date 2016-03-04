import commands
import os

def buildAndRun(lang, code):
    if lang == 'GO':
        return buildAndRunGo(code)
    elif lang == 'PYTHON':
        return buildAndRunPython(code)
    elif lang == 'JAVA':
        return buildAndRunJava(code)
    elif lang == 'C':
        return buildAndRunC(code)
    elif lang == 'CPP':
        return buildAndRunCpp(code)
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

    if os.path.isfile('Hello.class'):
        os.remove("Hello.class")

    return result


def buildAndRunC(code):
    result = {}

    fo = open("code.c", "wb")
    fo.write(code)
    fo.close()

    comp_cmd = 'gcc -o code code.c -Wall'
    comp_status, comp_output = commands.getstatusoutput(comp_cmd)

    if comp_status == 0:
        run_cmd = './code'
        run_status, run_output = commands.getstatusoutput(run_cmd)
        if run_status == 0:
            result['result'] = 'PASS'
        else:
            result['result'] = 'FAIL'
        result['msg'] = run_output
    else:
        result['result'] = 'COMPILE_FAIL'
        result['msg'] = comp_output

    os.remove("code.c")

    if os.path.isfile('code'):
        os.remove("code")

    return result


def buildAndRunCpp(code):
    result = {}

    fo = open("code.cpp", "wb")
    fo.write(code)
    fo.close()

    comp_cmd = 'g++ -o code code.cpp -Wall'
    comp_status, comp_output = commands.getstatusoutput(comp_cmd)

    if comp_status == 0:
        run_cmd = './code'
        run_status, run_output = commands.getstatusoutput(run_cmd)
        if run_status == 0:
            result['result'] = 'PASS'
        else:
            result['result'] = 'FAIL'
        result['msg'] = run_output
    else:
        result['result'] = 'COMPILE_FAIL'
        result['msg'] = comp_output

    os.remove("code.cpp")

    if os.path.isfile('code'):
        os.remove("code")

    return result
