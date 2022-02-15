potrebno je instalirati argon2
pip3 install argon2-cffi
Naredbe koje program prepoznaje su jednake kao na uputama.
U ovom dokumentu ću navesti predložene ulaze koje redom treba upisivati.
Nije moguća automatizacija jer getpass() ne ide preko standardnog ulaza.


python3 usermgmt.py add dominik - losalozinka
python3 usermgmt.py add dominik - dobraLozinka1 dobraLozinka1
python3 usermgmt.py add ana - Ana12345 ana12345
python3 usermgmt.py add ana - Ana12345 Ana12345
python3 usermgmt.py add dominik
python3 usermgmt.py passwd ana - Ana123456 Ana123456
python3 login.py dominik - dobraLozinka1
python3 usermgmt.py forcepass dominik
python3 login.py dominik - dobraLozinka1 novaLozinka3 novaLozinka3
python3 usermgmt.py del dominik
python3 login dominik - nesto nesto nesto



----------------------------------------------------------

Kako bih postigao otpornost na napade resursima koji su opisani u uputama,
odlučio sam koristiti argon2 za hashiranje lozinki.
Argon2 koristim jer automatski obrađuje i generira saltove,
pruža metodu validate(hash, password) i trebao bi biti siguran za 
upotrebu u ovoj vježbi.

Kako bi se spriječio napad grubom silom, lozinka mora biti od 6 znakova, 
sadržavati najmanje jedno malo, veliko slovo i broj.

Prilikom logina, ne govorimo je li kriva lozinka ili username kako bi
napadač imao što manje informacija.

U jednom pokretanju logina dozvolio sam samo 3 ispitivanja.

U txt datoteci svaki redak mi je jedan user.
Username, hash i zastavica treba li se lozinka izmijeniti su razdvojeni ascii(29)

Ukoliko je zastavica postavljana, korisnik će morati prilikom sljedećeg unosa izmijeniti lozinku.
Tu je i provjera tijekom mijenjanja, postoji uvijet da nova lozinka ne smije biti jednaka staroj.


 







