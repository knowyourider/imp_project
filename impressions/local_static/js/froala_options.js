// option settings for Froala

var froalaBasic = {
	heightMin: 200,
	htmlAllowedTags: ['a', 'article', 'aside', 'blockquote', 'br', 'caption', 
		'cite', 'dd', 'details', 'div', 'dl', 'dt', 'em', 'figure', 'footer', 
		'h1', 'h2', 'h3', 'h4', 'h5', 'header', 'label', 'li', 'link', 
		'main', 'ol', 'option', 'p', 'section', 'span', 'strong', 'sub', 
		'summary', 'sup', 'title', 'ul'],
	linkAutoPrefix: '',
	linkList: [
		{
			displayText: 'Froala',
			href: 'https://froala.com',
			target: '_blank'
		},
		{
			displayText: 'evidence',
			href: '/evidence/(evidence-shortname)/',
		}
	],
	linkStyles: {
		pop_item: 'slimpop',
		new_page: 'new page'
	},
	paragraphFormat: {
		N: 'Normal',
		H1: 'Heading 1',
		H2: 'Heading 2',
		ARTICLE: 'article element',
		DETAILS: 'read more'
	},
	pastePlain: true,
	toolbarButtons: ['fullscreen', 'italic', 'superscript', '|', 'paragraphStyle', 
		'|', 'paragraphFormat', 'formatOL', 'formatUL',  'quote', 'insertLink', 
		'-', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}

var froalaImage = {
	heightMin: 200,
	htmlAllowedTags: ['a', 'article', 'aside', 'blockquote', 'br', 'caption', 
		'cite', 'dd', 'details', 'div', 'dl', 'dt', 'em', 'figure', 'footer', 
		'h1', 'h2', 'h3', 'h4', 'h5', 'header', 'img', 'label', 'li', 'link', 
		'main', 'ol', 'option', 'p', 'section', 'span', 'strong', 'sub', 
		'summary', 'sup', 'title', 'ul'],
	linkAutoPrefix: '',
	linkList: [
		{
			text: 'Google',
			href: 'http://google.com',
			target: '_blank',
			rel: 'nofollow'
		},
		{
			displayText: 'Froala',
			href: 'https://froala.com',
			target: '_blank'
		},
		{
			displayText: 'evidence',
			href: '/evidence/(evidence-shortname)/',
		}
	],
	linkStyles: {
		pop_item: 'slimpop',
		new_page: 'new page'
	},
	paragraphFormat: {
		N: 'Normal',
		H1: 'Heading 1',
		H2: 'Heading 2',
		ARTICLE: 'article element',
		DETAILS: 'read more'
	},
	pastePlain: true,
	toolbarButtons: ['fullscreen', 'italic', 'superscript', '|', 'paragraphStyle', 
		'|', 'paragraphFormat', 'formatOL', 'formatUL',  'quote', 'insertLink', 
		'insertImage', '-', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'],
	width: '800'
}
