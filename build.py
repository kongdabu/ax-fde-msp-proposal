#!/usr/bin/env python3
# proposal.md → 자체 완결형 index.html 생성 빌더
# pandoc로 만든 본문 HTML 조각을 템플릿에 내장한다(런타임 fetch 없음).
import subprocess, re, sys, pathlib

SRC = "proposal.md"
OUT = "index.html"

# 1) pandoc로 본문 조각 생성 (GFM, 헤딩 id 포함)
frag = subprocess.run(
    ["pandoc", SRC, "--from", "gfm", "--to", "html5", "--syntax-highlighting=none"],
    capture_output=True, text=True, check=True,
).stdout

# 2) 맨 앞 중복 제목(h1)·부제(h3)·정의 blockquote는 히어로와 겹치므로 제거
frag = re.sub(r'<h1[^>]*>.*?</h1>', '', frag, count=1, flags=re.S)

TEMPLATE = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>AX FDE 사업 추진안 (v2.0) — 한국 MSP 운영 내재화형 FDE</title>
<meta name="description" content="한국 MSP 시장 운영 내재화형 AX FDE 조직·사업 추진안. 약 50명·Squad(4~7명)·6~8주 타임박스. 전략·조직·프로세스·툴·역량 5개 축 통합." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<style>
:root{
  --bg:#0e1726;--surface:#fff;--surface-2:#f4f7fb;--ink:#1a2233;--ink-soft:#5a6678;
  --line:#e3e9f2;--brand:#2563eb;--brand-deep:#1d4ed8;--accent:#06b6d4;--gold:#f59e0b;
  --good:#16a34a;--danger:#dc2626;--radius:14px;--shadow:0 8px 30px rgba(16,32,64,.08);
  --shadow-sm:0 2px 10px rgba(16,32,64,.06);--sidebar-w:288px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:"Noto Sans KR",system-ui,-apple-system,sans-serif;color:var(--ink);
  background:var(--surface-2);line-height:1.75;-webkit-font-smoothing:antialiased}
code,pre,.mono{font-family:"JetBrains Mono",ui-monospace,monospace}

/* Hero */
.hero{background:
  radial-gradient(1200px 500px at 80% -10%,rgba(6,182,212,.25),transparent 60%),
  radial-gradient(900px 500px at 0% 0%,rgba(37,99,235,.35),transparent 55%),
  linear-gradient(135deg,#0e1726 0%,#14213a 60%,#1b2c52 100%);
  color:#eaf1ff;padding:74px 24px 64px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;inset:0;
  background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:44px 44px;
  -webkit-mask-image:radial-gradient(700px 400px at 70% 0%,#000,transparent 75%);
  mask-image:radial-gradient(700px 400px at 70% 0%,#000,transparent 75%);pointer-events:none}
.hero-inner{max-width:1080px;margin:0 auto;position:relative;z-index:1}
.tag{display:inline-block;font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#8fd4ff;
  background:rgba(6,182,212,.12);border:1px solid rgba(6,182,212,.35);padding:6px 14px;border-radius:999px;text-transform:uppercase}
.hero h1{font-size:clamp(28px,5vw,46px);font-weight:900;line-height:1.25;margin:20px 0 12px;letter-spacing:-.02em}
.hero h1 .hl{color:#5ec6ff}
.hero p.lead{font-size:clamp(15px,2.2vw,18px);color:#b9c8e6;max-width:780px;margin:0 0 28px;font-weight:300}
.hero-meta{display:flex;flex-wrap:wrap;gap:10px 22px;font-size:13.5px;color:#9fb2d6}
.hero-meta b{color:#dfe9ff;font-weight:500}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:36px}
.kpi{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:16px 18px;backdrop-filter:blur(6px)}
.kpi .v{font-size:clamp(20px,3vw,28px);font-weight:800;color:#fff}
.kpi .v small{font-size:13px;font-weight:500;color:#9fd}
.kpi .l{font-size:12.5px;color:#aebfe0;margin-top:4px}

/* Layout */
.shell{max-width:1300px;margin:0 auto;display:flex;gap:28px;padding:0 24px}
.sidebar{width:var(--sidebar-w);flex:0 0 var(--sidebar-w);position:sticky;top:0;align-self:flex-start;
  height:100vh;overflow-y:auto;padding:28px 0 40px}
.sidebar h4{font-size:12px;letter-spacing:.12em;color:var(--ink-soft);text-transform:uppercase;margin:22px 8px 8px}
.toc a{display:block;padding:8px 14px;margin:2px 0;border-radius:9px;text-decoration:none;color:var(--ink-soft);
  font-size:14px;border-left:3px solid transparent;transition:all .15s}
.toc a:hover{background:#fff;color:var(--ink)}
.toc a.active{background:#fff;color:var(--brand-deep);border-left-color:var(--brand);font-weight:700;box-shadow:var(--shadow-sm)}
.toc a .num{display:inline-block;width:24px;color:var(--brand);font-weight:700}
main{flex:1 1 auto;min-width:0;padding:36px 0 80px}
#content{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:clamp(22px,4vw,52px)}

/* Content */
#content>h2:first-child{margin-top:6px}
#content h2{font-size:23px;font-weight:800;margin:56px 0 18px;padding-bottom:12px;border-bottom:2px solid var(--line);
  scroll-margin-top:20px;color:var(--ink);position:relative}
#content h2::before{content:"";position:absolute;left:-52px;top:4px;bottom:14px;width:5px;
  background:linear-gradient(var(--brand),var(--accent));border-radius:3px}
#content h3{font-size:18px;font-weight:700;margin:30px 0 12px;color:var(--brand-deep)}
#content p{margin:12px 0}
#content ul,#content ol{margin:12px 0;padding-left:22px}
#content li{margin:6px 0}
#content strong{color:var(--ink);font-weight:700}
#content a{color:var(--brand)}
#content blockquote{margin:18px 0;padding:14px 20px;background:linear-gradient(135deg,#eef4ff,#f0fbff);
  border-left:4px solid var(--brand);border-radius:0 10px 10px 0;color:#2c3a52}
#content blockquote strong{color:var(--brand-deep)}
#content hr{border:none;border-top:1px dashed var(--line);margin:40px 0}
.tbl-wrap{overflow-x:auto;margin:18px 0;border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow-sm)}
#content table{border-collapse:collapse;width:100%;font-size:14px;min-width:540px}
#content thead th{background:linear-gradient(135deg,#1e2f54,#25406f);color:#eaf1ff;font-weight:600;text-align:left;
  padding:12px 14px;font-size:13.5px}
#content tbody td{padding:11px 14px;border-top:1px solid var(--line);vertical-align:top}
#content tbody tr:nth-child(even){background:var(--surface-2)}
#content tbody tr:hover{background:#eef4ff}
#content td strong{color:var(--brand-deep)}
#content pre{background:#0e1726;color:#cfe0ff;padding:18px 20px;border-radius:12px;overflow-x:auto;
  font-size:13px;line-height:1.55;border:1px solid #1f3a63}
#content :not(pre)>code{background:#eef2f9;color:#1d4ed8;padding:1px 7px;border-radius:6px;font-size:13px}

.navbar{display:none}
.backtop{position:fixed;right:22px;bottom:22px;width:46px;height:46px;border-radius:50%;background:var(--brand);
  color:#fff;border:none;font-size:20px;cursor:pointer;box-shadow:var(--shadow);opacity:0;pointer-events:none;
  transition:opacity .25s;z-index:50}
.backtop.show{opacity:1;pointer-events:auto}
footer{text-align:center;color:var(--ink-soft);font-size:13px;padding:30px 24px 50px}

@media (max-width:980px){
  .kpis{grid-template-columns:repeat(2,1fr)}
  .navbar{display:flex;align-items:center;justify-content:space-between;gap:12px;position:sticky;top:0;z-index:40;
    background:rgba(255,255,255,.92);backdrop-filter:blur(8px);padding:12px 18px;border-bottom:1px solid var(--line)}
  .navbar b{font-size:14px}
  .menu-btn{background:var(--brand);color:#fff;border:none;border-radius:9px;padding:8px 14px;font-size:14px;font-weight:600;cursor:pointer}
  .shell{display:block;padding:0 14px}
  .sidebar{position:fixed;left:0;top:0;height:100vh;width:84%;max-width:320px;z-index:60;background:var(--surface-2);
    transform:translateX(-105%);transition:transform .25s;box-shadow:var(--shadow);padding:24px 14px}
  .sidebar.open{transform:translateX(0)}
  .scrim{position:fixed;inset:0;background:rgba(8,15,30,.5);z-index:55;opacity:0;pointer-events:none;transition:opacity .25s}
  .scrim.show{opacity:1;pointer-events:auto}
  main{padding:18px 0 60px}
  #content h2::before{display:none}
  #content{padding:20px}
}
@media (max-width:560px){.kpis{grid-template-columns:1fr 1fr;gap:10px}.hero{padding:48px 18px 40px}}
</style>
</head>
<body>
<header class="hero">
  <div class="hero-inner">
    <span class="tag">한국 MSP · AX Forward Deployed Engineer · v2.0</span>
    <h1>운영 내재화형 <span class="hl">AX FDE</span> 조직·사업 추진안</h1>
    <p class="lead">고객의 기존 IT운영(MSP) 현장에 내재화되어, AI(AIOps·GenAI)로 운영 성과를 내고 그 성과로 값을 받는 전담 엔지니어 조직. 약 50명·Squad(4~7명) 편제로 과제를 6~8주 타임박스로 수행한다. 전략·조직·프로세스·툴·역량 5개 축을 하나의 논리로 통합한 경영진 보고용 추진안입니다.</p>
    <div class="hero-meta">
      <span>작성 기준일 <b>2026-06-05</b></span>
      <span>버전 <b>v2.0</b></span>
      <span>독자 <b>경영진</b></span>
      <span>구성 <b>5개 축 · 9개 장 · 부록 3</b></span>
    </div>
    <div class="kpis">
      <div class="kpi"><div class="v">7→12<small>조원</small></div><div class="l">국내 MSP 시장 (’23→’26, 추정)</div></div>
      <div class="kpi"><div class="v">74<small>%</small></div><div class="l">AIOps 도입사 MTTR 단축</div></div>
      <div class="kpi"><div class="v">50<small>명</small></div><div class="l">초기 전담조직 · 약 6 Squad</div></div>
      <div class="kpi"><div class="v">6~8<small>주</small></div><div class="l">과제 타임박스 딜리버리</div></div>
    </div>
  </div>
</header>

<div class="navbar"><b>AX FDE 사업 추진안 v2.0</b><button class="menu-btn" id="menuBtn">목차 ☰</button></div>
<div class="scrim" id="scrim"></div>

<div class="shell">
  <aside class="sidebar" id="sidebar"><h4>목차</h4><nav class="toc" id="toc"></nav></aside>
  <main><article id="content">
__CONTENT__
  </article></main>
</div>

<button class="backtop" id="backtop" aria-label="맨 위로">↑</button>
<footer>본 추진안은 5개 축 산출물을 표준 스키마(항목→목표→Activity→Action Item)로 통합·정합성 검수한 결과입니다. · 자체 완결형 정적 페이지 · GitHub Pages 자동 배포</footer>

<script>
(function(){
  var content=document.getElementById('content');
  var tocEl=document.getElementById('toc');

  // 본문 표를 가로 스크롤 래퍼로 감싼다
  [].forEach.call(content.querySelectorAll('table'),function(t){
    var w=document.createElement('div');w.className='tbl-wrap';
    t.parentNode.insertBefore(w,t);w.appendChild(t);
  });

  // h2 기반 사이드바 목차 생성 ('목차' 섹션은 제외)
  var heads=[].filter.call(content.querySelectorAll('h2'),function(h){
    return h.textContent.replace(/\\s/g,'')!=='목차';
  });
  heads.forEach(function(h){
    if(!h.id) h.id='sec-'+Math.random().toString(36).slice(2,8);
    var a=document.createElement('a');a.href='#'+h.id;
    var m=h.textContent.match(/^(\\d+|부록\\s*[A-Z])\\.?\\s*/);
    if(m){a.innerHTML='<span class="num">'+m[1].replace('부록 ','')+'</span>'+h.textContent.slice(m[0].length);}
    else{a.textContent=h.textContent;}
    a.addEventListener('click',closeNav);
    tocEl.appendChild(a);
  });

  // 스크롤 스파이
  var links=[].slice.call(tocEl.querySelectorAll('a'));
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          var i=heads.indexOf(e.target);
          links.forEach(function(l){l.classList.remove('active');});
          if(links[i]) links[i].classList.add('active');
        }
      });
    },{rootMargin:'-10% 0px -75% 0px',threshold:0});
    heads.forEach(function(h){obs.observe(h);});
  }

  // 모바일 네비게이션
  var sidebar=document.getElementById('sidebar'),scrim=document.getElementById('scrim');
  function openNav(){sidebar.classList.add('open');scrim.classList.add('show');}
  function closeNav(){sidebar.classList.remove('open');scrim.classList.remove('show');}
  document.getElementById('menuBtn').addEventListener('click',openNav);
  scrim.addEventListener('click',closeNav);

  // 맨 위로
  var backtop=document.getElementById('backtop');
  window.addEventListener('scroll',function(){backtop.classList.toggle('show',window.scrollY>600);});
  backtop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
})();
</script>
</body>
</html>
'''

html = TEMPLATE.replace("__CONTENT__", frag)
pathlib.Path(OUT).write_text(html, encoding="utf-8")
print("생성 완료:", OUT, "(", len(html), "bytes )")
