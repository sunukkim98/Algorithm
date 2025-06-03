import sys
input = sys.stdin.readline

out = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """
n = int(input().strip())
for _ in range(n):
    print(out)
