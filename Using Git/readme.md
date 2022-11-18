# Using Git

For more in-depth documentation see the git docs [here](https://git-scm.com/doc).  

**git and GitHub are two different things.**

**git** is a software tool for creating repositories and tracking changes within files. It gives us flexibility to make incremental changes and revert changes in case of mistakes.

**GitHub** is a web platform that works with git to host git repositories online. It helps us use git in a collaborative setting, and provides tools & UI/UX to make using git easier (for example, pull requests).

## Useful Terms

**Repository** - A git project  
**Commit** - A save point in the history of the git repository  
**Branch** - A copy of the project code at a certain commit  
**Master/Main** - The main branch of your project  
**Tracking/Tracked files** - When you make changes to files they are initially *untracked*, and can be tracked by using `git add`  
**Stage** - A record of the current changes that are ready to be committed, not finalized until being committed with `git commit`  
**HEAD** - A reference to the latest commit on the current branch  
**Remote** - Usually called `origin`, the remote is the server hosting your git repository  
**Conflict** - When a file has changes in the same area on two branches that are being combined (with `git merge` or `git rebase`)  

## Git Commands

+ `git add path/to/your.file` - Add one or more files or directories to the staging area
+ `git rm path/to/your.file` - Set one or more files or directories as removed from the project in the staging area
+ `git commit -m "commit message"]` - Create a commit on the current branch from the changes in the stage
+ `git status` - Get the status of your project - shows which files are changed, added, or removed, not yet tracked by git, etc.
+ `git push` - Upload any new changes on the current branch to your remote (in this case, GitHub)
+ `git pull` - Download any new changes from the remote to your local git repository
+ `git branch` - Show list of all branches. This command can also be used to create new branches, remove branches, etc
+ `git checkout branch-name` - Switch to a different branch


## Handy Commands

`git commit -am "Your commit message here"` - Add all changed files and commit at the same time (only works with *changed* files, not newly created or removed files)

`git reset --hard` - Remove all changes and reset to the most recent commit. **Use with caution: This will delete any changes you've made without any way to get them back**

`git rebase master` - If the main branch has changed since you started working on your branch, you can use this to combine those changes with the current branch. If there are conflicts you will have to fix them before continuing with this.

`git checkout -b branch-name-here` - Creates a new branch from the current commit and switches to it

`git stash` - "Stashes" current untracked changes that aren't ready to be committed yet. Very useful when you need to switch to another branch but you are not ready to commit your changes. Get the changes back by doing `git stash pop [stash-id]`. The stash-id is optional, and can be found using `git stash list`. If stash-id is left out, the most recent stash will be used.
