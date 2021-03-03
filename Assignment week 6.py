def computepay(h,r):
   if h > 40:
      sp = 40 * r
      oh = h-40
      op = r*oh*1.5
      gp = op+sp
   else:
      gp = h*r
   return gp

print('Hello')

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter numbers please")

gp = computepay(h,r)
print("Pay",gp)
