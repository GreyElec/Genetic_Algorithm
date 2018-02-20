from html.parser import  HTMLParser

class Myhtmlparser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print(tag)
		for ele in attrs:
			print('->',ele[0],'>',ele[1])

parser = Myhtmlparser()
parser.feed('<head><title>HTML</title></head><object type="application/x-flash"data="your-file.swf"width="0" height="0"><!-- <param name="movie" value="your-file.swf" /> --><param name="quality" value="high"/></object>')