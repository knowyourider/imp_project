eApps Impressions install commands
==========================

tools
-----------
::

	yum groupinstall "Development tools"
	yum install zlib-devel
	yum install bzip2-devel
	yum install openssl-devel
	yum install ncurses-devel
	yum install sqlite-devel

Python
------------
::

	cd /usr/local/src
	wget http://python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
	tar xf Python-3.5.1.tar.xz
	cd Python-3.5.1
	./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
	make && make altinstall

	python3.5 --version

WSGI
------------
::

	(determine apache version)
	apachectl -V
	(Apache/2.2.21)

	yum install httpd-devel-2.2.21

	cd /usr/local/src
	wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.4.22.tar.gz
	(downloaded as 4.4.22)
	cp 4.4.22 4.4.22.tar.gz
	tar xf 4.4.22.tar.gz
	cd mod_wsgi-4.4.22
	./configure --with-python=/usr/local/bin/python3.5
	make
	make install

	cd /etc/httpd/conf.d
	(create the file: wsgi.conf -- will contain only the following:)
	LoadModule wsgi_module modules/mod_wsgi.so
	(jan 2016 - created it w/ ISP manager, Latin1)

Shared Python Library
Edit file /etc/ld.so.conf
Add /usr/local/lib
::

	include ld.so.conf.d/*.conf
	/usr/local/lib

	(run)
	ldconfig

Virtual Environment
-----------

From any dir
::

	pip3.5 install virtualenvwrapper

Assuming we have the user path set up on the server.
Edit ~/.bash_profile to indlude:
::

	export WORKON_HOME=/var/www/pvma/data/.envs
	export PROJECT_HOME=/var/www/pvma/data/www
	### to use Python 3
	export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.5
	export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv-3.5
	source /usr/local/bin/virtualenvwrapper.sh

Log out and log back in to make the profile changes take effect


Git clone the project
-----------------
Delete/rename the default, then clone
while in /var/www/pvma/data/www
:: 

	git clone https://github.com/knowyourider/imp_project.git impdev.deerfield-ma.org

To make a virtual env and bind it to an existing project
(don't think it matters what directory you're in)
::

	mkvirtualenv -a /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions --python=/usr/local/bin/python3.5 impressions

Automatically puts you in the env, but later:
::

	workon impressions

Install Django
--------------
::

	workon impressions
	pip install Django==1.9.1
	pip install Unipath==1.1

Postgresql
------------
Posgres can be installed per: [PostgreSQL 9 and phpPgAdmin - Powered by Kayako Fusion Help Desk Software]
https://support.eapps.com/index.php?/Knowledgebase/Article/View/414/53/postgresql-9-and-phppgadmin

Installed 9.2.4-1.1
Also, phpPgAdmin

Set up the Postgresql database via ISP mangager with user and pass from local
Owner pvma
Encoding UTF8
new user per settings base
Password has to pass muster upper and lower (or did it work after I selected the auto generator?)


Install psycopg2
--------------

Prepare by installing the postgres devloper tools
(one note said to run yum within virtenv, but it doesn't seem like that should be necessary)
::

	workon impressions
	yum install python-setuptools python-devel postgresql-devel

	pip install psycopg2==2.6


Run server to test.
::

	./manage.py runserver --settings=config.settings.staging

WSGI part 2
-----------

in /etc/httpd/conf/httpd.conf
(oftn in /etc/httpd/conf/vhosts/<user name>, but not here)
We're in Apace version 2.2.21
(changed SuexecUserGroup to apache apache late January 2017)
::

	<VirtualHost 68.169.58.50:80>
		ServerName impdev.deerfield-ma.org
		DocumentRoot /var/www/pvma/data/www/impdev.deerfield-ma.org
		SuexecUserGroup apache apache 
		CustomLog /var/www/httpd-logs/impdev.deerfield-ma.org.access.log combined
		ErrorLog /var/www/httpd-logs/impdev.deerfield-ma.org.error.log
		ServerAlias www.impdev.deerfield-ma.org
		ServerAdmin donpublic@digitalgizmo.com
		php_admin_value open_basedir "/var/www/pvma/data:."
		php_admin_value sendmail_path "/usr/sbin/sendmail -t -i -f donpublic@digitalgizmo.com"
		php_admin_value upload_tmp_dir "/var/www/pvma/data/mod-tmp"
		php_admin_value session.save_path "/var/www/pvma/data/mod-tmp"
		AddType application/x-httpd-php .php .php3 .php4 .php5 .phtml
		AddType application/x-httpd-php-source .phps

        Alias /static/ /var/www/pvma/data/www/imp_static/
        Alias /design/ /var/www/pvma/data/www/mpdev.deerfield-ma.org/impressions/design/
		Alias /robots.txt /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions/robots.txt

        WSGIDaemonProcess staging python-path=/var/www/pvma/data/www/impdev.deerfield-ma.org/impressions:/var/www/pvma/data/.envs/impressions/lib/python3.5/site-packages
        WSGIProcessGroup staging
        WSGIScriptAlias / /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/config/wsgi.py

        <Directory /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/config>
        <Files wsgi.py>
        Order deny,allow
        Allow from all
        </Files>
        </Directory>

	</VirtualHost>
	<Directory /var/www/pvma/data/www/impdev.deerfield-ma.org>
	        Options +Includes +ExecCGI
	</Directory>
	~            	
 
Rich text editing
-------------------
We're using Froala (https://www.froala.com/wysiwyg-editor)
We decided not to use django-froala-editor -- that required using FroalaField in models -- doesn't seem right. Integrated "by hand": 
- put the required css and js in local_static, 
- add script calls in our local templates/admin/change_field.html
- created per-app, per-field calls in admin -- inspired by py Danny's wysiwyg package.


Create ssh key on eApps PVMA for use with github knowyourider
---------------------------------------------------------------

https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-linux

generate key
::
	ssh-keygen -t rsa -b 4096 -C "dbutton@digitalgizmo.com"

passphrase in 1password

+--[ RSA 4096]----+
|                 |
|     .           |
|    . . .        |
|   . . o o       |
|    o + S        |
|     o O         |
|   o .. o        |
|  + * .o +       |
| .E= oo.o .      |
+-----------------+

add to ssh-agent
::
	eval "$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa

Add to github per github instructionis


changed https:// to ssh:// in .git/config

still probs

test
::
	ssh -T git@github.com

GIT ssh take 2
---------------

The above was done as root. Rather than use ssh I'm going to stick with https
The eApps KB article bleow about setting up a repository server. 
[Using Git - Powered by Kayako Help Desk Software](https://support.eapps.com/index.php?/Knowledgebase/Article/View/457/55/using-git#git-configuration---virtual-server)

GIT runs fine when logged in as pvma user, just have to change to the working directory manually (as opposed to using "workon impressions").

the git conf file is at ...www/data/www/imp../.git/config
Stock has pull and push the same. 
But, in order to push I added user@, requireing password, for pushy
::
	git remote set-url --push origin knowyourider@github.com/knowyourider/imp_project.git

Upgrades
---------

to 1.10
::
	pip install --upgrade pip
	pip install --upgrade django==1.10.7
	pip install --upgrade django==1.11.1

New virtual env -- didn't work
::
	mkvirtualenv -a /Users/don/Sites/imp_project/impressions --python=/usr/local/bin/python3.6 imp36
	mkvirtualenv -a /Users/don/Sites/temp36 --python=/usr/local/bin/python3 temp36

install prev version of django
:: 
	pip uninstall django
	pip install django==1.10.7
