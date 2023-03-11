from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojos

@app.route('/')
def home_page():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojos.get_all()
    return render_template("dojos.html", dojos = dojos)

@app.route('/create/dojo', methods = ["POST"])
def create_dojo():
    # data = {
    #     "name": request.form["name"]
    # }
    Dojos.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/single_dojo/<int:id>')
def view_dojos_with_ninjas(id):
    data={
        "id": id
    }
    logged_dojo = Dojos.dojo_with_ninjas(data)
    
    return render_template('dojo_show.html', one_dojo = logged_dojo)
    # return render_template('show.html', one_dojo=Dojos.dojos_with_ninjas(data))





# @app.route('/')
# def login_reg():
#     return render_template('log_reg.html')

# @app.route('/user/register', methods=['POST'])
# def register_user():
#     if not user_model.User.validate_user(request.form):
#         return redirect('/')
#     new_user= user_model.User.save_user(request.form)
#     print(new_user)
#     return redirect(f'/user/{new_user}')

