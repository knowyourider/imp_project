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

Symbolic Links to make model work online
---------------------------------------

The design directory contains "static" html mockups. In that directory we make a symboic link to the "real" local_static directory so that these files can use the live css, js etc. 
These the sym directories are excluded in .gitignore. The need to be created separately on local and staging environments.

(Rationale: For eApps/online, the path to any static mockup asset has to start with /design/, so we can't refer directly to /local_static/. (Could all be relative I suppose, ../../local_static, but the directory layer depth would vary from file to file.)

local -- in Terminal, doesn't matter what directory you're in, don't need "workon."
::
	
	ln -s ~/Sites/imp_project/impressions/local_static ~/Sites/imp_project/impressions/design/local_static_sym

eapps
::
	
	ln -s /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/local_static /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/design/local_static_sym
