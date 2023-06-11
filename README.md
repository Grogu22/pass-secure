# pass-secure
- A CLI based password manager and password generator written entirely in ```python3```
- Uses ```sqlite3``` database and ```pycryptodomex``` for **AES-256** based _encryption_ and _decryption_
- Also includes a **strong password generator**
## Getting started
- clone this repository
- install dependencies using ```pip install -r requirements.txt```
- run ```main.py```
## How this works
#### Insert values :
- run ```python main.py -i <params>```
- params : 
  - ```-u``` : url
  - ```-us``` : username
  - ```-e``` : email
- The program will ask for ```password``` and ```key```
![12](https://github.com/Grogu22/pass-secure/assets/83173038/cff1daeb-d6ab-401b-966e-521b7a17e466)

#### Queries :
- run ```python main.py -q <params>```
- params : 
  - ```-u``` : url
  - ```-us``` : username
  - ```-e``` : email
- using just ```-q``` and no params will simply show all records for a particular key(you can view all records in one run if all of them have the same key)
- The program will ask for ```password``` and ```key```
![12](https://github.com/Grogu22/pass-secure/assets/83173038/51a9ac6c-fc04-4f4a-bb84-aec46a2af365)

#### Update values :
- run ```python main.py -upd <updatearg> <params>```
- update arguments :
  - add only one argument among the following
  - ```-u``` : url
  - ```-us``` : username
  - ```-e``` : email
  - ```-p``` : password
- params : 
  - ```-u``` : url
  - ```-us``` : username
  - ```-e``` : email
- The program will ask for ```password``` and ```key```
![12](https://github.com/Grogu22/pass-secure/assets/83173038/96069aff-19d1-4638-9dfb-0eb11c3969bb)
