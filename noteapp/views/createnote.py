from flask import Blueprint, render_template, request, redirect
import random

bp = Blueprint(__name__,__name__,template_folder='templates')

# def random_id(length=16):
#     final_string = ''
#     chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#     for i in range(0, length):
# 	final_string += chars[random.randint(0, len(chars)-1)]
#     return final_string

@bp.route('/createnote', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
	if request.form.get('createnote'):
	    text = request.form.get('notetext')
	    title_text = request.form.get('title')
	    
	    with open('noteapp/notes/{}.note'.format(title_text), 'w+') as _file:
	      _file.write(text)
		
	    _file.close()
	    return redirect('/')		

	   	
    return render_template('createnote.html')
