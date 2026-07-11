---
type: note
title: Git
description: "fundamentals, workflow, rebase, stash, bisect, cherry-pick"
tags: [git]
topic: tools
status: notes
updated: 2026-06-13
related:
  - engineering/practices/trunk-based-development.md
  - engineering/practices/polyrepo-branching-strategy.md
  - engineering/practices/code-review-policy.md
  - engineering/practices/gitops.md
source: "https://gist.github.com/fabianmagrini/155e09d4ff0e49aaa8b66017aa7b96e5"
---

# Git

Git is a **distributed version control system (DVCS)**. Every developer has a full copy of the repository including its history, making it fast and flexible for branching and merging.

## Core concepts

| Concept | Description |
|---|---|
| Repository | Collection of files and their entire history |
| Commit | Snapshot of files at a point in time |
| Branch | Pointer to a series of commits, used to isolate work |
| Merge | Combining changes from different branches |
| Remote | A shared repository (e.g., GitHub, GitLab) |

## Essential commands

```bash
git init                                      # initialise a new repo
git clone https://github.com/example/repo    # clone an existing repo

git status                                    # working tree status
git branch                                    # list branches

git add file.txt                              # stage a file
git add -p                                    # stage hunks interactively
git commit -m "message"                       # commit staged changes

git log                                       # full history
git log --oneline --graph                     # compact visual history
```

## Branching workflow

```bash
git checkout main && git pull origin main     # sync with remote
git checkout -b feature/my-feature           # create feature branch
# ... make changes ...
git add . && git commit -m "add feature"
git push origin feature/my-feature           # push branch, open PR
```

After merge, clean up:

```bash
git checkout main && git pull origin main
git branch -d feature/my-feature             # delete local branch
```

For branching strategy guidance (trunk-based, polyrepo, release branches) see [[trunk-based-development]] and [[polyrepo-branching-strategy]].

## Resolving merge conflicts

When two branches change the same lines, Git marks the conflict:

```text
<<<<<<< HEAD
console.log("current branch code");
=======
console.log("incoming branch code");
>>>>>>> feature/my-feature
```

Edit the file to the desired state, then:

```bash
git add file.js
git commit
```

Use `git diff --merge` or a mergetool (`git mergetool`) for complex conflicts.

## Rebase

Rebase moves commits on top of another branch, producing a linear history.

```bash
git checkout feature/my-feature
git rebase main                              # replay commits onto main
```

Prefer **rebase** for keeping feature branch history clean before merging.
Prefer **merge** when you want to preserve the fact that a branch existed (e.g., release branches, long-running integration branches).

Rebase is destructive — do not rebase commits that have been pushed to a shared branch.

## Interactive rebase

Rewrite, squash, or reorder commits before merging:

```bash
git rebase -i HEAD~3                         # edit last 3 commits
```

Options per commit:

| Command | Effect |
|---|---|
| `pick` | Keep the commit as-is |
| `squash` / `s` | Combine with the previous commit |
| `reword` / `r` | Keep the commit, edit the message |
| `edit` / `e` | Pause to amend the commit |
| `drop` / `d` | Remove the commit entirely |

Use this before opening a PR to collapse WIP commits into clean, logical units.

## Stash

Temporarily shelve in-progress work without committing:

```bash
git stash                                    # save current changes
git stash list                               # see all stashes
git stash pop                                # restore and remove top stash
git stash apply stash@{1}                    # restore without removing
git stash drop stash@{0}                     # discard a stash
```

Useful for context-switching mid-task or pulling remote changes cleanly.

## Bisect

Binary search through commit history to find the commit that introduced a bug:

```bash
git bisect start
git bisect bad HEAD                          # current state is broken
git bisect good v1.0                         # last known good state
```

Git checks out the midpoint. Test, then mark:

```bash
git bisect good                              # this commit is fine
git bisect bad                               # this commit is broken
```

Repeat until Git identifies the exact commit. Exit with:

```bash
git bisect reset
```

Automate the test step:

```bash
git bisect run npm test                      # Git marks good/bad automatically
```

## Cherry-pick

Apply a specific commit from another branch:

```bash
git cherry-pick <commit-hash>
```

Common use case: backport a hotfix from `main` onto a release branch without merging the entire branch.

```bash
git checkout release/v1.2
git cherry-pick abc1234                      # apply the fix commit only
```

## Useful inspection commands

```bash
git diff                                     # unstaged changes
git diff --staged                            # staged changes
git show <commit>                            # show a specific commit
git blame file.js                            # who changed each line
git log --follow file.js                     # history including renames
git reflog                                   # full local operation history (recovery)
```

`git reflog` is a recovery tool — it records every HEAD movement, so you can restore commits lost by a bad reset or rebase.

## Best practices

- Commit small, logical changes with descriptive messages
- Sync with `main` frequently to avoid large merge conflicts
- Use branches for features and fixes — not as personal backups
- Rebase to clean history before merge; merge to preserve branch context
- Protect `main` with CI/CD checks and required reviews
- Never rebase shared/public branches
- Use `git reflog` before panicking about lost work
