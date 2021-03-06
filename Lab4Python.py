#!/usr/bin/python37all
import json
import cgi
import cgitb
cgitb.enable() 

data = cgi.FieldStorage()
s1 = data.getvalue('option')
s2 = data.getvalue('ledvalue')
info = {"option":s1, "ledvalue":s2}

with open('Lab4.txt', 'w') as f:
  json.dump(info,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/Lab4Python.py" method="POST">')
if s1 == "red":
  print('<input type = "radio" name="option" value="red" checked> Red Led <br>')
  print('<input type = "radio" name="option" value="yellow"> Yellow Led <br>')
  print('<input type = "radio" name="option" value="blue"> Blue Led <br>')
elif s1 == "yellow":
  print('<input type = "radio" name="option" value="red"> Red Led <br>')
  print('<input type = "radio" name="option" value="yellow" checked> Yellow Led <br>')
  print('<input type = "radio" name="option" value="blue"> Blue Led <br>')
else:
  print('<input type = "radio" name="option" value="red"> Red Led <br>')
  print('<input type = "radio" name="option" value="yellow"> Yellow Led <br>')
  print('<input type = "radio" name="option" value="blue" checked> Blue Led <br>')

print('<input type = "range" name="ledvalue" min="0" max="100" value="%s"> <br>' %s2)
print('<input type = "submit" value="Send Changes Over">')
print('</form>')
print('</body>')
print('Brightness = %s' % s2)
print('</html>')
