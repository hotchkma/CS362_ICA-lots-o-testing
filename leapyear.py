def check(n):
     if n%4==0:
         if n%100==0:
                 if n%400==0:
                         return 1
                 else:
                         return 0
         else:
             return 1
     else:
         return 0
