from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'dist';OUT.mkdir(exist_ok=True)
pages=json.loads((ROOT/'content/pages.json').read_text())
nav='<a class="brand" href="/">Leman FENG<span>冯乐满</span></a><nav aria-label="主导航"><a href="/#work">作品 / Work</a><a href="/visualization/">动图 / Visuals</a><a href="/about/">关于 / About</a><a href="https://github.com/flm8620">GitHub ↗</a></nav>'
def shell(title,body,desc='Leman FENG — embodied intelligence, computer graphics, simulation and selected projects.'):
 return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Leman FENG</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#f5f5ed"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"></head><body><a class="skip" href="#main">跳至内容</a><header>{nav}</header><main id="main">{body}</main><footer><span>© Leman FENG</span><span>Ideas made visible. 想法，化为可见。</span><a href="https://github.com/flm8620">GitHub ↗</a></footer></body></html>'''
def write(route,text):
 p=OUT/route/'index.html';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
projects=[
 ('high-order-mesh','01','Geometry · Research','高阶网格生成','Curved Optimal Delaunay Triangulation','flip_simulation_global.gif','SIGGRAPH 2018 · INRIA × Caltech'),
 ('2d-physics-sandbox','02','Physics · C++','二维物理沙盒','A small world, built from first principles.','angrybird2.gif','刚体动力学 · 碰撞求解'),
 ('ray-tracing','03','Rendering · C++','光线追踪','Following light, one ray at a time.','Day8.3.png','从第一张图到完整渲染'),
 ('calib3dtools-software','04','Vision · Tools','Calib3DTools','Tools for seeing the world in 3D.','calib3.png','IMAGINE 实验室 · 计算机视觉'),
 ('building-modeling','05','Modeling · Interactive','把教学楼搬进游戏','From surveying a building to a playable space.','building1.jpg','测绘 · 三维建模'),
 ('visualization','06','Math · Motion','让数学动起来','An animated collection of mathematical ideas.','joukozsky.gif','线性代数 · 流体 · 几何')]
cards=''
for slug,num,tag,title,sub,img,meta in projects:
 cards+=f'<a class="project" href="/{slug}/"><div class="preview"><img src="/assets/{img}" alt="{title}作品预览" loading="lazy" decoding="async"></div><div class="project-meta"><span>{tag}</span><span>{num} ↗</span></div><h3>{title}</h3><p>{sub}</p><small>{meta}</small></a>'
hero='''<section class="hero"><div><p class="eyebrow"><span class="dot"></span> ENGINEER · RESEARCHER · MAKER</p><h1>从几何，<br>到智能。<em>From geometry<br>to intelligence.</em></h1><p class="intro">我是冯乐满，Leman FENG。<br>关注具身智能、计算机图形学与闭环仿真，<br>让算法走进真实世界。</p><a class="text-link" href="#work">探索我的作品 <span>↓</span></a></div><figure class="hero-art"><img src="/assets/untangling.gif" alt="高阶网格的几何优化与变形过程"><figcaption><span>GEOMETRY IN MOTION</span><span>高阶网格 · SIGGRAPH 2018</span></figcaption></figure></section>'''
body=hero+'<section id="work"><div class="section-heading"><div><p class="eyebrow">SELECTED WORK</p><h2>一些想法，一些作品。</h2></div><p>图形、物理、视觉，以及它们之间的联系。<br>Selected projects & visual experiments.</p></div><div class="projects">'+cards+'</div></section><section class="about-strip"><p class="eyebrow">CURRENT INTERESTS</p><h2>具身智能全栈</h2><p>深度学习 · 强化学习 · 闭环仿真<br>计算机图形学 · 工程机械纯 Sim2Real 落地</p><a class="text-link" href="/about/">关于我 <span>↗</span></a></section>'
write('',shell('从几何，到智能',body))
def clean(content):
 content=re.sub(r'https?://(?:www\.)?lemanfeng\.com/wp-content/uploads/[^"\s<>]+',lambda m:'/assets/'+m[0].split('/')[-1],content)
 content=re.sub(r'https?://(?:www\.)?lemanfeng\.com/(?:index\.php/)?', '/',content)
 content=re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]',r'<figure>\1</figure>',content,flags=re.S)
 content=re.sub(r'\s(?:width|height|class|style)="[^"]*"','',content)
 content=re.sub(r'<img([^>]+)>',r'<img\1 loading="lazy" decoding="async">',content)
 content=re.sub(r'alt=""', 'alt="作品演示"',content)
 chunks=re.split(r'\n\s*\n',content.strip())
 return '\n'.join('<div class="content-block">'+c.replace('\r','').replace('\n','<br>')+'</div>' for c in chunks)
for p in pages:
 if p['slug'] in ('home','works','projects','resume','chinese_resume'):continue
 body='<div class="article-heading"><a class="back" href="/#work">← 全部作品 / All work</a><p class="eyebrow">PROJECT ARCHIVE</p><h1>'+html.escape(p['title'])+'</h1></div><article class="archive">'+clean(p['content'])+'</article><div class="article-end"><a class="text-link" href="/#work">继续探索作品 ↗</a></div>'
 write(p['slug'],shell(p['title'],body))
about='''<div class="article-heading"><a class="back" href="/">← 首页 / Home</a><p class="eyebrow">ABOUT</p><h1>Leman FENG <span>冯乐满</span></h1><p class="lead">具身智能全栈 · 从计算机图形学到真实世界的智能系统。</p></div><article class="about-copy"><h2>研究与工程方向</h2><p>深度学习、强化学习、闭环仿真、计算机图形学，以及工程机械的纯 Sim2Real 落地。</p><h2>一些经历</h2><p>在三一重工 / 树根科技从事 L4 无人叉车 VLA 端到端算法工作。此前的经历包括广州美央创新科技、文远知行与大疆创新。</p><p>在法国国立路桥学校（École des Ponts）学习，曾在 INRIA、Caltech 与 IMAGINE 实验室参与研究与项目。</p><h2>作品与研究</h2><p>这里保留了我在计算机图形学、计算机视觉与物理仿真方面的一些作品，包括高阶德劳内三角化、二维物理沙盒、光线追踪和三维标定工具。</p><a class="text-link" href="https://github.com/flm8620">在 GitHub 查看更多 ↗</a></article>'''
write('about',shell('关于我',about))
for slug in ('resume','chinese_resume'):
 write(slug,shell('关于我',about))
for slug in ('home','works','projects'):
 write(slug,shell('作品集',body if False else '<div class="article-heading"><p class="eyebrow">WORK & EXPERIMENTS</p><h1>作品集</h1></div><div class="projects">'+cards+'</div>'))
# Retain old /index.php/slug paths and WordPress numeric permalinks without a server.
for p in pages:
 dest='/'+p['slug']+'/' if p['slug']!='home' else '/'
 redir=f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={dest}"><title>Moved · Leman FENG</title><a href="{dest}">前往页面</a></html>'
 write('index.php/'+p['slug'],redir)
write('index.php',shell('Leman FENG',hero+'<a class="text-link" href="/">进入主页 ↗</a>'))
(OUT/'404.html').write_text(shell('页面未找到','<div class="article-heading"><p class="eyebrow">404</p><h1>这条路径还没有作品。</h1><p><a class="text-link" href="/">返回首页 ↗</a></p></div>'))
(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#215d50"/><text x="12" y="47" font-family="serif" font-size="45" fill="#f5f5ed">F</text></svg>')
print('Built',len(list(OUT.rglob('*.html'))),'HTML pages')
