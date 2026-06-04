name = "kunal"
print(name[-5:]) # kunal
print(name[-4:]) # unal
print(name[-4: -1]) # una 
print(name[:]) # kunal prints full string
print(name[3:]) # al prints from index 3 to end of string
print(name[-3:]) # nal prints from index -3 to end of string

print(name[:4]) # kuna prints from index 0 to 3
print(name[:-3]) # ku prints from index -5 to -4

n = "0123456789"
print(n[1:6:2]) # 135 prints from index 1 to 5 with a step of 2
# the 2 in the above code means that it will take every second character from index 1 to 5. So it will take n[1], n[3], n[5] and will not take n[2], n[4]