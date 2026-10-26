"""Gera assets/traje/Bombacha_Cinto.png a partir do pants.png do SEU jogo (desempacotado).
Uso: python ferramentas/gerar_bombacha.py CAMINHO/Characters/Farmer/pants.png [--indice 8]
Recorta o bloco 192x688 da calça base (padrão: índice 8, Genie Pants), recolore em
cinza-azulado e pinta um cinto preto com fivela dourada no topo de cada quadro."""
import sys, os
from PIL import Image
args=sys.argv[1:]
if not args: sys.exit(__doc__)
idx=int(args[args.index('--indice')+1]) if '--indice' in args else 8
src=Image.open(args[0]).convert('RGBA')
bx,by=(idx%10)*192,(idx//10)*688
blk=src.crop((bx,by,bx+192,by+688))
pal=[(84,92,108),(122,132,150),(158,168,186),(186,196,212),(208,216,230)]
belt,beltH,gold=(30,25,27),(56,48,50),(232,188,66)
px=blk.load()
for y in range(688):
    for x in range(192):
        r,g,b,a=px[x,y]
        if a==0: continue
        l=(r*299+g*587+b*114)//1000
        px[x,y]=pal[min(4,l*5//256)]+(a,)
def faixa(x0,y0,w,h,fivela):
    for y in range(y0,y0+h):
        xs=[x for x in range(x0,x0+w) if px[x,y][3]>0]
        if len(xs)>=3:
            for x in xs: px[x,y]=belt+(255,)
            px[xs[0],y]=beltH+(255,)
            if fivela:
                m=(xs[0]+xs[-1])//2
                for x in (m,m+1):
                    if x<=xs[-1]: px[x,y]=gold+(255,)
            return
for fy in range(0,672,32):
    for fx in range(0,192,16):
        faixa(fx,fy,16,32,fivela=(fy==0))   # linha 0 = personagem de frente
faixa(0,672,192,16,fivela=False)            # área do ícone
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','traje','Bombacha_Cinto.png')
blk.save(out); print('Gerado:',os.path.normpath(out))
