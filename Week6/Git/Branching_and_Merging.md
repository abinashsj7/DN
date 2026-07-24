# Branching and Merging

## What is a Branch?

A branch is an independent line of development that allows developers to work on new features without affecting the main code.

Default branch:
- main

Example:

main
 |
 +---- feature-login

---

## Create a Branch

```bash
git branch feature-login
```

---

## Switch to a Branch

```bash
git checkout feature-login
```

---

## Create and Switch Together

```bash
git checkout -b feature-login
```

---

## Merge Branch

```bash
git checkout main
git merge feature-login
```

This combines the changes from the feature branch into the main branch.

---

## Advantages

- Safe development
- Parallel work
- Easy collaboration
- Isolated feature development
