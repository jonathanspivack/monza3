import os
import hashlib
from pathlib import Path
#lst = ['mellon','stacey']

def read_from_namespace_file(file_name):
    lst = []
    with open(file_name) as f:
        for line in f:
            lst.append(line[:-1])
    
    
    return sorted(list(set(lst[1:])))


def hash_namespace(lst):
    
    #clean_lst = []
    #for word in lst:
    #    word = word.replace("-","_")
    #    clean_lst.append('zzz' + word + 'qqq')
    

    words_dict = {}
    for word in lst:
         hash_object = hashlib.sha1(word.encode('utf-8'))
         words_dict[word] = 'zz' + hash_object.hexdigest()   
    
    return words_dict
    


def generate_stuff(lst,words_dict):
    for word in lst:
        #print(word)
        #os.system('touch templates/{}.html'.format(word))
        #Path('run/core/templates/{}.hmtl'.format(word)).touch()

        os.system('echo {} > run/core/templates/{}.html'.format(word,words_dict[word]))
        #file = open("run/core/templates/{}.html".format(words_dict[word]),"a")
        #file.write("<br>")
        #file.write("<a href='/buy>buy</a>")
        #file.close()
        #print('created html file {}'.format(words_dict[word]))
        os.system('echo \#!/usr/bin/env python3 > run/core/controllers/{}.py'.format(words_dict[word]))
        

        file = open("run/core/controllers/{}.py".format(words_dict[word]),"w")
        file.write("#/usr/bin/env\n")
        file.write("from flask import Blueprint, render_template\n")
        file.write("controller = Blueprint('{}', __name__, url_prefix='/{}')\n".format(words_dict[word],word))
        file.write("@controller.route('/',methods=['GET'])\n")
        file.write("def show_{}():\n".format(words_dict[word]))
        file.write("\t return render_template('{}.html')\n".format(words_dict[word]))
        file.write("@controller.route('/buy',methods=['GET'])\n")
        file.write("def buy():\n")
        file.write("\t return 'you can buy a {} here'".format(word))        
        file.close()

        file = open("run/core/__init__.py","a")
        file.write("from core.controllers.{} import controller as {}\n".format(words_dict[word],words_dict[word]))
        file.write("omnibus.register_blueprint({})\n".format(words_dict[word]))
        file.close

        file = open("run/core/templates/main_page.html","a")
        file.write("<br>")
        file.write("<a href='/{}'>{}</a>".format(word,word))
        file.close()

        file = open("run/core/templates/{}.html".format(words_dict[word]),"a")
        #if word == 'mellon':
        #    file.write("<br>")
        #    file.write("<h1>On sale!!!</h1>")
        file.write("<br>")
        file.write("<a href='/{}/buy'>buy</a>".format(word))
        file.close()

        




lst = read_from_namespace_file('test/namespace.txt')
words_dict = hash_namespace(lst)
generate_stuff(lst,words_dict)

#print(words_dict['if'])
