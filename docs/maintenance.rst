Maintenance
===========

Backup remote and restore local
~~~~~~~~~~~~~~~~~~~~~~~~~~

On eapps, login as root. We're not using the -O option since local and remote have the same user.
::

    cd /var/www/pvma/data/FTP_transfer
	pg_dump -Fc --clean --verbose impdb --user=impdb_user > impdb_$(date +"%Y_%m_%d").backup
    [impdb_user password]
	
    cd /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions (or workon impressions)

Transfer to local via FTP pvma root.
::

	cd ~/Documents/Projects/Impressions/DataBaks/from_remote
	pg_restore --clean --dbname=impdb --user=impdb_user --verbose impdb_$(date +"%Y_%m_%d").backup


Renew WSGI after code change
~~~~~~~~~~~~~~~~~~~~~~~
::

	touch /var/www/pvma/data/www/impdev.deerfield-ma.org/impressions/config/wsgi.py

Tools
~~~~~~~~~
phpPgAdmin
http://68.169.58.50/phppgadmin/
user: postgres
Pass: in 1pass, keychain
