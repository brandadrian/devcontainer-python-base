from flask import Flask, jsonify, request
app = Flask(__name__)

commandsDict = {
    1: "Command one",
    2: "Command two",
    3: "Command three",
    4: "Command four",
    5: "Command five"
}

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#-------------------------------
# Call route with /send-message?message=Hello
#-------------------------------
@app.route("/send-message")
def sendMessage():
    messageParameter = request.args.get("message", "")
    message = f"Message: {messageParameter}"
    print(message)
    return message

#-------------------------------
# Call route with /commands/1
#-------------------------------
@app.route("/commands/<int:commandId>")
def sayHello(commandId):
    command = commandsDict.get(commandId)
    if command:
        result = {"id": commandId, "name": command}
    else:
        result = {"error": "Command not found!"}
    print(result)
    return jsonify(result)

#-------------------------------
# Call route with /commands
#-------------------------------
@app.route("/commands")
def print_all_commands():
    all_commands = [
        {"id": cmd_id, "name": cmd_text}
        for cmd_id, cmd_text in commandsDict.items()
    ]
    print(all_commands)
    return jsonify(all_commands)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)