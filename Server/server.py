#  export FLASK_APP=server.py

from flask import Flask, json
from flask_cors import CORS
from githubAccess import GithubAccess 
import json

app = Flask(__name__)
CORS(app)



@app.route('/repo/<groupName>')
def getGroupRepos(groupName):
    print(groupName)
    gh = GithubAccess()
    data = gh.getGroup(groupName)
    return app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')


if __name__ == "__main__":
    app.run()

