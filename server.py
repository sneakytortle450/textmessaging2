from flask import Flask, request

app = Flask(__name__)


chat_messages = [{
        "username":"User",
        "message":"Hello world!!",
    

        
    },{
        "username":"User2",
        "message":"Hello mars!!",
    }]

@app.route("/messages", methods = ["post","get"])
def messages():
    if(request.method == "POST"):
        chat_messages.append(request.json)

    return chat_messages


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
    const messages = document.querySelector("#messages")
    form.addEventListener("submit", event => {
       console.log(username.value)
       event.preventDefault()
    })
    sendMessageForm.addEventListener("submit", event => {
       console.log(username.value)
       event.preventDefault()
       fetch("messages", {
         method: "post",
            headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },

  //make sure to serialize your JSON body
  body: JSON.stringify({
    username: username.value,
    message: event.target.querySelector("input").value
  })
})
.then( (response) => { 
   //do something awesome that makes the world a better place
});
    })
    setInterval(() => {
    fetch("messages").then(response => {
            return response.json()
       }).then(data =>{
        let html = ""
        for(const element of data){
        html += (`<li>${element.username} : ${element.message}</li>`)
        }
        messages.setHTML(html)
       })
    },1000)
    </script>'''


app.run(host='0.0.0.0', port=81,debug=True)