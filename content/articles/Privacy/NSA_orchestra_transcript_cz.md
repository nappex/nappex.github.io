---
Title: Transcript of NSA operation orchestra in czech
Date: 2022-05-11
Category: Privacy, Networks
Tags: networks, privacy, talk
Slug: NSA-orchestra-transcript-cz
Authors: David
Summary: Czech translation of transcript to talk about NSA habits
Status: published
---

[TOC]

# Úvod
Tento text slouží jako český překlad přednášky NSA operation orchestra
z konference FOSDEM, která proběhla v roce 2014.

Originální přepis přednášky v anglickém jazyce nalezenete na těchto
stránkách [zde](https://nappex.github.io/myblog/NSA-orchestra-transcript-en).

## Základní informace k přednášce

NSA annual state report by Poul-Henning Kamp (FreeBSD vývojář) - FOSDEM 2014

odkazy na video:

* [youtube](https://www.youtube.com/watch?v=fwcl17Q0bpk)
* [vimeo](https://vimeo.com/86567061)
* [FOSDEM](https://ftp.fau.de/fosdem/2014/Janson/Sunday/NSA_operation_ORCHESTRA_Annual_Status_Report.webm)

odkaz na prezentaci:

* [Poul-Henning Kamp personal page](http://phk.freebsd.dk/pubs/FOSDEM_2014.pdf)


Přednáška se skládá z těchto částí, proto ji autor nazývá jako orchestr:

**Playlist spoiler**:

* Electric Light ORCHESTRA: Confusion

* ABBA: Money, Money, Money

* Backman Turner OVERDRIVE: Taking Care Of Business

* QUEEN: Bicycle Race

* Beastie BOYS: Sabotage

* PASADENA Roof Orchestra: Pennies From Heaven


# Rozhovor s Poul-Henning Kamp před přednáškou:

Poul-Henning Kamp bude mít přednášku s názvem
*NSA operation ORCHESTRA: Annual Status Report at FOSDEM 2014*

1. Q: Mohl byste se stručně představit?

    Jsem šest stop vysoký lidoop, který si vydělává děláním divných věcí
    na počítačích.
    Jsem v počítačové branži 30 let a v open source 29.
    Býval jsem jeden z hlavních vývojařů ve FreeBSD, nyní jsem ten
    člověk, který stojí za projektem Varnish HTTP accelerator.

2. Q: O čem přesně bude vaše přednáška?

    A:

    Má přednáška je o vztahu NSA - FOSS.

    Myslím si, že jej potřebujeme přehodnotit.

3. Q: Co vás k tomuto tématu přivedlo, proč se vlastně o něj zajímáte?
    Proč je pro vás tak důležité o tomto tématu přednášet?

    A:

    Inspirací pro mě je odhalení, které udělal Edward Snowden.
    Mezitímco se hlavně zaměřili na širokou veřejnost a politiky,
    se zde objevuje zcela odlišné sdělení pro IT svět a obzvláště pro
    FOSS komunitu, ale většině lidí to uniká.

4. Q: Mohl byste objasnit hlavní sdělení, které chcete přednáškou předat?
    Kdyby si lidé měli odnést jednu věc z vaší přednášky,
    co by to mělo být?

    A:

    “Komu věříte a proč...”

5. Q: V co doufáte, že dosáhnete svou přednáškou? Co očekáváte?

    A:

    Doufám, že se lidé budou smát a přemýšlet.

6. Q: Jaká je role FOSS v této době sledování NSA a dalších pochybných agentur?
     Jsme schopni bojovat se souřasnou krizí soukromí s pomocí FOSS?

    A:

    Tohle jsou velmi dobré otázky, doufám, že má přednáška inspiruje lidi, aby
    přemýšleli a zkoumali důkazy k nalezení odpovědí.

7. Q: Užil jste si předchozí FOSDEM konferenci?

    A:

    Ne, nikdy jsem ještě na FOSDEM konferenci nebyl.


# Český přepis přednášky NSA operation ORCHESTRA: Annual Status Report
**Moderátor:**

Děkuji vám, že jste se k nám připojili. Nyní bude Poul-Henning Kamp,
také možná lépe známého pod přezdívkou phk, a jeho přednášku na téma
annual status report on NSA operation orchestra.
Vítejte.


## Přednáška
**Poul-Henning Kamp:**
Děkuji.

### Úvod - O co se jedná?
Před pár lety se objevila nová věc, která mě přinutila si sednout na židli
a přemýšlet. Nejspíše to není ta věc nad kterou teď přemýšlíte, že FBI odhalila
milostnou aféru ředitele CIA, tím že vyměnila tuto telekomunikaci.
Býti bezpečnostním výzkumníkem, což není něco, čím bych se normálně nazýval,
znamená umět pracovat s představivostí. V situacích jako je tato si musíte sednout
a pokusit se přemýšlet stejně jako mysl těch, kteří to provedli.

Později jsme získali odhalení od Edwarda Snowdena a já si sednul a
přemýšlel co bych dělal kdybych měl rozpočet jeden bilion dolarů, pověření
a příkaz nasbírat tolik komunikace, kolik je jen možné.

### Operation ORCHESTRA

Pak před týdnem jsem dostal email of Filipa, nějaký chlápek z FOSDEMu,
v tomto znění:

"Potřebuji nějakého přednášejícího, co děláš příští týden?"

Protože dlužím Filipovi hodně laskavostí, řekl jsem:

"můžu udělat přednášku"

a tak jsem si sedl a vytvořil dnešní prezentaci.

Základní předpoklad k mé přednášce je, že byste si měli představit juniorního
pracovníka NSA přijíždějícího do Bruselu, aby poskytl NATO aktuální informace
o jednom z programů NSA a namísto toho tam skončí, protože je Američan.

Kdybych měl plno času, udělal bych tu část s černými vlasy, slunečními brýlemi
a všeho toho, ale budete si to muset pouze představit.

Tohle je Operace "Orchestr" (pozn. fiktivní tajná operace NSA vymyšlená autorem
přednášky). Jsem si jist, že žádné informace z této operace, která je samozřejmě
v nejvyšším stupni utajení, neopustí tuto místnost.

### ORCHESTRA operation na první pohled

Základním úkolem Operace "orchestra" je redukovat náklady při sběru informací.
Organizace NSA má ve svých regulích, které řídí jejich financování, sbírej
co nejvíce infromací je možné, ale jako zodpovědná vládní organize se je
snažíme sbírat s co největší hospodárností.

Operace "orchestra" je tedy o redukování NSA nákladů při sběru informací.
Veškerá činnost musí být přes vedení operace.
Nejsou dovoleny žádné tajné operace typu
"black-ops". Black ops jsou operace, kde se porušují zákony.
Nemáme žádnou speciální autorizaci, nemáme žádného 007 s povolením
odposlouchávat nebo něco podobného.

A možnost nebo způsob, jak to udělat je, že se pokusíme zlikvidovat činnost,
která zabraňuje oslabování šifrování. Snažíme se naopak umožnit přístup
k informacím a zároveň frustrovat hráče, kteří se nám pokoušejí to ztížit
(např. kvalitním šifrováním).

### Historie
Něco k historii...
Ve skutečnosti se jedná o velmi starý program.
Začal velmi brzy po úniku Inter-Netu.

Internet byl vymyšlen jako projekt pro armádu, úmyslem nebylo, aby jej
začala používat babička, teroristi apod. Velkým problémem internetu
narozdíl od telekomunikační sítě tak jak ji známe je, že do něj můžete zapojit
cokoliv aniž byste k tomu nejdříve dostali nějaké povolení.
Lidé si mohou stavět své vlastní počítače a zapojit si je do sítě.
To jste nemohli udělat se starou telekomunikační sítí.
To jste šli do FCC (Federal Communications Commission) a dostali jste
malou nálepku a všechny další náležitosti.

Najednou jsme v této neregulované síti. A v této síti je podstatně více
účastníků. Kdysi jsme si povídali jenom s AT&T,
která tak mohla odposlouchávat kohokoliv. A také to ve velkém dělali.
Nyní ale máme milióny internetových sítí a mnoho z nich je v zahraničí.
Nemůžeme se vypořádat se všemi z nich. Musíme nalézt škálovatelní metody,
které budou schopny se s tím vypořádat.
A náš pokus zkoušet manipulovat vnější protokoly na místo protokolů tcp/ip,
bohužel selhal. To by pokračovalo v modelech spojované komunikace telefonní
sítě, ale to nefungovalo. Bylo to opravdu velmi špatné.

### Původ Orchestru

Zdrojem je pracovní skupina deep thought (hluboké myšlenky?),
která přišla s těmito nápady ohledně snahy získat kontrolu
nad klíčovými pákovými body (key leverage points) na internetu.
Stále zde existují místa, kde se věci skutečně dějí.

Ovlivňovat průběh k naší výhodě and identifikovat klíčové osoby,
kde levně můžeme získat velký účinek.

### ABBA operation
Jedna z nových věcí v operaci orchestr je něco, čemu říkáme ABBA operace.

A tohle je velice starý problém. Nějaký chytrý vynálezce vynalezne něco,
čím nám více zkomplikuje naše životy.

My tohle nechceme.
Takže co budeme dělat?

#### Stará škola
Způsob, kterým bychom tohle udělali by byl, že bychom se jej snažili uplatit,
udělat s ním pracovní poměr nebo něco podobného.
Zařadili bychom jeho patent mezi utajované.
Takže by měl sice patent, ale nemohl by ho nikomu ukázat.
V některých případech můžeme lidi zavázat mlčenlivostí, s ohledem
na národní bezpečnost a tak dále. Prezident si s váma podá ruku a všechny
tyhle věci.
Ale do toho je zahrnuto hodě papírování a zanechává to za vámi plno stop.
Také do toho musíte zapojit mnoho lidí. Jedná se tedy o druh velmi dráhého
procesu.

#### Nová škola
Nalezli jsme nový způsob, jak tohle dělat.
Využíváme surový trh kapitalismu.
Jendoduše házíme peníze na problém.

Nalezneme nějaký start-up, který nám bude způsobovat problémy.
Samozřejmě čteme HackerNews a podobné noviny.

Zde je rizikový kapitalista, který start-up kontaktuje se slovy:
"Oh, viděl jsem vás v HackerNews můžu za vámi někdy zaskočit?"

Tenhle chlápek se zastaví, ukecává je a zve je ven na luxusní večeře, kde
upustí 10k dolarů, aby dostali lepší místa nebo něco podobného.
Vše probíhá v duchu - o všem mě informujte, jak vám můžeme pomoci apod.

Nyní když už ví, co chystali, přijde domů a začneme hledat dobrý patent.

Když máme štěstí, hledaný patent už je u jednoho z přátel od NSA a
natáhl by linku k IBM a k jejich patentovým právníkům.
Vy byste se měli na tyto chlapíky podívat, protože jsou strašlivě blízko
vašemu patentu.

Ne méně jako IBM, vyšleme pár patentových právníků s mnoha patenty
a start-up bude mrtev.
Velmi často dokonce zavolají zpět rizikovému podnikateli se slovy:
"Oh, omlouváme se..."
Takže dostaneme zpětnou vazbu a víme, že to ukončili.
To je úžásné, to je jako 30k dolarů.

Jestliže patent není v něčem, co nazýváme správné ruce.
Budeme se zjevně snažit nalézt lepší patent nebo jej zkusíme převést.
If the patent is not in, what we call good hands.
Zde existují nějaké patentové společnosti, které spolupracují
a patent odkoupí. Pak jej mohou používat pod naším jménem.

### Operace PASADENA
Jedná se o velmi výhodný proces.
Využili jsme nějaké podobnosti k vyřešení dalšího starého problému.
My máme totiž problém s lidmi, kteří pro nás pracují v odlišných situacích
a my je za jejich práci potřebujeme odměnit.

A tohle býval druh nějaké podvodné operace,
víte, jakože najednou by vyhráli v loterii.
Nějaký vzdálený příbuzný by jim zanechal majetek.
Nemůžeme se omluvit za "Nigerian scam", ale to je typ toho jak to začalo.
Lidé dostávají užásné pracovní nabídky. Někdy i nové identity
a tenhle typ možností.
Vy musíte ohnout mnoho pravidel, aby jste byli schopni tohle vše udělat.
Je velmi těžké tyto stopy skrýt a Google to učinil neuvěřitelně obtížné.
To je něco jako:
"Oh, vy jste náhle ztratili vzdáleného příbuzného, jaktože nemůžeme k této
osobě najít vůběc žádné stopy na googlu.
To by dopadlo s podivením: "hmm?!"

Ne. Dnes je to daleko jednodušší.
"Šéfe, končím tady."
Poté si udělá start-up, najde rizikového podnikatele, který vyklopí pár miliónů
do start-upu.
A potom sedí a prochází internet pár roků nebo cokoliv jiného co chce dělat.
A je to!
Kancelářská práce je zcela běžná, existuje na to i daňový formulář.
To je vlastně jedna z daní, díky kterým jsem nakonec vytvořil společnost,
která fungovala.

To je přesně ono, Rubín.
Tohle je způsob, jak dostat peníze k našim cílům.
Tohle je způsob, jak můžeme přesunout peníze do lidí, po kterých chceme,
aby něco dělali.

### OVERDRIVE aktivity
Na druhém konci žebříčku, mluvíme-li ohledně peněz, máme něco, čemu říkáme
overdrive aktivity (aktivity rychloběhu).
Jde o ovlivňování obchodních rozhodnutí.

Využijeme NSA kontrakty na poměrně velké nákupy IT služeb.
Můžeme si sami do značné míry rozhodnout, komu zakázku dáme.
Nejedná se o férové nakupování, když se jedná o národní bezpečnost.
Dobrá věc na smluvním právu je, že sním můžete dělat cokoliv.
Nemůže být přímo nezákonný,
nemůžete mít smlouvu na něčí zabití, ale můžete smluvně udělat cokoliv
co je v mezích zákona.

Jedná se o velmi dobrý mechanismus, jak řešit velké problémy.
Špatnou zprávou jsou obvykle velcí hráči, kde jsou právníci, to je pak
trochu drahé.
Můžou být nějaké cíle k zaměření, ale jedná se o dobrý způsob, jak
řešit problémy a jedná se vlastně o způsob, jak jsme vyřešili problém
s aplikací Skype.

#### OVERDRIVE: příklad programu Skype
Skype byl program na způsob peer-to-peer, kde byl šifrován video i zvuk.
Nepoužívali standardní protokoly. Byli mimo FCC. My nemůžeme říct
jen tak "tohle je nelegální!" a zakazát je.
Nejedná se o open-source. Ani to nekoupili přes naše usílí o jejich nápravu.
Je populární u nezávislých herců a skupin na lidská práva
například v Bělorusku.
Také je velmi oblíben politickými hnutí, která jsou v nepřízni
politického směru USA na blízkém východě (střední východ).
Samozřejmostí je používání teroristy, tím jsem si naprosto jisti.

Nejprve jsme se spolupracovali s eBay, která je velmi významný přítel NSA.
Po menším přemýšlení a schválení zpravodajskou službou pro nás nakonec
Skype koupili.
Bohužel to zpackali.
Koupili pouze přístup do Skype.
Nezískali zdrojové kódy, ani kontrolu nad sítí.
Něco jako "Achjoo".

Není zřejmé proč jejich právníci nebyli instruování, nicméně jsme nezískali
co jsme chtěli.
Takže jsme to museli zkusit znova, ale nemůžeme to udělat,
když tady sedí eBay.
eBay musí Skype znovu prodat ve ztrátě a už není tak docela dobrý přítel NSA.
My neustále pracujeme na těchto vzájemných vztazích.
My dostali Microsoft, který nám to místo toho nakoupí.
A nyní dostali vše, co potřebujeme.
Nyní Microsoft změnil architekturu Skypu na centralizovanou.
Celá komunikace je nyní vedena přes Microsoft servery, velmi výhodné,
bude zde dešifrována když to bude potřeba.
Byla to velmi nákladná operace, ale bylo to nezbytné udělat.
Nemohli jsme mít komunikující lidi mimo naše soudní pravomoce.

#### OVERDRIVE: Summary
Je to opravdu velké kladivo.
Vyžaduje to podpisy, které jsou velmi vysoko nad mou mzdou,
ale jedná se o velmi dobrý způsob, jak dělat věci.
A jedna ze zajímavých věcí, které se zde vyskytují jsou velcí hráči.
Bez ohledu na to co udělají, je to vynikající.
"Sice tomu nerozumíme, ale je to vynikající."
"Nedává to smysl, ale je to vynikající, protože on je génius, víme to."
Můžete dělat skutečně divné věci tímto způsobem, zcela otevřeně
a nikdo ani nemrkne okem. Máme to rádi.

### QUEEN activities
Pak zde máme Queen aktivity a na tomhle pracujeme hodně.
Open-source a internet jako takový je aktivita založena na konsenzu,
což znamená, že se nich může podílet kdokoliv.
Nikdo nemá speciální pravomoce.
Mohou se zde vyskytovat někteří lid, kteří jsou první mezi rovnými a podobné
typy výmyslů, ale není to jako, že je zde někdo,
kdo má ve své zadní kapse právní listinu a může říct:
Já to říkám protože tento zákon číslo bla.

Jedná se o velmi hrubý konsenzus a fungující kód,
s výjimkou současných dnů, kdy je to spíše
o velmi dlouhých, komplikovaných standardů, než o více fungujícím kódu.
Objevuje se zde ve velkém také mezinárodní součinnost, což znamená,
že se nemůžete odvolávat na lidové vlastenectví, nemůžete říct:
"pro dobro národa, musíš tohle...". Tohle moc nefunguje.
Také se jedná o velmi významnou masu talentů, která je ale problém,
protože odhaluje naše věci (nekalosti).

Teoreticky tohle vše spadá pod státní tajemství,
protože v mnoha případech se jedná o zahraniční vztahy,
ale
because these are foreign relations in many cases,
ale "Foggy Bottom" (přízemní mlha, inverze, jméno městské části Washington DC)
není natolik technicky zdatný když na to přijde.
Diplomaté jsou naprosto nevystopovatelní díky nastavení jako IETF.
Když vstoupíte s kravatou mohou se na vás dívat divně.
A našimi cíli nejsou .....,
oni smí být v rozporu s cíli státních tajemství.
Do toho všeho jsou zde zahrnutí další hráči (jako DoC, NIST, DoD, FBI, CIA),
s kterými nemusíme nutně ve všem souhlasit.
Jedná se trochu o komplikovaný prostor.

Takže to co děláme je, že máme páky na naše existující zdroje.
Máme webové zdroje vryté s přáteli NSA.
Máme svobodné agenty. Lidé, kteří něco provedou až po zdravé úvaze.
A taky máme, co my nazýváme bezelstné dobrovolníky,
kteří mohou být manipulováni tak, aby splnili naše nabídky
bez toho aniž bychom jim za to něco zaplatili.
To je velmi dobré, protože zde neexistuje žádná vystopovatelnost.
Takže co mi děláme je, že my rozmístíme velmi pečlivě navrhnuté
přednáškové místa. Nečestně pokud můžeme.
Máme oddělení, které má na svých dveřích nápis,
na kterém stojí "PSYOPS pro nerdy"
Myšlenkou je směrovat diskuzi na těchto fórech k nebo od
podrobných témat, tam kam chceme.
Obecně se velmi často nerušujeme budovaný konsenzus,
která jde proti našim účelům.

#### QUEEN: úspěšné příklady SSC (Self Signed Certificates)
Certifikáty podepsané sám sebou, které jsou v prohlížečích
to je velmi dobrý příklad.
Certifikát podepsaný sám sebou je certifikát, který zaručuje, že se jedná o mě.
Ve skutečnosti mě nepotrzuje jako nevinnost světa,
ale pokud mám takový certifikát na svém webovém serveru, můžete pomocí
svého prohlížeče vytvořit tajný kanál s mým serverem.

Tohle pro nás není příliš dobré, protože budeme muset utratit velmi
nákladné zdroje na odšifrování kdykoliv to bude potřeba.
Ale lidi tohle mohou dělat prakticky zadarmo.
Jediná důvod proč to lidi nedělají je, že to po nich opravdu nechceme.
Bylo by nápadné kdyby to bylo jak výchozí nastavení na Apache, vždy
jen udělej Certifikát podepsaný sám sebou, pokud se nejedná o pravý certifikát.

Už jsme strávili hodně času v této místnosti.
A na některých přednáškových místech, které bez pochyby neubližují,
to může vypadat takto:
"Oh, ale utajení bez ověření je zbytečné, mohli byste mluvit s NSA
a ani byste o tom nevěděli!"

Tenhle máme opravdu rádi, jsem na tento opravdu pyšní.
"To dává falešný pocit bezpečí!"

To hlavní ohledně těchto věcí je, že pokud je opatrně upravíte,
promlouvají pak k lidksé politické náklonosti.
Pokud jsou lidé lehce paranoidní, aby s tím začali,
což mnoho lidí, ktěří dělají v IT bezpečnosti jsou.
Pak to je to něco jako:
"Jasně, ne to bych nedělal, pokud nemám 2048-bit obrněnou garanci toho,
že vím kdo je na druhém konci, potom to není dobré."

Pokud se pokoušíte v dnešní době dostat na webový server, který má sám sobě
podepsaný certifikát, dostanete tyhle škaredé upozornění, kde je:
"Oh, ty bys neměl tohle dělat, tohle je nebezpečné. Jsi si opravdu jistý,
že víš co děláš a že máš na tohle PhD titul?"
A čím více tlačítek zmáčknete, tím více varování byste měli dostat.
Od této chvíle se babičky a teroristé internetu úplně vyhýbají.
A vtomhle je jedna věc, někteří z našich předchůců, které opravdu
milujeme za to, že obstarali certifikáty x.509, to bylo opravdu úžasné.
Pokoušeli jste se někdy podívat na všechny ty věci, které jsou
v certifikátu, nikdo z toho nerozumí ani slovu.
Většinou to vypadá nějak takto:
"Ne, nerozumím tomu, jdu odtud pryč."

Tohle je velmi dobrý příklad toho, jak program QUEEN funguje.
Jednoduše přimějte lidi aby nedělali věci, když na ně nezaměří svou pozornost.

#### QUEEN úspěchy
Oblkopen dalšími věcmi, které jsme udělali v QUEEN je, že zde není
žádný multihomig
(*poznámka překladatele*: síť, která je přípojena k více ISP najednou,
když jeden ISP vypadne přepne se na jiného) bez možnosti vlasnit své vlastní
AS čísla. (AS - autonomní systém. Vlastní autonomní systém mají typicky ISP,
datacentra nebo jiné společnosti s rozsáhlou počítačovou sítí)
Což znamená, že my můžeme vždy najít, kudy jde veškerý váš provoz, protože vždy
teče přes vašeho ISP (internetového poskytovatele).
Nepotřebujeme vás sledovat kolem sedmi odlišných stran apod.

Také zde neexistuje, žádné flow routing v IP verzi 6
Když bylo IPv6 předloženo byl v něm velmi chytrý návrh, který říkal,
že bychom neměli zabouchnout komunikující adresy ve všech paketech,
že to budeme dělat pouze v prvním paketu.
Poté dostaneme malé plovoucí (desetinné) číslo,
které řekne, že všechny tyhle pakety plují tímto směrem
And then we'll get a small flow number,
that says all the packets in this flow go that direction,
ale to by ovšem pro nás bylo velmi nepraktické,
protože bychom museli sledovat všechny tyhle plovoucí čísla najednou.
Když máte IP adresu v jednom balíčku, můžete prostě jen sebrat všechny
ty pakety a máte všechny informace, které potřebuje od všech paketů
za celou dobu.
Nepotřebujete mít všechny plovoucí stavy a na konci znát co každý tok znamená.
To byl veliký úspěch - ne že by IPv6 byla, ale že pro nás už
nepředstavuje velký problém.
Moudré schromážďování, ale připraveni IPv6 vystřelit.
Také jsme zde vytvořili prostředí, kde prakticky není možné kompatibilně
poslat zašifrovaný email.
Tam kde je na obou koncích šifrování nutné použít stejný program
jsou všichni potopeni, protože v opačném případě to nebude fungovat
a výsledek tak nebude nikdy použitelný.

A také se nám dařilo zpozdit službu Voice over IP (VoIP), dokud se nestala
příhoda se Skypem.
Voice over IP je velký problém,
protože nemůžete automaticky hledat skrze hlasová data.
Je daleko snažší, když si lidé navzájem posílají emaily,
hledáte prostě jen určité patterny apod.

Takže tohle jsou naše velmi velké úspěchy v QUEEN programu.

#### QUEEN nedávná práce
Nyní pracujeme na standardu HTTP 2.0.
Chtějí, aby tam bylo velké zastoupení a všechno bylo TLS,
které by mohlo být nepohodlné.
Pokoušíme se nasměrovat špatným směrem a tím se pokusit celý proces zhatit.
Mám tím na mysli, koukněte se na dobrou stránku věci, pokud bychom je přivedli
do TLS, dostali bychom všechny root certifikačních autorit,
které by dělali práci za nás.
Takže máme všechny klíče pokud přijde na to, že uděláme
man in the middle či jiné podobné věci.
Pokud to je možné raději, zůstaneme zašifrovaní.
A jako fallback se je snažíme natlačit do nějakých špatně navržených protokolů.
Bohužel jeden z nich zdá se býti už odhalen, ale pracujeme na vydání nového.
To už není práce našeho oddělení
my se pouze snažíme natlačit lidi do druhu věci.

#### QUEEN metody
Metody, které používáme jsou obyčejný strach, nejistota a pochybnosti.
Musíte být nejistí a pochybovační.
Hraní si s tématem GPL versus BSD karta stále funguje, je to úžasné.
To je už jako: "Oni se tímto tématem snad nikdy neunaví?"
Ano, to je opravdu užasný kryptografický kód,
"já vím, ale nemůžeme jej použít z licenčních důvodů."

Diskuse typu bikeshed jsou úžasné. (*Poznámka*: bikeshed znamená nikdy
nekončící diskuse, termín bikeshed
vymyslel sám phk jako reakci na diskusi okolo funkce "sleep",
[zde](http://phk.freebsd.dk/sagas/bikeshed/#the-bikshed-email) je
k tomu celý článek),
Někdy stačí pouze jeden jediný email od neznámé osoby, který je
schopen na měsíce vykolejit práci celého open-source projektu.

A můžeme nasát ohromné množství šířky vlnového pásma kryptografů
s falešnými návrhy na kryptografii.
Pošlete návrh, který říká:
"Oh, vymyslel jsem tento úžasný způsob,
jak to udělat"
Ostatní stráví měsíc přehrabováním se v tomto návrhu,
namísto dělání skutečné (prospěšné) práce.

#### QUEEN nedávná práce
Takže takhle to nějak ve světě funguje.
Jedna z oblastí na kterou se v současné chvíli změřujeme je tlak na
změnu používaní certifikátu modelu PKI na model DANE, který schvaluje
vaše certifikáty skrze DNS.
One of the current focus areas is that there's a push to go from the certificate PKI model to DANE which is getting your certificates approved through DNS.
A tohle je cena zaplacena za to, že si lidé uvědomili skutečnost, že
všichni mají kompromitovaný CA/PKI systém.
Co mám na mysli, je že, pokud se podívate do svého prohlížeče naleznete
tam asi 200 schválených CA's (certifikačních autorit) a polovina z nich
je vlastněna neznámými službami napříč celým světem.
V tuto chvíli je to už trochu zbytečné.

Lidé se tak chtěli přesunout do něčeho co nazýváme DANE protokol.
Myšlenkou zde je validace certifikátu za použití DNSSEC.
Takže máte tento podpis v root zóně a ten podepisuje další klíč, a ten
podepisuje další, a ten podepisuje další, který říká, že můj
server používá tento certifikát.
Nyní tomu můžete věřit, věříte pouze jednomu klíči, že?
Takže výhodou modelu PKI/CA je, že máme dneska přístup, ale DANE projekt
by tohle velmi rád, protože nyní věříme pouze jednomu jedinému certifikátu.
"Šťouch, šťouch, mrk, mrk, řekl on záměrně .... "

A dokonce nejelpší část toho všeho je, že nerozumím tomu jak tito
údajně profesionálové mohou přehlédnout toto:

DNS je jen UDP.

Je daleko snažší udělat útok typu "packet-race" s UDP než s protokolem TCP.
Prostě pošlou DNS požadavek a vy nebudete první, hotovo.

### BOYS - speciální dar
To je další velmi zajímavý program na kterém teď děláme.
Doopravdy je to vlastně inspirováno "field accident".
Kdy jsme museli vystěhovat vysoce rizikový a vysoce kvalitní zdroj
a neměli k tomu žádné vhodné vybavení poblíž jeho polohy.
Vytvořili jsem z něj tedy nezávislého dodavatele.

Příběh byl něco jako unavený šéfem a nějaká špatná politika společnosti,
a tak dále ... Jsem zaseknutý nemám se, kde posouvat...
Měl jsem štěstí, že jsem našel nějaké zákazníky a tak dále.
Zatímco si jen tak sedí, tak strávil nějaký čas na nějakých open source
projektech... Musel něco dělat.
Všimnul si nějakých příložetostí k přípravným pracem.

Většina open-source projektů je založena na důvěře.

Není v nich oficiální kontrola,

není v nich  kontrola kontrola životpisů,

ani kontrola, zda jste opravdu ten, za koho se vydáváte.

V praxi to často vypadá následovně:
"Oh, jsem týpek z Ulaanbaataru a zde máma pro vás nějaké patche."

Pokud posíláte dobré patche po několik let, lidé vám začnou důvěřovat,
a přestanou kontrolovat vaše patche a nakonec vám mohou dát i "commit bit",
takže můžete přidat vaše změny kódu rovnou sami, protože je to mnohem snažší.
Jedná se o úžasné prostředí, kde lidé mohou přijít a nikdo o vás
neví jestli jste ve skutečnosti pes nebo NSA agent.
Tímto způsobem můžete nejen sbírat informace o projektu přímo ze vnitř,
ale jakmile si vybudujete důvěru můžete začít přímo ovlivňovat jejich kód.

Získat právě zde pochopení je pro nás velmi snadné, představte si to jako:
"Oh ano, víš já jsem sys-admin této neziskové věci tak dlouho, dokud
emaily fungují a tiskárny tisknou."
Tohle celé je takové šumění, mám tím na mysli, že si tu tak sedím sedm hodin
denně a nedělám ani hovno.
"Ok, cool"
Je tady nějaký chlapík, je to jeho čas.. dodává dobrý kód,
my jsme s tím v pohodě.
Jedna z věcí, které tímto zjistíme je,
že by to tak ve skutečnosti mohlo fungovat.
Ve skutečnosti je tohle jeden z našich lidí.
On sedí někde v přední části nějakého obchodu, aby pro nás zastavil,
co já vím, opadávání dubového listí přes cokoliv vás může napadnout
a celé to je jako ta nezisková věc před chvílí.
Vlastně to je áš soused, který sedí v té přední části toho obchodu.
A potom vždy je potřeba někdo, kdo zajistí aby jim počítače, které mají
fungovaly v této malé tajné pasti.
A potřebujeme mít internet a stůl pro našeho člověka.
Takže to je velmi pohodlné.
Šéfové mohou vlastně prohlašovat něco jako:

"Oh, děláme kooperativní práci a šetříme tím peníze" apod.

Je to opravdu velmi dobré.

Samozřejmě nemůžete přijít a začít přidávat zřejmé zranitelnosti do kódu.

Lidé by si tohohle všimli. Musí to být více záludné.

Programovací chyby.
Znáte je jako nepozornost, středníky a tak dále,
you know the careless, semicolon yade, yade serial one based error,
všechny tyhle klasiky.
Nemůžete je dělat přímo vy, to by bylo nebezpečné.
Nejlepší je říct:

"Oh, dostal jsem tuto opravu na kód a mrknul jsem na to a vypadá to OK."

A potom to začleníte do kódu.

Lidé si všimnou, když váš kód stojí za nic, ale jestliže přijmete opravu
od někoho jiného, která nění jak se říká úplně podle standardu.
Všichni můžou mít špatný den.

Obecně je těžší pochopit kód, jehož kritické části jsou úmyslně zamlžovány.
Usnadňuje to následně vytvořit skoro cokoliv co bylo vašim záměrem.

Další mimořádně úžasnou praxí pro kryptograficky citlivé věci je vždy vytvoření
klamavá či mylné dokumentace. Dále zavádějící výchozí hodnoty,
které zapřičiní, že se nedějí věci, které lidé očekávají.

Nemusí se nutně jednat o core code, nemusí to být kernel operačního systému.
Ve FreeBSD je 20 000 balíčků softwaru.
Jsou zde používáné buildy.
Vyskytují se zde nějaké patche, které jsou ptořebné pro FreeBSD a tak dále,
ok vybuildi to a máte použitelný balíček.
Nikdo se nikdy na ty patche ani nepodívá.
Kdokoliv kdy portoval tenhle kus softwaru dělající tyhle patche, ví
že to akorát zabalí a je to hotovo. Nikdo to nikdy nezkontroloval.
Možná, když se nastavuje něco jako "setuid" program, tak někdo
na to mrkne, ale obecně se nikdo nikdy na tyhle patche
ve FreeBSD kolekci nepodíval.

A měli by je kontrolovat!

Tohle je náš plakátový chlapec.
Generator náhodných čísel v Debianu.
Tohle je opravdu nádherně provedeno.
Je tady chlápek co pošle sadu patchů, však víte.
Program Valgrind sice dostává stížnosti,
ale já nevidím nic rozumného co by jsi měl jen tak smazat.
A takhle to udělali
Takže po dobu dvou let, všechny debiany měly mizerný generátor
náhodných čísel, který umožnoval brute-force SSL klíčů a takovéto věci.
Hotovo.

Tady skončíme velmi dobrým bonusem.
OpenSSL je korunovační klenot.
OpenSSL je standardní knihovnou, pokud chcete pracovat s kryptografii.
Přimět SSL aby pracovalo proti všem prohlížečům a všem těmto věcem,
bez použití OpenSSL je velmi složité.
Přečtení manuálů a zdrojové kódu OpenSSL není složité,
to se velmi blíží něčemu, co můžeme nazvat jako téměř nemožné.
Má to něco okolo 300 000 řádků kódu.
Takže vám přeji mnoho štěstí s přečtením.
Dokumentace je nedostatečná až zavádějící.
Výchozí stavy jsou ošidné či zavádějící, nedělají co si myslítě, že dělají.
Nemáte představu kolik tohle ušetřilo peněz ve sběru dat.

### Operation ORCHESTRA současný stav
Takže celkový stav operace orchestra je obrovský úspěch,
utratili jsme méně než třetinu procenta rozpočtu NSA.
To pravděpodobně stálo náklady na sběr okolo 50%.
Tohle drží většinu internetu ve formě plain textu.
It's kept most of the Internet in plaintext.
A nikdy nebyl odkryt.
Byl to Snowden, který nemá vůbec žádné papíry k Orchestře.
Tohle si nepřečtete v Guardianu, protože je to vše
pohřbeno v nudných odděleních.

Operace OVERDRIVE je o nákupech.

BOYS je správa příslušenství či vybavení.

ABBA a Pasadena je personální, něměl přístup k ničemu z toho.

Děkuji!

### Závěrečná řeč
Běžnou reakcí open-source prostředí na Snowdenovo odhalení, je:

"Potřebujeme zesílit protokoly. Zajistit, že SSL bude všude."

A můj názor je, že tohle míjí hlavní smysl toho všeho.
Věci, které byli doposud publikovány ve Snowdenových dokumentech,
jsou věci, které může pochopit široká veřejnost přečtením si jich v novinách.
Věci, které by nás zajímaly ještě nebyli publikovány a nejspíše ani nikdy nebudou.
Přidávání dalších pokusů ke většímu zvýšení šifrování s největší pravděpodobností
povede k tomu, že budeme mít více pokaženého šifrování na internetu.
Nejedná se o technický problém, jedná se o politický problém.
To musí bát vyřešeno politickou vůlí.
Mám na mysli najděte politiky ve své zemi, kteří mohou pochopit tento
problém a ujistěte se, že tomu opravdu rozumí.
Pokud njste schopni takové politiky najít, tak sežeňte politiky, kteří tomu rozumí.
Politická vůle je obnovitelný zdroj, použijte svou tužku, když budete volit
nebo budete voleni.
Jedná se o budoucnost společnosti našich dětí a našich pradětí na kterou se díváme.
A my jsme ti chlápci, kterým tak trochu ujiždí loď.

## Q&A SECTION

There's a time for questions, if anybody want.
We are going to take questions and afterwards FOSDEM staff will perform the closing talk.
So please don't go away.

Could ask anybody that's leaving to try and keep it quiet boss Q&A is going on.

1. **Question**: So one of the biggest security leaks for the OpenSSL for instance
    is actually their documentation and all the stuff,
    people generally say like: I'd rather be coding?

    **Answer:**

    Yes. Yeah I mean OpenSSL is a catastrophy in my eyes.
    And should be thrown out and started from scratch,
    written in a readable style and documented.

2. **Question**: Yeah, I found your last remark very interesting referring
    to politics and especially in FOSDEM. Well we had this a little
    encounter where it was about politics and FOSDEM and then the
    reaction was like "no no no politics it's FOSDEM it's only about
    open source but how would you feel about that the relationship
    between open source and politics apart from what you
    just said in the end.

    **Answer:**

    I have the same feeling about it I have about global warming.
    It may be that the open source community doesn't believe in
    politics that doesn't mean politics doesn't apply to them.
    So you can ignore politics, but the politics will not ignore you.


3. **Question**: Thank you for your awesome presentation.
    I might have been experiencing with friends some of those situations.
    I just wonder about the OpenSSL bit, if it's your guess because
    maybe there is a little bit of guessing or.
    And I wonder if we should really start having some
    investigations ourself as the open source community into these cases.
    Maybe in the OpenSSL case there is no malignity intended
    I'm not sure where you got your analysis.

    **Answer:**

    Show me.


4. **Question**: Yes, thank you very much for the presentation very interesting,
    very inspiring for the NSA wannabes.
    You mentioned that some of the Snowden documents may never be leaked
    those are your exact words.
    Why do you think that why do you think that the largest leak
    in basically human history at this point, could go quietly under
    wraps and people will forget about it? why?

    **Answer:**

    Three reasons:

    *One of them is* - that Glenn Greenwald is a very responsible person.
    So there's undoubtedly stuff in there that he will not publish because
    there would be too damaging for whatever reason.

    *Second* - some of them will be so technical that he will not be able
    to explain them to the readers of The Guardian, much
    less other newspapers and.

    *Third* - because I think USA is getting ready to make a deal with
    Snowden to stop the flow. This has been Chinese water torture
    for them every time.
    They've said something in public one week, two weeks later
    Snowden document come out showing they're lying.
    And I think they're kind of tired of that now so I would be
    surprised if there is not already known negotiations going on
    for terms that will allow Snowden to return to the USA
    in return for the flow of documents to stop.
    And what the terms will be we'll probably never know.

    I presume at some point the documents will just stop and we'll never
    hear from Snowden again.
    So I don't think they'll have time to leak all of it,
    however much it is not that NSA might know.
    I mean that's the aspect of this that.
    I think is most interesting is that NSA has absolutely
    no idea what's going on.
    They know that 4,000 of their employees and contractors have used
    that data to check up on their love interests but they know
    this because people have volunteered the information
    they don't know it because they have like locked files or anything
    showing it.
    So it's a totally leaky bucket with no idea what they're doing.
    That should be the real scandal.
    They're not competent.


5. **Question**: Well first of all, thanks for a great talk.
    I would like to ask, answer you, what is the level on the European
    level, not just politics in the the countries, but on the European level.
    We saw that was it CIA or NSA hacking into until Americans mobile phone.
    So I don't know where ?veto? stand there?

    **Answer:**

    I'm pretty sure that they do not have a public relations
    department that have any influence on that kind of decision,
    but if they had, I'm pretty sure that public relations
    department would said whatever you do, do not hack into Merkle.
    Merkle is the one person in Europe you do not want to spy on,
    because she's from the eastern Germany.
    They would have been better off not knowing what she said in her
    phone than having what came out now.
    I would never have taken that risk if I'd been sitting there.

    The other thing is that I don't think anybody who think they can
    trust the mobile phone, I deceived themselves.
    All mobile phones are controlled by everybody else,
    but the guy who has it in his pocket.
    Same thing goes for iPads, computers pretty much anything
    I don't think we have many devices where we can say this one
    is by guaranteed not rooted at this point in time.
    That's one place where the European Union could step in.
    They could actually go in and mandate computing platforms
    that can be verified as free from all kind of trap.
    And Angela Merkel is actually a scientist.
    She may get the idea behind this.
    I could hope that she would do something like that and push it
    through the European Union.
    Unfortunately she's kept busy with the economy in southern EU.
    I don't know if she has a time but a good place to go in
    would be to say the person who pays for the device controls it,
    only that person.
    And Tell-Telcos and people like that to get the fuck out of
    people's mobile phones.


6. **Question**: So discussing politics I have a very short remark to make.
    Techie people usually believe that we can overcome political
    issues by using technical tools like "oh they are spying
    on us, hmm!? Now we have encryption, we have Tor things like that."

    But that is not actually the question, because of course
    we can avoid being tracked by doing technical stuff.
    But the question rather is: Do we really want to have a society like that?
    And I believe that us as people, who understand
    things more from the technical point of view should help
    the rest of the society the dozens.
    So I think that this really is a political issue so there
    are elections this May in the European Parliament as a matter
    of fact I run for a seat.

    **Answer:**

    I can only agree that this is very much a matter of what
    kind of society we leave to our kids.
    Some of the opportunities for goofing around that we had
    our kids will never have without having it pasted all over
    YouTube ten minutes later.
    And I realized this big.
    You start thinking differently once you have kids.
    I have to admit it myself, but I'm pretty sure those of
    you who have kids will see what I mean when I say this
    is about what your grandchildren will live in.

7. **Question**: Hi, very good presentation ?nerves? and impressed.
    So you mentioned the strategy that it's quite easy to disturb
    important open source projects by just creating some discord
    over issues that have been problematic issues for a very
    long time and then like 10 minutes later, you suggest
    ripping OpenSSL out of everything and replacing it with
    something that's a new implementation.
    How is that any different?

    **Answer:**

    Do you think is it really a controversial opinion to think
    that OpenSSL is a pile of crap.

    **Q7 continue...**

    It actually a lot of components in the internet rely on that for encryption.
    So if you rip that out it's not getting any more secure is it.
    It's a controversial issue you just can accepted that.
    And your comment. how's that making anything more secure
    I think this is the same kind of strategy that,
    you're suggesting the NSA and other evil forces do with other open-source project.

    **Answer continue ...:**

    So how do you know I don't work for NSA?

    **Q7 continue ...:**

    exactly

    **A continue ...:**

    It's a tricky question right?
    And there's a lot of, if you want to take the technical path on it.
    The FreeBSD patch collection last time I looked had thirteen
    hundred and forty two copies of the md5 algorithm.
    That's bogus from a software engineering perspective, right.
    OpenSSL is sort of the non solution to that in that
    we have this library that has any encryption algorithm
    anybody has ever thought up and the defaults will let you use them.
    All the downgrade attacks is no SSL is ?pill areas?.
    So if we want to use technical means to reduce the ability
    of governmental players to spy on people.
    We'll have to start acting like grown-up software developers.
    Who do things a sensible way, rather than saying
    "Oh I have this fancy new algorithm I'll stick
    it into a OpenSSL with the rest of them so now we have 50".
    And that would probably require some kind of architectural
    oversight which means we'd probably have to find you
    know maximum of eight persons globally we could agree on probably trust.
    We can start out with Bruce Schneier and seven others.
    But I don't think that the cat herding is up to that
    level of ability, yet.
    So I don't simply don't believe we will have technical
    solutions to this problem.
    There's always going to be some bungholes somewhere
    who does something stupid.

    And you pretty soon are up against some very big companies
    who has a very big interest in defending certain protocols
    and stuff like that.
    So I think the OpenSSL is making things worse because people think it works.
    And people trust it without understanding it.
    And I met two persons who claimed to understand OpenSSL
    one of them was absolutely lying.
    So yes I think OpenSSL is a big problem because people
    think it gives security and it doesn't.

8. **Question**: Yes and I agree with you that this is more over a political
    issue but I wonder what should I or we ask or try to explain
    to a politician if I can get hold of one.
    What is what is a concrete thing I can suggest or,  yeah.

    **Answer:**

    I think a very good place to start is to demand ownership
    of our device..... VIDEO CUT!


9. **Question**:...............work technically speaking should we go and repair
    to OpenSSL everywhere or should we start a new SSL stack.
    Or what should what's our homework we've just had a weekend
    of technical inundation what should we now go and do other
    than harassing our politicians.

    **Answer:**

    I don't know.
    Fair enough.
    And the reason why I don't know is I don't see a technical solution.
    With 1 billion dollars of budget to collect information
    we are not going to be able to stand up to that with any kind of technical solution.
    I only see political solutions.
    But I mean obviously we can write better code we can stop copying
    and pasting code we don't understand and use
    libraries instead of copy and pasting and so on.
    And that will help.
    But it's not gonna solve the problem.
    It's just gonna close some of the security holes.
    Which is a good idea but that's not a real problem right now.
    So know, I mean yes write better code!


**Moderator:**

Should we stop here? yes.

Thank you, all!
