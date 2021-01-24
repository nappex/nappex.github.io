---
Title: Introduction to terminology in networks
Date: 2020-12-31
Category: Networks
Tags: networks, beginner
Slug: basics-terminology-networks
Authors: David
Summary: Learn the basics about networks through terminology which you will meet on every corner
Status: published
---

[TOC]

# Resources

My article is just rewritten form from articles below in my words, which I understand....

- **An Introduction to Networking Terminology, Interfaces, and Protocols** published on [digitalocean.com](https://www.digitalocean.com/community/tutorials/an-introduction-to-networking-terminology-interfaces-and-protocols)


# Local area network (LAN)

Lokální síť u Vás doma. Ethernetová - vytvořená pomocí kabelů.

# Wide area network (WAN)

Jedná se o Internet tam venku.

# Wireless local area network (WLAN)

Bezdrátová lokální síť.

# OSI model

Open Systems Interconnection model

Tento model charakteruzije dílčí rozdělení síťových vrstev.

Pro lepčí zapamatování slouží tyto mnemotechnické pomůcky:

1. **A**ll **P**eople **S**leeping **T**hrough **N**etworking **D**on't **P**ass [CCNA course od David Bombal - Udemy.com]
1. **A**plikace potkala **P**rezentaci a **R**ealizovaly spolu **T**ransport **S**ítí spojením **F**yzickým. [wikipedie.org]

Jednotlivé vsrtvy jsou:

1. Physical layer (fyzická vrstva)
2. Data link layer (linková vrstva)
3. Network layer (síťová vrstva) - IP, DHCP, ARP, ICMP
4. Transport layer (transportní vrstva) - TCP, UDP
5. Session layer (relační vrstva)
6. Presentation layer (prezentační vrstva)
7. Application layer (aplikační vrstva) - HTTP, FTP, NTP, SSH, Telnet, SMTP, POP3


# TCP/IP model

Jedná se o model vycházející z OSI modelu, který je více zasazen do reality.

Tvoří ho pouze 5 vrstev. To je způsobeno tím, že tento model slučuje 3 vrstvy do jedné. A to konkrétně, redukuje tři OSI vrstvy aplikační, prezentační a relační na -> pouze jednu APLIKAČNÍ.

Výsledný model potom vypadá následovně dle CCNA course:

1. Physical
2. Data link
3. Network
4. Transport
5. Application

Některé jiné zdroje uvádějí pouze čtyři úrovně:

1. Physical - Ethernet, ADSl, WiFi (předávání MAC address fyzických zařízení)
1. Network - IP, ARP, DHCP, ICMP (předávání IP adres)
1. Transport - TCP, UDP (Způsob přenosu TCP -> spojitě, UDP –> nespojitě (videa))
1. Application - HTTP, FTP, SMTP, POP3, SSH, Telnet, NTP


# DHCP (Dynamic Host Configuration Protocol)

# Protokoly

## TCP

Transmission control protocol - primární přenosový protokol

## IP

Internet protokol - protokol síťové vrstvy

