# Git

## Learning objectives

* Use the basic commands of git
* Manipulating repositories
* Understanding the *branching* concept

## Git vs Github

*Git* is a versioning software. Concretely, it's an essential tool to collaborate
and store all the details about code modifications on your repository.

*Github* is an online service that allows among other things to host Git repositories.

## Install Git

### Linux (Debian)

```SHELL
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```

### Other distributions, Windows, Mac...

[Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Configuration

For a smoother use of git you should set it up properly. To do so you must,
define your identity (name, email) and your text editor.

* git config --global user.name "John Doe"
* git config --global user.email "johndoe@example.com"
* git config --global core.editor "vim"

## Access (Token or SSH)

### Token

[Personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### SSH

You might want to use an *ssh key* to avoid entering your password for each
interaction with `git`. If so, follow this [GUIDE](https://help.github.com/en/articles/connecting-to-github-with-ssh).

## Let's practice !

### Intro

- [Intro](https://try.github.io)

### Branching

- [Branching](http://learngitbranching.js.org)

### More

- [Need more ?](https://lab.github.com/)

## Resources

- [Git Book](http://git-scm.com/book/en/v2)


![Merge](https://media.giphy.com/media/cFkiFMDg3iFoI/giphy.gif)