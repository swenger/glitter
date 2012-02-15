import gl

def adderrcheck(generate_code=False):
    for key, value in gl.__dict__.items():
        if key.startswith("gl") and key != "glGetError":
            if generate_code:
                print "%s.errcheck = errcheck" % key
            else:
                from errors import errcheck
                value.errcheck = errcheck

if __name__ == "__main__":
    print "from errors import errcheck"
    adderrcheck(generate_code=True)

