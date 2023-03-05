---
Title: OpenBSD installation with disk encryption
Date: 2023-02-26
Category: unix, openbsd
Tags: advanced, openbsd, unix
Slug: install-openbsd-encryption
Authors: David
Summary: OpenBSD installation with disk encryption
Status: published
---

[TOC]

# Introduction

This article can be consider as following part to article [how to give a new life
of old computer](https://nappex.github.io/myblog/Acer-V5-431-BIOS-OCC)
particulary to laptop Acer. The main motivation of giving a new life
was to install OpenBSD as main OS. Another motivation was article about Old Computer Chanllenge - OCC.
I am planning if everything happen well, to try using it as my main developing machine.
The following article should be about what to do after installation.

All articles about installation OpenBSD I've met declared that installation process of OpenBSD is so
easy! That's true if we presume that your level of knowledge meets certain conditions.

IMHO level of knowledge should be:

* how to mount disk and how the mounting works
* know the diff between partitioning scheme (table) and partitions
* what means /dev/sd0 resp. /dev/rsd0
* how work disks and their drivers on OpenBSD
* how work RAID and why it is useful (for encryption)

Someone can complain that is not necessary. Yes that's true. You can just follow installation
guide and try to insert defaults which should work in the most cases. And if the defaults won't work,
you will just switch to another option. Especially if you combine this approach with reading
[OpenBSD FAQ](https://www.openbsd.org/faq/index.html) then the success will come for sure.

Honestly I do not like this approach but I understand it. When someone just started and wants
to learn things it is good way to start no matter how. Learn by little steps. It is not possible to
learn everything at the start. Amount of knowledge in IT world is huge.
Maybe I suggest to start with something easier. I've started with Linux distros as Ubuntu, Mint, Fedora.
These distros have easier installation process than OpenBSD in my opinion. When you gain
some knowledge from easier distros then you will enjoy process with openbsd more.
A lot of info metinoned in [OpenBSD FAQ](https://www.openbsd.org/faq/index.html) assume
some your knowledge. Nevertheless the FAQ are written very nice. I had just one problem.
I was hurry and then I overlooked some important information. Read the FAQ carefully.
Most of the time all info you need is mention there but sometimes the info you need is not,
so highligt that you notice it at first sight.
That knowledge can be obtained by reading a several books or by trying things
with user friendly linux distro where a lot things are pre-set for user.

Personally I had some basic knowledge when I was started with OpenBSD installation. Because of
tweaking Linux distros as Mint, Fedora, Debian, Artix, Void in past. Even so I have to read
some books to know what I am doing. I wanted to make the install properly and I want to know
what I've set to my PC. When I have the OS which has features as
open source, flexible, customizable and gives me the power to fully operate my computer
I want to use that advantage. I love the power to operate my PC by my rules and not rely
to external service or settings as Windows or Mac do. Books which I strongly recommend for proper installation
are from [Michael W. Lucas](https://mwl.io/). I really love this author. He writes books with
style which perfect suits to my expectations. He explains things from the ground with the context
and he goes after some introduction context deeper and deeper with language of "ordinary" people.
He does not use difficult technical naming or describiton on every corner if not necessary.
The books which helps me a lot with OpenBSD are [OpenBSD Mastery: Filesystems](https://mwl.io/nonfiction/os#omf)
and [Absolute OpenBSD 2nd edition](https://mwl.io/nonfiction/os#ao2e). The latter book can be little bit
obsolete because it was written at 2014.

Installation starts with laptop Acer V5 431, where I am able to boot both legacy and UEFI.
The tech spec of laptop are:

* Laptop model: Acer V5-431 (BIOS V2.18)
* CPU: Intel Celeron 1007U (2 cores) 1500GHz
* RAM: 4 Gb DDR3 (max is 8GB)
* Disk: Seagate ST500LT012 500GB SATA (find out it by `$disklabel -p g sd0` and check the label)
* Wifi card: Atheros AR9462 (not supported)
* Ethernet: Realtek 8168 (proprietary [dongle](https://www.notebookcheck.net/Review-Acer-Aspire-V5-431-Notebook.83411.0.html#1021134-7))
* GPU: Mesa Intel HD Graphics 2500 (IVB GT1)
* Audio: Realtek ALC269
* Card reader: Realtek RTL8411

# Install preparation

## Hardware review, drivers availability

### CPU

Process unit is amd64 with two cores. Everything should works fine.

### GPU

Laptop contains Mesa Intel HD Graphics 2500, which is supported by OpenBSD driver `intel(4)`.
Manual page for this driver declares that support Intel(R) HD Graphics: 2000-6000.

Only one problem occurs. During startup screen is blinking. When X server is loaded, blinking will stop.
So far I dont know if it is problem with OpenBSD or laptop.

### Wireless network card

Unfortunately my wifi card is not support. OpenBSD does not provide driver for it.
So I solve that issue that I am using external USB wifi card Atheros 9271 which is supported
by driver `athn`. This USB wifi card should be available for purchase in most eshops.

Another USB wifi card which should be fine, working and available in eshops is TP-Link TL-WN722N.
I dont test TP-Link card, but driver `urtwn(4)` listed this WiFi.

There are dozens of USB wifi cards which are supported by OpenBSD, but I found two problems
with them. First problem is that most of them is difficult to buy in eshops and second problem
is that reviews were not quite good about the quality and reliability.

### Ethernet

There is also little problem because laptop contain proprietary
[dongle](https://www.notebookcheck.net/Review-Acer-Aspire-V5-431-Notebook.83411.0.html#1021134-7)
where can be connected either RJ45 or VGA, but special adapter is needed for both.

Fortunately ordinary adapter USB-RJ45 from apple worked fine.

### Disk

Disk is handled by driver `sd` without any problem.

### Audio

Audio is working pretty well without any extra tweaking after installation.

### Fucntion key to control volume and screen brightness

The `Fn` on keyboard in combination with other keys. Specifically arrow keys on Acer V5.
This functionality is working out of the box immediately after installation.
It is really cool. Most of the time I had problem with that funcionality on FreeBSD or Linux distros.

### Conclusion

I do not recommend to buy this old laptop for OpenBSD because of problematic network interfaces.
You can handle it with a several adapters, but you will find more old laptops whose network
interfaces will be more compatible (without need of extra adapters) and accexible with OpenBSD.

That is pity because other things working quite well. Unfortunately network interfaces are
really important aspect for comfortable usage in my opinion.

## Wireless network

If your laptop has only wifi card without ethernet socket there is a little problem with driver.
There is problem with driver also if OpenBSD support your wifi card. OpenBSD image does not
contain all available drivers out of the box. OpenBSD does not want to mess your system with
drivers which are not intend to use. I like that approach, but it has a drawback.
You can easily install all available drivers with command `fw_update`. It will detect your
hardware and download just drivers you need nothing more. Unfortunately this command takes
the drivers from internet. If you can not connect to the internet by other option than a wifi.
You have to manually download on other computer particular driver for your wifi, put on USB and
install with `fw_update` manually. Note the install proces does not need the internet.
So you can solve missing driver after installation. Theres are instructions in FAQ chapter
[Bootstrapping wireless firmware](https://www.openbsd.org/faq/faq4.html#WifiOnly). You will
find there a link to all available firmwares and download the needed one.

## Preparation of install media

I'll cover only preparation of USB stick. Nowadays other devices are not use a lot.

### Donwload the right image of OpenBSD

Go to [download page](https://www.openbsd.org/faq/faq4.html#Download). There is main table
where you click the version you want and directly download the image file.

There are some little bit confusing parts. If you directly download image you just download
the image without signing key and without file containing hashes to verify donwloaded image.
Unfortunately further links to these files are not showed at first sight.

You have to look at the first sentence below the table and there is html link to [mirror sites](https://www.openbsd.org/ftp.html).
Currently you can choose the mirror from a list you most prefer. When I was exploring some of these mirrors they look ok.
The latest version of OpenBSD should be found at all of mirrors, but some of mirrors
contains also older version for example the 6.8 and older. On top of that in mirrors you found
all needed files to installation - images, patches, file sets (image contains its, but you can download it separately here).
You will find there the file with hashes, signature file, public key to verify your image.
I strongly recommend to verify every file you download from the internet to avoid future problems.
There is located also file with name `INSTALL.<CPU_architecure>`. This file is very handy because
it describes how to install OpenBSD on specific CPU architecture. If you do not want to read
any book I recommend to you read this file and [FAQ](https://www.openbsd.org/faq/index.html) at least.

To choose right image you have to know the type of CPU architecture. Most of laptops are
amd64 in nowadays, but some of them can be also ARM. Neverthless you should not have a problem
to find image for your CPU architecture if you don't have really exotic hardware.


### Verify the image file

I will not describe how to verify the image. Nice tutorial how to do it is in [Download section](https://www.openbsd.org/faq/faq4.html#Download). Under the table with images available to download. I just mention that you will find
link to public key in text, but there is no link for file with SHA256 hashes and signature.
These files you will find in mirrors link.


### Create install media - USB

There are dozen of articles how to write image file of OS to USB so I will not replicate them.
OpenBSD FAQ show usage with `dd` program on OpenBSD or Linux. You can use `BalenaEtcher` on
MacOS or `RUFUS` on Windows.


# Installation OpenBSD with disk Encryption

When you have prepared USB stick as install media boot it, perhaps with `F12`. If OpenBSD booting went well
you should see four option to choose in terminal. (I)nstall, (U)pgrade, (A)utoinstall, (S)hell.
Type a leading letter and enter to confirm the choice. The reason why the letters are in parentheses.
Install ordinary install process. Upgrade I have not used it yet, but it will be likely option when
you have already installed OpenBSD and you want to upgrade it to higher version.
Autoinstall, it should make automatic installation for you, but I did not try it. So I don't know
details. Shell is shell.
If you choose any other option than shell you can enter to shell with exclamation mark `!` and
if you want to return back type exit. It is not recommended to use `Ctrl-C`. This information is written
in prompt. READ carefully what Installer write to you, all needed informations are mentioned there.


## Indetify the disk for installation

Choose from option Shell. Now you can operate your computer from live OpenBSD.
Indetifying disk is one of thing which are not documented well in FAQ. I didn't find it at least.
There is a point when OpenBSD documentation assume that the reader has some basic knowledge.
I did not have it. I suppose all OSes I've tried in past before OpenBSD served me
names and basic info about disk in really nice and easy overview. I saw all connected disks
and the decision which to choose was really without any thinking. OpenBSD will not serve you
these information. When you want to install OpenBSD you have to know which disk you want to use.
Disk names are create from the name of driver which operates the disk and number. Choosing the right
driver for the disk OpenBSD makes automatically. For example we have one SATA disk. SATA disks are
operated by driver `sd`. The name of disk will be `sd0`. If you connect another SATA disk it'll be
`sd1` and so on. USB sticks are operated by `sd` also.
Information about connected disks can be found out with several tools.

First tool is [sysctl(2)](https://man.openbsd.org/man2/sysctl.2) - command to get or set system information.

Honestly I am really happy that OpenBSD do it like that. I've learned a lot. It pushed me to learn how do it and why...
When you will use distro which show you disk and everthing about them, you don't have any
reason to learn or dig where the information come from until problems occur.


