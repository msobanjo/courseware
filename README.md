# Notes
Centralised project for learning Cloud and DevOps Topics, just getting started.
<!--TOC_START-->
### Contents
	- [Repository Forking & Rebasing](#repository-forking--rebasing)
	- [Collaboration](#collaboration)
		- [Concepts](#concepts)

<!--TOC_END-->
### Repository Forking & Rebasing
It's recommended to fork this repository to benefit from the examples and exercises.
To handle updates from this main repository on you forked one, you can rebase to update any changes:
1. Add this project as an upstream from your forked repository:
```bash
git remote add upstream https://github.com/bob-crutchley/notes
```
2. Fetch the remote branches from the new upstream:
```bash
git fetch upstream
```
3. Rewrite your master branch to accommodate for the new changes:
```bash
git rebase upstream/master
```
4. Push the changes to your repository:
```bash
git push -u origin master
```
If you are having issues pushing to your master branch you may need to add the `--force` option to the previous command and try it again.
### Collaboration
Anyone is welcome to collaborate on this project but please adhere to conventions in place.
#### Concepts
- Topics
    This is a subject, which could be a programming language or tool; Java, Jenkins, Kubernetes, Google Cloud Platform for instance.
- Modules
    Modules are the topics broken down into much smaller, digestible content and tasks.
- Courses
    A course is a carefully ordered set of modules from any topics that are relevant for the course outcome.
- Pathways
    Pathways are courses that have been put in order.
