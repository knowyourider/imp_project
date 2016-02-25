// option settings for Froala

var froalaChapter = {
	heightMin: 200,
	linkAutoPrefix: '',
	linkList: [
		{
			displayText: 'evidence',
			href: '/evidence/SHORTNAME/'
		},
		{
			displayText: 'person',
			href: '/people/SHORTNAME/'
		},
		{
			displayText: 'context',
			href: '/context/SHORTNAME/'
		}
	],
	linkStyles: {
		pop_item: 'slimpop'
	},
	paragraphFormat: {
		N: 'Normal',
		DETAILS: 'read more'
	},
	pastePlain: true,
	toolbarButtons: ['fullscreen', 'italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote', 'insertLink', 
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaSlim = {
	heightMin: 200,
	paragraphFormat: {
		N: 'Normal',
		H2: 'Subheading - h2'
	},
	pastePlain: true,
	toolbarButtons: ['fullscreen', 'italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote',  
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaIntro = {
	heightMin: 200,
	pastePlain: true,
	toolbarButtons: ['fullscreen', 'italic', 'quote',
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaBlurb = {
	heightMin: 100,
	pastePlain: true,
	placeholderText: 'Single (short) paragraph only.',
	toolbarButtons: ['fullscreen', 'italic', '|', 
		'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '400'
}
