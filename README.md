# BIM Project Database API 3 Nodes Consortium Chain User guide
###### tags: `BIM Project Database`

## Code
> GitHub: https://github.com/jkcharlie6679/BIM_API.git
> 

## File structure
> ├── api.py

> ├── config.ini

> ├── create_table

> │   └── create_table.py

> │   └── hash_analysis.py

> │   └── test_table.py

> ├── Ethereum_Transaction.py

> ├── ethereum.txt

> ├── nohup.out

> ├── __pycache__

> │   ├── Ethereum_Transaction.cpython-36.pyc

> │   └── subfunction.cpython-36.pyc

> └── subfunction.py

> 

## Create a MySql DB
> Install MySql DB. 
> Step 1. `sudo apt-get install mysql-server`
> Step 2. `sudo apt install mysql-client`
> Step 3. `sudo apt install libmysqlclient-dev`
> Step 4. `sudo mysql`
> Step 5. `SELECT user,authentication_string,plugin,host FROM mysql.user;`
> Step 6. `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345678';`
> Step 7. `FLUSH PRIVILEGES;`
> Step 8. `SELECT user,authentication_string,plugin,host FROM mysql.user;`
> Step 9. `exit`
> Step 10. `sudo mysql -u root -p`
> Step 11. `show databases;`

## Create an ethereum
> 1. Use `mkdir ethereum` to create a new folder.
> 2. Use `cd ./ethereum` to change your location.
> 3. Use `geth --datadir test init ./genesis.json` to create an ethereum.
>
```yaml=1
Node1:
{
  "config": {
    "chainId": 4567,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "ethash": {}
  },  
  "nonce": "0x0",
  "timestamp": "0x5e64ebff",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x47b760",
  "difficulty": "0x80",
  "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": {},
  "number": "0x0",
  "gasUsed": "0x0",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
Node2:
{
  "config": {
    "chainId": 4567,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "ethash": {}
  },  
  "nonce": "0x0",
  "timestamp": "0x5e64ebff",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x47b760",
  "difficulty": "0x80",
  "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": {},
  "number": "0x0",
  "gasUsed": "0x0",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
Node3:
{
  "config": {
    "chainId": 4567,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "ethash": {}
  },  
  "nonce": "0x0",
  "timestamp": "0x5e64ebff",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x47b760",
  "difficulty": "0x80",
  "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": {},
  "number": "0x0",
  "gasUsed": "0x0",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```
> 4. Use `personal.newAccount("password")` to create a miner account. And it will return a AccountID back to you.
> 5. Use `personal.newAccount("password")` to create a user account. And it will return a AccountID back to you.
> 6. You can use the `eth.accounts` to list all account.
> 7. Use `miner.start()` start to dug.
> 8. After dug the coin, you can use `miner.stop` to stop dug.
> 9. Use `eth.getBalance(<miner account>)` to check the coin of miner account.

## Setting the config of python
> The config file is at BIM_API/cinfig.ini.
> 
```python=1
[MYSQL]
host = localhost
port = 3306
user = root
password = 12345678

[FLASK]
host = 0.0.0.0
port = 5054

[PATH]
file_path = /home/hj/3N_Files

[ETHEREUM_Node1]
host = 192.168.1.99
port = 30223
miner_account = 0x2e6c3ccfe2b71e66d179d0375a2fbaa8f5d93159
miner_passwd = password
user = 0xa93d7f0ce88f4ac50918044c02026a4a707dfbb4
user_passwd = password

[ETHEREUM_Node2]
host = 192.168.1.99
port = 30224
miner_account = 0x026605cef491436cf381fd3cdb6e276043ac3286
miner_passwd = password
user = 0x8409164c9e19e7a14cc75b3dfee664fa10f6ea2f
user_passwd = password

[ETHEREUM_Node3]
host = 192.168.1.99
port = 30225
miner_account = 0x62e79b354adfcb519a00aa620f808cc772b1bf84
miner_passwd = password
user = 0xfc12f01b44d9d94199b5ab53ea9341f0f4b46151
user_passwd = password
```
> Accroding to your system setting to edit your config.ini.

## Iinitiate the DB
> In `BIM_P_API` use `python3 ./create_table/create_table.py` to initiate the DB.
> 

## Run the api
> In `BIM_P_API` use `python3 ./api.py` to run the api.
> 

## API Function

```
1. Upload information to the Database and Blockchain
POST : http://140.118.121.110:30600/upload 
Rule: Body -> raw -> json
Parameters: 
{
        "Project_id": "Test_project",
        "Project_user_id": "Susanwu",
        "Object_id": "susanwu20201215151615251353",
        "Element_location": [
          0.99849714986386384,
          -0.054803665148789531,
          0.0,
          0.0,
          0.054803665148789531,
          0.99849714986386384,
          0.0,
          0.0,
          0.0,
          0.0,
          1.0,
          2100.0,
          0.0,
          0.0,
          0.0,
          1.0
        ],
        "Element_parameters": {
          "Panel Length1": 600.0,
          "Panel Length2": 600.0,
          "Panel Thickness": 10.0,
          "Control Ratio": 0.1,
          "Hole Radius": 20.0,
          "Material Option": 0
        },
        "Label_name":[
            "Object",
            "Color",
            "Owner"
        ],
        "Label":[
            "Object_D",
            "Red",
            "Susan1"
        ]
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Check_in.png)
```
2. Conditional search the parameters from the database.
POST : http://140.118.121.110:30600/location
Rule: Body -> raw -> json
Parameters: 
{
    "Project_id": "TestProject",
    "Object_id" : "susanwu20201215151615251353",
    "Element_id": "",
    "Label": "",
    "Check_in_status": "1",   
    "Check_in_time": "2021/05/05/",
    "Check_out_status": "",   
    "Check_out_time": ""
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Get%20data.png)
```
3. Upload files to File Management and record the path in the database.
POST : http://140.118.121.110:30600/upload_file
Rule: Body -> form-data (Key, Value)
Parameters: 
  a. Element_id [test]
  b. Element_location_file [file]
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Upload_file.png)
```
4. According to the path stored in the database, and download files from the File Management. 
POST : http://140.118.121.110:30600/download_file 
Rule: Body -> form-data (Key, Value)
Parameters:
  a. Element_id [test]
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Download_file.png)
```
5. Check out the Element of the Project. 
POST : http://140.118.121.110:30600/check_out 
Rule: Body -> raw -> json
Parameters:
{
	"Project_id" : "Test_project",
    "Project_check_out_user_id" : "HuangJun",
	"Element_id" : ["Test_projectN7", "Test_projectN8", "Test_projectN9", "Test_projectN10", "Test_projectN11"]
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Check_out.png)
```
6. Check in data verification 
POST : http://140.118.121.110:30600/Checkin_verification 
Rule: Body -> raw -> json
Parameters:
{
    "Check_in_hashcode": "0xcce0d044e21bc5d85dd43b88da1969489ea767b62e2ebfa75269863e4b29569e" 
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Check_in_verify.png)
```
7. Check out data verification
POST : http://140.118.121.110:30600/Checkout_verification
Rule: Body -> raw -> json
Parameters:
{
    "Check_out_hashcode": "0xe1681b78cce1f1e34b5c03bac3284c319550a717d94a95b1394d2907484c3b81" 
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/Check_out_verify.png)
```
8. Use the SQL command: "SELECT"
POST : http://140.118.121.110:30600/sql_select 
Rule: Body -> raw -> json
Parameters:
{
    "SQL_command": "select * from BIMP.Project_Information where Element_id = 'Test_projectN1';"
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/SQL_select.png)
```
9. Use the SQL command: "INSERT"
POST : http://140.118.121.110:30600/sql_insert 
Rule: Body -> raw -> json
Parameters:
{
	"SQL_command" : "insert into TEST.test(Project_id, Project_user_id, Object_id, Element_id, Element_location, Element_parameters, Label_name, Label)values('Test_project', 'Susanwu', 'susanwu20201215151615251353', 'HJPN1', '[0.99849714986386384, -0.054803665148789531, 0.0, 0.0, 0.054803665148789531, 0.99849714986386384,0.0, 0.0, 0.0, 0.0, 1.0, 2100.0, 0.0, 0.0, 0.0, 1.0 ]', '[ Panel Length1: 600.0, Panel Length2: 600.0, Panel Thickness: 10.0, Control Ratio: 0.1, Hole Radius: 20.0, Material Option: 0]', '[Object, Color, Owner]', '[Object_D, Red, Susan1]')"
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/SQL_insert.png)
```
10. Use the SQL command: "UPDATE"
POST : http://140.118.121.110:30600/sql_update
Rule: Body -> raw -> json
Parameters:
{
	"SQL_command" : "Update TEST.test set Project_user_id = '11', Element_id = '11' where Project_id = '1';"
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/SQL_update.png)
```
11. Use the SQL command: "DELETE"
POST : http://140.118.121.110:30600/sql_delete
Rule: Body -> raw -> json
Parameters:
{
	"SQL_command" : "delete from TEST.test where Project_id = '1';"
}
```
![Image text](https://github.com/xiehuangjun/BIM_Project_Database/blob/main/Grasshopper%20Figure/SQL_delete.png)

> editor editor HJ 2021/07/08
