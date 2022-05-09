# Table of Contents

1. ["force_text" Import Error](#force_text_Import_Error)

---

<div id='force_text_Import_Error'/>

## "force_text" Import Error

> ### **Error**

```
ImportError: cannot import name ‘force_text’ from ‘django.utils.encoding’ Error
```

> ### **[Fix](https://exerror.com/importerror-cannot-import-name-force_text-from-django-utils-encoding/#:~:text=encoding'%20Error%20%3F-,To%20Solve%20ImportError%3A%20cannot%20import%20name%20'force_text'%20from%20',utils.py%3A%20from%20django.)**

From Django 4 we dont have force_text You Just have to Use force_str Instead of force_text.

Replace this line in your venv/lib/site-packages/graphene_django/utils/utils.py

```python
from django.utils.encoding import force_text
```

to

```python
from django.utils.encoding import force_str
```

And

```python
def _camelize_django_str(s):
    if isinstance(s, Promise):
        s = force_text(s)
    return to_camel_case(s) if isinstance(s, six.string_types) else s
```

to

```python
def _camelize_django_str(s):
    if isinstance(s, Promise):
        s = force_str(s)
```
