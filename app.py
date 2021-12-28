from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def file_uploader():
    if request.method == 'GET':
      return render_template('upload.html')
    else:
      f = request.files['file']
      f.save("./uploads/" + secure_filename(f.filename))
      return render_template('complete.html')

@app.route('/<file>', methods=['GET', 'POST'])
def file_downloader(file):
    path = f"./uploads/"
    try:
        return send_file(path + file,
#               attachment_filename = file,
                download_name = file,
                as_attachment = False)
    except FileNotFoundError:
        return render_template('error.html', error="404 Not Found<br><br>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."), 404
    except:
        return render_template('error.html', error="500 Internal Server Error<br><br>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."), 500
 
@app.errorhandler(404) 
def page_not_found(error): 
    return render_template('error.html', error="404 Not Found<br><br>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."), 404

@app.errorhandler(500) 
def internal_server_error(error): 
    return render_template('error.html', error="500 Internal Server Error<br><br>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."), 500

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True)