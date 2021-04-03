# PerlemirUI
## Web app UI for the Perlemir Algo Bot API

Web app for the user-level dashboard and application.

Wraps around the bot's API and configuration to provide a simple, out-of-the-box experience using the bot.

### Layout

The code base is split into three parts: the web client, math library, and server.

This project uses TypeScript + React to power the front end, and Express.js for the back end*. Additionally, for the front end, it is "bundled" using Snowpack to ensure high performance and a better user experience with a lightweight bundler.

Additionally, the front end depends heavily on mathematical computations on large data sets representing financial data. This is handled using a math library written in C and compiled to WebAssembly using LLVM.

#### Client

Source code for the client can be found under `view`.

The source code is written using React+TypeScript and must be compiled. This is performed automatically using Snowpack.

The output of Snowpack can be found under `public`. The generated files are actually completely static, and can be accessed (minus server API functionality) via the entry point at `public/index.html`.

#### Transformer

Source code for the math libraries can be found under `lib`.

These are intended to be bundled/exported as an NPM package, which makes it easier for development and distribution. In production or during development, you will be able to install the NPM package without actually having to compile the source code yourself.

Optionally, if developing for the transform library itself, you may use the local copy of the transform library.

#### Server

Source code for the server can be found under `src`.

The source code is written in TypeScript and must be compiled. The emitted JS code will be placed in the `dist` folder, and the entry-point can be found at `dist/app.js`.

The server provides the Client by simply mapping the root of the webpage, `/`, to the static files generated from Snowpack. The rest of the site's functionality (mostly the management API provided by the server) is mapped to `/api`.


### Development

This is currently just a skeleton of a project; a more advanced build toolchain will be involved, and this Readme and documentation will be updated to reflect this.

#### Installation

Make sure the following tools are installed:

1. Node.js v14.0+ (if using NVM, run `nvm use` in repository root)

2. NPM v6.14+

#### Running

0. `npm install` to load dependencies

1. `npm start` to start the local dev server

2. `npm start:ui` to start the front end, without running the server

3. `npm build` to create a production build for both client and server

4. Open to `http://localhost:8000`

#### Transform Library

In order to develop for the transform library locally, you'll need to use the package located in `lib/transform` instead of the published NPM package. To do this, use the [npm link](https://docs.npmjs.com/cli/v6/commands/npm-link) command.

##### Linking to Local Package

1. Change to `lib/transform` directory.
2. Run `npm link` to create a global reference to the local package.
3. Return to the root directory of the repository.
4. Run `npm link @unca-acm/lib-transform`.

##### Running Local Package

To rebuild, use `npm run build`.
