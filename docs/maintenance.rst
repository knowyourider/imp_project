Maintenance
===========

Django
~~~~~~~~~~~~~~~~~

eApps
Working directories e.g. /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org
::
	workon impressions


Both dev.dino and dino use the same database: impdb
Both are on the new eApps server, vm2, but there's a legacy dev on vm1 (I think)

Backup remote and restore local
~~~~~~~~~~~~~~~~~~~~~~~~~~

On eapps, login as root. We're not using the -O option since local and remote have the same user.
::

    cd /var/www/pvma/data/FTP_transfer
	pg_dump -Fc --clean --verbose impdb --user=impdb_user > impdb_$(date +"%Y_%m_%d").backup
    [impdb_user password]
	
    cd /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions (or workon impressions)
Fro the current server, vm2 
::
    cd /var/www/pvma-django/data/FTP_transfer
	pg_dump -Fc --clean --verbose impdb --user=impdb_user > impdb_$(date +"%Y_%m_%d").backup
    [impdb_user password]
	
    cd /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions (or workon impressions)

Or, run script from local which accesses remote:
:: 
	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	ssh root@68.169.58.50 'bash -s' < copy_stagedb.sh
	(remote root password)
or, vor vm2 
hmm, looks like I need to set up remote password
::
	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	ssh root@68.169.61.104 -p 2789 'bash -s' < copy_stage2db.sh
	(remote root password)

Transfer to local via FTP pvma root.
::
	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	(edit remote pvma password into the following, ad hoc)
	wget --user=pvma --password='pvma password by hand' ftp://deerfield-history-center.org/FTP_transfer/impdb_$(date +"%Y_%m_%d").backup
or vm2 ::
	wget --user=pvma-django --password='pvma-django password by hand' ftp://68.169.61.104/FTP_transfer/impdb_$(date +"%Y_%m_%d").backup

In either case:
::
	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	pg_restore --clean --dbname=impdb --user=impdb_user --verbose impdb_$(date +"%Y_%m_%d").backup

Copy devel database to public
~~~~~~~~~~~~~~~~~~~
( to edti , from mse)
Note msedb_ed as the target.
Log into shell as root
::

	su - postgres
	cd /var/www/mseadmin/data/FTP_transfer
	pg_restore --clean --dbname=msedb_ed --user=msedb_user --verbose msedb_$(date +"%Y_%m_%d").backup
	[db password here]


Renew WSGI after code change
~~~~~~~~~~~~~~~~~~~~~~~
::

	touch /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/config/wsgi.py
	touch /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org/impressions/config/wsgi.py
	touch /var/www/pvma-django/data/www/dinotracksdiscovery.org/impressions/config/wsgi.py

Tools
~~~~~~~~~
phpPgAdmin
https://68.169.58.50/pgadmin/
user: postgres
Pass: in 1pass, keychain, and in ISP > Server Settings --> Database Servers


GIT
----

Logon as pvma (or, for vm2, pvma-django)
::
	cd /var/www/pvma/data/www/impdev.deerfield-ma.org
	cd /var/www/pvma-django/data/www/dev.dinotracksdiscovery.org
	git status
	etc.

Then, to collect (since we're alread in as pvma user):
::
	cd ../../
	./collect.sh

To push from server:
::
	git push -u origin develop
	(github password)

AWStats - not enabled
::
	http://dinotracksdiscovery.org/cgi-bin/awstats/awstats.pl
