Transitionoal issues during development
========================================

Changing url path for Special Features
---------------------------------------

::
	UPDATE your_table SET your_field = REPLACE(your_field, 'cat','dog')

	UPDATE stories_chapter SET narrative = REPLACE(narrative, '/supporting/special/','/special/feature/')

	SELECT * from stories_chapter WHERE narrative LIKE '%/supporting/special/%'

	SELECT * from stories_chapter WHERE narrative LIKE '%/special/feature/%'
	SELECT * from stories_chapter WHERE narrative LIKE '%/supporting/%'
	SELECT * from stories_chapter WHERE narrative LIKE '%orra-pilgrimage-1%'

	UPDATE stories_chapter SET narrative = REPLACE(narrative, '/supporting/special/','/special/feature/')


phase 2
::

	SELECT * from stories_chapter WHERE narrative LIKE '%/special/feature/%'

	UPDATE stories_chapter SET narrative = REPLACE(narrative, '/special/feature/','/special/voices/')

	SELECT * from stories_chapter WHERE narrative LIKE '%/special/voices/%'

Set voices to not on menu
::
	SELECT * from special_feature WHERE special_type = 'voices'
	SELECT * from special_feature WHERE is_on_menu = FALSE

	UPDATE special_feature SET is_on_menu = FALSE WHERE special_type = 'voices'

Multiple databases
--------------------

Migrate is separate
::
	./manage.py migrate --database=imp_voting
