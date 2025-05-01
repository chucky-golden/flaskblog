from flask import render_template, request, flash, redirect, session
from datetime import datetime
from middlewares.checklogin import login_required
from middlewares.uploads import  upload_file
from models.auth import get_user_by_email, createUser, getSinglePost, loginUser, createPost, getAllPost, getAllContact, deleteData, editPost
import os
from flask import current_app


# login admin account
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']

            # check user exists
            if loginUser(email, password):
                return redirect('/auth/dashboard')
            else:
                flash("Invalid credentials!")
                return redirect('/auth/login')
        except:
            flash("error processing request!")
            return redirect('/auth/login')
    return render_template('/auth/login.html')

# create admin account
def register():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']

            # check user exists
            if get_user_by_email(email):
                flash("email already eists!")
                return redirect('/auth/register')
            
            createUser(email, password)
            flash("Registration successful!")
            return redirect('/auth/login')
        except:
            flash("error processing request!")
            return redirect('/auth/login')        

    return render_template('/auth/register.html')
        

# admin dashboard
@login_required
def dashboard():
    if request.method == 'POST':
        try:
            title = request.form['title']
            category = request.form['category']
            description = request.form['description']

            popular = 0 if 'popular' in request.form else 1

            file = request.files['file']

            photo = upload_file(file)
            if not photo:
                flash("Invalid or missing image file")
                return redirect('/auth/dashboard')

            # Format date like "April 22 2025"
            postDate = datetime.now().strftime("%B %d %Y")
            
            createPost(title, category, description, photo, postDate, popular)
            flash("post uploaded!")
            return redirect('/auth/dashboard')
        except:
            flash("error processing request!")
            return redirect('/auth/login')
         
    return render_template('/auth/dashboard.html')

# admin viewpost
@login_required
def viewpost():
    posts = getAllPost()
    return render_template('/auth/viewpost.html', posts=posts)

# admin viewcontact
@login_required
def viewcontact():
    contacts = getAllContact()
    return render_template('/auth/viewcontact.html', contacts=contacts)

# admin editpost
@login_required
def editpost(post_id):
    if request.method == 'POST':
        try:
            title = request.form['title']
            category = request.form['category']
            description = request.form['description']
            img = request.form['img']
            id = request.form['id']

            popular = 0 if 'popular' in request.form else 1

            file = request.files['file']
            photo = img

            if file:
                photo_filename = img
                photo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], photo_filename)

                # Then delete the file if it exists
                if os.path.exists(photo_path):
                    os.remove(photo_path)

                photo = upload_file(file)

            if not photo:
                flash("Invalid or missing image file")
                return redirect('/auth/editpost/'+id)
            
            editPost(title, category, description, photo, id, popular)
            flash("post updated!")
            return redirect('/auth/editpost/'+id)
        except:
            flash("error processing request!")
            return redirect('/auth/login')
        
    post = getSinglePost(post_id)
    return render_template('/auth/editpost.html', post=post)

# admin deletepost
@login_required
def deletepost(post_id):
    if not post_id:
        return redirect('/')
    post = getSinglePost(post_id)
    if post:
        delPost = deleteData(post_id, 'post')

        if delPost:
            photo_filename = post[4]
            photo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], photo_filename)

            # Then delete the file if it exists
            if os.path.exists(photo_path):
                os.remove(photo_path)
    return redirect('/auth/viewpost')


# admin deletecontact
@login_required
def deletecontact(post_id):
    deleteData(post_id, 'contact')
    return redirect('/auth/viewcontact')


# admin logout
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect('/auth/login')