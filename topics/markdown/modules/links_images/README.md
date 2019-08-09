# Links and Images

<!--TOC_START-->
### Contents
- [Overview](#overview)
- [Links](#links)
	- [Inline Link](#inline-link)
		- [Search for it on [Google](www.google.com)](#search-for-it-on-googlewwwgooglecom)
	- [Reference Link](#reference-link)
- [Images](#images)
	- [Inline Image Link](#inline-image-link)
	- [Reference Image Link](#reference-image-link)

<!--TOC_END-->
## Overview
This module explains how to integrate links and images into your Markdown files. Links and images make your Markdown more interactive and interesting, so it's really useful to learn how to use them.

## Links
There are two different link types in Markdown, but both of them render the exact same way.
### Inline Link
An inline link occurs within the text body, and is a really quick way of creating a link in your Markdown file. To do an inline link, you wrap the text you want to use as the link in square brackets `[]`, and then put the link in normal brackets `()`:
```
[Search for it](www.google.com)
```

[Search for it](www.google.com)

You could also add an inline link to a heading:
```
#### Search for it on [Google](www.google.com)
```

#### Search for it on [Google](www.google.com)

### Reference Link
These links, as the name implies, reference another place on your document, where the link is defined. The syntax for these is similar to, but not the same as, inline links:
```
Here's a link to [Google][google-link]
And one to [GitHub][github-link]

[google-link]: www.google.com
[github-link]: www.github.com
```

Here's a link to [Google][google-link]
And one to [GitHub][github-link]

[google-link]: www.google.com
[github-link]: www.github.com

The advantage of a reference link is that if you had multiple links to the same place in your document, and the link changed, you'd only need to update the link in one place (think variable in programming!)

You can add other Markdown elements to links, such as bold and italics, by simply using the syntax you saw in the last module.
## Images
Once you know how to create links in Markdown, you can work with images! The main difference is that images are prefaced with an exclamation mark `!`.

Just like links, images have two styles that render in exactly the same way:
### Inline Image Link
To create an inline image link, enter an exclamation mark `!`, wrap the text you want to use as a link in squafre brackets `[]`, and then wrap the link in normal brackets `()`:
```
A picture of an ![egg](https://static.standard.co.uk/s3fs-public/thumbnails/image/2019/01/14/09/worldrecordegg1401a.jpg?w968)
```

A picture of an ![egg](https://static.standard.co.uk/s3fs-public/thumbnails/image/2019/01/14/09/worldrecordegg1401a.jpg?w968)

You don't necessarily need to add the text you want to use as a link (in this case `egg`), but it makes the content asccesible to your audience, which is always a good thing.
### Reference Image Link
For this, you follow the same pattern as the reference link above, but use the `!` as well:
```
![Manchester City][blue]
![Manchester United][red]

[blue]: https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2019/5/12/1ded5ce1b11546adb562b21a7fcafb27_18.jpg
[red]: https://images.footyroom.com/posts/52f298e49dc85c55bcba71990c73153d/16111905-10211321425782611-258512663-n
```

![Manchester City][blue]
![Manchester United][red]

[blue]: https://www.aljazeera.com/mritems/imagecache/mbdxxlarge/mritems/Images/2019/5/12/1ded5ce1b11546adb562b21a7fcafb27_18.jpg
[red]: https://images.footyroom.com/posts/52f298e49dc85c55bcba71990c73153d/16111905-10211321425782611-258512663-n

> If you want the image to just appear in the body of your Markdown file (without having to follow a link), just remove the `!` mark and see the ![magic](https://cambridgewords.files.wordpress.com/2017/11/magic-wand.jpg) happen.
