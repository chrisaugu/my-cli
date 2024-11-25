#!/usr/bin/env node

import { program } from "commander";
import chalk from "chalk";
import inquirer from "inquirer";
import ora from "ora";
import figlet from "figlet";

program.version("1.0.0").description("ZykNet CLI");

console.log(
  chalk.yellow(figlet.textSync("ZykNet CLI", { horizontalLayout: "full" }))
);

// program
//   .option("-n, --name <type>", "Add your name")
//   .action((options) => {
//     console.log(`Hey, ${options.name}!`);
//     console.log(chalk.blue(`Hey, ${options.name}!`));
//     console.log(chalk.green(`Hey, ${options.name}!`));
//     console.log(chalk.red(`Hey, ${options.name}!`));
//   });

program.action(() => {
  inquirer
    .prompt([
      {
        type: "input",
        name: "name",
        message: "What's your name?",
      },
    ])
    .then((answers) => {
      console.log(chalk.green(`Hey there, ${answers.name}!`));
    });

  inquirer
    .prompt([
      {
        type: "list",
        name: "choice",
        message: "Choose an option:",
        choices: ["Option 1", "Option 2", "Option 3"],
      },
    ])
    .then((result) => {
      const spinner = ora(`Doing ${result.choice}...`).start(); // Start the spinner

      setTimeout(() => {
        spinner.succeed(chalk.green("Done!"));
      }, 3000);
    });
});

program.parse(process.argv);