from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo, ninja

@app.route('/new/ninja')
def new_ninja():
    new_ninja= ninja.Ninjas.save_ninja(request.form)
    return render_template ("ninjas.html", dojos= dojo.Dojos.get_all())

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    ninja.Ninjas.save_ninja(request.form)
    # all_ninjas.Ninjas.save_ninja(request.form)
    return redirect ('/')

@app.route('/update/ninja/<int:id>')
def edit_ninja(id):
    data={
        'id': id
    }
    return render_template('edit.html', one_ninja = ninja.Ninjas.get_one_ninja(data))

@app.route('/update/ninja', methods=['POST'])
def update_ninja():
    update= ninja.Ninjas.update_ninja(request.form)

    # return redirect ('/')


    return redirect(f"/single_dojo/{request.form['dojo_id']}")
    # return redirect(request.referrer)
    
    
@app.route('/ninja/delete/<int:id>/<int:dojo_id>')
def delete_ninja(id, dojo_id):
    data={
        'id': id
    }
    ninja.Ninjas.delete_ninja(data)
    return redirect(f'/single_dojo/{dojo_id}')



# @app.route('/create_post', methods=['POST'])
# def create_post():
#     new_post = post_model.Post.save_post(request.form)
#     return redirect(f'/post/{new_post}')

# @app.route('/ninja/<int:id>')
# def view_one_dojo():
#     # id_data={
#     #     'id': id
#     # }
#     logged_dojo = dojo.Dojos.dojo_with_ninjas()
#     return render_template('show_dojo.html', one_ninja = logged_dojo)


# TRIAL TWO ------------------------------
# @app.route('/update/ninja/<int:id>')
# def edit_ninja(id):
#     data={
#         'id': id
#     }
#     return render_template('edit.html', one_ninja = ninja.Ninjas.get_one_ninja(data))

# @app.route('/update/ninja', methods=['POST'])
# def update_ninja(id):
#     one_ninja= ninja.Ninjas.update_ninja(request.form)
#     # return redirect ('/')

#     data= {
#         "id": id
#     }

#     # return render_template('show.html', one_ninja=one_ninja)
#     return redirect(f'/dojo/{one_ninja.id}')

# @app.route('/dojo/<int:id>')
# def dojo_profile(id):
#     data={
#         "ninja_id":id
#     }
#     updated_dojo =ninja.Ninjas.dojos_with_ninjas(data)
#     return render_template('dojo_show.html', one_dojo = updated_dojo )





# TRIAL ONE-----------------------------

# @app.route('/ninja/delete/<int:id>')
# def delete_ninja(id):
#     data={
#         'id': id
#     }
#     ninja.Ninjas.delete_ninja(data)
#     return redirect('/dojos')

# @app.route('/update/ninja')
# def update_ninja(id):
#     data={
#         'id': id
#     }
#     ninja.Ninjas.update_ninja(data)
#     return render_template('edit.html')





# @app.route('/update/ninja')
# def update_ninja():
#     # ninja.Ninjas.update_ninja(request.form)
#     return render_template('edit.html')

# # @app.route('/update/ninja', methods=['POST'])
# # def update_ninja():
# #     ninja.Ninjas.update_ninja(request.form)
# #     return render_template('edit.html')

# @app.route('/after/update')
# def after_ninja_edit(id):
#     data={
#         'id': id
#     }
#     return redirect('/single_dojo/<int:id>')

# @app.route('/update/ninja/<int:id>', methods=['POST'])
# def update_ninja():
#     ninja.Ninjas.update_ninja(request.form)
#     return redirect(f'/after/update/{id}')

# @app.route('/after/update/<')
# def after_ninja_edit(id):
#     data={
#         'id': id
#     }
#     return redirect('/single_dojo/<int:id>')










# @app.route('/create_post', methods=['POST'])
# def create_post():
#     new_post = post_model.Post.save_post(request.form)
#     return redirect(f'/post/{new_post}')

# @app.route('/post/<int:id>')
# def view_one_post(id):
#     id_data={
#         'id': id
#     }
#     return render_template('one_post.html', one_post = post_model.Post.get_one_post(id_data))




