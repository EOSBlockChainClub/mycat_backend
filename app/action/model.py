import subprocess
import shlex
import json


def _common(act_name, arguments):
    command_raw = "cleos push action bryanrhee {} '[{}]' -j -p bryanrhee@active".format(act_name, arguments)
    command = shlex.split(command_raw)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = p.communicate()

    return out.decode('utf8')

def search(searcher, receiver, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", "{}", {}'.format(searcher, receiver, source_lang, target_lang, sentence_id)
    command_raw = "cleos push action bryanrhee search '[{}]' -j -p bryanrhee@active {}@active".format(args, receiver)
    command = shlex.split(command_raw)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = p.communicate()
    return True

def translate(user, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", {}'.format(user, source_lang, target_lang, sentence_id)
    out = _common("translate", args)
    return True
