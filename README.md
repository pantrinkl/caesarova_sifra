# Caesarova šifra
Tento program slouží k zašifrování textu z textového souboru pomocí Caesarovi šifry. 

Zašifrovaný text je uložen do textového souboru. 
Po zašifrování je provedeno opětovné rozšifrování ze zašifrovaného souboru a rozklíčovaný text je uložen do dalšího textového souboru.

## Vstupní data 
Po spuštění programu je nutné zadat:
* Jméno vstupního souboru.\
V textovém souboru je třeba mít text, který má být zašifrován.\
Zašifrovány jsou pouze malá a velká písmena bez diakritiky.\
Písmena s diakritikou, čísla a další znaky zůstavají nezašifrované.
* Celočíselnou hodnotu pro klíč.\
Tím je myšlena hodnota, o kolik se zašifrovaná abeceda posune vůči původní.

## Výstupní data
Zašifrovaný text je uložen do souboru `zaklicovane.txt`. 
Pro kontrolu je následovně soubor `zaklicovane.txt` převeden zpět do čitelného stavu. Ten je uložen do souboru `rozklicovane.txt`.
Pokud se ve složce tyto soubory nevyskytují, jsou vytvořeny nové. V případě, že ve složce již takové soubory existují, jsou přepsány.


Podrobné popsání tohoto programu je v souboru `dokumentace.pdf`.

Pro vyzkoušení programu můžete využít z tohoto repozitáře testovací soubor `vstup.txt`. Výsledek zašifrovaného textu pro hodnotu klíče = 4 naleznete v testovacím souboru `zaklicovane.txt`, stejně tak jako následovné rozšifrování v souboru `rozklicovane.txt`.
