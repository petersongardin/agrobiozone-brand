from PIL import Image, ImageDraw, ImageFont
import sys
S='/tmp/claude-0/-home-claude/4f04e38a-a493-52ec-ad26-d26f9f0be4a3/scratchpad/'
F=S+'fonts/BarlowCondensed-'
W,H=1080,1350
INK=(15,46,34); GREEN=(7,157,80); BG=(245,248,246)
im=Image.new('RGBA',(W,H),(0,0,0,0))
px=im.load()
# top band solid then fade
for y in range(0,470):
    a=255 if y<360 else int(255*(1-(y-360)/110))
    for x in range(W): px[x,y]=BG+(a,)
# bottom dark gradient
for y in range(820,H):
    a=int(235*min(1,(y-820)/200))
    for x in range(W): px[x,y]=INK+(a,)
d=ImageDraw.Draw(im)
# brand gradient bar top
for x in range(W):
    t=x/W
    c=(0,175,239) if t<0 else None
    if t<0.55: k=t/0.55; c=tuple(int(a+(b-a)*k) for a,b in zip((0,175,239),(84,185,82)))
    else: k=(t-0.55)/0.45; c=tuple(int(a+(b-a)*k) for a,b in zip((84,185,82),(7,157,80)))
    d.line([(x,0),(x,13)],fill=c+(255,))
logo=Image.open('/home/claude/agrobiozone-brand/logo/mista/logo-mista-horizontal-claro.png').convert('RGBA')
lh=84; logo=logo.resize((int(logo.width*lh/logo.height),lh),Image.LANCZOS)
im.alpha_composite(logo,(70,52))
f1=ImageFont.truetype(F+'ExtraBold.ttf',104)
d.text((68,160),'Gotejador entupido?',font=f1,fill=INK)
d.text((68,262),'Olhe dentro do cano.',font=f1,fill=GREEN)
# label
fl=ImageFont.truetype(F+'Bold.ttf',30)
t='IMAGEM ILUSTRATIVA'; tw=d.textlength(t,font=fl)
d.rounded_rectangle([W-70-tw-36,480,W-70,528],radius=10,fill=INK+(220,))
d.text((W-70-tw-18,485),t,font=fl,fill=(255,255,255))
fb=ImageFont.truetype(F+'Bold.ttf',50); fr=ImageFont.truetype(F+'Medium.ttf',44)
d.text((70,1000),'Esse limo é biofilme: fecha o tubo',font=fb,fill=(255,255,255))
d.text((70,1056),'e entope o gotejador.',font=fb,fill=(255,255,255))
d.text((70,1124),'O ozônio dissolve a matéria orgânica e reduz entupimentos.',font=fr,fill=(220,235,226))
# whatsapp button
fw=ImageFont.truetype(F+'ExtraBold.ttf',48)
bt='WhatsApp (49) 99815-0994'; bw=d.textlength(bt,font=fw)
d.rounded_rectangle([70,1206,70+bw+60,1286],radius=40,fill=GREEN+(255,))
d.text((100,1214),bt,font=fw,fill=(255,255,255))
im.save(S+'var/overlay_biofilme.png')
print('ok')
