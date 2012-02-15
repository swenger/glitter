import glob
import logging
import os
import subprocess
import tempfile

import gl

def finddocs(basedir="/local/wenger/code/man4", docbook="/usr/bin/docbook2x-texi", makeinfo="/usr/bin/makeinfo"):
    docs = {}
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.close()

    for filename in sorted(glob.glob(os.path.join(basedir, "gl*.xml"))):
        funcname = os.path.splitext(os.path.basename(filename))[0]
        logging.info("creating docs for %s", funcname)

        docbook_args = [docbook, "--encoding=utf-8", "--string-param", "output-file=%s" % os.path.basename(tfile.name), filename]
        logging.debug("running %s", " ".join(docbook_args))
        p = subprocess.Popen(docbook_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.path.dirname(tfile.name))
        stdout, stderr = p.communicate()
        logging.debug("output from docbook:")
        logging.debug("stdout: %s", stdout)
        logging.debug("stderr: %s", stderr)
        if p.returncode != 0:
            logging.warn("docbook returned exit code %d while processing %s", p.returncode, funcname)
            continue

        makeinfo_args = [makeinfo, "--plaintext", tfile.name]
        logging.debug("running %s", " ".join(makeinfo_args))
        p = subprocess.Popen(makeinfo_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.path.dirname(tfile.name))
        stdout, stderr = p.communicate()
        logging.debug("output from makeinfo:")
        logging.debug("stdout: %s", stdout)
        logging.debug("stderr: %s", stderr)
        if p.returncode != 0:
            logging.warn("makeinfo returned exit code %d while processing %s", p.returncode, funcname)
            continue

        docs[funcname] = stdout[:stdout.find("\x1f")]

    os.remove(tfile.name)
    return docs

def finddoc(name, docs):
    if name in docs:
        return docs[name]
    candidates = sorted([x for x in docs if name.startswith(x)])
    if candidates:
        logging.info("forwarding docs for %s to %s", name, candidates[-1])
        return docs[candidates[-1]]
    for key, value in {"Disable": "Enable", "Unmap": "Map", "End": "Begin"}.items():
        if key in name:
            doc = finddoc(name.replace(key, value), docs)
            if doc:
                logging.info("forwarding docs for %s to %s", name, name.replace(key, value))
                return doc
    return None

def adddoc(basedir, docbook="/usr/bin/docbook2x-texi", makeinfo="/usr/bin/makeinfo", generate_code=False):
    docs = finddocs()

    for key, value in sorted(gl.__dict__.items()):
        if key.startswith("gl"):
            doc = finddoc(key, docs)
            if doc:
                if generate_code:
                    print "%s.__doc__ = '''%s'''" % (key, doc)
                else:
                    gl.__dict__[key].__doc__ = doc
            else:
                logging.warn("no docstring for %s", key)

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.WARN)
    adddoc(basedir=sys.argv[1], generate_code=True)

