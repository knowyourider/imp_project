// option settings for Froala

var froalaChapter = {
	heightMin: 200,
	linkAutoPrefix: '',
	linkList: [
		{
			displayText: 'evidence',
			href: '/supporting/evidenceitem/'
		},
		{
			displayText: 'person',
			href: '/supporting/person/'
		},
		{
			displayText: 'context',
			href: '/supporting/context/'
		},
		{
			displayText: 'fast fact',
			href: '/supporting/fastfact/'
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
	toolbarButtons: ['italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote', 'insertLink', 
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsMD: ['italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote', 'insertLink', 
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsSM: ['italic', 'superscript',  
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
	toolbarButtons: ['italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote',  
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsMD: ['italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote',  
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsSM: ['italic', 'superscript',  
		'paragraphFormat', 'formatOL', 'quote',  
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaIntro = {
	heightMin: 200,
	pastePlain: true,
	toolbarButtons: ['italic', 'quote',
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsMD: ['italic', 'quote',
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	toolbarButtonsSM: ['italic', 'quote',
		'|', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaBlurb = {
	heightMin: 100,
	pastePlain: true,
	placeholderText: 'Single (short) paragraph only.',
	toolbarButtons: ['italic', '|', 'undo', 'redo', 'clearFormatting', 
		'selectAll', 'html'],
	toolbarButtonsMD: ['italic', '|', 'undo', 'redo', 'clearFormatting', 
		'selectAll', 'html'],
	toolbarButtonsSM: ['italic', '|', 'undo', 'redo', 'clearFormatting', 
		'selectAll', 'html'],
	width: '400'
}
