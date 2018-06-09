import subprocess
import shlex
import json


def _common(act_name, arguments):
    command_raw = "cleos push action bryanrhee {} '[{}]' -j -p bryanrhee@active".format(act_name, arguments)
    command = shlex.split(command_raw)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = p.communicate()
    ret = json.loads(out.decode('utf8'))['processed']['action_traces'][0]["console"] if out.decode('utf8') is not None and len(out.decode('utf8')) > 0 else '[]'

    return ret

def getWholeAction(page=1):
    out = _common("getwholeact", page)
    ret = json.loads(out)
    return ret

def getUserAction(user, page=1):
    args = '"{}", {}'.format(user, page)
    out = _common("getuseract", args)
    ret = json.loads(out)
    return ret
