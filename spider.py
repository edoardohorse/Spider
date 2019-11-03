from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as soup
import urllib.request, sys, replit

LOG = lambda toPrint: print(f"*** {toPrint} ***")

def getProperty(htmlElement, prop):
    try:
        value = getattr(htmlElement, prop)
        if value is None:
            value = htmlElement.attrs[prop]
        elif value is '':
            LOG("Empty property")
    except KeyError:
        LOG("Property not exists")
        return None

    return value

def connect(link):
    try:
        req = urllib.request.Request(
            link, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        page = urllib.request.urlopen(req)
        
        
    except (UnicodeEncodeError, URLError):
        LOG(f"Failed: {link}")
        return False

    page= urllib.request.urlopen(link)

    return soup(page, "html.parser",from_encoding="utf-8")

def inputIfArgNotExist(index, text, default = None):
    try:
        if sys.argv[index]:
            return sys.argv[index] 
    except IndexError:
        strInput = input(f"{text}: ")

        if strInput == '':
            if default is None:
                while strInput == '':
                    strInput = input(f"{text}: ")
                return strInput
            else:
                return default
        return strInput


def launch(link, cssSelector, prop):
    page = connect(link)
    el = page.select(cssSelector)

    if prop == 'textContent':
        prop = 'text'
        print("***For bf4 textContent is text. Replaced with text***")

    if len(el) == 1:
        return getProperty(el[0],prop)
    
    res = []
    for i in el:
        r = getProperty(i, prop)
        if r is not None:
            res.append(r)

    return res

def main():

    # , default="https://google.it"
    # ,default='title'
    link        = inputIfArgNotExist(1, "Insert link")
    cssSelector = inputIfArgNotExist(2, "Insert the css Selector")
    prop        = inputIfArgNotExist(3, "Insert the property to visualize (default textContent)", default='text')# text == textContent 

    DEFAULT_PRINT = lambda e,f: f.format(e) if '{0}' in f else f+" {0}".format(e)
    stringFormatted = inputIfArgNotExist(4, "Format of print (default '{0}')", default='{0}')
    
    res = launch(link, cssSelector, prop)
    nRes = len(res)
    print("\n")
    # print(f"\nFound {nRes} item{'s' if nRes > 1 else ''}\n")
    if type(res) is list:
        [print(DEFAULT_PRINT(r.strip(), stringFormatted)) for r in res] 
    else:
        print(DEFAULT_PRINT(res.strip(), stringFormatted))



if __name__ == '__main__':
    
    main()

    while input("\nNew request? (Y = Enter/N = Any)") == '':
        replit.clear()
        main()
   