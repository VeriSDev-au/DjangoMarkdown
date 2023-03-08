# DjangoMarkdown
This is Django Project only focusing how to utilise Python-Markdown. The code is prof of concept before start using it for the blog in vsdwebsite project. Basically we plan to build a blog inside vsdwebsite. Content of the blog will use Markdown as the standard format and stored in postgresql database. 

## Markdown Library
Markdown Library was wrote by John Gruber's. To install this library:

```
pip install markdown
```

## Implementation Markdown in this project
This project implementing templatetags to convert markdown format into html. You can find blog_utility.py inside templatetags within app folder.

code for blog_utility.py:

```py
import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(value):
    return markdown.markdown(value, extensions=["markdown.extensions.fenced_code"])

```

the implementation in the html templates can be like this:

```html
{% load blog_utility %}

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="css/bootstrap.min.css" rel="stylesheet" integrity="sha384-" crossorigin="anonymous">
</head>
<body>
    {{ content_readme|convert_markdown|safe }}
    <script src="js/bootstrap.bundle.min.js" integrity="sha384-" crossorigin="anonymous"></script>
</body>
</html>
```