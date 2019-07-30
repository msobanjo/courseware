#! /usr/bin/env python
# generate a table of contents for every readme file
from pathlib import Path
from collections import Counter
import re

toc_start = "<!--TOC_START-->"
toc_end = "<!--TOC_END-->"
# get every readme file
for readme in Path("topics").glob("**/README.md"):
    print(readme)
    headings = []
    with open(readme, "r") as file:
        lines = file.read().split("\n")
        code_block = False
        for line in lines:
            if line.startswith("```"):
                code_block = not code_block
            if not code_block and line.startswith("#"):
                headings.append(line)

    heading_links = []
    for heading in headings:
        # remove special characters
        heading_link = re.sub('[^A-Za-z0-9 ]+', '', heading.replace("#", "")).strip().lower().replace("#", "").replace(" ", "-")
        heading_links.append(heading_link)
    # get rid of title heading
    heading_links.pop(0)
    headings.pop(0)
    # add numbers to headings
    heading_duplicates = dict(Counter(heading_links))
    for duplicate_heading, count in heading_duplicates.items():
        if count > 1:
            x = 0
            for i, heading in enumerate(heading_links):
                if heading == duplicate_heading:
                    if x != 0:
                        heading_links[i] = heading + "-" + str(x)
                    x += 1
    toc = {}
    for i, heading in enumerate(headings):
        depth = 0
        for letter in heading:
            if letter != "#":
                break
            depth += 1
            toc[heading.replace("#", "").strip()] = depth
    table_of_contents = ""
    for heading, depth in toc.items():
        indent = ""
        for i in range(2, depth):
            indent = indent + "\t"
        table_of_contents = table_of_contents + indent + "- " + heading + "\n"
    readme_no_toc = ""
    in_toc = False
    for line in lines:
        if line == toc_start:
            in_toc = True
        if line == toc_end:
            in_toc = False
            continue
        if not in_toc:
            readme_no_toc = readme_no_toc + line + "\n"
    print(readme_no_toc)
    new_readme = ""
    heading_count = 0
    for line in readme_no_toc.split("\n"):
        if line.startswith("#"):
            heading_count += 1
        if heading_count == 2:
            new_readme = new_readme + toc_start +  "\n" + table_of_contents + "\n" + toc_end + "\n"
            toc_added = True
        new_readme = new_readme + line + "\n"

    file = open(readme, "w")
    file.write(new_readme)
    file.close()

