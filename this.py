from math import cos,sin,pi,floor
from subprocess import Popen,PIPE
def asg(l,v,i=0):
    l[i]=v
class Img:
    def __init__(self,r,c):
        self.c,self.r,self.img,self.lns,self.ln,self.s,self.oof,self.pgs=c,r,[13754608]*r*c,(lambda p:[[self.ln(r-round(p[i+1]/p[i+3]),round(p[i]/p[i+3]),r-round(p[i+5]/p[i+7]),round(p[i+4]/p[i+7]),2514585)for i in range(0,len(p),8)],self][1]),(lambda rs,cs,rf,cf,v,e=[0,0]:self.ln(rf,cf,rs,cs,v)if(rs>rf if abs(rf-rs)<abs(cf-cs)else cs>cf)else([asg(e,rs,1),asg(e,2*abs(rf-rs)-abs(cf-cs)),[[self.s(e[1],c,v),asg(e,e[1]+1,1),asg(e,e[0]+2*abs(rf-rs)-2*abs(cf-cs))]if 0<e[0]else[self.s(e[1],c,v),0,asg(e,e[0]+2*abs(rf-rs))]for c in range(cs,cf-1 if cs>cf else cf+1,-1 if cs>cf else 1)]]if abs(rf-rs)<abs(cf-cs)else[asg(e,cs,1),asg(e,2*abs(cf-cs)-abs(rf-rs)),[[self.s(r,e[1],v),asg(e,e[1]+1,1),asg(e,e[0]+2*abs(cf-cs)-2*abs(rf-rs))]if 0<e[0]else[self.s(r,e[1],v),0,asg(e,e[0]+2*abs(cf-cs))]for r in range(rs,rf-1 if rs>rf else rf+1,-1 if rs>rf else 1)]])),(lambda r,c,v:[asg(self.img,v,c+r*self.c)]if-1<r<self.r and-1<c<self.c else 0),(lambda:"P3 "+str(self.c)+" "+str(self.r)+" 255\n"+" ".join(str(floor(i/65536)%256)+" "+str(floor(i/256)%256)+" "+str(i%256) for i in self.img)),(lambda p:[[[self.ln(r-round(p.m[i+(4*j+1)%12]/p.m[i+(4*j+3)%12]),round(p.m[i+4*j%12]/p.m[i+(4*j+3)%12]),r-round(p.m[i+(4*j+5)%12]/p.m[i+(4*j+7)%12]),round(p.m[i+(4*j+4)%12]/p.m[i+(4*j+7)%12]),4968864)for j in range(3)]for i in range(0,len(p.m),12)if p.bfc(i,(0,0,-1))>0],self][1])
class Etrx:
    def __init__(self,m=[]):
        self.m,self.e,self.oof,self.x,self.idm,self.c,self.hb,self.t,self.bfc,self.dtp,self.crs,self.nilrecurring=m[:],(lambda s,f:[self.m.append(i)for i in(*s,1,*f,1)]),(lambda:"\n".join(" ".join(("  "if i<10 else" "if i<100 else"")+str(i) for i in self.m[j::4]) for j in range(4))+"\n"),(lambda m:[self,[asg(self.m,e,i)for(i,e)in enumerate([sum(float(m[i%4+k*4])*self.m[i-(i%4)+k]for k in range(4))for i in range(len(self.m))])]][0]),(lambda:[asg(self.m,1.0 if i==j else 0.0,j+4*i)for j in range(4)for i in range(4)]if self.m else[self.m.append(1.0 if i==j else 0.0)for j in range(4)for i in range(4)]),(lambda x,y,z,r:[[self.e(*[[x+r*cos((t+d)/mx*2*pi),y+r*sin((t+d)/mx*2*pi),z]for d in(0,1)])for t in range(round(mx))]for mx in[40]]),(lambda xyxy,m:[[self.e(*[[(lambda a,t:sum(pow(t,3-i)*a[i]for i in range(4)))(Etrx([xyxy[2*i+k]for i in range(4)]).x(m).m,(h+d)/mx)for k in(0,1)]+[0]for d in(0,1)])for h in range(mx)]for mx in[20]]),(lambda p,b,d:[self.m.append(i)for i in(*p,1,*b,1,*d,1)]),(lambda i,lk:self.dtp(lk,self.crs(*[[self.m[i+j+k]-self.m[i+j]for j in(0,1,2)]for k in(4,8)]))),(lambda m,pth:sum(m[i]*pth[i]for i in range(len(pth)))),(lambda p,vi:(p[1]*vi[2]-p[2]*vi[1],p[2]*vi[0]-p[0]*vi[2],p[0]*vi[1]-p[1]*vi[0])),(lambda x:[i/sqrt(dtp(x,x))for i in x])
(lambda m,edgm,pogm,filename:[[{"ident":(lambda:m.idm()),"line":(lambda:edgm.e([float(i)for i in b[1][:3]],[float(i)for i in b[1][3:]])),"circle":(lambda:edgm.c(*[float(i)for i in b[1]])),"hermite":(lambda:edgm.hb([float(i)for i in b[1]],(2,-3,0,1,-2,3,0,0,1,-2,1,0,1,-1,0,0))),"bezier":(lambda:edgm.hb([float(i)for i in b[1]],(-1,3,-3,1,3,-6,3,0,-3,3,0,0,1,0,0,0))),"box":(lambda:[pogm.t(*ooo)for ooo in[(((o[0],o[1],o[2]+o[5]),(o[0],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1],o[2]+o[5])),((o[0],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1],o[2]+o[5])),((o[0],o[1],o[2]),(o[0]+o[3],o[1],o[2]),(o[0],o[1]-o[4],o[2])),((o[0],o[1]-o[4],o[2]),(o[0]+o[3],o[1],o[2]),(o[0]+o[3],o[1]-o[4],o[2])),((o[0]+o[3],o[1],o[2]+o[5]),(o[0]+o[3],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1],o[2])),((o[0]+o[3],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1]-o[4],o[2]),(o[0]+o[3],o[1],o[2])),((o[0],o[1],o[2]+o[5]),(o[0],o[1],o[2]),(o[0],o[1]-o[4],o[2]+o[5])),((o[0],o[1]-o[4],o[2]+o[5]),(o[0],o[1],o[2]),(o[0],o[1]-o[4],o[2])),((o[0],o[1],o[2]),(o[0],o[1],o[2]+o[5]),(o[0]+o[3],o[1],o[2])),((o[0],o[1],o[2]+o[5]),(o[0]+o[3],o[1],o[2]+o[5]),(o[0]+o[3],o[1],o[2])),((o[0],o[1]-o[4],o[2]),(o[0]+o[3],o[1]-o[4],o[2]),(o[0],o[1]-o[4],o[2]+o[5])),((o[0],o[1]-o[4],o[2]+o[5]),(o[0]+o[3],o[1]-o[4],o[2]),(o[0]+o[3],o[1]-o[4],o[2]+o[5])))for o in [[float(oo)for oo in b[1]]]][0]]),"sphere":(lambda:[[[(pogm.t(p[i],p[i+1],p[(i+k)%len(p)]),pogm.t(p[(i+1+k)%len(p)],p[(i+k)%len(p)],p[i+1]))for i in range(len(p))if i%k!=k-1]for p in[[(float(b[1][0])+float(b[1][3])*cos(pi*j/(k-1)),float(b[1][1])+float(b[1][3])*sin(pi*j/(k-1))*cos(2*pi*i/k),float(b[1][2])+float(b[1][3])*sin(pi*j/(k-1))*sin(2*pi*i/k))for i in range(k)for j in range(k)]]]for k in[20]]),"torus":(lambda:[[[(pogm.t(p[i],p[(i+k)%len(p)],p[i-i%k+(i+1)%k]),pogm.t(p[(i+k)%len(p)],p[(i-i%k+(i+1)%k+k)%len(p)],p[i-i%k+(i+1)%k]))for i in range(len(p))]for p in[[(float(b[1][0])+(float(b[1][3])*cos(2*pi*i/k)+float(b[1][4]))*cos(2*pi*j/k),float(b[1][1])+float(b[1][3])*sin(2*pi*i/k),float(b[1][0])+(float(b[1][3])*cos(2*pi*i/k)+float(b[1][4]))*sin(2*pi*j/k))for i in range(k)for j in range(k)]]]for k in[20]]),"scale":(lambda:m.x((float(b[1][0]),0,0,0,0,float(b[1][1]),0,0,0,0,float(b[1][2]),0,0,0,0,1))),"move":(lambda:m.x((1,0,0,0,0,1,0,0,0,0,1,0,float(b[1][0]),float(b[1][1]),float(b[1][2]),1))),"rotate":(lambda:m.x({"x":(1,0,0,0,0,cos(float(b[1][1])/180*pi),sin(float(b[1][1])/-180*pi),0,0,sin(float(b[1][1])/180*pi),cos(float(b[1][1])/180*pi),0,0,0,0,1),"y":(cos(float(b[1][1])/180*pi),0,sin(float(b[1][1])/180*pi),0,0,1,0,0,sin(float(b[1][1])/-180*pi),0,cos(float(b[1][1])/180*pi),0,0,0,0,1),"z":(cos(float(b[1][1])/180*pi),sin(float(b[1][1])/-180*pi),0,0,sin(float(b[1][1])/180*pi),cos(float(b[1][1])/180*pi),0,0,0,0,1,0,0,0,0,1)}[b[1][0]])),"project":(lambda:m.x((1,0,0,0,0,1,0,0,0,0,0,0,0,0,1/float(b[1][0]),1))),"apply":(lambda:[edgm.x(m.m),pogm.x(m.m)]),"clear":(lambda:[edgm.m.clear(),pogm.m.clear()]),"display":(lambda:[open("temp.ppm","w+").write(Img(500,500).lns(edgm.m).pgs(pogm).oof()),Popen(("display","temp.ppm"),stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate(),Popen(("rm","temp.ppm"),stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate()]),"save":(lambda:[open("temp2.ppm","w+").write(Img(500,500).lns(edgm.m).pgs(pogm).oof()),Popen(("convert","temp2.ppm",b[1][0]),stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate(),Popen(("rm","temp2.ppm"),stdin=PIPE,stdout=PIPE,stderr=PIPE).communicate()])}[b[0]]()for b in[(e[0],(*tuple(fl),[])[i+1])for(i,e)in enumerate(fl)if e and e[0]in("ident","line","circle","hermite","bezier","box","sphere","torus","scale","move","rotate","project","apply","clear","display","save")]]for fl in[[k.split(" ")for k in open(filename,"r").read().split("\n")if k]]])(Etrx(),Etrx(),Etrx(),"test.txt")
