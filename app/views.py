"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify
from bs4 import BeautifulSoup
import requests
import urlparse



images = []
###
# Routing for your application.
###

@app.route('/api/thumbnails')
def api():
    
    url = "https://www.walmart.com/ip/54649026"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

   
    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        images.append(str(og_image['content']))
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        images.append(str(thumbnail_spec['href']))
        image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
        images.append(str(img["src"]))
    
    error = 'null'
    message = 'success'
    #thumbnails = images
    thumbnails = []
    out = {'error' : error , 'message' : message , 'thumbnails' : images }
    
    return jsonify(out)

@app.route('/')
def home():
    """Render website's home page."""
    
    return render_template('home.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
