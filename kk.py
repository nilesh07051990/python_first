year= int(input())
def is_leap(year):
    leap = false

    if year % 400 == 0 :
     leap=true
    elif year % 100 ==0 :
     leap=false
    elif year % 4 ==0:
     leap=true

    return leap

year = int(input())
print (is_leap())