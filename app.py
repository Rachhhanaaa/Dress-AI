from flask import Flask, render_template, request
import os
from avatar import handle_avatar  # importing the avatar handler function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_method = request.form.get('input_method')

        if input_method == 'avatar':
            return handle_avatar(request.form)  # call the avatar handler

        elif input_method == 'photo':
            photo = request.files.get('user_photo')
            dress_type = request.form.get('dress_type')
            if photo:
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))
                return f"You uploaded photo for {dress_type} outfit!"

        return "Invalid input method selected."

    return render_template('index.html')  # render form on GET

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)