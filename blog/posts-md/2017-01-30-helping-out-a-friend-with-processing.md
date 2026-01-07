---
layout: layouts/blog-post.njk
title: "Helping out a friend with Processing"
date: 2017-01-30
author: Itzik Ben-Shabat
permalink: "/blog/posts/2017-01-30-helping-out-a-friend-with-processing.html"
---

<div class="post-content">
{% raw %}




<p>My best friend’s girlfriend studies design. As part of her studies, they learned some programming using <a href="https://processing.org/">Processing</a>.  As a designer (and not a programmer) she had a hard time getting things to work. Even though I don’t know processing at all I figured my experience in programming might come in handy.</p>
<p>And here is the result (I think it turned out quite well):</p>

<div style="text-align: center;">
<script data-processing-target="MySketch" type="text/processing">
ball[] balls;
int numBalls = 7;
void setup(){
size (300,300,P3D);
background(255);balls=new ball[numBalls];
for(int i=0; i<numBalls;i++){
  float r=random(5,20);
 balls[i] = new ball(random(r,width-r),random(r,height-r),0,r,random(-1,10),random(-1,10));
}

}

void draw(){
 background(255);
lights();
 for(int i=0; i<numBalls;i++){ ball b; b=balls[i]; b.drawBall(); b.moveBall(); b.boundaries(); } } class ball{ float x; float y; float z; float r; float vx; float vy; ball(float x1,float y1,float z1,float r1,float vx1,float vy1 ){ x=x1; y=y1; z=z1; r=r1; vx=vx1; vy=vy1; } void drawBall(){ noStroke(); fill(255,0,0); pushMatrix(); translate(x, y,z); sphere(r); popMatrix(); } void moveBall(){ x=x+vx; y=y+vy; } void boundaries(){ if(x>=width-r || x<0+r) vx=vx*-1; if(y>=height-r || y<0+r)
  vy=vy*-1;
 }
}
</script><br/>
<canvas id="MySketch"></canvas></div>
<p>The next day she sent me this result (Notice what happens when you click, hold and release):</p>

<div style="text-align: center;">
<script data-processing-target="MySketch2" type="text/processing">
ball[] balls;
int numBalls =20;bigBall bigB= new bigBall(75,0.01,0.09);
void setup(){
  size(300, 300, P3D);
  balls=new ball[numBalls];
  for(int i=0; i<numBalls;i++){
  float r=random(5,15);balls[i] = new ball(random(r,width-r),random(r,height-r),0,r,random(-5,5),random(-5,5));
}
}

void draw(){
  background(#aa0cbb);
   lights();
 for(int i=0; i<numBalls;i++){ balls[i].drawBall(); balls[i].moveBall(); balls[i].boundaries(); balls[i].a(); } bigB.showBigBall(); } class ball{float x;float y;float z;float r;float vx;float vy;boolean flagg; ball(float x1,float y1,float z1,float r1,float vx1,float vy1 ){ x=x1; y=y1; z=z1; r=r1; vx=vx1; vy=vy1; flagg=false;} void drawBall(){pushMatrix(); noStroke(); fill(#00ffd2); translate(x, y,z); sphere(r); popMatrix(); } void moveBall(){x=x+vx;y=y+vy;} void boundaries(){ if(x>=width-r || x<0+r) vx=vx*-1;if(y>=height-r || y<0+r) vy=vy*-1;} void a(){ if(mousePressed){ if(flagg==false){ flagg=true; x=width/2; y=height/2; } if(pow(x-(width/2),2)+pow(y-(height/2),2) >=pow(75-r,2)){
  vx=vx*-1;
  vy=vy*-1;
 }
 }
 else{
   flagg=false;
 } 
 }
}
class bigBall{ float radious; float noiseScale;float timeScale;
   bigBall(float radious1,float noiseScale1,float timeScale1 ){
   radious=radious1;
   noiseScale=noiseScale1;
   timeScale=timeScale1;
   }
   void showBigBall(){
 stroke(255);
  noFill();
  translate(width / 2, height / 2, 0);
  rotateZ(PI/2);
  rotateX(PI/2);
  for(float y = -radious * 1.0 / 3; y <= radious * 2.0 / 3; y += 6){
    float r = radious * cos(asin(abs(y / radious)));
    beginShape();
    for(float radian = 0; radian < TWO_PI; radian += PI / 128){ float x = r * cos(radian); float z = r * sin(radian); float yy = y + map(noise(x * noiseScale, frameCount * timeScale, z * noiseScale) , 0, 1, -radious / 3, radious / 3); if(yy > radious){
        yy = radious;
      }
      float rr = radious * cos(asin(abs(yy / radious)));
      float xx = rr * cos(radian);
      float zz = rr * sin(radian);
      vertex(xx, yy, zz);
    }
    endShape(CLOSE);
  }
}
}
</script><br/>
<canvas id="MySketch2"></canvas></div> </p>
<p>Credit: She told me that for the center circle she adapted a code snippet by "aa_debdeb" shown <a href="https://www.openprocessing.org/sketch/375003">here</a>.</p>
 

{% endraw %}
</div>