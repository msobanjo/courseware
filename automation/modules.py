#! /usr/bin/env python
# generate modules list for every topic
import os

#set global variables
start = "<!--MODULES_START-->"
end = "<!--MODULES_END-->"

# get everything from a folder but the README.md file
def get_folders(dir):
    return list(filter(lambda file: file != "README.md", os.listdir(dir)))


# find all modules and create markdown for the links
# function 1 - return module_links
def get_module_links(topic):
	module_links = "## Modules"
	module_name = ""
	modules = get_folders("./topics/" + topic + "/modules")
	modules.sort()
	for module in modules:
		# get the module name from the module's readme
		with open("./topics/" + topic + "/modules/" + module + "/README.md") as file:
			for line in file.read().split("\n"):
				if line.startswith("#"):
					module_name = line.replace("#","").strip()
					break
			print("\t" + module_name)
			module_links = module_links + "\n- [" + module_name + "](./modules/" + module + ")"
	module_links = start  + "\n" + module_links + "\n" + end
	return module_links

# build readme with module links
# function 2 - takes module_links as parameter
def build_readme(topic, module_links, readme_file):
	readme = ""
	with open(readme_file, "r") as file:
		delete = False
		for i, line in enumerate(file.read().split("\n")):
			if line == start:
				delete = True
			if line == end:
				delete = False
				continue
			if not delete:
				if i == 0:
					readme = readme + line
				else:
					readme = readme + "\n" + line
	readme = readme + module_links
	return readme

# update readme file
# function 3 - takes read me as parameter
def update_readme(topic, readme, readme_file):
	with open(readme_file, "w") as file:
		#file.write(readme)
		print(readme)

#for each topic create the modules
for topic in get_folders("./topics"):
	print(topic + ":")
	readme_file = "./topics/" + topic + "/README.md"
	module_links = get_module_links(topic)
	readme = build_readme(topic, module_links, readme_file)
	update_readme(topic, readme, readme_file)
