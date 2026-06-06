from flask import Flask

app = Flask(__name__)


messages = [{
        "username":"User",
        "message":"Hello world!!",
    

        
    },{
        "username":"User2",
        "message":"Hello mars!!",
    }]

@app.route("/messages")
def messages():
    print("hello")
    return messages

@app.route("/")
def index():
    return ''' <div>
    Username:
    <form>
   <input>
   <button>
   Submit
   </button>
   </form>

    </div>
    
    <div>
        <div id="messages">

        </div>
            <form id="send-message">
            
                <input>
                <button>
                    Submit
                </button>
            </form>
    </div>
    
    <script>
    const form = document.querySelector("form");
    const sendMessageForm = document.querySelector("#send-message");
    const username = document.querySelector("input")
    form.addEventListener("submit", event => {
       console.log(username.value)
       event.preventDefault()
    })
    sendMessageForm.addEventListener("submit", event => {
       console.log(username.value)
       event.preventDefault()
       fetch("messages").then(response => {
            return response.json()
       }).then(data =>{
        console.log(data)
       })
    })
    setInterval(() => {
    fetch("messages").then(response => {
            return response.json()
       }).then(data =>{
        console.log(data)
       })
    },1000)
    </script>'''


app.run(host='0.0.0.0', port=81,debug=True)