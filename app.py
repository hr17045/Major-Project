from bottle import run, get, view, post, request, redirect

# REDIS, MYSQL/MARIADB, SQLITE, MONGODB
users = [
    { 
        "id":"1", 
        "name":"a", 
        "last_name":"aa", 
        "email":"a@a.com",
        "password":"pass1"
     },
     { 
        "id":"2", 
        "name":"b", 
        "last_name":"bb", 
        "email":"b@b.com",
        "password":"pass2"
     },

]

######################
@get("/login")
@view("login")
def _():
    return

######################
@get("/admin")
@view("admin")
def _():
    return

######################
@post("/login")
def _():
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")
    for user in users:
        if user_email == user["email"] and user_password == user["password"]:
           return redirect("/admin")

    return redirect("/login")

######################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)