from sticke import app 
from flask import render_template, send_from_directory, url_for, request, redirect 


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template('layout.html')