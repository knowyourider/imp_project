Site structure and overall logic
================================

Main menu, content types
------------------------

Each content type (story, artifact, etc.) has an entry in ContentType. Each content record, e.g. an artifact) is tied to ContentType with a foreign key.

Rich text editing
-------------------
We're using Froala (https://www.froala.com/wysiwyg-editor)
We decided not to use django-froala-editor -- that required using FroalaField in models -- doesn't seem right. Integrated "by hand" -- put the required css and jss in local_static, addeed script calls in our local templates/admin/chang_field.html, and then created per-app, per-field calls in admin -- inspired by py Danny's wysiwyg package.

Guidelines
---------
Fast facts only link from text in chapters -- not in dig deeper "gallery"

