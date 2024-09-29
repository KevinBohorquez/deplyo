from fasthtml.common import *

css = Style('''
            :root {
                --pico-font-size: 100%;
                --pico-font-family: "Comic Sans MS", cursive;
                background-color: #f0f0f0;
            }
            
            .container {
                color: red;
                font-size: 300%;
                font-family: "Comic Sans MS"
                
            }
            ''')

app, rt = fast_app(live=True, hdrs=(picolink, css))
messages = ["This is a message, which will get rendered as a paragraph"]

@app.get("/")
def homel():
    return Main(H1('Messages'), 
                *[P(msg) for msg in messages],
                A("Link to Page 2 (to add messages)", href="/page2"))



@app.get("/page2")
def page2():
    return Main(P("Add a message with the form below:"),
                Form(Input(type="text", name="data"),
                    Button("Submit"),
                    action="/", method="post"))

@app.post("/")
def add_message(data:str):
    messages.append(data)
    return homel()  
serve()