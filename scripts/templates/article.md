Title: {{ title }}
Category: {{ category }}
Date: {{ date }}
Position:
Summary: {{ summary }}
Disqus_identifier: {{ disqus_id }}


{% include "context_header.md" %}

Context goes here.

Example definition
: This text defines *example definition*. It could be short, or a few lines
long. Try not to make it too long, though.

More context could go here. And for example, an image:

{% from 'img_desc.html' import img_desc %}
{{ img_desc("path_to_image.svg", "Description text.") }}


{% include "problem_header.md" %}


Introduce the challenge, and state the goal precisely.

Describe the input file.

Describe the desired output.


{% include "input_header.md" %}

```
example input
```

{% include "output_header.md" %}

```
example output
```


{% include "solutions_header.md" %}

The solution to this challenge is hosted on
[Github](https://github.com/leotrs/erdos/blob/master/solutions/{{ path.split('.')[0]}}.py).


{% include "question_header.md" %}

1. Make sure these are actually questions,
2. Or at the very least, explain exactly
3. What it is to be discussed


{% include "answers_header.md" %}


1. Make sure these are actually questions,
2. Or at the very least, explain exactly
3. What it is to be discussed


{% include 'footnote_header.md' %}


[^1]: [footnote 1]()
[^2]: [footnote 2]()
[^3]: [footnote 3]()
