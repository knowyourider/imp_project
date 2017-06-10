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
- eApps Github - ref'd by support: [Install and Configuration CentOS 7 Server Python/Django/Virtualenv/Postgres/Nginx/uWSGI · GitHub](https://gist.github.com/Lh4cKg/ffc60c312586223ca5750fef5879ee99)
- Digital Ocean Python (but not wsgi): [How To Install Python 3 and Set Up a Local Programming Environment on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
- Digital Ocean apache, wsgi, Django - but not python: [How To Serve Django Applications with Apache and mod_wsgi on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-centos-7)
- Digital Ocean, CentOS 7 - only Django: [How To Install the Django Web Framework on CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-centos-7)
- Super user acct. to use with sudo: [Initial Server Setup with CentOS 7 | DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7)
- mod_wsgi: [Getting Started — mod_wsgi 4.5.14 documentation](https://modwsgi.readthedocs.io/en/develop/getting-started.html)


Install Python 3.6
--------------------

From Ocean Python: operate as a non-root "superuser" using sudo. Eriksson says either root or sudo. Going with root.

Test current built-in version on CentOS7 -- 2.7.5

Install tools
+++++++++++++

Ocean Python says to update yum
eApps Github says update yum and wget epel

Diving in, going to stick most closely to Eriksson, but first the updates, per Ocean Python
::
	yum update -y && yum upgrade -y
	# yum -y install yum-utils (already installed by the above)
	# yum groupinstall -y "development tools" (hit error)

Going back to eApps Github in case these are prerquisites.
Changed release-7-5 to 7-9
::
	# wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
	# rpm -ivh epel-release-7-9.noarch.rpm (already installed)
	# yum update -y && yum upgrade -y (nothing new)
	# dnf install redhat-rpm-config (command not found)

eApps support: cause was related to a missing configuration on the CentOS Plus repository required to install the kernel and its related packages.
They ran
::
	yum groupinstall 'Development Tools' --enablerepo=centosplus
So I ran groupinsall again
::
	yum groupinstall -y "development tools"
	> 1 packages excluded due to repository priority protections
	> Maybe run: yum groups mark install (see man yum)
	> No packages in any requested group available to install or update

Next line from Eriksson
::
	# Libraries needed during compilation to enable all features of Python:
	yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel

Install Python
++++++++++++++

Pay particular attention to the part in Eriksson about using the LDFLAGS as will be required by mod_wsgi
Dir to be in for the download: /usr/local/src
Check that all destinations exist before running.
::
	cd /usr/local/src
	# Python 3.6.1:
	wget http://python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
	tar xf Python-3.6.1.tar.xz
	cd Python-3.6.1
	./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
	make && make altinstall

Rebooted to new kernel
now redo and update
Redo tools
::
	yum update -y && yum upgrade -y
	# 1 packages excluded due to repository priority protections
	yum groupinstall 'Development Tools'
	# 1 packages excluded due to repository priority protections
	yum update -y zlib-devel
	yum update -y bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel

Check Python install. Redo? 
No, going to try to proceed and see if any problems arise
::
	# cd /usr/local/src/Python-3.6.1
	# ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
	# make && make altinstall

Back to Eriksson
::
	strip /usr/local/lib/libpython3.6m.so.1.0
	cd /usr/local/src
	wget https://bootstrap.pypa.io/get-pip.py
	python3.6 get-pip.py
	# enables: pip3.6 install [packagename]

Visit flag issue per my PyDjango docs and the previous eApps_install.rst
::
	cd /etc
	vim ld.so.conf
	# add: /usr/local/lib 

	ldconfig


WSGI
-----
Switching to Digital Ocean Apache as a ref.
Do I need to build mod_wsgi? Or "just" yum install mod_wsgi?
Ocean Apache has yum install
My previous eApps install has yum apache tools, download and build.
Per mod_wsgi doc: [Getting Started — mod_wsgi 4.5.14 documentation](https://modwsgi.readthedocs.io/en/develop/getting-started.html)
Be sure to enable daemon mode.

From prev notes
::
 	(determine apache version)
	apachectl -V
	(Apache/2.4.6 (CentOS))
	yum install httpd-devel-2.4.6

	cd /usr/local/src
	wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.14.tar.gz
	tar xf 4.5.14.tar.gz
	cd mod_wsgi-4.5.14
	./configure --with-python=/usr/local/bin/python3.6
	make
	make install

	cd /etc/httpd/conf.d
	(create the file: wsgi.conf -- will contain only the following:)
	LoadModule wsgi_module modules/mod_wsgi.so

oops, I didn't run that command after include ld.so.conf.d/*.conf
Now run ldconfig from /etc
::
	ldconfig

	cd /usr/local/src/mod_wsgi-4.5.14
	make
	make install

Double check that mod_wsgi was created with shared lib
Per: https://modwsgi.readthedocs.io/en/develop/user-guides/checking-your-installation.html
::
	cd /etc/httpd/modules
	ldd mod_wsgi.so
	# Good:
	# libpython3.6m.so.1.0 =>

Enable module in apache
++++++++++++++++++++++++
In ISP look at /etc/httpd/conf/httpd.conf
Modules are listed in Include conf.modules.d/*.conf

Add file 00-wsgi.conf with LoadModule wsgi_module modules/mod_wsgi.so


::
	cd /etc/httpd/conf.modules.d
	vim 00-wsgi.conf
	# Added by Don Button for mod_wsgi - Django
	LoadModule wsgi_module modules/mod_wsgi.so

Come back to Apache server conf later
wsgi getting started: https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html


Super user
-----------
Belatedly
I'm thinking that, per Ocean, it would be good to have a non-root user that could use sudo.
Could add some flexibility -- could add to group. 
Create user in isp, then
::
	gpasswd -a [my-name] wheel

hmm, not that kind of user that has a bash login, so sticking with root

Install Virtual Environment
-----------

Ocean Apache, prev notes and PyDjangoDocs virtual env

Python 3 comes with venv built-in, so we can proceed straight to Virtualenvwrapper.

From any dir:
::
	pip3.6 install virtualenvwrapper


[look at .bash_profile on vm1 root and vm2 pvma_django user]

Edit ~/.bash_profile to indlude:
::
	export WORKON_HOME=/var/www/pvma-django/data/.envs
	export PROJECT_HOME=/var/www/pvma-django/data/www
	# to use Python 3
	export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.6
	export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
	source /usr/local/bin/virtualenvwrapper.sh

logout and log back in.
Then, as documented in VirtualenvWrapper.md, create project and use workon proj etc.

Create site
-------------
- Add subdomain in Portal
- Add domain in ISP

Set up a virtual env
____________________

from anywhere (in terminal)
(looks like the --python option is redundant (with .bash_profile above))
::
	mkvirtualenv -a  /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions --python=/usr/local/bin/python3.6 impressions

Install Django 
---------------------
::

	workon impressions
	pip install Django==1.10.7
	pip install Unipath==1.1


Postgresql
------------
Posgres can be installed in ISP per: 
[PostgreSQL 9 and phpPgAdmin - Powered by Kayako Help Desk Software](https://support.eapps.com/index.php?/Knowledgebase/Article/View/414/53/postgresql-9-and-phppgadmin)

Installed PostgreSQL 9.2.18-1.el7
Also, phpPgAdmin

Set up the Postgresql database via ISP mangager with user and pass from local
Owner pvma-django -- (impdb_user created on separte line in dialog)
Encoding UTF8
new user per settings base
Password has to pass muster upper and lower (or did it work after I selected the auto generator?)
Entering my current IP for remote access -- will need to change as needed.

Install psycopg2
--------------

(Didn't Prepare by installing the postgres devloper tools -- from prev docs.
	# yum install python-setuptools python-devel postgresql-devel
::

	workon impressions
	pip install psycopg2==2.6


Git clone the project
-----------------
Delete/rename the default, then clone
while in /var/www/pvma-django/data/www

Log in as pvma-django !!
:: 
	cd /var/www/pvma-django/data/www
	git clone https://github.com/knowyourider/imp_project.git dev.dinotracksdiscovery.org

Test and migrate
----------------

::
	./manage.py migrate

