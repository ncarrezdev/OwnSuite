'''
This project and its content is under proprietary licence and belongs to Nicolas CARREZ (n.carrez.dev@gmail.com).
Copyright (c) Nicolas CARREZ 

The code in this repository is NOT free for use.
Please read the LICENCE file before making any use of the code below
'''


def flatten_list(list_):
    if (type(list_) not in (list, tuple)):
        return (list_,)
    elif (len(list_) == 0): 
        return ()
    else:
        return flatten_list(list_[0]) + flatten_list(list_[1:])

def get_py_files_list(current_dir):
    import os
    res = []
    dir_content = os.listdir(current_dir)
    folders = [f for f in dir_content if os.path.isdir(os.path.join(current_dir,f))]
    for f in folders:
        res.append(get_py_files_list(os.path.join(current_dir, f)))
    files = [f for f in dir_content if os.path.isfile(os.path.join(current_dir,f))]
    py_files = [f for f in files if f.endswith('.py')]
    for f in py_files:
        res.append(os.path.join(current_dir, f))
    return flatten_list(res)

def check_header(header, file):
    file_to_write = open(file, 'r+')
    file_content  = file_to_write.read()
    if(not file_content.startswith(header)):
        file_to_write.seek(0,0)
        file_to_write.write(header + '\n' + file_content)
    file_to_write.close()

def preppend_py_files_header():    
    for f in get_py_files_list('.'):
        header = open('./HEADER', 'r').read()
        check_header(header, f)