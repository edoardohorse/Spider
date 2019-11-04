from spider import launch
import os, progressbar

COLLECTIVE = "https://tympanus.net/codrops/collective"
NEXT_COLLECTIVE = lambda index: f"{COLLECTIVE}/page/{index}" if index >= 2 else COLLECTIVE

def appendToFile(filename, value):
    with open(filename, 'a+') as file:
        for v in value:
            file.write(v+"\n")

if __name__ == "__main__":
    CSS_SELECTOR = ".ct-archive-container > article > h2 > a"

    progressbar.ProgressBar()
    
    for i in progressbar.progressbar(range(1,25)):
        res = launch(link=NEXT_COLLECTIVE(i),  cssSelector=CSS_SELECTOR, prop='href')
        appendToFile(filename="linksCollective.txt",value=res)