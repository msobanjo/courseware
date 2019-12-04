# Notes
Centralised project for learning Cloud and DevOps Topics.
<!--TOC_START-->
## Contents
- [Repository Forking & Rebasing](#repository-forking--rebasing)
	- [Contributing](#contributing)
	- [Automation](#automation)
		- [Circle CI](#circle-ci)
		- [Local Setup](#local-setup)

<!--TOC_END-->
## Where to start?
To start using this Project to develop your knowledge, you need to know how best to use this Project.
What you need to understand starting out is that the majority of the content is described in README.md files, you can read these easily directly on GitHub.

Above this README.md is a list of the files included in the Repository, your main focus should be the **topics** folder.
Select this now.

Here you will see the topics that exist within the project.
Each Topic has its own directory, some are very broad (aws) whilst some are more focused (wireshark).
When you are looking for material to learn from you should be looking at **all** the topics that are available here.
Select one of these topics, for our example now we will be using the **powershell** topic.

The README.md in this directory will describe various things, however there is a common high level-structure.

### Contents

This will describe all the sections in this document, including those that might exist which we won't cover here.

### Overview

A simple overview of the tool or service you will be looking at.

### Modules

A list of all the modules on offer within this topic.
**This is where you will find most of the content on offer.**

Select one of these Modules, for our example we will be selecting the **Introduction** module.

In most cases you will find a single README.md, this is where you will find the information for this module.  As a general rule the module README.md will follow the structure below.
 
### Contents

This will describe all the sections in this document, including those that might exist which we won't cover here.

### Overview

A simple overview of the the specific module, usually detailing what you can expect to learn from this module.

### Tasks

For most of the modules there will be a task for you to perform, this can be a short guided tutorial, or a more problem-solving driven exercise.

In summary there is a vast wealth of information available in this project, please take the time to look through the topics that might apply to you.


## Repository Forking & Rebasing
It's recommended to fork this repository to benefit from the examples and exercises.
To handle updates from this main repository on your forked one, you can rebase to update any changes:
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
If you are having issues pushing to your master branch, you may need to add the `--force` option to the previous command and try it again.
### Contributing
Please see the [contributing guidelines](./CONTRIBUTING.md).
### Automation
Links to topic modules are included on main topic README files and a table of contents is entered into every README file.
This has been automated by Python scripts in the `automation` folder:
- `modules.py` - Generate module links for the main README on topics
- `toc.py` - Generate a table of contents for every README on the project
#### Circle CI
Circle CI has been setup to run these scripts automatically and then commit the changes back to the branch being built, so don't feel like you need to get these scripts working before making a pull request.
#### Local Setup
You'll need to install some dependencies from the `pip_dependecies` files; using a virtual environment is also recommended.
1. Make sure you have Python 3.* installed, as well as Pip
2. Make sure virtualenv is installed with `pip install virtualenv`
3. Configure a virtual environment with `virtualenv -p python3 venv` 
4. Load into the virtual environment: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r pip_dependecies`
