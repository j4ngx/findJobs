import requests
from bs4 import BeautifulSoup

url = "https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=python"

if "__main__" == __name__:
    page = requests.get(url)
    soup=BeautifulSoup(page.content,"html.parser")

    results=soup.find_all('li',attrs={'class':'ij-ListItem'})

    for job in results:
        try:
            title = job.find("a",attrs={"class":"ij-OfferCardContent-description-title-link"}).get_text()
            company = job.find("a",attrs={"class":"ij-OfferCardContent-description-subtitle-link"}).get_text()
            joblink = job.find("a", attrs={"class":"ij-OfferCardContent-description-title-link"})["href"]
            salary = job.find("span",attrs={"class":"ij-OfferCardContent-description-salary-info"})
            salary = salary.get_text() if salary else 'n/a'

            job="Titulo:{}\nEmpresa:{}\nSalario:{}\nLink:{}a\n"
            job=job.format(title,company,salary,joblink)
            print(job)
        
        except Exception as e:
            print("Exception:{}".format(e)) 
            pass
