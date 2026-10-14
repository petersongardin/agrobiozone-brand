from PIL import Image, ImageDraw, ImageFont
import sys
R='/home/claude/agrobiozone-brand/'
F='/tmp/claude-0/-home-claude/4f04e38a-a493-52ec-ad26-d26f9f0be4a3/scratchpad/fonts/BarlowCondensed-'
OUT=sys.argv[1]
W,H=1080,1350
INK=(15,46,34); GREEN=(7,157,80); LIME=(149,201,73); WHITE=(255,255,255); SOFT=(205,224,213)
def font(w,s): return ImageFont.truetype(F+w+'.ttf',s)
def wrap(d,text,f,maxw):
    out=[];line=''
    for w in text.split():
        t=(line+' '+w).strip()
        if d.textlength(t,font=f)<=maxw: line=t
        else: out.append(line); line=w
    out.append(line); return out
P=[
 ('AGZ-VAR-01','agua_antes_e_depois.jpg',(40,340,1040,1000),'Água turva, com cheiro?','O ozônio trata na hora.','Age contra microrganismos e ajuda com odor, sabor e turbidez. Depois volta a ser oxigênio.','IMAGEM ILUSTRATIVA'),
 ('AGZ-VAR-02','efluentes_cor_e_turbidez_antes_e_depois.jpg',(40,340,1040,990),'Efluente com cor e cheiro?','Teste antes de investir.','O ozônio reduz cor, turbidez, odor, DQO e DBO. Dá para fazer um teste-piloto.','IMAGEM ILUSTRATIVA'),
 ('AGZ-VAR-03','irrigacao_raizes_com_mais_vigor.jpg',(40,340,1040,1095),'Raiz fraca na irrigação?','Pode faltar oxigênio na água.','O ozônio aumenta o oxigênio dissolvido na água de irrigação.','IMAGEM ILUSTRATIVA'),
 ('AGZ-VAR-04','irrigacao_injecao_linha_e_reservatorio.jpg',(40,360,1040,1290),'Como o ozônio entra','na sua irrigação?','Direto na linha pressurizada ou no reservatório, de forma automática.','ESQUEMA SIMPLIFICADO'),
 ('AGZ-VAR-06','camara_instalacao_do_gerador_1.jpg',(40,290,1040,1040),'Ozônio na câmara fria:','o gerador fica fora.','Dentro da câmara ficam só o injetor, a trampa de condensados e o sensor.','FOTO REAL DE INSTALAÇÃO'),
 ('AGZ-VAR-07','efluentes_gerador_na_estacao.jpg',(40,360,1040,1220),'Onde entra o ozônio','na estação de efluentes?','Na pré-oxidação e no tratamento terciário, para descarte ou reúso.','ESQUEMA SIMPLIFICADO'),
 ('AGZ-VAR-08','certificacoes.jpg',(50,470,1030,1175),'Equipamento europeu,','3 certificações.','Fabricado na Espanha pela ZonoSistem. Distribuído no Brasil pela Agrobiozone.',None),
 ('AGZ-VAR-09','camara_contaminacao_em_caixas.jpg',(40,330,1040,990),'Fungo nas caixas','da câmara fria?','O ozônio age no ar e nas superfícies, inclusive nos cantos de difícil acesso.','IMAGEM ILUSTRATIVA'),
 ('AGZ-VAR-10','camara_frutos_com_e_sem_ozonio.jpg',(40,350,1040,990),'Fruta mofando','na câmara fria?','O ozônio age contra fungos e bolores no ar e nas superfícies da câmara.','IMAGEM ILUSTRATIVA'),
]
icon=Image.open(R+'logo/figurativa/icone.png').convert('RGBA'); icon=icon.resize((int(icon.width*84/icon.height),84),Image.LANCZOS)
wm=Image.open(R+'logo/nominativa/wordmark-escuro.png').convert('RGBA'); wm=wm.resize((int(wm.width*34/wm.height),34),Image.LANCZOS)
for pid,fn,box,h1,h2,sup,tag in P:
    im=Image.new('RGBA',(W,H),INK+(255,)); d=ImageDraw.Draw(im)
    for x in range(W):
        t=x/W
        if t<0.55: k=t/0.55; c=tuple(int(a+(b-a)*k) for a,b in zip((0,175,239),(84,185,82)))
        else: k=(t-0.55)/0.45; c=tuple(int(a+(b-a)*k) for a,b in zip((84,185,82),(7,157,80)))
        d.line([(x,0),(x,13)],fill=c+(255,))
    im.alpha_composite(icon,(70,48)); im.alpha_composite(wm,(70+icon.width+18,48+25))
    fh=font('ExtraBold',92)
    d.text((68,158),h1,font=fh,fill=WHITE); d.text((68,252),h2,font=fh,fill=LIME)
    src=Image.open(R+'midias_darcy/'+fn).convert('RGB').crop(box)
    cw=940; ch=int(src.height*cw/src.width); maxh=650
    if ch>maxh: cw=int(cw*maxh/ch); ch=maxh
    src=src.resize((cw,ch),Image.LANCZOS)
    x0=(W-cw)//2; y0=380
    m=Image.new('L',(cw,ch),0); ImageDraw.Draw(m).rounded_rectangle([0,0,cw-1,ch-1],radius=24,fill=255)
    im.paste(src,(x0,y0),m)
    y=y0+ch+18
    if tag:
        ft=font('Bold',26); tw=d.textlength(tag,font=ft)
        d.text(((W-tw)//2,y),tag,font=ft,fill=SOFT); y+=44
    fs=font('Medium',44)
    for ln in wrap(d,sup,fs,940):
        d.text((70,y),ln,font=fs,fill=WHITE); y+=54
    fw=font('ExtraBold',48); bt='Chama no WhatsApp: (49) 99815-0994'; bw=d.textlength(bt,font=fw)
    d.rounded_rectangle([70,1212,70+bw+60,1292],radius=40,fill=GREEN)
    d.text((100,1220),bt,font=fw,fill=WHITE)
    if y>1200: print('ESTOUROU',pid,y)
    im.convert('RGB').save(f'{OUT}/{pid}.jpg',quality=92)
    print(pid,'img',cw,ch,'texto ate',y)
