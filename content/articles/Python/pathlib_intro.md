---
Title: Python knihovny pro práci se soubory
Date: 2020-9-2
Category: Python
Tags: python, beginners
Slug: files-introduction
Authors: David
Summary: How to handle paths and files with python
Status: published
---

[TOC]

# 1. Knihovna pathlib

Jedná se o knihovnu, která je od pythonu 3.4 built-in a není tedy potřeba ji doinstalovávat.

    import pathlib

    pathlib.Path("folder1/folder2/run.exe")

    Output: PosixPath('folder1/folder2/run.exe')

Výše je základní příkaz třídy Path pomocí které se vytváří cesta - objekt cesty. Výstupem tohoto příkazu je `PosixPath("cesta")`
Třída Path se dá použít i bez toho, aniž bychom museli zadat cestu. Třída disponuje metodami jako například `cwd()` nebo nebo `home()`

---

`pathlib.Path.cwd()`

Zjistí v našem systému current working directory. Tedy složku v které se právě nacházíme.

    pathlib.Path.cwd()

    Output: PosixPath('/Users/your_name/Documents/Python')

---

`pathlib.Path.home()`

Vypíše domovskou adresu našeho účtu v operačním systému. Na linuxu by mohla výstupní cesta vypadat jako /home/user_1/

    pathlib.Path.home()

    Output: PosixPath('/Users/your_name')

---

`pathlib.Path("relativni_cesta").resolve()`

Tato metoda nám vytvoří z relativní cesty cestu absolutní. Ovšem pozor, pokud zadáte cestu, která obsahuje lomítko na začátku cesty, tak tento zápis cesty znamená, že zadávate už absolutní cestu.

**Cesta s lomítkem**

    pathlib.Path('/files_introduction/index.ipynb').resolve()

    Output: PosixPath('/files_introduction/index.ipynb')

**Cesta bez lomítka**

    pathlib.Path("files_introduction/index.ipynb").resolve()

    Output: PosixPath('/Users/your_name/Documents/files_introduction/index.ipynb')

## 1. Otevírání souborů

Klasické otevírání souborů vypadá nějak takto:

`with open(path, mode="r", encoding="UTF-8") as file_:`

S knihovnou pathlib lze soubory otevírat velmi podobným způsobem:

`with pathlib.Path("cesta").open(mode="r", encoding="UTF-8") as file_:`

nebo také to samé rozepsáno:

`path = pathlib.Path("cesta")`

`with path.open(mode="r", encoding="UTF-8") as file_:`

Tímto způsobem je spuštěno open() stejně jako v prvním přikladě, ovšem zápis může být pro někoho příjemnější nebo intuitivnější. V zásadě se ale jedná o totéž.

Pomocí třídy Path můžete pro zápis nebo čtení souborů, otevírání souborů rovnou přeskočit pomocí method - **read_text()**, **read_bytes()**, **write_text()**, **write_bytes()**<br>

`pathlib.Path("cesta").read_text()`

# 2. Knihovna os.path

# 3. fnmatch

# 4. glob

# Použité zdroje - další studium

* Portál naučse:

[naucse.python.cz/2019/brno-jaro-2019-pondeli/intro/pathlib/](https://naucse.python.cz/2019/brno-jaro-2019-pondeli/intro/pathlib/)

* RealPython:

[realpython.com/python-pathlib/](https://realpython.com/python-pathlib/)

