const EventEmitter = require("events");
const readline = require("readline");

const client = new EventEmitter();

// class Logger extends EventEmitter() {}
// const myEmitter = new EventEmitter();

// const logger = new Logger();
// // Create an interface with standard I/O
const cursorPrompt = "taskterm> "; // our custom prompt

// myEmitter.emit("event-name");
// logger.emit("event-name", arg1, arg2); // passing arguments down to the listener

// myEmitter.on("event-name", function () {});

// // listener function can take any number of argument
// logger.once("event-name", function (arg1, arg2) {});

// myEmitter.on("checkout", (executeFirst = () => {}));
// myEmitter.on("checkout", (executeSecond = () => {}));
// myEmitter.on("checkout", (executeThird = () => {}));

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: cursorPrompt,
});

r1.on("line", (input) => {
  // we split string to separate the command and the optional arguments
  [cmd, ...args] = input.trim().split(" ");
  client.emit("command", cmd, args);
});

const server = require("./server")(client);

server.on("response", (response) => {
  process.stdout.write("\u001B[2J\u001B[0;0f"); // clear the prompt
  process.stdout.write(response);
  process.stdout.write(`\n${cursorPrompt}`);
});
