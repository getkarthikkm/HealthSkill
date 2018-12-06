# Customer Skill Assessment

Restful web service built using flask-restful to perform post operation on customer class.
Uses sqlite database.

### Setup (local)

#### Pre-requisites

1. Python2.7+ installed

#### Installation

1. Open up terminal and navigate to the `HealthSkill` folder
2. Execute the following commands:

```cmd

pip install -r requirements.txt

```

#### Verify installation

1. Execute the following command in a CMD window and check if all dependencies are installed.

```cmd
pip freeze
```

#### Running the application
1. Open up terminal and navigate to the `HealthSkill` folder
2. Execute the following commands:

```cmd

python2 run.py
```

This should produce the following output

```
2018-12-02 19:38:13,848 INFO  * Restarting with stat
2018-12-02 19:38:14,440 WARNING  * Debugger is active!
2018-12-02 19:38:14,443 INFO  * Debugger PIN: 301-582-767
2018-12-02 19:38:14,454 INFO  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
The endpoint would be as below:

http://127.0.0.1:5000/skill/health

## Usage
### List all customers
**Request**
`GET http://127.0.0.1:5000/skill/health`
**Response**
`200 OK` on success
```json
{
    "customer": [
        {
            "age": 54, 
            "cover_type": "hospital", 
            "gender": "male", 
            "has_children": true, 
            "has_provider": false, 
            "id": 1, 
            "name": "0", 
            "postcode": 6169, 
            "skill": "S001"
        }, 
        {
            "age": 66, 
            "cover_type": "hospital", 
            "gender": "male", 
            "has_children": false, 
            "has_provider": false, 
            "id": 2, 
            "name": "1", 
            "postcode": 3485, 
            "skill": "S001"
        }, 
        {
            "age": 55, 
            "cover_type": "extras", 
            "gender": "female", 
            "has_children": true, 
            "has_provider": true, 
            "id": 3, 
            "name": "2", 
            "postcode": 4408, 
            "skill": "S004"
        }
        ]
}
```
### Get Customer by Name
**Request** 
`GET http://127.0.0.1:5000/skill/health?name=51`
**Response**
`200 OK` on success
```json
{
    "skill": {
        "age": 43, 
        "cover_type": "extras", 
        "gender": "male", 
        "has_children": false, 
        "has_provider": false, 
        "id": 52, 
        "name": "51", 
        "postcode": 7555, 
        "skill": "S001"
    }, 
    "status": "success"
}
```

### Create new customer 
**Request**
`POST http://127.0.0.1:5000/skill/health`
```json
{
  "customer": {
    "name": "102",
    "postcode": "1281",
    "age": 61,
    "gender": "female",
    "has_provider": 1,
    "has_children": 1,
    "marital_status": "single",
    "cover_type": "combined"
  }
}
```
**Response**
`201 CREATED` on success
```json
{
"skill": "S003",
"status": "success"
}
```


# Unit Testing

Start the application using the below steps.

1. Open up terminal and navigate to the `HealthSkill` folder
2. Execute the following commands:

```cmd

python2 run.py
```

This should produce the following output

```
2018-12-02 19:38:13,848 INFO  * Restarting with stat
2018-12-02 19:38:14,440 WARNING  * Debugger is active!
2018-12-02 19:38:14,443 INFO  * Debugger PIN: 301-582-767
2018-12-02 19:38:14,454 INFO  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
3. Open up a new terminal and navigate to the `HealthSkill\test` folder
4. Execute the following commands:

```cmd

python2 test_helper.py
```
This should execute the unit tests and produce the following output


----------------------------------------------------------------------
Ran 1 tests in 0.356s

OK

