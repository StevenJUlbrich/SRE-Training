# Module 3: Conflict Resolution (Days 5-6)

## Learning Objectives

- Understand why merge conflicts occur
- Develop strategies to minimize conflicts
- Master techniques for resolving conflicts when they arise
- Compare merging and rebasing approaches

### Understanding Conflicts

A merge conflict occurs when Git cannot automatically reconcile differences between branches. This typically happens when[^9]:

[^9]: [Resolving a merge conflict using the command line - GitHub Docs](https://docs.github.com/articles/resolving-a-merge-conflict-using-the-command-line#:~:text=Merge%20conflicts%20occur%20when%20competing,information%2C%20see%20About%20merge%20conflicts)

1. **Same line conflicts**: Two branches modify the same lines differently
2. **Delete vs. modify**: One branch deletes a file another branch modified
3. **Complex structural changes**: Overlapping changes that can't be automatically merged

### Conflict Markers Explained

When Git encounters a conflict, it inserts markers in the affected files[^10]:

[^10]: [How to resolve merge conflicts in Git](https://graphite.dev/guides/how-to-resolve-merge-conflicts-in-git#:~:text=Terminal)

```git
<<<<<<< HEAD
Your changes (current branch)
=======
Their changes (branch being merged)
>>>>>>> branch-name
```

Your task is to edit these files, decide on the final content, and remove the markers.

### Resolution Process

1. **Identify conflicted files**: Use `git status` to see which files are in conflict
2. **Understand both changes**: Review the conflict markers to understand both versions
3. **Decide on resolution**: Choose one version, combine them, or rewrite as needed
4. **Remove conflict markers**: Edit the file to contain only the final content
5. **Mark as resolved**: Use `git add <file>` to stage the resolved file
6. **Complete the merge**: Run `git commit` to finalize (or `git rebase --continue` if rebasing)
7. **Test the result**: Ensure your code still works after resolution

### Merge vs. Rebase

Both `git merge` and `git rebase` can cause conflicts, but they approach integration differently:

**Merge**:

- Creates a new commit combining changes from both branches
- Preserves complete history with branch structure
- Better when the branch structure is meaningful

**Rebase**:

- Replays your commits on top of the target branch
- Creates a linear history as if you started work later
- Better for cleaning up history before sharing

### Minimizing Conflicts

Prevention is better than cure:

1. **Communicate with your team** about who works on what
2. **Pull changes frequently** to stay in sync[^11]
3. **Keep branches short-lived** to reduce divergence
4. **Make smaller, focused commits** to reduce conflict surface area
5. **Structure code to minimize overlap** between team members

[^11]: [Git Branching Strategies: GitFlow, Github Flow, Trunk Based...](https://www.abtasty.com/blog/git-branching-strategies/#:~:text=Because%20trunk,any%20conflicts%20that%20may%20arise)

### Hands-On Exercise: Creating and Resolving Conflicts

1. **Simulate a conflict**:

   ```git
   # Create conflicting changes on two branches
   git checkout main
   echo "Line added by main" >> conflict.txt
   git commit -am "Main branch change"
   
   git checkout -b feature-branch
   echo "Line added by feature" >> conflict.txt
   git commit -am "Feature branch change"
   
   # Try to merge
   git checkout main
   git merge feature-branch
   # Conflict will occur
   ```

2. **Resolve the conflict**:

   - Edit conflict.txt to clean up markers and decide on content
   - Stage the resolved file: `git add conflict.txt`
   - Complete the merge: `git commit`

3. **Practice rebasing**:

   ```git
   git checkout feature-branch
   git rebase main
   # If conflicts occur, resolve them
   # After resolving: git add <file>
   # Then: git rebase --continue
   ```

### Resolving with Tools

Many tools can help visualize and resolve conflicts:

1. **Visual editors**: VS Code, IntelliJ, etc. have built-in conflict resolution
2. **Git mergetool**: Run `git mergetool` to use your configured visual merger
3. **Simpler scenarios**: Use `git checkout --ours <file>` or `git checkout --theirs <file>` to choose one version entirely
4. **Merge strategies**: For specific cases, Git supports different merge strategies like `git merge -X ours <branch>` to favor current branch changes[^12]

[^12]: [Git Merge Theirs Explained - Built In](https://builtin.com/articles/git-merge-theirs#:~:text=Git%20Merge%20Theirs%20Explained%20,branch%2C%20resolving%20git%20merge%20conflicts)
