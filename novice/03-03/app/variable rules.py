from flask import Flask
app = Flask(__name__)

@app.route("/")
def index(): 
    return 'Halaman Index'

@app.route('/heh')
def heh(): 
    return "Hello cur"

# menampilkan nama pengguna
@app.route('/user/<user_name>')
def show_user_profil(user_name): 
    return f'User, {user_name}'

# menampilkan link berupa angka
@app.route('/post/<int:post_id>')
def show_post(post_id): 
    return f'Post {post_id}'

# membuat kondisional
if __name__ == "__main__":
    app.run()