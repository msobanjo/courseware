#! /usr/bin/env python
import os
# get everything from a folder but the README.md file
def get_folders(dir):
    return filter(lambda file: file != "README.md", os.listdir(dir))

for topic in get_folders("./topics"):
    print(topic + ":")
    # find all modules and create markdown for the links
    module_links = "## Modules"
    for module in get_folders("./topics/" + topic + "/modules"):
        print("\t" + module)
        module_links = module_links + "\n- [" + module + "](./modules/" + module + ")"
    start = "<!--MODULES_START-->"
    end = "<!--MODULES_END-->"
    module_links = start  + "\n" + module_links + "\n" + end
    # build readme with module links
    readme = ""
    readme_file = "./topics/" + topic + "/README.md"
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
    readme = readme + "\n" + module_links
    print(readme)
    # update readme file
    with open(readme_file, "w") as file:
        file.write(readme)

