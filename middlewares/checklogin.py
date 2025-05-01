from functools import wraps
from flask import flash, redirect, session

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'id' not in session:
            flash('Please log in first.')
            return redirect('/auth/login')
        return f(*args, **kwargs)
    return wrap
