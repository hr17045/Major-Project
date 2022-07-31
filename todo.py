import re
import sqlite3
from bottle import route, run, debug, template, request, static_file, error, view, static_file, redirect


# only needed when you run Bottle on mod_wsgi
from bottle import default_app
from datetime import date
req = 0

#mainpage
@route("/")
@route('/home')
def main():
    return template("main.html")

#route for static files
@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='C:/Users/Harvey/Desktop/Major-Project/static')



@route('/todo')
def todo_list():

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()

    output = template('make_table.html', rows=result)
    return output


@route('/new', method='GET')
def new_item():

    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

    else:
        return template('new_task.html') 

@view('select.html')
def select_edit():
    
    req = request.GET.option_value()
    redirect("/edit/{}".format(req))


     #   return template('select.html')



@route('/find_item', method = 'GET')   # executed from index.html and button 'edit item in Todo list' pressed
def show_all_items():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo")
    result = c.fetchall()             # fetches all items in Todo database and stores data in variable 'result'
    c.close()
    
    return template('find_edit_item.tpl',rows=result) # sends result data to template to display all items in todo list and choose item to edit


@route('/find_item', method = 'POST')   # returns edit item ID and stores in variable edit_id
def edit_item_found():
    edit_id = request.POST.get('todoID','').strip()
    redirect('/edit/{}'.format(edit_id))

@route('/edit/<no:int>')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()              #returns task from edit template and stores in variable 'edit' to update Database#
        status = request.GET.status.strip()         # returns status from edit template and stores in variable 'status' to update Database

        if status == 'open':                    
            status = 1                              # stores appropriate value to update status value in Database
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))   # queries Database and updates entry
        conn.commit()                           # writes data to file

        return template('edit_exit.tpl',no=no)  # after editing, displays template for confirmation message and button to return to index page
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        if not cur_data:
            redirect('/invalid_item')

        return template('edit_task.tpl', old=cur_data, no=no)    # template to display item for editing


#------------------------------------------------------------------------------------------------------------
# Find Item to Delete Block
#------------------------------------------------------------------------------------------------------------



@route('/item<item:re:[0-9]+>')
def show_item(item):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' % result[0]


@route('/help')
def help():

    static_file('help.html', root='.')


@route('/json<json:re:[0-9]+>')
def show_json(json):

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


@route('/edititem')
def edit():
    return template('edititem.html')

debug(True)
run(reloader=True)
# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment

