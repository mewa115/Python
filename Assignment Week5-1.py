hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter numbers please")
if h > 40:
   sp = 40 * r
   sp = float (sp)
   oh = h-40
   oh = float (oh)
   op = r*oh*145.5
   op = float (op)
   gp = op+sp
   gp = float (gp)
else:
   gp = h*r
   gp = gloat (gp)
print(gp)
try:
    print(gps)
except:
    gps = -1
