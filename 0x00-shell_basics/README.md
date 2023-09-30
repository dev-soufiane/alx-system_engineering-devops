# Shell Basics - Project 0x00

Welcome to the **Shell Basics** project (Project 0x00) in the DevOps curriculum! 🚀 This repository is a comprehensive collection of shell scripts and command-line operations. 

## Table of Contents
- [Introduction](#introduction)
- [Tasks](#tasks)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Author](#author)
- [License](#license)

## Introduction

This project covers various fundamental concepts of shell scripting, designed to help you build a strong foundation in shell scripting and command-line operations. Below, you'll find details about each task and its purpose.

## Tasks

1. [Where am I?](#task-0-where-am-i)
   - Description: This script prints the absolute path name of the current working directory.

2. [What’s in there?](#task-1-whats-in-there)
   - Description: Display the contents list of your current directory.

3. [There is no place like home](#task-2-there-is-no-place-like-home)
   - Description: This script changes the working directory to the user’s home directory.

4. [The long format](#task-3-the-long-format)
   - Description: Display current directory contents in a long format.

5. [Hidden files](#task-4-hidden-files)
   - Description: Display current directory contents, including hidden files, in the long format.

6. [I love numbers](#task-5-i-love-numbers)
   - Description: Display current directory contents in long format with user and group IDs displayed numerically, including hidden files.

7. [Welcome](#task-6-welcome)
   - Description: Create a script that creates a directory named `my_first_directory` in the `/tmp/` directory.

8. [Betty in my first directory](#task-7-betty-in-my-first-directory)
   - Description: Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

9. [Bye bye Betty](#task-8-bye-bye-betty)
   - Description: Delete the file `betty` from `/tmp/my_first_directory`.

10. [Bye bye My first directory](#task-9-bye-bye-my-first-directory)
    - Description: Delete the directory `my_first_directory` from the `/tmp` directory.

11. [Back to the future](#task-10-back-to-the-future)
    - Description: Write a script that changes the working directory to the previous one.

12. [Lists](#task-11-lists)
    - Description: Write a script that lists all files (even ones with names beginning with a period character) in the current directory, the parent of the working directory, and the `/boot` directory, in long format.

13. [File type](#task-12-file-type)
    - Description: Write a script that prints the type of the file named `iamafile`, which will be in the `/tmp` directory when executed.

14. [We are symbols, and inhabit symbols](#task-13-we-are-symbols-and-inhabit-symbols)
    - Description: Create a symbolic link to `/bin/ls`, named `__ls__`, in the current working directory.

15. [Copy HTML files](#task-14-copy-html-files)
    - Description: Create a script that copies all HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent directory or are newer.

16. [Let’s move](#task-15-lets-move)
    - Description: Move all files beginning with an uppercase letter to the directory `/tmp/u`.

17. [Clean Emacs](#task-16-clean-emacs)
    - Description: Delete all files in the current working directory that end with the character `~`.

18. [Tree](#task-17-tree)
    - Description: Create directories `welcome/`, `welcome/to/`, and `welcome/to/school` in the current directory with limited lines and spaces.

19. [Life is a series of commas, not periods](#task-18-life-is-a-series-of-commas-not-periods)
    - Description: Write a command that lists all files and directories of the current directory, separated by commas, following specific sorting rules.

20. [File type: School](#task-19-file-type-school)
    - Description: Create a magic file `school.mgc` that can be used with the `file` command to detect School data files.

## Learning Objectives

By completing these tasks, you will:

- Gain a strong understanding of shell scripting fundamentals.
- Learn essential shell commands and navigation techniques.
- Develop the ability to write efficient and concise shell scripts.
- Enhance your skills in managing files and directories using the command line.

## Requirements

- Allowed editors: vi, vim, emacs.
- All your scripts will be tested on Ubuntu 20.04 LTS.
- Scripts should be exactly two lines long (`$ wc -l file` should print 2).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/bin/bash`.
- Include a `README.md` file at the root of the repo, containing a description of the repository.

## How to Use

To run any of these scripts, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the specific task's directory (e.g., `0x00-shell_basics/task-0-where-am-i`).
3. Run the script by executing `./script-name` in your terminal.

Happy scripting! 🎉

## Author

- [Soufiane](https://github.com/dev-soufiane)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
