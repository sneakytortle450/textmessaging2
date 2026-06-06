# User experience/application behaviour


- Begin by declaring a username
  - No permenant profile
- Can join public chatrooms
  - Users can see the usernames of others in chatrooms they are in
- Can create private or public chatrooms
  - Private chatrooms
- mvp has only one chatroom
- next version can see others usernames
- next version has message scrolling when they go off the screen
- Draft panal you can type in
- You can submit the draft to the chatroom and it sends a message
- Message has this format:
  - Username
  - Time message was sent
  - The message
 
# Lightweight design

- Architecture is multi-page server rendered flask application
- Flask will build html and send it to the client
  - One page for starters, more later
- Flask will also provide an apt route that is called GET /messages
- /messages will return the list of all messages in the channel
- The client will send a fetch request every second to /messages and render those messages using javascript
- Flask will provide an api route that is called POST /messages
- When the user submitts a message, javascript will send the message to POST /messages
