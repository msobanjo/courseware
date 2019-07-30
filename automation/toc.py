#! /usr/bin/env python
# generate a table of contents for every readme file
from pathlib import Path

# get every readme file
for name in Path("topics").glob("**/README.md"):
    print(name)

# test (hardcoded) readme file for now
toc_start = "<!--TOC_START-->"
toc_end = "<!--TOC_END-->"
readme = "./topics/groovy/README.md"
with open(readme, "r") as file:
    print(file.read())
