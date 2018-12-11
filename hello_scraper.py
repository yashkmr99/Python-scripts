from bs4 import BeautifulSoup
import requests
import re

def get_currentaffairs(month,num):
	url = "https://currentaffairs.gktoday.in/month/current-affairs-"+str(month)+"-2018/page/"+str(num);
	response = requests.get(url);
	soup = BeautifulSoup(response.content,'html.parser')

	# scrapdiv = open('scrapdiv.txt','w')

	data = soup.findAll("div",{"class":"post-content"})

	for div in data:
		links = div.findAll('a')[0]	
		result = re.sub(r"http\S+", "", str(links))
		print(result)
		#print (links.text.strip(), '=>', links.attrs['href'])
		# scrapdiv.write(str(data))
		# scrapdiv.write("\n\n")


def main():

	months = ['september','october','november','december']
	for month in months:
		print(str(month))
		for i in range(1,50):
			get_currentaffairs(month,i);

if __name__ == '__main__':
	main()