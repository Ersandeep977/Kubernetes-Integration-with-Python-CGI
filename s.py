Sandeep Kumar Patel, [26.06.21 00:13]
#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()
f = cgi.FieldStorage()
cmd = f.getvalue("x")
print(" <h2>Your Command is :-</h2>",cmd,"<h2> \n OutPut is :-</h2>")
output = subprocess.getoutput("sudo " + cmd)
print("*"*100)
print()
print(output)
print()
print("*"*100)
time.sleep(3)
print("<h1> thank you for using this Docker UI Page</h1>")
