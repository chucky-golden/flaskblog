from flask import render_template, request, flash, redirect, session
from datetime import datetime
from models.auth import getAllPost, getPopularPost, getSinglePost, getAllPostByCategory, createContact

def index():
    posts = getAllPost()
    popular = getPopularPost()
    return render_template('/basic/index.html', posts=posts, popular=popular)


def about():
    return render_template('/basic/about.html')


def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            message = request.form['message']

            # Format date like "April 22 2025"
            contactDate = datetime.now().strftime("%B %d %Y")
            
            createContact(name, email, subject, message, contactDate)
            flash("contact saved, we will get back to you!")
            return redirect('/contact')

            # if its an API
            # data = request.get_json()

            # name = data.get('name')
            # email = data.get('email')
            # subject = data.get('subject')
            # message = data.get('message')

            # if not all([name, email, subject, message]):
            #     return jsonify({
            #         "success": False,
            #         "message": "All fields are required"
            #     }), 400

            # return jsonify({
            #     "success": True,
            #     "message": "Contact saved, we will get back to you!"
            # }), 201

        except:
            flash("error processing request!")
            return redirect('/contact')
            # return jsonify({
            #     "success": False,
            #     "message": "Error processing request",
            #     "error": str(e)
            # }), 500
    return render_template('/basic/contact.html')


def category():
    popular = getPopularPost()
    category_type = request.args.get('type')  # Gets the `?type=Business` part
    posts = getAllPostByCategory(category_type)
    return render_template('/basic/category.html', category_type=category_type, posts=posts, popular=popular)


def single(post_id):
    if not post_id:
        return redirect('/')
    post = getSinglePost(post_id)
    popular = getPopularPost()
    return render_template('/basic/single.html', post_id=post_id, popular=popular, post=post)