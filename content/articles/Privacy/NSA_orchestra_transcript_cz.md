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
So in the other end of the scale speaking of money we have what we call the overdrive activities.
This is about influencing bussines decisions.
We used NSA's contracting we have rather big purchases of IT services.
And we can pretty much decide who we give the order to ourselves there's no fair purchasing when it's national security.
And the good thing about contract law is you can do anything.
It cannot be directly illegal you cannot have a contract to kill somebody but you can do anything that's possible within the law with a contract.
And it's very good mechanism to solve big problems the bad news is it usually very big players so there's lawyers and it's kind of expensive and stuff like that.
And that can be some objective screw but it's a good way to solve problems and this is actually how we solve the Skype problem.
Skype was peer-to-peer encrypted video and audio.
They didn't use standard protocols. They are out of the FTC we cannot just say "this is illegal" and get them banned.
It's not open source and they did not buy it on our attempt to write them.
It's very popular with independent actors, human rights groups in Belarus for instance.
It's also very popular with a political movements adverse to the US course in Middle East.
And of course terrorists use its we're absolutely sure.
So first we partnered with eBay which is a very special friend of NSA.
For some minor considerations and foreign intelligence they bought Skype for us.
Unfortunately they bungled it, they bought only the access to Skype.
They didn't get the source code they didn't get control with the network.
So that's sort of like "phrkkkk".
It's unclear why their lawyers were not briefed, but we didn't get what we want.
So we had to try again but we can't do that while eBay is sitting there.
So we get eBay to sell it again at a loss and now they're not quite as good a friend of NSA. We're working in that relationship so we've got Microsoft to buy it instead and this time they got all of it.
Microsoft has now changed the architecture of Skype to be centralized, now Skype goes through Microsoft servers very convenient, where it will be decrypted if need be.
That was a pretty expensive operation but it was necessary we couldn't have people communicating outside our jurisdiction.
So it's a very big hammer it requires signatures very high above my pay level, but it's a very good way to do things.
And one of the interesting things here is some of these big players no matter what they do it's brilliant.
We don't understand this but it's brilliant, it doesn't make sense but it's brilliant, because he's a genius we know that.
So you can do pretty strange things this way, totally in the open, nobody blinks an eye, we like that.
Then we have the Queen activities and this is we're working this a lot.
So open source and the internet as such is a consensus-based activity which means anybody can participate.
Nobody has special authority.
There may be some people, who are you know the first among equals adeadeade kind of thing,but it's not like there's somebody who has a the letter of the law on his back/bag. I say because lawn of a black.
It's very much rough consensus and working code except it's these days it's more very long elaborate standard not very much working code and there's a heavy international participation which means that you cannot appeal to people's patriotism you can say for the good of the country you have to, it doesn't really work.
That's a very significant talent mass which is a problem because they will spot things.
In theory all of this belong under the Secretary State because these are foreign relations in many cases, but Foggy bottom is not really that tech-savy once it comes to it.
Diplomats have absolutely no traction then setting like the IETF, if you come in with a tie they kind of looks - strange on you.
And our goals not all already ...... it's they may be misaligned to the Secretary State's goals.
And there are other players involved in this also which we are not necessarily agreeing with in all kind of things.
So it's kind of a tricky space.
So what we do is we leverage our existing resources. We have web resources embedded with friends of NASA.
We have free agents, people who will do things for a consideration.
And we have what we call witless volunteers people who can be manipulated to do our bidding without ours ever paying them anything for it, but it's very good there's no traceability.
So what we do is we deploy very carefully designed talking points.
Meanness/mean this  if we can we have a department who have that put a sign on their door saying "PSYOPS for nerds".
And the idea is to steer discussions in these forums to or from particulars topics where we want them.
And in general very often to disrupt consensus building that goes against our purposes.

So self signed certificates in browsers is a very good example.
So a self signed certificate is a certificate I make that says this is me. So it doesn't really authenticate me an innocence of the world, but if I have that on my web server you can take your browser and we can establish a secret channel.
That's not very good for us because we will have to spend very expensive resources decrypting that if we ever need to but it's practically free for people to do this.
The only reason why people are not doing this is because we really don't want them to. It would be obvious to be a default on Apache just always do a self signed certificate if that's not a real certificate.

So we have spent a lot of time on this room.
And some of the talking points you've no doubt hurt these is like "Oh but secrecy without authentication is pointless you might be talking to the NSA and you wouldn't know it" right.

We like that one we're proud of that one.
It gives a false sense of security, right.
The point is these kind of things if you tailor them carefully they speak to people's political leanings.
If people are slightly paranoid to begin with, which is what a lot of security people are.
This is like "Yeah no that wouldn't do it, if I don't have a 2048-bit ironclad guaranteed that I know who's the other end, then it's no good.
So today if you try to go into a web server that has itself signed certificate you get these hideous warning like "Oh you shouldn't do that, this is dangerous are you really sure you know what you're doing do you have a PhD in this.
And the more buttons you press the more warnings should get right.
By now grandmother and terrorists are totally turned off, right.
And that's one thing in this, some of our predecessors we really loved them getting certificates to be x.509 that was so brilliant.
Have you ever tried looking at all this stuff that's in certificate, nobody understands a word of it.
So it's like "No, I don't understand this, get me out of here"

This is a very good example of how the Queen program works simply getting people to not do things by miss directing their attention on it.
So among the other thing we've done in the Queen is that there's no multihoming without having your own AS number. That means we can always find where all your traffic goes because it always goes through your ISP.
We don't need to track you around seven different sides and stuff like that.
There's also no flow routing in IP version 6.
When IP version 6 were proposed there was a very intelligent proposal that said we should/shouldnt slam these speak addresses into all the packets, we'll just do it in the first packet.
And then we'll get a small flow number that says all the packets in this flow go that direction but that would be very inconvenient for us because we would have to track all these flow numbers all the time.
When you have the IP numbers in package you can just grab all the packets and you have all the information you need for all time in those packets. You don't need to have all the flow States and know what the flows means in all the end that was a very big success not that IP version 6 was it's not really a big problem for us yet, collection wise, but we prepared shoot IP version 6 off.
We've also made it so that there's practically no way compatibly to send encrypted email everybody does down where you have to have the same program in both ends because otherwise it doesn't work and the result is nobody ever uses it.

And we've managed to delay voice over IP until Skype happened.

The voice over IP is a big problem, because you cannot automatically search through voice data.
It's a lot easier when people send emails you can just look for patterns and stuff again.

So these are some of very big successes in the Queen program.
Recently we're working on the HTTP 2.0 standard.
They want there's a very big contingent they wants everything to be TLS, which would be inconvenient.
We're trying to misdirect that we're trying to screw up that process.
I mean look at the good side it would bring them into TLS we have all the routed CAS doing a job for us.
So we have all the keys if it comes to that we'd get man in the middle and all that stuff.
We prefer to stay on encrypted if we can. As a fallback we're trying to push them to some of the broken by design protocols.
Unfortunately one of them seem to have been exposed now but we're working on getting new ones launched.
That's not our department we just try to push people into that sort of thing.
The methods we use is basic fear uncertainty and doubt if you're uncertainty and doubt playing the GPL versus BSD card still works, it's wonderful.
It's like do they never get tired of that?
Yeah that's some wonderful crypto code but I know we can't use it for licence reasons.

Bikeshed discussions, it's so wonderful.
Sometimes just one single email from an anonymous person can derail an open-source project for months.

And we can soak up immense amount of cryptographers bandwidth with bogus proposals for cryptography. You sent this proposal saying "oh I found this wonderful way to do" and they spent like a month tearing it apart, instead of doing real work.

So that works for the world.
One of the current focus areas is that there's a push to go from the certificate PKI model to DANE which is getting your certificates approved through DNS.
And this is a cost brought on by the fact that people realizing that everybody has compromised the CA PKI system.
I mean, if you look in your browser there's like 200 approved CAS and half of them are owned by secret services throughout the world.
It's sort of pointless at this point, right.
So people want to move that into what's called the DANE protocol.
And the idea here is you validate the certificate using the DNSSEC.
So you have this signature on the root zone and that signs the next one and signs next one of the signs next one that says my server has this certificate.
So you can trust that now, you only trust this one single key, right.
So the advantage of PKI/CA is of course we have access today, but the DANE project would really like that, because now we only trust one single certificate, right. "Nudge, nudge, wink wink he said knowingly ....".

And the best part about this is - "I don't understand how these supposedly professional people can overlooked, but DNS is UDP.
It's much easier to do a packet-race with UDP than with TCP.
They send a DNS request you aren't to come first, done.

BOYS - program
This is another interesting program we're working on.
It's actually inspired by a field accident.
We had to evacuate a high risk and high-quality resource and we had no facilities nearby his location that could be used.
So we set him up as a independent contractor.
Story was you know tired of the Boss and bad company politics bla bla bla .... I'm stuck for himself and so on.
And I was lucky to find some customers and so on.
And while sitting there he spent some time on some open source projects had to do something. He spotted some opportunities for groundwork.
So most open source projects are based on trust.
There's no formal vetting there's no checking people's resumes there's no checking, if they're really who they say they are.It's like "Oh I'm this dude who sits in Ulaanbaatar and here's some patches".
If you send good patches for some years people will start to trust you and not check your patches and that will give you a "commit bit", so you can add them yourself because that's really much easier.
It's a fantastic environment that people can come in and announcly nobody knows that you're a dog or NSA agent.
So not only can you collect information about the project's interiors by that way.
Once the trust is in place, you can start to influence their code.

So perception is an easy thing to get right here it's like:
"Yeah, you know I'm sysad of this nonprofit thing and as long as the email works and the printers print.
It's all humming I mean I'm sitting here seven hours a day doing no a shit.
And okay cool here's a dude last time and he's delivering a good code we cool with that.
And one of the things we found out here is would actually can do in reality this is one of our people, right.
And he's sitting somewhere in a shop front that looks like it's this nonprofit thing for you know stopping, I don't know, oak trees falling over or whatever it is.
Actually that's our neighbors who has this kind of shop-front.And then need somebody to get the computers to work in this little stealth setup they have.
And we need to have an Ethernet and a desk for our man so it's very convenient that. And the bosses can actually claim:
"Oh we're doing cooperative work and we're saving money" and stuff like that.
It's really really really well.
And of course, you cannot go in and add obvious vulnerabilities to source code.
People would spot that, it has to be more subtle than that.
Programming mistakes, you know the careless, semicolon etc. sir one based error is, all these classics.
It's kind of dangerous to do it yourself.
It's best to say "Oh I got this patch and I look at it and it looks okay and you stick that in."
People will start to notice if your own code quality sucks, but if you accept patches which are not you know quite up to standard.
Everybody can have a bad day. So, in general obfuscating the code making it harder to understand critical bits of the code makes it easier to make it, almost do what it was supposed to do.
Misleading documentation is always a wonderful thing particular for crypto sensitive stuff.
And deceptive defaults so that things don't do what people think.
It doesn't have to be the core code.
It doesn't have to be the operating system kernel.
In FreeBSD there's 20,000 packages of software.
They are built using, you know.
There're some patches needed for FreeBSD and so on bla bla, okay it builds and you have a package.
Nobody ever looks at those patches.
Who ever ported this piece of software does these patches, it takes the packaging and that's it, it's never reviewed.
It maybe, if it's set "setuid" program somebody may look at it, but in general nobody has ever looked at all the patches in the previously ports collection.
They should.
So this is our poster board.
The Debian random number generator.
This is really beautifully executed.
There's dude who sends in the Patch set you know.
This gets Valgrind to complain and I can't see does anything sensible you should just remove it.
And they did. So for two years, all the debians had lousy random numbers, which made you know brute-forcing SSL keys and stuff like that, done.
Here end up a pretty good bonus.
OpenSSL is the crown jewel.
OpenSSL is a standard library if you want crypto.
Getting SSL to work against all browsers and all that stuff without using openSSL is very very tricky.
Reading the OpenSSL manuals or source code is not tricky as close to impossible.
And that's three hundred thousand lines of code.
So good luck with that.
The documentation is deficient and misleading.
And the defaults are deceptive, they don't do what do you think they do.
This saves so much money in collection you have no idea.
So the overall status of operation orchestra is, it's a resounding success we spend less than a third of the percent of the NSA budget.
And it probably cost the collection cost by something like 50%.
It's kept most of the Internet in plaintext.
And has never been exposed.
That was snowden has no papers on Orchestra at all.
You're not going to read about this in the Guardian because it's all buried in boring departments.
Operation overdrive that's in purchasing.
BOYS that's facility management.
ABBA and Pasadena that's Personel, he didn't have access to any of that.

Thank you!


So the standard reaction in the open source environment to it would Snowden's disclosures have been "We need to strengthen the protocols. We need to have SSL everywhere."
And I think that misses the point by a large margin.
The things that have been published of the Snowden documents by now is the thing the general public can understand reading their newspaper.
The stuff we would be interested in have not been published and maybe never will.
And adding more attempting to add more encryption is most likely just going to have more broken encryption on the internet.
This is not a technical problem, this is a political problem. It must ??? be solved by political means.
That means find politicians in your country who can understand this and make sure they understand it.
If you cannot find politicians get you some politicians who can understand it.
Political will is a renewable resource use your pencil when you vote or run yourself.
This is your children and grandchildren's future society you're looking at.
And we're the guys who sort of missed the boat.


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
