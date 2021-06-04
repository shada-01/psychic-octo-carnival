import requests
import bs4
import sys

def song_links(link):

	s_link=[]
	resp=requests.get(link)
	soup=bs4.BeautifulSoup(resp.content,"html.parser")
	lyrics=soup.find_all("a",attrs={"class":"title"})

	for ele in lyrics:
		s_link.append(ele['href'])
	
	return s_link

def song_lyrics(url_song):
	lyr=[]
	res=requests.get(url_song)
	soup=bs4.BeautifulSoup(res.content,"html.parser")
	s_lyr=soup.find_all("p",class_="verse")
	for j in s_lyr:
		lyr.append(j.get_text())
	
	return "\n".join(lyr)

def file_name(url_s):
	return url_s.split("/")[-1].replace("html","txt")


def main():
	url=sys.argv[1]
	links=song_links(url)
	for i in links:
		lyric=song_lyrics(i)
		fname=file_name(i)
		s_name=(fname.replace(".txt"," ")).replace("-"," ") 
		print(f"Downloading {s_name}")
		f=open(fname,"w")
		f.write(lyric)
		f.close()
	
if __name__=="__main__" :
	main()
	
#https://www.metrolyrics.com/grateful-dead-lyrics.html

