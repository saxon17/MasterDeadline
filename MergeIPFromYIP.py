import pickle
import pprint 
import pandas as pd

DASH = open('F:\youtube_proj\yip\DASH.yip', 'rb')
iphone4g = open('F:\youtube_proj\yip\iphone4g.yip', 'rb')
iphoneweb =  open('F:\youtube_proj\yip\iphoneweb-safari.yip', 'rb')
sanchr = open('F:\youtube_proj\yip\sanchr.yip', 'rb')
sanzidai = open('F:\youtube_proj\yip\sanzidai.yip', 'rb')
p7app = open('F:\youtube_proj\DataPCap\p7app.yip', 'rb')
p7chrome = open('F:\youtube_proj\DataPCap\p7chrome.yip', 'rb')
p7selfweb = open('F:\youtube_proj\DataPCap\p7selfweb.yip', 'rb')

app = pickle.load(p7app)
chrome = pickle.load(p7chrome)
web = pickle.load(p7selfweb)


das = pickle.load(DASH)
i4g = pickle.load(iphone4g)
iweb = pickle.load(iphoneweb)
sanchr = pickle.load(sanchr)
sanzidai = pickle.load(sanzidai)

pklst = [das,i4g,iweb,sanchr,sanzidai,app,chrome,web]
FinalIPSET  = {}
for ipdict in pklst:
      FinalIPSET.update(ipdict)

# pprint.pprint(FinalIPSET)

s = pd.Series(FinalIPSET, name = 'Youtube Server Name')
s.index.name = 'YoutubeIP'
s = s.reset_index()
s = s.sort(columns='YoutubeIP')
s.to_excel('Hole.xls')



