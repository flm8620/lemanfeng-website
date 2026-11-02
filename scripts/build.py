from pathlib import Path
import json,re,html,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'dist';OUT.mkdir(exist_ok=True)
pages=json.loads((ROOT/'content/pages.json').read_text())
asset_version=hashlib.sha256((OUT/'style.css').read_bytes()).hexdigest()[:12]
script_version=hashlib.sha256((OUT/'slideshow.js').read_bytes()).hexdigest()[:12]
pdf_version=hashlib.sha256((OUT/'CV_Leman_FENG_2026_CN.pdf').read_bytes()).hexdigest()[:12]
nav='<a class="brand" href="/">Leman FENG<span>冯乐满</span></a><nav aria-label="主导航"><a href="/#cv">个人 CV</a><a href="/#work">作品 / Work</a><a href="/#visualization">动图 / Visuals</a><a href="https://github.com/flm8620">GitHub ↗</a></nav>'
def shell(title,body,desc='Leman FENG — embodied intelligence, computer graphics, simulation and selected projects.'):
 body=body.replace('href="/CV_Leman_FENG_2026_CN.pdf"',f'href="/CV_Leman_FENG_2026_CN.pdf?v={pdf_version}"')
 return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Leman FENG</title><meta name="description" content="{html.escape(desc)}"><meta name="theme-color" content="#f5f5ed"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css?v={asset_version}"><script src="/slideshow.js?v={script_version}" defer></script></head><body><a class="skip" href="#main">跳至内容</a><header>{nav}</header><main id="main">{body}</main><footer><span>© Leman FENG</span><span>Ideas made visible. 想法，化为可见。</span><a href="https://github.com/flm8620">GitHub ↗</a></footer></body></html>'''
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
 write(slug,shell('作品集','<div class="article-heading"><p class="eyebrow">WORK & EXPERIMENTS</p><h1>作品集</h1></div><div class="projects">'+cards+'</div>'))
# Retain old /index.php/slug paths and WordPress numeric permalinks without a server.
for p in pages:
 dest='/'+p['slug']+'/' if p['slug']!='home' else '/'
 redir=f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={dest}"><title>Moved · Leman FENG</title><a href="{dest}">前往页面</a></html>'
 write('index.php/'+p['slug'],redir)
write('index.php',shell('Leman FENG',hero+'<a class="text-link" href="/">进入主页 ↗</a>'))
(OUT/'404.html').write_text(shell('页面未找到','<div class="article-heading"><p class="eyebrow">404</p><h1>这条路径还没有作品。</h1><p><a class="text-link" href="/">返回首页 ↗</a></p></div>'))
(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#215d50"/><text x="12" y="47" font-family="serif" font-size="45" fill="#f5f5ed">F</text></svg>')
print('Built',len(list(OUT.rglob('*.html'))),'HTML pages')

# A complete, single-page portfolio. Standalone legacy project pages remain available.
def carousel(content):
    slides=[]
    for image,caption in re.findall(r'\[caption[^\]]*\](<img[^>]+>)\s*(.*?)\[/caption\]',content,re.S):
        src=re.search(r'src="([^"]+)"',image)[1]
        # Prefer the full image when the WordPress caption used a thumbnail.
        name=re.sub(r'-\d+x\d+(?=\.[^.]+$)','',src.split('/')[-1])
        if not (OUT/'assets'/name).exists():name=src.split('/')[-1]
        label=html.escape(re.sub('<[^>]+>','',caption).strip())
        slides.append((name,label))
    frames=''.join(f'<figure class="slide" {"hidden" if i else ""}><img src="/assets/{name}" alt="光线追踪渲染进展 {label}" loading="lazy" decoding="async"><figcaption>{label}</figcaption></figure>' for i,(name,label) in enumerate(slides))
    dots=''.join(f'<button type="button" data-slide="{i}" aria-label="查看 {label}" aria-pressed="{str(i==0).lower()}"></button>' for i,(_,label) in enumerate(slides))
    return f'<div class="slideshow" role="region" aria-roledescription="carousel" aria-label="光线追踪开发进展" tabindex="0">{frames}<div class="slide-controls"><div><button type="button" data-prev aria-label="上一张">←</button><button type="button" data-next aria-label="下一张">→</button><span class="slide-count" aria-live="polite">1 / {len(slides)}</span></div><div class="slide-dots">{dots}</div><button type="button" data-play aria-label="暂停自动播放">暂停 ⏸</button></div></div>'

def codt_media():
    return '<div class="inline-gallery codt-media"><figure><video controls autoplay muted loop playsinline preload="metadata" poster="/assets/codt-3d-bimba-poster.jpg" aria-label="三维人头像高阶网格生成演示"><source src="/assets/codt-3d-bimba.mp4" type="video/mp4">您的浏览器不支持内嵌视频。<a href="/assets/codt-3d-bimba.mp4">下载演示视频</a></video><figcaption>三维高阶网格 · The Making of Bimba</figcaption></figure><figure><img src="/assets/untangling.gif" alt="二维高阶网格解缠与优化动画" loading="lazy" decoding="async"><figcaption>二维高阶网格 · Untangling</figcaption></figure></div>'

def inline_project(p,preview=False):
    content=p['content']
    if p['slug']=='high-order-mesh' and preview:
        return '<div class="project-description"><p>SIGGRAPH 2018 · <a href="https://dl.acm.org/doi/10.1145/3197517.3201358">Curved Optimal Delaunay Triangulation</a> · Leman FENG et al.</p><p>INRIA × Caltech · 高阶网格的几何与拓扑优化</p></div>'+codt_media()
    if p['slug']=='ray-tracing':
        intro=content.split('[caption')[0]
        return '<div class="project-description">'+clean(intro)+'</div>'+carousel(content)
    if p['slug']=='visualization':
        blocks=re.split(r'\n\s*\n',content.strip())
        if preview: content='\n\n'.join(blocks[:4])
        return '<div class="inline-gallery math-gallery">'+clean(content)+'</div>'
    image_tags=re.findall(r'<img[^>]+>',content)
    if preview: image_tags=image_tags[:2]
    description=re.sub(r'<img[^>]+>','',content)
    if preview: description=description.replace("How it's made:",'')
    images=''.join('<figure>'+clean(tag)+'</figure>' for tag in image_tags)
    if p['slug']=='building-modeling' and not preview:
        description=description.replace("How it's made:",'')
        main_images=''.join('<figure>'+clean(tag)+'</figure>' for tag in image_tags[:8])
        process_images=''.join('<figure>'+clean(tag)+'</figure>' for tag in image_tags[8:])
        return '<div class="project-description">'+clean(description)+'</div><div class="inline-gallery">'+main_images+'</div><h4 class="process-title">制作过程 / How it’s made</h4><div class="inline-gallery">'+process_images+'</div>'
    return '<div class="project-description">'+clean(description)+'</div><div class="inline-gallery">'+images+'</div>'

page_by_slug={p['slug']:p for p in pages}
all_projects=''
for slug,num,tag,title,sub,img,meta in projects:
    p=page_by_slug[slug]
    all_projects+=f'<section class="inline-project" id="{slug}"><div class="inline-heading"><p class="eyebrow">{num} / {tag}</p><h3>{title}</h3><p>{sub}</p></div>'+inline_project(p,preview=True)+f'<a class="text-link" href="/{slug}/">查看完整项目 ↗</a></section>'
project_nav='<nav class="project-index" aria-label="项目目录">'+''.join(f'<a href="#{slug}">{title} ↘</a>' for slug,_,_,title,*_ in projects)+'</nav>'
cv=(ROOT/'content/cv.html').read_text()
cv_intro='<section id="cv" class="cv-intro"><div><p class="eyebrow">CURRENT INTERESTS & CV · 02</p><h2>具身智能全栈</h2><p>深度学习 · 强化学习 · 闭环仿真<br>计算机图形学 · 工程机械纯 Sim2Real 落地</p></div><div class="cv-intro-links"><a class="text-link" href="/cv/">查看网页版 CV ↗</a><a class="text-link secondary" href="/CV_Leman_FENG_2026_CN.pdf" download>下载 PDF 简历 ↓</a><small>Leman FENG / 冯乐满 · 中文详细版</small></div></section>'
home_body=hero+cv_intro+'<section id="work"><div class="section-heading"><div><p class="eyebrow">SELECTED WORK · 03</p><h2>一些想法，一些作品。</h2></div><p>精选预览，点击查看完整项目。<br>Graphics, physics & visual experiments.</p></div>'+project_nav+all_projects+'</section>'
write('',shell('从几何，到智能',home_body))
for slug in ('cv','about','resume','chinese_resume'):
    write(slug,shell('个人 CV','<div class="cv-back"><a class="back" href="/">← 首页 / Home</a></div>'+cv))
ray=page_by_slug['ray-tracing']
write('ray-tracing',shell(ray['title'],'<div class="article-heading"><a class="back" href="/#ray-tracing">← 返回首页作品</a><p class="eyebrow">RENDERING · C++</p><h1>Ray-tracing 光线追踪</h1></div>'+inline_project(ray)))

mesh=page_by_slug['high-order-mesh']
write('high-order-mesh',shell(mesh['title'],'<div class="article-heading"><a class="back" href="/#high-order-mesh">← 返回首页作品</a><p class="eyebrow">GEOMETRY · RESEARCH</p><h1>High-order Mesh 高阶网格生成</h1></div>'+codt_media()+'<article class="archive">'+clean(mesh['content'])+'</article>'))
