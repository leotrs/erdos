# erdos/templates

This folder contains resources to automatically generate a new article.

Just run the `genarticle.py` script from the top level folder, and pass it
the path of the new article:

```
erdos $ python scripts/templates/genarticle.py path_to_article
```

`path_to_article` must be relative to the `erdos/content` directory.

`genarticle.py` will use `jinja2` and the templates in this directory to
generate a skeleton of the file, complete with date and !INCLUDE directives
already there.
