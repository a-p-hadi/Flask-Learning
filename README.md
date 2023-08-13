# Flask-Learning
This resource contains a number of Python codes using the Flask library, and you will learn how to set up web services using it.
To run programs, you must first enter its virtual environment 

in Linux:
```bash
source venv/bin/activate
```
<br />

**lesson 1**\
Run the `00_chair.py` and `00_desk.py` files to understand the use of the \_\_name\_\_ variable
```bash
python 00_chair.py
python 00_desk.py
```
<br />
<br />

**lesson 2**\
In this lesson, we receive data for the next 4 days in Jason format from a weather forecasting web service
```bash
python 01_get_API.py
```
<br />
<br />

**lesson 3**\
In this lesson, we will set up a very simple web service with the Flask library
```bash
python 02_Start_Flask.py
```
> 192.168.1.2:5000/\
> 192.168.1.2:5000/login
<br />
<br />

**lesson 4**\
In this code, you will get to know how to receive data through URL
```bash
python 03_URL_Variable.py
```
> 192.168.1.2:5000/fruitcode/banana
<br />
<br />

**Lesson 5**\
The purpose of this lesson is to get familiar with the "GET" method in web services. By executing this code, you can send 2 numbers to the server and receive the product and sum of them in json format
```bash
python 04_GET.py
```
> 192.168.1.2:5000/math?num1=10&num2=14
<br />
<br />

**Lesson 6**\
The purpose of this course is to familiarize you with the "POST" method. By executing this code, you will launch a webservice that you must send two numbers to when calling it, and it will return their sum and product in json format. Just remember to pass the num1 and num2 attributes in the body.
```bash
python 05_POST.py
```
> 192.168.1.2:5000/math
<br />
<br />

**Lesson 7**\
In this lesson, we will learn how to use both "GET" and "POST" methods in the same address.
```bash
python 06_Methods.py
```
> 192.168.1.2:5000/math?num1=10&num2=14\
> 192.168.1.2:5000/math
<br />
<br />

**Lesson 8**\
This lesson consists of 2 parts, the first part is connecting to the SQLServer database in the Linux and the second part is sending the data received from the database to the webservice. The guide for the first part will be at the end of the article.
```bash
python 07_Database.py
```
> 192.168.1.2:5000/Purchasing.Vendor\
> 192.168.1.2:5000/rfm?customer_id=14324\
> 192.168.1.2:5000/rfm
<br />
<br />

**Lesson 9**\
By running this code, you can send a file to the web service using the post method.
```bash
python 08_FileUpload.py
```
> 192.168.1.2:5000/upload
<br />
<br />

[*]Create Simple API\
[*] Variable in URL\
[x] GET Method\
[x]POST Method\
[x] Database Connect\
[x] RFM\
[ ] Predictor API\

