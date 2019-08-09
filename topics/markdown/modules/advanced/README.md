# Advanced

<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Image Align](#image-align)
	- [Left Alignment](#left-alignment)
	- [Right Alignment](#right-alignment)
	- [Centre Alignment](#centre-alignment)
- [Collapse Sections](#collapse-sections)
- [Tables](#tables)
	- [Table Alignment](#table-alignment)
- [Closing](#closing)
- [Task](#task)

<!--TOC_END-->
## Overview
This topic will go over some of the more advanced Markdown syntax and formatting. There's lots you can do with Markdown, so experiment beyond this brief introduction to it!

## Image Align
As you saw in the last topic, we didn't dictate where we wanted our images to be displayed on the page. You'll be glad to hear that we are able to do this: 
### Left Alignment
To left align your images, you need to do the following:
```
<img align="left" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
```

<img align="left" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
___
### Right Alignment
```
<img align="right" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
```

<img align="right" width="100" height="100" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
___
### Centre Alignment
To align your images in the centre of a page, simply use:
```
<img align="center" width="460" height="300" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">
```

<img align="left" width="460" height="300" src="https://s3.amazonaws.com/spectrumnews-web-assets/wp-content/uploads/2018/11/13154625/20181112-SHANK3monkey-844.jpg">

As you can see, you can also dictate the width and height of an image here!
___
## Collapse Sections
<details>
<summary>"Click to learn!"</summary>
Collapsing large blocks of text can make your Markdown easier to read. It is also really useful for solutions or hints to exercises.

To add a collapsing section, you need to do:
```
<details>
<summary>"Click to expand"</summary>
this is hidden
</details>
```
</details>
## Tables
To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. You can optionally add pipes on either end of the table:
```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
### Table Alignment
You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row:
```
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
## Closing
By no means is this an extensive Markdown module, but it should give you the tools to create Markdown README.md files to a relatively good standard. Make sure to give the task below a go!
## Task
* Go to the [projects folder](./project)
* Create a README.md to explain how to get the simple python game up and running
* The formatting is for you to be creative with, but you must highlight to the user that they need to:
  * Install python3 (including a link to the website)
  * Install [pip](https://pip.pypa.io/en/stable/installing/)
  * Pip install virtualenv with `pip install virtualenv`
  * Create their vierual environment - `virtualenv venv`
    * And make sure they are working inside of it - `source venv/bin/activate`
  * Install the pip dependencies file, using `pip install -r pip_dependencies`
  * Run the python program - `python hangman.py`
