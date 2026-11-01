'use strict';
document.querySelectorAll('.slideshow').forEach(root=>{
  const slides=[...root.querySelectorAll('.slide')],dots=[...root.querySelectorAll('[data-slide]')],play=root.querySelector('[data-play]'),count=root.querySelector('.slide-count');
  const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let index=0,playing=!reduced,timer=null,hovered=false,focused=false,inView=false;
  function render(){
    slides.forEach((slide,i)=>slide.hidden=i!==index);
    dots.forEach((dot,i)=>dot.setAttribute('aria-pressed',String(i===index)));
    count.textContent=`${index+1} / ${slides.length}`;
    play.textContent=playing?'暂停 ⏸':'播放 ▶';
    play.setAttribute('aria-label',playing?'暂停自动播放':'开始自动播放');
  }
  function schedule(){clearInterval(timer);timer=null;if(playing&&inView&&!hovered&&!focused&&!document.hidden)timer=setInterval(()=>{index=(index+1)%slides.length;render()},3500)}
  function go(i){index=(i+slides.length)%slides.length;render();schedule()}
  root.querySelector('[data-prev]').addEventListener('click',()=>go(index-1));
  root.querySelector('[data-next]').addEventListener('click',()=>go(index+1));
  dots.forEach((dot,i)=>dot.addEventListener('click',()=>go(i)));
  play.addEventListener('click',()=>{playing=!playing;render();schedule()});
  root.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();go(index-1)}if(e.key==='ArrowRight'){e.preventDefault();go(index+1)}});
  root.addEventListener('mouseenter',()=>{hovered=true;schedule()});root.addEventListener('mouseleave',()=>{hovered=false;schedule()});
  root.addEventListener('focusin',()=>{focused=true;schedule()});root.addEventListener('focusout',e=>{if(!root.contains(e.relatedTarget)){focused=false;schedule()}});
  document.addEventListener('visibilitychange',schedule);
  new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;schedule()},{threshold:.1}).observe(root);
  render();
});
