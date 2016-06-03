Design Environment
===================

Some cheats we had to do to make things work both in the design environment work both locally, statically and to work statically on the server when referenced through wsgi as well as Apache.

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

CSS Background images
---------------------

We need bg css def in story pages in order to use variable names. We put the images in local_static/images/stories and use the local_static_sym describe above.
