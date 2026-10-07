"""Extract editorial page semantics for a native CoreText vector PDF fallback."""
from html.parser import HTMLParser
from html import unescape
import pathlib,re,json
R=pathlib.Path(__file__).resolve().parents[1]
class N:
 def __init__(self,tag='',attrs=()):self.tag=tag;self.attrs=dict(attrs);self.children=[]
 def text(self):
  if self.tag=='br':return '\n'
  return re.sub(r'\n+', '\n', ''.join(c.text() if isinstance(c,N) else c for c in self.children)).strip()
 def find(self,tag):
  for c in self.children:
   if isinstance(c,N):
    if c.tag==tag:return c
    r=c.find(tag)
    if r:return r
 def all(self,tag):
  out=[]
  for c in self.children:
   if isinstance(c,N):
    if c.tag==tag:out.append(c)
    out.extend(c.all(tag))
  return out
 def cls(self,v):return v in self.attrs.get('class','').split()
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.root=N();self.stack=[self.root]
 def handle_starttag(self,t,a):
  n=N(t,a);self.stack[-1].children.append(n)
  if t=='br':n.children.append('\n')
  if t not in ['br','img','input','meta','link','hr']:self.stack.append(n)
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==t:self.stack=self.stack[:i];break
 def handle_data(self,d):self.stack[-1].children.append(d)
def blocks(n):
 out=[]
 for c in n.children:
  if not isinstance(c,N):continue
  if c.tag in ['h2','table','img'] or c.cls('kicker') or c.cls('folio'):continue
  if c.tag in ['p','h3'] or c.cls('note') or c.cls('check'):
   t=c.text()
   if t:out.append(dict(kind='heading' if c.tag=='h3' else 'note' if c.cls('note') else 'body',text=t))
  else:out+=blocks(c)
 return out
book=(R/'book/index.html').read_text();pages=[]
for cls,num,chunk in re.findall(r'<section class="page ([^"]*)" id="p(\d+)">(.*?)</section>',book,re.S):
 p=Parser();p.feed(chunk);n=p.root;title=n.find('h2').text();kicker=next((c.text() for c in n.children if isinstance(c,N) and c.cls('kicker')),'22NFT');page=dict(number=int(num),title=title,kicker=kicker)
 if int(num)==1:
  page.update(type='cover',image=str(R/'renders/01.jpg'),lede=n.find('p').text())
 elif int(num)==3:
  page.update(type='image',image=str(R/'renders/05-annotated.jpg'),caption='The interactive HTML edition embeds the full GLB model and Three.js viewer: orbit, zoom, pan and shell/power/solar/laundry A/laundry B/interior toggles. This print edition carries the annotated power view.')
 elif 'render' in cls:
  image=n.find('img').attrs['src'];page.update(type='image',image=str((R/'book'/image).resolve()),caption=n.find('p').text())
 elif n.find('table'):
  table=n.find('table');rows=[]
  for tr in table.all('tr'):
   cells=[]
   for c in tr.children:
    if isinstance(c,N) and c.tag in ['td','th']:cells.append(dict(text=c.text(),span=int(c.attrs.get('colspan','1')),url=c.find('a').attrs.get('href') if c.find('a') else None))
   rows.append(cells)
  page.update(type='table',rows=rows,blocks=blocks(n))
 else:
  grid=next((c for c in n.children if isinstance(c,N) and (c.cls('grid') or c.cls('checks'))),None)
  if grid:
   children=[c for c in grid.children if isinstance(c,N)]
   if grid.cls('checks'):
    half=(len(children)+1)//2;cols=[[dict(kind='body',text='□ '+c.text()) for c in children[:half]],[dict(kind='body',text='□ '+c.text()) for c in children[half:]]]
   else:cols=[blocks(c) for c in children]
   # Metrics outside grid are retained as a compact leading block.
   metrics=next((c for c in n.children if isinstance(c,N) and c.cls('metrics')),None)
   page.update(type='columns',columns=cols,summary='  |  '.join(' / '.join(d.text() for d in c.children if isinstance(d,N)) for c in metrics.children if isinstance(c,N)) if metrics else '')
  else:page.update(type='text',blocks=blocks(n))
 pages.append(page)
(R/'docs/pdf-layout.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
print('LAYOUT',len(pages),'pages')
