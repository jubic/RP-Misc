import os.path

PATH = "."

def visit(path):
    dircontent = os.listdir(path)
    for content in dircontent:
        content_path = path + "/" + content    
        if os.path.isdir(content_path):
            print "[DIR ]", content_path
            visit(content_path)
        elif os.path.isfile(content_path):
            print "[FILE]", content_path

visit(PATH)

 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
