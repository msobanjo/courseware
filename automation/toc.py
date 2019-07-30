#! /usr/bin/env python
# generate a table of contents for every readme file
from pathlib import Path
import re

# get every readme file
for name in Path("topics").glob("**/README.md"):
    print(name)

# test (hardcoded) readme file for now
toc_start = "<!--TOC_START-->"
toc_end = "<!--TOC_END-->"
readme = "./topics/groovy/README.md"
with open(readme, "r") as file:
    headings = list(filter(lambda line: line.startswith("#"), file.read().split("\n")))

formatted_headings = []
for heading in headings:
    # remove special characters
    formatted_heading = re.sub(r'\W+', ' ', heading.replace("#", "")).strip().lower().replace("#", "").replace(" ", "-")
    formatted_headings.append(formatted_heading)

# get rid of title heading
formatted_headings.pop(0)

# testing duplicate headings
formatted_headings.append("overview")

for heading in formatted_headings:

