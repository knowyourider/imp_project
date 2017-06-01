eApps install with CentOS 7
=============================

References
-----------
- Eriksson - Best ref: [How to install the latest version of Python on CentOS - Daniel Eriksson](https://danieleriksson.net/2017/02/08/how-to-install-latest-python-on-centos/)
	- forwarded to this from previous Too Much Data article
	- has the Shared Library step necessary for mod_wsgi
- need python with mod_wsgi
	- previous Ocean, os6 doc -- doesn't address mod_wsgi.
	- the previous ref from eApps (os6) doesn't have the mod_wsgi hook either.
- eApps - ref'd by support: [Install and Configuration CentOS 7 Server Python/Django/Virtualenv/Postgres/Nginx/uWSGI · GitHub](https://gist.github.com/Lh4cKg/ffc60c312586223ca5750fef5879ee99)
- Digital Ocean Python (but not wsgi): [How To Install Python 3 and Set Up a Local Programming Environment on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
- Digital Ocean apache, wsgi, Django - but not python: [How To Serve Django Applications with Apache and mod_wsgi on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-centos-7)
- Digital Ocean, CentOS 7 - only Django: [How To Install the Django Web Framework on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-centos-7)


Install Python 3.6
--------------------

From Ocean Python: operate as a non-root "superuser" using sudo. Eriksson says either root or sudo.

Test current built-in version on CentOS7 -- 2.7.5
Test pvma-django user and pass

Install tools
Ocean Python says to update yum
