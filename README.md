# perlemir-api
## Perlemir Algo Bot API

The API connecting all aspects of the Perlemir Algo-Bot application.

### TODO

(See GitHub Projects tab for details)

- [ ] Web Aspects
    - [ ] User Creation
    - [ ] User Login
    - [ ] User Logout
    - [ ] User Modification
    - [ ] User Deletion
- [ ] Bot Interface
    - [ ] Bot Creation
    - [ ] Bot Modification
    - [ ] Bot Start
    - [ ] Bot Pause
    - [ ] Bot Deletion
    - [ ] Bot Query
    - [ ] Bot Summary
- [ ] Fabrication Interface
    - [ ] ~

### Aspects

This API will accomodate multiple parts of the Perlemir Algo-Bot project. The current API will facilitate communications between the bot and a 3D printer, the bot and a web-server, and the bot to the coinbase API. This repo is one aspect of the Perlemir project and will be combined in later stages to build the entirety of the program.


### Development

Development has begun in its initial stages. A basic layout has been setup in the files.

#### Dependencies

Make sure the following are installed:

1. Python3
2. flask-jwt-api
3. bcrypt

### Running the App
The app.py file in the top level directory is the main file. Run app.py to open the Flask server on port 5000. After naviating to the directory the app.py file is in, run the following command:
```bash
python3 app.py
```
