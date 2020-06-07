import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

output = {}
source_url = sys.argv[1]
output_filename = sys.argv[2]

webpage = urlopen(source_url)
soup = BeautifulSoup(webpage, "lxml")

# temp = soup.find("meta", property="og:url")
# output["og:url"] = temp["content"] if temp else ""

temp = soup.find("meta", property="og:type")
output["og:type"] = temp["content"] if temp else ""

temp = soup.find("meta", property="og:title")
output["og:title"] = temp["content"] if temp else ""

temp = soup.find("meta", property="og:image")
output["og:image"] = temp["content"] if temp else ""

temp = soup.find("meta", property="og:description")
output["og:description"] = temp["content"] if temp else ""

temp = soup.find("meta", property="og:site_name")
output["og:site_name"] = temp["content"] if temp else ""

output_meta = ""
for key, value in output.items():
	if value:
		output_meta += '<meta property="' + key + '" content="' + value + '">\n'
	
# print(output_meta)

output_html = ''
with open('./index-template.html', 'r', encoding="utf-8") as f:
	template = f.read()
	template = template.replace('{url}', source_url)
	output_html = template.replace('{meta data}', output_meta)
	
	
with open('./docs/redirect/' + output_filename, 'w', encoding="utf-8") as f:
	f.write(output_html)
	
print('mission complete')
