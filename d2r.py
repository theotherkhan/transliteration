#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
import sys
import nltk.data
from nltk.tokenize import word_tokenize

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[1]+'roman', 'w')
d2r_dict=OrderedDict([

('ख़्त','k͟ht'),
('र्फ़','rf'),
('ख़ु','khu'),
('फ़्ज़','fz'),
('ज़्य','ziy'),
('ख़्व', 'khv'),
('ज़्ल','zl'),
('फ़्तु','ftu'),
('फ़्त', 'ft'),
('फ़्तु','ftu'),
('ख़्य','k͟hy'),

('क्','k'),
('क़्','q'),
('ख्','kh'),
('क़','q'),
('ग्','g'),
('घ्','gh'),
('ङ्','n'),
('च्','ch'),
('छ्','chh'),
('ज्','j'),
('झ्','jh'),
('ञ्','n'),
('ट्','t'),
('ठ्','th'),
('ड्','d'),
('ढ्','dh'),
('ण्','n'),
('त्','t'),
('थ्','th'),
('द्','d'),
('ध्','dh'),
('न्','n'),
('प्','p'),
('फ्','ph'),
('ब्','b'),
('भ्','bh'),
('म्','m'),
('य्','y'),
('ड़्','ṛ'),
('ढ़्','ṛ'),
('र्','r'),
('ल्','l'),
('व्','w'),
('श्','sh'),
('ष्','s'),
('स्','s'),
('ह्','h'),
('ग़्', 'ġ'),
('ज़्','z'),
('फ़्','f'),
('फ़','f'),
('ख़्','k͟h'),


('ष','श'),



('का','kaa'),
('को','ko'),
('कौ','kau'),
('कि','ki'),
('की','kee'),
('कु','ku'),
('कू','ku'),
('के','ke'),
('कै','kai'),
('कं','kunn'),
('फ़ा','faa'),
('फ़ो','fo'),
('फ़ौ','fau'),
('फ़ि','fi'),
('फ़ी','fee'),
('फ़ु','fu'),
('फ़ू','fu'),
('फ़े','fe'),
('फ़ै','fai'),
('फ़ं','fum'),
('खा','khaa'),
('खो','kho'),
('खौ','khau'),
('खि','khi'),
('खी','khee'),
('खु','khu'),
('खू','khu'),
('खे','khe'),
('खै','khai'),
('खं','khuṅ'),
('क़ा','qaa'),
('क़ो','qo'),
('क़ौ','qau'),
('क़ि','qi'),
('क़ी','qee'),
('क़ु','qu'),
('क़ू','qu'),
('क़े','qe'),
('क़ै','qai'),
('क़ं','quṅ'),
('गा','gaa'),
('गो','go'),
('गौ','gau'),
('गि','gi'),
('गी','gi'),
('गु','gu'),
('गू','gu'),
('गे','ge'),
('गै','gai'),
('गं','guṅ'),
('घा','ghaa'),
('घो','gho'),
('घौ','ghau'),
('घि','ghi'),
('घी','ghee'),
('घु','ghu'),
('घू','ghu'),
('घे','ghe'),
('घै','ghai'),
('घं','ghuṅ'),
('ङा','naa'),
('ङो','no'),
('ङौ','nau'),
('ङि','ni'),
('ङी','ni'),
('ङु','nu'),
('ङू','nu'),
('ङे','ne'),
('ङै','nai'),
('ङं','nun'),
('चा','chaa'),
('चो','cho'),
('चौ','chau'),
('चि','chi'),
('ची','chee'),
('चु','chu'),
('चू','chu'),
('चे','che'),
('चै','chai'),
('चं','chun'),
('छा','chhaa'),
('छो','chho'),
('छौ','chhau'),
('छि','chhi'),
('छी','chhee'),
('छु','chhu'),
('छू','chhu'),
('छे','chhe'),
('छै','chhai'),
('छं','chhunn'),
('जा','jaa'),
('जो','jo'),
('जौ','jau'),
('जि','ji'),
('जी','jee'),
('जु','ju'),
('जू','ju'),
('जे','je'),
('जै','jai'),
('जं','jum'),
('झा','jhaa'),
('झो','jho'),
('झौ','jhau'),
('झि','jhi'),
('झी','jhi'),
('झु','jhu'),
('झू','jhu'),
('झे','jhe'),
('झै','jhai'),
('झं','jhum'),
('ञा','naa'),
('ञो','no'),
('ञौ','nau'),
('ञि','ni'),
('ञी','ni'),
('ञु','nu'),
('ञू','nu'),
('ञे','ne'),
('ञै','nai'),
('ञं','num'),
('टा','taa'),
('टो','to'),
('टौ','tau'),
('टि','ti'),
('टी','ti'),
('टु','tu'),
('टू','tu'),
('टे','te'),
('टै','tai'),
('टं','tuṅ'),
('ठा','thaa'),
('ठो','tho'),
('ठौ','thau'),
('ठि','thi'),
('ठी','thi'),
('ठु','thu'),
('ठू','thu'),
('ठे','the'),
('ठै','thai'),
('ठं','thunn'),
('डा','daa'),
('डो','do'),
('डौ','dau'),
('डि','di'),
('डी','dee'),
('डु','du'),
('डू','du'),
('डे','de'),
('डै','dai'),
('डं','dum'),
('ढा','dhaa'),
('ढो','dho'),
('ढौ','dha'),
('ढि','dhi'),
('ढी','dhee'),
('ढु','dhu'),
('ढू','dhu'),
('ढे','dhe'),
('ढै','dhai'),
('ढं','dhuṅ'),
('ता','taa'),
('तो','to'),
('तौ','tau'),
('ति','ti'),
('ती','tee'),
('तु','tu'),
('तू','tu'),
('ते','te'),
('तै','tai'),
('तं','tun'),
('था','thaa'),
('थो','tho'),
('थौ','thau'),
('थि','thi'),
('थी','thee'),
('थु','thu'),
('थू','thu'),
('थे','the'),
('थै','thai'),
('थं','thuṅ'),
('दा','daa'),
('दो','do'),
('दौ','dau'),
('दि','di'),
('दी','dee'),
('दु','du'),
('दू','du'),
('दे','de'),
('दै','dai'),
('दं','dun'),
('धा','dhaa'),
('धो','dho'),
('धौ','dhau'),
('धि','dhi'),
('धी','dhee'),
('धु','dhu'),
('धू','dhu'),
('धे','dhe'),
('धै','dhai'),
('धं','dhum'),
('ना','naa'),
('नो','no'),
('नौ','nau'),
('नि','ni'),
('नी','ni'),
('नु','nu'),
('नू','nu'),
('ने','ne'),
('नै','nai'),
('नं','nun'),
('पा','paa'),
('पो','po'),
('पौ','pau'),
('पि','pi'),
('पी','pee'),
('पु','pu'),
('पू','pu'),
('पे','pe'),
('पै','pai'),
('पं','pum'),
('फा','phaa'),
('फो','pho'),
('फौ','phau'),
('फि','phi'),
('फी','phee'),
('फु','phu'),
('फू','phu'),
('फे','phe'),
('फै','phai'),
('फं','phum'),
('बा','baa'),
('बो','bo'),
('बौ','bau'),
('बि','bi'),
('बी','bee'),
('बु','bu'),
('बू','bu'),
('बे','be'),
('बै','bai'),
('बं','bum'),
('भा','bhaa'),
('भो','bho'),
('भौ','bhau'),
('भि','bhi'),
('भी','bhi'),
('भु','bhu'),
('भू','bhu'),
('भे','bhe'),
('भै','bhai'),
('भं','bhum'),
('मा','maa'),
('मो','mo'),
('मौ','mau'),
('मि','mi'),
('मी','mee'),
('मु','mu'),
('मू','mu'),
('मे','me'),
('मै','mai'),
('मं','mum'),
('या','yaa'),
('यो','yo'),
('यौ','yau'),
('यि','yi'),
('यी','yi'),
('यु','yu'),
('यू','yu'),
('ये','ye'),
('यै','yai'),
('यं','yum'),
('रा','raa'),
('रो','ro'),
('रौ','rau'),
('रि','ri'),
('री','ree'),
('रु','ru'),
('रू','ru'),
('रे','re'),
('रै','rai'),
('रं','rum'),
('ड़ा','ṛaa'),
('ड़ो','ṛo'),
('ड़ौ','ṛau'),
('ड़ि','ṛi'),
('ड़ी','ṛee'),
('ड़ु','ṛu'),
('ड़ू','ṛu'),
('ड़े','ṛe'),
('ड़ै','ṛai'),
('ड़ं','ṛum'),
('ला','laa'),
('लो','lo'),
('लौ','lau'),
('लि','li'),
('ली','lee'),
('लु','lu'),
('लू','lu'),
('ले','le'),
('लै','lai'),
('लं','lum'),
('वा','waa'),
('वो','wo'),
('वौ','wau'),
('वि','wi'),
('वी','wee'),
('वु','wu'),
('वू','wu'),
('वे','we'),
('वै','wai'),
('वं','wum'),
('शा','shaa'),
('शो','sho'),
('शौ','shau'),
('शि','shi'),
('शी','shi'),
('शु','shu'),
('शू','shu'),
('शे','she'),
('शै','shai'),
('शं','shum'),
('सा','saa'),
('सो','so'),
('सौ','sau'),
('सि','si'),
('सी','see'),
('सु','su'),
('सू','su'),
('से','se'),
('सै','sai'),
('सं','sum'),
('हा','haa'),
('हो','ho'),
('हौ','hau'),
('हि','hi'),
('ही','hi'),
('हु','hu'),
('हू','hu'),
('हे','he'),
('है','hai'),
('हं','hum'),
('ग़ा','ġaa'),
('ग़ो','ġo'),
('ग़ौ','ġau'),
('ग़ि','ġi'),
('ग़ी','ġee'),
('ग़ु','ġu'),
('ग़ू','ġu'),
('ग़े','ġe'),
('ग़ै','ġai'),
('ग़ं','ġun'),
('ज़ा','zaa'),
('ज़ो','zo'),
('ज़ौ','zau'),
('ज़ि','zi'),
('ज़ी','zee'),
('ज़ु','zu'),
('ज़ू','zu'),
('ज़े','ze'),
('ज़ै','zai'),
('ज़ं','zum'),
('ख़ा','k͟haa'),
('ख़ो','k͟ho'),
('ख़ौ','k͟hau'),
('ख़ि','k͟hi'),
('ख़ी','k͟hee'),
('ख़ु','k͟hu'),
('ख़ू','k͟hu'),
('ख़े','k͟he'),
('ख़ै','k͟hai'),
('ख़ं','k͟huṅ'),
('ख़्रा','k͟haa'),
('ख़्रो','k͟ho'),
('ख़्रौ','k͟hau'),
('ख़्रि','k͟hi'),
('ख़्री','k͟hee'),
('ख़्रु','k͟hu'),
('ख़्रू','k͟hu'),
('ख़्रे','k͟he'),
('ख़्रै','k͟hai'),
('ख़्रं','k͟huṅ'),

('क़ ','q '),
('क ','k '),
('ख़ ','k͟h '),
('ख़्र ','k͟h '),
('ख ','kh '),
('ग़़ ','ġ '),
('ग़ ','gh '),
('ग ','g '),
('घ ','gh '),
('ङ ','n '),
('च ','ch '),
('छ ','chh '),
('ज़ ','z '),
('ज ','j '),
('झ ','jh '),
('ञ ','n '),
('ट ','t '),
('ठ ','th '),
('ड़ ','ṛ '),
('ड ','d '),
('ढ़ ','ṛ '),
('ढ ','dh '),
('ण ','n '),
('त ','t '),
('थ ','th '),
('द ','d '),
('ध ','dh '),
('न ','n '),
('प ','p '),
('फ़ ','f '),
('फ ','ph '),
('ब ','b '),
('भ ','bh '),
('म ','m '),
('य ','y '),
('र ','r '),
('ल ','l '),
('व ','w '),
('श ','sh '),
('स ','s '),
('ज़ ','z '),
('ह ','h '),


('क़','qa'),
('क','ka'),
('ख़','k͟ha'),
('ख़्र','k͟ha'),
('ख','kha'),
('ग़़', 'ġa'),
('ग़','gha'),
('ग','ga'),
('घ','gha'),
('ङ','na'),
('च','cha'),
('छ','chha'),
('ज़','za'),
('ज','ja'),
('झ','jha'),
('ञ','na'),
('ट','ta'),
('ठ','tha'),
('ड़','ṛa'),
('ड','da'),
('ढ़','ṛa'),
('ढ','dha'),
('ण','na'),
('त','ta'),
('थ','tha'),
('द','da'),
('ध','dha'),
('न','na'),
('प','pa'),
('फ़','fa'),
('फ','pha'),
('ब','ba'),
('भ','bha'),
('म','ma'),
('य','ya'),
('र','ra'),
('ल','la'),
('व','wa'),
('श','sha'),
('स','sa'),
('ज़','za'),
('ह','ha'),


('ष','श'),
('ँ','n'),
('ं','ṉ'),
('ः','h'),
('अ','a'),
('आ','a'),
('इ','i'),
('ई','i'),
('उ','u'),
('ऊ','u'),
('ऋ','ri'),
('ए','e'),
('ऐ','ai'),
('ओ','o'),
('औ','au'),
('ा','a'),
('ि','i'),
('ी','i'),
('ु','u'),
('ू','u'),
('ृ','ri'),
('े','e'),
('ै','ai'),
('ो','o'),
('ौ','au'),
('ॉ','au'),
('।', '.'),
('ों', 'onn'),
('़', ''),
])

punct_dict_1 = OrderedDict([
 (',',' ,'),
 ('.',' .'),
 ('।', ' ।'),
 ('?',' ?'),
 ('!',' !'),
 ('"',' " '),
 (':',' : '),
])

punct_dict_2 = OrderedDict([
 (' ,',','),
 (' .','.'),
 (' ।', '।'),
 (' ?','?'),
 (' !','!'),
 (' " ','"'),
 (' : ',':'),
])

colloquial_dict = OrderedDict([
(' kee ', ' ki '),
(' kaa ', ' ka '),
(' jee ', ' ji '),
(' yaa ', ' ya '),
(' lie ', ' liye '),
(' men ', ' mein '),
(' meṉ ', ' meiṉ '),
(' n ', ' na '),
(' sakate ', ' sakte '),
(' thee ', ' thi '),
(' usakaa ', ' uska '),
(' usako ', ' usko '),
(' unakee ', ' unkee '),
(' usakee ', ' uskee '),
(' humane ', ' humne '),
(' tumane ', ' tumne '),
(' usane ', ' usne '),
(' apane ', ' apne '),
(' a ', ' aa '),
(' saahab ', ' sahib '),
(' apane ', ' apne '),
(' apani ', ' apni '),
(' karate ', ' karte '),
(' apako ' , ' apko '),
(' tumako ' , ' tumko '),
(' isake ', ' iske '),
(' isakee ', ' iskee'),
(' isako ', ' isko '),
])

###################################################


def main():

  text=fin.read()

  for key,value in punct_dict_1.items():
  	text=text.replace(key,value)

  for key,value in d2r_dict.items():
  	text=text.replace(key,value)

  for key,value in punct_dict_2.items():
    text=text.replace(key,value)

  for key,value in colloquial_dict.items():
    text=text.replace(key,value)

  print(text)
  fout.write(text)


if __name__ == '__main__':
    main()
