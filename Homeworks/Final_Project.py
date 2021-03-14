ques_ans={"2 üssü 3 kaçtır ? ":'8',
"Amerika'nın başkenti neresidir ? ":'Washington',
"Dünya'nın uydusu hangi gezegendir ? ":'Ay',
"Telefonu bulan bilim insanı kimdir ? ":'Alexander Graham Bell',
"Türkçe hangi dil grubuna aittir ? ":'Ural-Altay',
"İlk evcilleştirilmiş hayvan hangisidir ? ":'Köpek',
"Türkiye'nin en fazla yağış alan ili hangisidir ? ":'Rize',
"Atatürk'ün yurt gezilerinde (1935-1938) yılları arasında kullandığı trenin adı nedir?":'Beyaz Tren',
"Türkiye'nin en büyük kış ve doğa sporları merkezi olan Uludağ'ın eski adı nedir?":'Keşiş dağı',
"Hangi tarihte güney yarımkürede en uzun gündüz yaşanır?":'21 Aralık'
}
 
total_point=0

for question in ques_ans.keys():
    print(question,end='')

    z=input().strip()
   
    if z==ques_ans[question]:
        total_point+=10

if total_point>50:
    print('Başarılı')
else:
    print('Başarısız')