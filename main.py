import sys
import json
import dbs
import encdec
from master_secrets import master_password
from passgen import strongPass
from getpass import getpass

help = """
table has schema: (url, username, email, password_dict)
Generate password:
    use arg -pgen with maximum length of password as param
Deleting:
    For deleting records from table use -d and params -e, -u, -us
Inserting:
    -i as argument with -e, -u, -us as params
    Password will be asked
Updating:
    -upd as argument with a single param -e, -u, -us or -p
    state the conditions with params afterwards
    -new value will be asked
Querying:
    initially add -q argument
    add argument -e <params> for adding email
    add argument -u <params> for adding url
    add argument -us <params> for adding username
    add argument -t <params> for adding tablename
    -e, -u, -us can be used for querying the database
"""
print(help)
argdict = {'-e': 'email', '-u': 'url', '-us': 'username','-p': 'password_dict'}
querydict = {}
if len(sys.argv) == 1: 
    print("Enter some fucking arguments..")
    sys.exit()

if sys.argv[1] == '-pgen':
    if int(sys.argv[2]) > 4:
        print(f"Strong password of {sys.argv[2]} is : {strongPass(int(sys.argv[2]))}")
        sys.exit()
    else:
        print("Strong password must be greater than length 4 !!")
        print("Exiting..")
        sys.exit()

for i in range(3):
    password = getpass("Enter master password :")
    if password == master_password:
        print("Correct password")
        print("fetching queries...")
        break
    elif i==2:
        print("Wrong password. Try again later.")
        sys.exit()
    else:
        print("Wrong password. Try again.")

print("You will have to enter a key that encrypts the message, remember it!")
key = getpass("Enter the key : ")

if sys.argv[1] == '-i':
    if len(sys.argv) != 8:
        print("Enter the correct number of arguments.You should enter all fields!!")
        print("Exiting..")
        sys.exit()
    db_pass = getpass("Enter password for this record:")
    db_pass = encdec.encrypt(db_pass, key)
    for i in range(2,len(sys.argv), 2):
        if sys.argv[i] not in argdict:
            print("Entered wrong argument")
            print("Exitting..")
            sys.exit()
        else: querydict[sys.argv[i]] = sys.argv[i+1]
    query = f"INSERT INTO {dbs.table_name} VALUES('{querydict['-u'] }','{querydict['-us']}','{querydict['-e']}','{json.dumps(db_pass)}' )"
    dbs.insert_values(query=query)

if sys.argv[1] == '-upd':
    for i in range(3,len(sys.argv), 2):
        if sys.argv[i] not in argdict:
            print("Entered wrong argument")
            print("Exiting..")
            sys.exit()
        else: querydict[sys.argv[i]] = sys.argv[i+1]
    q = f""
    for i in querydict:
        if q != "": q+= f" AND "
        q+= f"{argdict[i]} LIKE '%{querydict[i]}%' "
    if sys.argv[2] == '-p':
        db_pass = getpass("Enter password for this record : ")
        db_pass = encdec.encrypt(db_pass, key)
        query = f"UPDATE {dbs.table_name}  SET {argdict['-p']}='{json.dumps(db_pass)}' where "
        query += q
    elif sys.argv[2] == '-e':
        email = input("Enter email for this record : ")
        query = f"UPDATE {dbs.table_name}  SET {argdict['-e']}='{email}' where "
        query += q
    elif sys.argv[2] == '-u':
        url = input("Enter url to update : ")
        query = f"UPDATE {dbs.table_name}  SET {argdict['-u']}='{url}' where "
        query += q
    elif sys.argv[2] == '-us':
        username = input("Enter username to update : ")
        query = f"UPDATE {dbs.table_name}  SET {argdict['-us']}='{username}' where "
        query += q
    dbs.update_values(query=query)

if sys.argv[1] == '-q':
    if len(sys.argv) == 2:
        dbs.show_records(f"SELECT * FROM {dbs.table_name}",key=key)
        sys.exit()
    for i in range(2,len(sys.argv), 2):
        if sys.argv[i] not in argdict:
            print("Entered wrong argument")
            print("Exiting..")
            sys.exit()
        else: querydict[sys.argv[i]] = sys.argv[i+1]
    q = f""
    for i in querydict:
        if q != f"": q+= f" AND "
        q+= f"{argdict[i]} LIKE '%{querydict[i]}%' "
    query = f"SELECT * FROM {dbs.table_name} WHERE "
    query+= q
    dbs.show_records(query=query, key=key)

if sys.argv[1] == '-d':
    for i in range(2,len(sys.argv), 2):
        if sys.argv[i] not in argdict:
            print("Entered wrong argument")
            print("Exiting..")
            sys.exit()
        else: querydict[sys.argv[i]] = sys.argv[i+1]
    q = f""
    for i in querydict:
        if q != "": q+= f" AND "
        q+= f"{argdict[i]} LIKE '%{querydict[i]}%'"
    query = f"DELETE FROM {dbs.table_name} WHERE "
    query+= q
    dbs.update_values(query=query)
