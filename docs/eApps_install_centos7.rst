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

from anywhere (in terminal) -- dev
(looks like the --python option is redundant (with .bash_profile above))
::
	mkvirtualenv -a  /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions --python=/usr/local/bin/python3.6 impressions

Public
::
	mkvirtualenv -a  /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions --python=/usr/local/bin/python3.6 implive

Install Django 
---------------------
::

	workon impressions
	pip install Django==1.10.7
	pip install Unipath==1.1

upgrade 7/17/2017
::
	pip install --upgrade django==1.11.3

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

log location: /var/lib/pgsql/data/pg_log/


Install psycopg2
--------------

(Didn't Prepare by installing the postgres devloper tools -- from prev docs.
This has to be installed in virtual env
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

	cd /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org

for public
::
	git clone https://github.com/knowyourider/imp_project.git dinotracksdiscovery.org
	cd /var/www/pvma-django/data/www/dinotracksdiscovery.org

Transfer database
------------------

Get the backup
::
Transfer the backup from "old" to local.
::
	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	(edit remote pvma password into the following, ad hoc)
	wget --user=pvma --password='pvma password by hand' ftp://deerfield-history-center.org/FTP_transfer/impdb_$(date +"%Y_%m_%d").backup

Restore to new server.
[hmm, phppgadmin? or command line?]
Get phpPgAdmin fired up

phpPgAdmin
https://68.169.61.104/pgadmin/ # nope, goes to African american -- need to talk with Tony
user: postgres
Pass: in 1pass, keychain, and in ISP > Server Settings --> Database Servers

Try pgAdmin3
Password: Settings > Database servers > Edit
Can't connect -- dialog just bounces back to me.

Setup access for postgres user
-------------------------------

Command Line
Based on copy data to educators
# Note msedb_ed as the target.
Upload vis FTP this time
Log into shell as root
::

	su - postgres
	cd /var/www/pvma-django/data/FTP_transfer
	#pg_restore --clean --dbname=msedb_ed --user=msedb_user --verbose msedb_$(date +"%Y_%m_%d").backup
	pg_restore --dbname=impdb --user=impdb_user --verbose impdb_$(date +"%Y_%m_%d").backup
	[db password here]


Edit pg_hba.conf located at /var/lib/pgsql/data

from vm1
::
	local template1 postgres password
	host template1 postgres 0.0.0.0 0.0.0.0 password
	host	impdb	impdb_user	0.0.0.0	0.0.0.0	password
	local all postgres password
	local all root password
	local	impdb	impdb_user	password
	local template1 all password
	host all all 127.0.0.1/32 md5
	host all all ::1/128 md5

As is on vm2
::
	local	postgres	postgres	ident
	host	all	all	127.0.0.1/32	md5
	host	all	all	::1/128	md5
	host	impdb	impdb_user	173.48.47.251/32	md5

eApps KB article says other users to have access then lines need to be added
Allow su postgres when logged in as root
::
	local	impdb	impdb_user	password

Allow access from my local PGAdmin3
Ip address will need to be changed in pg_hba as needed
::
	host	postgres	postgres	173.48.47.251/32	md5
	host	impdb	postgres	173.48.47.251/32	md5

With PGAdmin3 change owner of public schema to impdb_user

Had database prob:
password authentication failed for user "impdb_user"
But support fixed the password on impdb

Test with runserver - ok


Set up Apache
----------------
WSGI part 2

in /etc/httpd/conf/vhosts/pvma-django/dev.dinotracksdiscovery.org
We're in Apace version 2.2.21??

As is, from server, plus my insertion
::

	<VirtualHost 68.169.61.104:80>
		ServerName dev.dinotracksdiscovery.org
		DocumentRoot /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org
		ServerAdmin webmaster@dev.dinotracksdiscovery.org
		AddDefaultCharset UTF-8
		SuexecUserGroup pvma-django pvma-django
		CustomLog /var/www/httpd-logs/dev.dinotracksdiscovery.org.access.log combined
		ErrorLog /var/www/httpd-logs/dev.dinotracksdiscovery.org.error.log
		DirectoryIndex index.html

	# Don inserting here
	Alias /static/ /var/www/pvma-django/data/www/imp_static/
	Alias /design/ /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/design/
	WSGIDaemonProcess staging python-path=/var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions:/var/www/pvma-django/data/.envs/impressions/lib/python3.6/site-packages
	WSGIProcessGroup staging
	WSGIScriptAlias / /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/config/wsgi.py
	# end insertion


	</VirtualHost>
	<Directory /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org>
		Options +Includes -ExecCGI
	</Directory>

Just the insertions, for dev.dino
::
		# Don inserting here
	    Alias /static/ /var/www/pvma-django/data/www/imp_static/
	    Alias /design/ /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/design/

	    WSGIDaemonProcess staging python-path=/var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions:/var/www/pvma-django/data/.envs/impressions/lib/python3.6/site-packages
	    WSGIProcessGroup staging
	    WSGIScriptAlias / /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/config/wsgi.py
	    # end insertion

	# Don adding this
	<Directory /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/config>
	    <Files wsgi.py>
		    Order deny,allow
		    Allow from all
	    </Files>
	</Directory>

	# robots alias
	Alias /robots.txt /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/robots.txt

Insertions for public dinotracks
::
		# Don inserting here
	Alias /static/ /var/www/pvma-django/data/www/imp_static/

	WSGIDaemonProcess production python-path=/var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions:/var/www/pvma-django/data/.envs/imppub/lib/python3.6/site-packages
	WSGIProcessGroup production
	WSGIScriptAlias / /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions/config/wsgi.py
	    # end insertion

	# Don adding this
	<Directory /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions/config>
	    <Files wsgi.py>
		    Order deny,allow
		    Allow from all
	    </Files>
	</Directory>

	# robots alias
	Alias /robots.txt /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions/robots.txt

NEXT: 
- change collected static to pvma-django
- post with allowed hosts

collect static as pvma-django

touch
::
	touch /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/config/wsgi.py
	
As root
::
	workon impressions
	./manage.py migrate
	./manage.py runserver

Transfer assets
---------------

Use wget
::
	wget --user=pvma --password='pvma password by hand' ftp://68.169.58.50/www/impdev.deerfield-ma.org/impressions/themes/themes-static.zip

Allow .htaccess for 301 redirect for www to non-www
----------------------------------------------------

allow override
::
	 <Directory /var/www/pvma-django/data/www/dinotracksdiscovery.org>
	    AllowOverride All
	 </Directory>




