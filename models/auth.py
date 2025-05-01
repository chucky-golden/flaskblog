from flask import session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from middlewares.dbconfig import mysql
import os

# get a user by id
def get_user_by_email(email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()
    return user

# register user
def createUser(email, password):
    password = generate_password_hash(password)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO admin (email, password) VALUES (%s, %s)", (email, password))
    mysql.connection.commit()
    cur.close()

# login user
def loginUser(email, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()
    if user and check_password_hash(user[2], password):
        session['id'] = user[0]
        session['email'] = user[1]
        return True
    else:
        return False

# create post
def createPost(title, category, description, photo, postDate, popular):
    cur = mysql.connection.cursor()
    post = cur.execute("INSERT INTO post (title, category, description, photo, postDate, popular) VALUES (%s, %s, %s, %s, %s, %s)", (title, category, description, photo, postDate, popular))
    mysql.connection.commit()
    cur.close()
    if post:
        return True
    else:
        return False

# get all post
def getAllPost():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM post ORDER BY id DESC")
    posts = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    posts = [dict(zip(columns, row)) for row in posts]
    cur.close()

    return posts

# get all post by category
def getAllPostByCategory(category):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM post WHERE category=%s", (category,))
    posts = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    posts = [dict(zip(columns, row)) for row in posts]
    cur.close()

    return posts

# get popular post
def getPopularPost():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM post WHERE popular = 0 ORDER BY id DESC LIMIT 7")
    posts = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    posts = [dict(zip(columns, row)) for row in posts]
    cur.close()

    return posts

# get single post
def getSinglePost(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM post WHERE id=%s", (id,))
    post = cur.fetchone()
    cur.close()

    return post


# create contact
def createContact(name, email, subject, message, contactDate):
    cur = mysql.connection.cursor()
    contact = cur.execute("INSERT INTO contact (name, email, subject, message, contactDate) VALUES (%s, %s, %s, %s, %s)", (name, email, subject, message, contactDate))
    mysql.connection.commit()
    cur.close()
    if contact:
        return True
    else:
        return False



# editPost contact
def editPost(title, category, description, photo, id, popular):
    cur = mysql.connection.cursor()
    contact = cur.execute("UPDATE post SET title = %s, category = %s, description = %s, photo = %s, popular = %s  WHERE id = %s", (title, category, description, photo, popular, id))
    mysql.connection.commit()
    cur.close()
    if contact:
        return True
    else:
        return False
    

# get all contact
def getAllContact():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contact ORDER BY id DESC")
    contact = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    contact = [dict(zip(columns, row)) for row in contact]
    cur.close()

    return contact


# delete data
def deleteData(id, cat):
    cur = mysql.connection.cursor()
    if cat == 'post':
        # Delete the post from DB
        cur.execute("DELETE FROM post WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()

        return True
    elif cat == 'contact':
        # Delete the contact from DB
        cur.execute("DELETE FROM contact WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
                
        return True
    else:
        return False