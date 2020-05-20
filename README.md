# DiceDetector

## Overview

This project is to estimate the pips of each dice in the image and return the result as a json and image.
The web server for this project is implemented by the Flask framework.

## Structure

- src

    The source code to download the image from the request url and estimate the pips of each dice

- utils

    The source code for management of files and folders of this project
    
- app

    The main execution file

- requirements

    All the dependencies for this project
    
- settings

    Several settings for this project
    
## Installation

- Environment

    Ubuntu 18.04, Windows 10, Python 3.6+

- Dependency Installation

    Please go ahead to this project directory and run the following command in the terminal.
    ```
    pip3 install -r requirements.txt
    ```

## Execution

- Please run the following command in the terminal.

    ```
    python3 app.py
    ```

- Then the web server will run on 127.0.0.1 with port 5000.

    * So if you want to get the result of the pips of each dice as a json, you can send the request like this 
    127.0.0.1:5000/detect?img={imgurl}.
    
    * Otherwise, if you want to get the saved image result you have already sent, you can send the request like this 
    127.0.0.1:5000/saved?name={filename}
