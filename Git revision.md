**Source Control** in **Visual Studio Code** is the section that integrates **Git** into VS Code so you can track changes, save versions, and collaborate on code.

### What is Source Control?

Think of it as a **time machine for your code**.

It lets you:

* See what files changed
* Save snapshots (**commits**)
* Undo mistakes
* Create branches for new features
* Merge code
* Push code to repositories like [GitHub](https://github.com?utm_source=chatgpt.com)

> Official doc link(https://code.visualstudio.com/docs/sourcecontrol/overview)  
> Official video(https://youtu.be/i_23KUAEtUM)
---

## Source Control Icon

On the left sidebar:

```
Explorer
Search
Source Control  ← (branch-like icon)
Run & Debug
Extensions
```

Shortcut:

```
Ctrl + Shift + G
```

---

## Basic Workflow

### 1. Initialize Git Repository

Open terminal:

```bash
git init
```

Or click **Initialize Repository** in Source Control.

---

### 2. Make Changes

Suppose you edit:

```cpp
main.cpp
```

Source Control will show:

```
Changes (1)
  M main.cpp
```

Meaning:

* M = Modified

---

### 3. Review Changes

Click the file.

VS Code shows:

```diff
- old line
+ new line
```

Red = removed

Green = added

---

### 4. Stage Changes

Click:

```
+
```

beside the file.

This moves it to:

```
Staged Changes
```

Equivalent Git command:

```bash
git add main.cpp
```

---

### 5. Commit

Write a message:

```
Fix reverse integer bug
```

Click ✓

Equivalent:

```bash
git commit -m "Fix reverse integer bug"
```

---

### 6. Push to GitHub

```bash
git push
```

Or click **Sync Changes** in VS Code.

---

## File Status Symbols

| Symbol | Meaning   |
| ------ | --------- |
| M      | Modified  |
| U      | Untracked |
| A      | Added     |
| D      | Deleted   |
| R      | Renamed   |

Example:

```
U notes.md
M main.cpp
D old.cpp
```

---

## Branches

Current branch appears at bottom-left:

```
main
```

Create branch:

```bash
git checkout -b feature-login
```

or click branch name in VS Code.

Useful for:

* New features
* Experiments
* Bug fixes

without affecting main code.

---

## Essential Git Commands

A consolidated list of the most important Git commands and short notes.

```bash
git init
git status
git add <file>        # e.g., git add main.cpp
git add .             # stage all changes
git commit -m "message"
git log
git diff
git restore <file>
git branch
git checkout <branch>      # legacy
git switch <branch>        # modern
git merge <branch>
git remote add origin <repo-url>
git remote -v
git push
git pull
```

- `git diff`: view unstaged/staged changes before committing.
- `git restore <file>`: revert working file to the last commit.
- Prefer `git switch` for branch switching; `git checkout` is still widely used.

---

## For Placement/Interview Preparation

Learn in this order:

1. Git basics
2. Source Control panel in VS Code
3. GitHub repositories
4. Branching
5. Merge conflicts
6. Pull Requests

A good developer should be comfortable with Git before graduation.

### Minimum commands every fresher should know

```bash
git init
git status
git add .
git commit -m ""
git push
git pull
git branch
git checkout
git merge
```

Good approach: learn Git from the terminal first, then use VS Code Source Control as a GUI on top of it.

# What is Git?

Git is a **Version Control System (VCS)**.

Without Git:

```text
project/
├── final.cpp
├── final_final.cpp
├── final_final_latest.cpp
├── final_final_latest_v2.cpp
```

With Git:

```text
project/
└── main.cpp
```

Git remembers every version internally.

---

# The 3 Areas of Git

This is the most important concept.

```text
Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Repository
```

## 1. Working Directory

Your actual files.

```cpp
cout << "Hello";
```

You modify:

```cpp
cout << "Hello World";
```

Git notices:

```bash
git status
```

Output:

```text
modified: main.cpp
```

---

## 2. Staging Area

A waiting room for changes.

```bash
git add main.cpp
```

Now Git says:

```text
Changes to be committed:
main.cpp
```

---

## 3. Repository

Permanent snapshot.

```bash
git commit -m "Added greeting"
```

Now the version is saved.

---

# Command 1: git init

Creates a Git repository.

```bash
git init
```

Before:

```text
project/
    main.cpp
```

After:

```text
project/
    main.cpp
    .git/
```

`.git` stores all Git history.

---

# Command 2: git status

Most used command.

```bash
git status
```

Shows:

* modified files
* staged files
* untracked files

Example:

```text
Untracked files:
notes.txt
```

means Git isn't tracking it yet.

---

# Command 3: git add

Move changes to staging.

```bash
git add main.cpp
```

Or everything:

```bash
git add .
```

Think:

```text
Working Directory
      ↓
git add
      ↓
Staging Area
```

---

# Command 4: git commit

Create a snapshot.

```bash
git commit -m "Fixed reverse function"
```

Git stores:

```text
Commit #1
```

Later:

```bash
git commit -m "Added login"
```

Git stores:

```text
Commit #2
```

---

# Command 5: git log

Show history.

```bash
git log
```

Example:

```text
commit abc123
Added login

commit xyz456
Fixed reverse function
```

---

# Command 6: git diff

See exact changes.

```bash
git diff
```

Example:

```diff
- int x = 5;
+ int x = 10;
```

Before committing, always check this.

---

# Command 7: git restore

Undo changes.

Suppose:

```cpp
cout << "BAD CODE";
```

You want the last committed version.

```bash
git restore main.cpp
```

File returns to previous state.

---

# Command 8: git branch

Show branches.

```bash
git branch
```

Output:

```text
* main
```

Current branch = main.

---

# Command 9: Create Branch

```bash
git branch feature-login
```

Switch:

```bash
git checkout feature-login
```

Or modern command:

```bash
git switch feature-login
```

---

# Command 10: Merge Branch

Move back:

```bash
git switch main
```

Merge:

```bash
git merge feature-login
```

Changes come into main.

---

# Command 11: Connect GitHub

First repository creation happens on GitHub.

Then:

```bash
git remote add origin https://github.com/user/repo.git
```

Check:

```bash
git remote -v
```

---

# Command 12: Push

Upload commits.

```bash
git push origin main
```

Local → GitHub

---

# Command 13: Pull

Download latest commits.

```bash
git pull origin main
```

GitHub → Local

---

# Full Real Workflow

Create project:

```bash
mkdir calculator
cd calculator

git init
```

Create file:

```cpp
main.cpp
```

Check:

```bash
git status
```

Add:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit"
```

Connect GitHub:

```bash
git remote add origin <repo-url>
```

Push:

```bash
git push -u origin main
```

---

# Now Compare with VS Code Source Control

| Git Command        | VS Code Source Control |
| ------------------ | ---------------------- |
| `git status`       | Changes panel          |
| `git add file`     | Click `+`              |
| `git add .`        | Stage All Changes      |
| `git commit -m ""` | Type message + ✓       |
| `git diff`         | Click file to see diff |
| `git push`         | Sync Changes / Push    |
| `git pull`         | Pull                   |
| `git branch`       | Branch selector        |
| `git merge`        | Merge branch menu      |

So VS Code is basically a visual wrapper around Git commands.

# Summary

If you understand **Working Directory → Staging Area → Repository**, you've already understood about 70% of Git fundamentals. The rest is mostly branching and collaboration.
