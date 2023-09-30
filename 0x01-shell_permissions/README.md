# Shell Permissions - Project 0x01

Welcome to the **Shell Permissions** project (Project 0x01) in the DevOps curriculum! 🚀 This repository is a collection of shell scripts focusing on file permissions and ownership.

## Table of Contents
- [Introduction](#introduction)
- [Tasks](#tasks)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Author](#author)
- [License](#license)

## Introduction

This project explores fundamental concepts related to shell permissions, file ownership, and access control in a Linux environment. Each task is designed to enhance your understanding of managing permissions and ownership through shell scripting.

## Tasks

1. [My name is Betty](#0-my-name-is-betty)
   - Description: Create a script that switches the current user to the user betty.

2. [Who am I](#1-who-am-i)
   - Description: Write a script that prints the effective username of the current user.

3. [Groups](#2-groups)
   - Description: Write a script that prints all the groups the current user is part of.

4. [New owner](#3-new-owner)
   - Description: Write a script that changes the owner of the file hello to the user betty.

5. [Empty](#4-empty)
   - Description: Write a script that creates an empty file called hello.

6. [Execute](#5-execute)
   - Description: Write a script that adds execute permission to the owner of the file hello.

7. [Multiple permissions](#6-multiple-permissions)
   - Description: Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

8. [Everybody](#7-everybody)
   - Description: Write a script that adds execution permission to the owner, the group owner, and the other users for the file hello.

9. [James Bond](#8-james-bond)
   - Description: Write a script that sets specific permissions to the file hello.

10. [John Doe](#9-john-doe)
    - Description: Write a script that sets specific permissions to the file hello.

11. [Look in the mirror](#10-look-in-the-mirror)
    - Description: Write a script that sets the mode of the file hello the same as olleh’s mode.

12. [Directories](#11-directories)
    - Description: Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users.

13. [More directories](#12-more-directories)
    - Description: Create a script that creates a directory called my_dir with specific permissions in the working directory.

14. [Change group](#13-change-group)
    - Description: Write a script that changes the group owner of the file hello.

15. [Owner and group](#14-owner-and-group)
    - Description: Write a script that changes the owner and group owner for all files and directories in the working directory.

16. [Symbolic links](#15-symbolic-links)
    - Description: Write a script that changes the owner and group owner of a symbolic link.

17. [If only](#16-if-only)
    - Description: Write a script that changes the owner of the file hello only if it is owned by a specific user.

18. [Star Wars](#17-star-wars)
    - Description: Write a script that plays the StarWars IV episode in the terminal.

## Learning Objectives

By completing these tasks, you will:

- Gain a deeper understanding of Linux file permissions.
- Learn how to manipulate file ownership and permissions using shell scripts.
- Develop practical skills in managing access control for files and directories.

## Requirements

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- Scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- Include a `README.md` file at the root of the repo, describing what each script is doing.

## How to Use

To run any of these scripts, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the specific task's directory (e.g., `0x01-shell_permissions/0-iam_betty`).
3. Run the script by executing `./script-name` in your terminal.

Happy scripting! 🎉

## Author

- [Soufiane](https://github.com/dev-soufiane)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
