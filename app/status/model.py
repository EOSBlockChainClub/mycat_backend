import subprocess
import shlex
import json


def _common(act_name, arguments):
    command_raw = "cleos push action bryanrhee {} '[{}]' -j -p bryanrhee@active".format(act_name, arguments)
    command = shlex.split(command_raw)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = p.communicate()
    ret = json.loads(out.decode('utf8'))['processed']['action_traces'][0]["console"]

    return ret

def getToken(user):
    out = _common("getlctoken", '"{}"'.format(user))
    return out

def getPoint(user):
    out = _common("getlcpoint",'"{}"'.format(user))
    ret = json.loads(out)
    return ret
