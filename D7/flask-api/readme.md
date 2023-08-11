# Flask pallets notes

### HTML injection prevention

HTML Escaping


When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from injection attacks. HTML templates rendered with Jinja, introduced later, will do this automatically.


```from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```


### Variable rules

Can specify type of argument in converter
```
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'  # notice the escaping here to prevent injection attacks

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'
```

```
string - accepts string w/o slash
path - accepts strings with slash

int - +ve integers

```

### Url redirection

Canonical url rules


#### differences b/w trailiing slashes
/about - can redirect

/about/ - 404 page


in the event /about/ is defined byt you hit '/about' then it redirects you to
/about/ ... this is because  _werkzeug_ is written to deal with this..

```
https://github.com/pallets/werkzeug/blob/3006051659821ceb0a0ba453a81efae3e9b64f90/werkzeug/routing.py#L223-L238
```

### Rendering Templates

Returning rendered templates which will contain HTML and optionally Jinja templates to inject python into the page's html for dynamic rendering.. 

```
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```


#### Request Object