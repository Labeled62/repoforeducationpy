s = 0
a = []
lm = []
lf = []
ll = []
i = 1
lsr=0
msr=0
fsr=0
t=0
with open(r"C:\Users\ПК\Downloads\file6.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(';')

        if line != 0:
            m = int(line[1])
            f = int(line[2])
            l = int(line[3])
            s = (m + f + l) / 3
            a.append(s)
ouf = open(r"C:\Users\ПК\Downloads\output.txt", 'w')
for i in range(len(a)):
    j=a[t]
    ouf.write(str(j))
    ouf.write('\n')
    t=t+1
with open(r"C:\Users\ПК\Downloads\file6.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(';')
        if line != 0:
            m = int(line[1])
            f = int(line[2])
            l = int(line[3])
            lm.append(m)
            lf.append(f)
            ll.append(l)
charslm =sum(lm)
lengtm =len(lm)
charslf =sum(lf)
lengtf =len(lf)
charsll=sum(ll)
lengtl=len(ll)
msr = charslm/lengtm
fsr = charslf/lengtf
lsr = charsll/lengtl
#ouf = open(r"C:\Users\ПК\Downloads\output.txt", 'w')
#for i in range(len(a)):
 #   ouf.write(str(msr))
  #  ouf.write(str(fsr))
   # ouf.write(str(lsr))


print(msr,fsr,lsr)

#print(lm)
#print(lf)
#print(ll)
#print(a)

# srednocenka=s[1]+s[2]+s[3]
#  print(s[2])
#    s = re.split("(\d*)", s)[:-1]
#   out = open(r"C:\Users\ПК\Downloads\output.txt", 'w')
#  for i in range(len(s)):
#     if i % 2 == 0:
#        k=i+1
#       output = s[i] * s[k]
#      print(output)
#     out.write(output + '')
# else:
#   continue
# out.close()
