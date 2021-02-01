# Python Sockets Tutorial
This code is adapted from Sockets Tutorial with Python 3 by [sentdex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ)

## To Run
Open a terminal window in the application folder and run the following command:
```bash
python server.py
```
After the server is running open a second terminal window and run the following command
```bash
python client.py
```
you will be prompted to enter a user name. You may open as many clients as you want. 

### Reader
To open a reader terminal window apply the following change to client.py
```python
message = ""
# message = input(f"{my_username} > ")
```
this allows for a more dynamic chat experience. 
