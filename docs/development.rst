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

	UPDATE stories_chapter SET narrative = REPLACE(narrative, '/special/feature/','/special/voices/')
