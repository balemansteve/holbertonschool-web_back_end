ES6 classes

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
    How to define a Class
    How to add methods to a class
    Why and how to add a static method to a class
    How to extend a class from another
    Metaprogramming and symbols

Requirements
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using node 20.x.x and npm 9.x.x
    Allowed editors: vi, vim, emacs, Visual Studio Code
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the js extension
    Your code will be tested using Jest and the command npm run test
    Your code will be verified against lint using ESLint
    Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test

Setup
Install NodeJS 20.x.x
(in your home directory):

    curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
    sudo bash nodesource_setup.sh
    sudo apt install nodejs -y

    $ nodejs -v
    v20.15.1
    $ npm -v
    10.7.0

Install Jest, Babel, and ESLint
in your project directory:
    Install Jest using: npm install --save-dev jest
    Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
    Install ESLint using: npm install --save-dev eslint

Configuration files

    package.json
    Click to show/hide file contents

    babel.config.js
    Click to show/hide file contents

    .eslintrc.js
    Click to show/hide file contents

and…
    Don’t forget to run $ npm install when you have the package.json
