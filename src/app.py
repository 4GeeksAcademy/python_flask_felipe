from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

#@app.route('/myroute', methods=['GET'])
#def hello_world():
#    return 'Hello World!'

#app.route('/todos', methods=['GET'])
#def hello_world():
#    return "<h1>Hello!</h1>" 

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json   
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    del todos[position]
# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
