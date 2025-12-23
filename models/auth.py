from . adminModel import Admin
from . postModel import Post
from . contactModel import Contact
from flask import session
from middlewares.dbconfig import db

# check if email exists
def get_user_by_email(email):
    return Admin.query.filter_by(email=email).first()


# register user
def createUser(email, password):
    try:
        user = Admin(email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        
        return user

    except Exception as e:
        db.session.rollback()
        return None


# login user
def loginUser(email, password):
    user = Admin.query.filter_by(email=email).first()

    if user and user.check_password(password):
        session['id'] = user.id
        session['email'] = user.email
        return True

    return False


# create post
def createPost(title, category, description, photo, postDate, popular):
    try:
        post = Post(
            title=title,
            category=category,
            description=description,
            photo=photo,
            postDate=postDate,
            popular=popular
        )

        db.session.add(post)
        db.session.commit()
        return post
    
    except Exception as e:
        db.session.rollback()
        return None


# get all post
def getAllPost():
    return Post.query.order_by(Post.id.desc()).all()


# get all post by category
def getAllPostByCategory(category):
    return Post.query.filter_by(category=category).order_by(Post.id.desc()).all()


# get popular post
def getPopularPost():
    return (
        Post.query
        .filter_by(popular=True)
        .order_by(Post.id.desc())
        .limit(7)
        .all()
    )


# get single post
def getSinglePost(id):
    return Post.query.get(id)


# create contact
def createContact(name, email, subject, message, contactDate):
    try:
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            contactDate=contactDate
        )

        db.session.add(contact)
        db.session.commit()
        return contact
    
    except Exception as e:
        db.session.rollback()
        return None


# editPost contact
def editPost(title, category, description, photo, id, popular):
    try:
        post = Post.query.get(id)

        if not post:
            return None

        post.title = title
        post.category = category
        post.description = description
        post.photo = photo
        post.popular = popular

        db.session.commit()
        return post

    except Exception:
        db.session.rollback()
        return None
    

# get all contact
def getAllContact():
    return Contact.query.order_by(Contact.id.desc()).all()


# delete post
def deletePost(id):
    try:
        post = Post.query.get(id)

        if not post:
            return False

        db.session.delete(post)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        return False


# delete contact
def deleteContact(id):
    try:
        contact = Contact.query.get(id)

        if not contact:
            return False

        db.session.delete(contact)
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        return False