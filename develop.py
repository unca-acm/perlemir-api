"""
App for running a local development copy of the server (and optionally the client)
TODO: Split dev server config into a YAML/JSON/something file.

:author: Joshua Cooper
:date: April 9, 2021
"""

import os
import subprocess

class WebClientServer():

    def __init__(self, path: str = None):
        if path is None:
            self.path = os.path.join(os.path.dirname(__file__), "client")
    
    def setup(self) -> int:
        # Start by installing the client dependencies
        # Currently requires `npm login` to GitHub servers
        # $ npm install
        try:
            returncode = subprocess.check_call(args=["npm", "install"], cwd=self.path, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            returncode = err.returncode
            print("Could not install client dependencies [error code {0}]".format(returncode))
            print("Errors: {0}".format(err.stderr))
            return returncode
        
        return returncode
    
    def publish(self, output: str = None):
        """
        Build the contents of the client directory and make them available.
        :param output: Path where output is placed (TODO)
        """
        try:
            print("Building client project...")
            retcode = subprocess.check_call(args=["npm", "run", "build"], cwd=self.path, stdout=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            retcode = err.returncode
            print("Could not build client project [error code {0}]".format(retcode))
        
        return retcode
    
    def start(self, port=8000):
        """
        Runs a development copy of the client app through a proxy port
        """
        subprocess.call(args=["npm", "start"], cwd=self.path)

def start_server():
    from app import app
    client = WebClientServer()

    # Install dependencies for client app and build
    retcode = client.setup()
    if retcode != 0:
        exit(retcode)
    retcode = client.publish()
    if retcode != 0:
        exit(retcode)
    
    # Start the flask server, serve the client from directory
    app.run(debug=True, port=5000)


if __name__ == "__main__":
    start_server()
