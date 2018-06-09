import subprocess
import shlex
import json


def _common(act_name, arguments):
    command_raw = "cleos push action bryanrhee {} '[{}]' -j -p bryanrhee@active".format(act_name, arguments)
    command = shlex.split(command_raw)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = p.communicate()

    return out.decode('utf8')

def search(user, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", {}'.format(user, source_lang, target_lang, sentence_id)
    out = _common("search", args)
    ret = json.loads(out)
    return ret

def confirm(user, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", {}'.format(user, source_lang, target_lang, sentence_id)
    out = _common("confirm", args)
    ret = json.loads(out)
    return ret

def inputtag(user, source_lang, target_lang, sentence_id, tag_id):
    args = '"{}", "{}", "{}", {}, {}'.format(user, source_lang, target_lang, sentence_id, tag_id)
    out = _common("inputtag", args)
    ret = json.loads(out)
    return ret

def original(user, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", {}'.format(user, source_lang, target_lang, sentence_id)
    out = _common("original", args)
    ret = json.loads(out)
    return ret

def translate(user, source_lang, target_lang, sentence_id):
    args = '"{}", "{}", "{}", {}'.format(user, source_lang, target_lang, sentence_id)
    out = _common("translate", args)
    ret = json.loads(out)
    return ret
