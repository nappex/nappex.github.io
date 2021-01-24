---
Title: Introduction to network devices
Date: 2021-01-23
Category: Networks
Tags: networks, beginner
Slug: basics-networks-devices
Authors: David
Summary: Learn the main network devices
Status: published
---

[TOC]

# Repeater

Pracuje na vrstvě 1 - fyzická vrstva (physical layer)

Repeater je služebně nejstarší síťový prvek. V historii se v síťařině používal ikabely, ve kterých se signál se vzdáleností značně zeslaboval. Když jsme tedy chtěli zachovat sílu signálu (informace) na větší vzdálenosti, tak jsme museli po určité vzdálenosti signál zesílit. Toho se docílilo pomocí tzv. **REPEATERŮ**. Signál, který přišel do repeateru v něm byl pouze zesílen a poslán dále. Repeater vůbec neřeší jaký signál nebo informace je mu poslána pouze je zesílí.

Repeatery si můžete také představit jako čerpadla vody a kabely mezi repeatery jako hadice, které dopravují vodu k požáru. Čím dále jste od čerpadla tím menší máte tlak. Pokud potřebujete dopravit vodu na velkou vzdálenost a zachovat hasební tlak musíte do hadicové trasy přidat další čerpadla, která tlak vody zase zesílí.

# HUB

Pracuje na vrstvě 1 - fyzická vrstva (physical layer)

Hub není nic jiného než multi repeater. Tedy dokáže zesílit signál z více vstupů na více výstupů. Opět u něj platí to co u repeaterů, že pouze zesiluje signály. Nijak je nevyhodnocuje ani jim nerozumí.

# Bridge

Pracuje na vrstvě 2 - linková vrstva (data link layer)

Jedná se o zařízení, které funguje jak switch, ovšem chytré přeposílání signálu na základě protokolů a portů dělá pomocí softwaru. Je tedy daleko pomalejší než switch, který tento úkol řeší na úrovni hardwaru.

# Switch (Přepínač)

Pracuje na vrstvě 2 - linková vrstva (data link layer)

Jedná se o takovou křižovatku síťového provozu na lokální úrovni, tedy spravuje pouze provoz na síti Local Area Network (LAN). Jinými slovy řídí síťový provoz pouze mezi zařízeními, které jsou připojeny na jednu stejnou síť. Toto není úplně správné protozže exituje i tzv. VLAN tedy virtual local area network a switch je schopen propojit i dvě různé lokální sítě. Switch se chytře snaží signál přeposílat dle jeho parametrů. Dokáže vyhodnotit, na jaký port a MAC adresu je signál posílán. Díky těchto informací je schopen efektivně řídit komunikaci, vyhodnotit jak bude nejefektivnější signál poslat, aby nedocházelo ke střetům a zpomalení síťového provozu. Switch posílá signál na správný port, čímž komunikaci zefektivňuje.
Logika přeposílání signálu je řešena na úrovni hardwaru pomocí chytrých obvodů ASICs (Application Specific Integrated Circuits). Switch je schopen se učit na základě toho, že ví kdej sou síťová zařízení, kde jsou jejich MAC adresy v síti.
Switch se také hodí pokud potřebuje příchozí signál rozdělit, tedy máme jeden vstup a potřebujeme je rozdělit na dalších 5 výstupů. Dá se tedy říct, že je to takový chytrý multi rozbočovač. Funguje tedy i jako klasická roztrojka, kterou máme doma a zvyšujeme pomocí ní počet výstupů ze zásuvky 240 V.

Switche obsahují většinou různé množství portů. Počet portů se pohybuje nejčastěji 5, 8, 16, 24, 48. Rychlosti switchů jsou 10, 100, 1000 Mb/s.

Switche pracují na tzv. linkové vrstvě neberou tedy v potaz nějaká práva apod. To znamená že bezpečnost se v nich neřeší. Ta se řeší až na vyšších vrstvách nebo na úrovni topologie sítě.

Switche se nejčastěji používají na rozšíření kabelové počítačové sítě (ethernet)

# Router

Pracuje na vrstvě 3 - síťová vrstva (Network layer)

Spojuje dvě různé sítě většinou se bude jednat a propojení mezi sítí Local Area Network (LAN - lokální síť) a Wide Area Network (WAN - Internet).
Routuje IP adresy mezi různými sítěmi.

# Modem

# Access Point

Access point nám vytvoří novou wireless local area network (WLAN). Pro představu router který máte doma je schopen vytvořit WLAN. Dosah této bezdrátové sítě je ale omezený výkonem, jak na vysílači, tak na příjímači. K zvětšení rozsahu stávající bezdrátové sítě můžete použít tzv. range extender vysvětlen níže. Nebo vytvořit úplně nový zdroj bezdrátové sítě pomocí acces pointu. Access point je zapojen kabelem do routeru, switche nebo hubu a vytváří nový zdroj nové bezdrátové sítě.

# Range extender

# Wireless LAN controller

If we have to manage and configure many access points. It is more efficient to manage them via Wireless LAN controller. But there is a problem Wireless LAN controller has not so many ports so if we have really a lot of access points we have to connect them to switch which is suitable for connection a very big number of devices and consequently switch is connected to Wireless LAN controller.

# Firewall (Hardware)

Dnes máme hardwarové firewally nové generace, které jsou vybaveny systémy jako Intrusion Detection System (IDS) a Intrusion Prevention System (IPS).

- IDS, detekuje útok a upozorní na něj něco jako když máte doma psa, který Vás svým štěkotem upozorní, že máte doma zloděje, ale už ho nezastaví. Nejsou přímo v síťovém provozu. Dělá si kopie síťového provozu.

- IPS útok detekuje a zároveň zablokuje, prevent the attack. Je přím osoučástí síťového provozu a provoz proudí přímo přes něj.