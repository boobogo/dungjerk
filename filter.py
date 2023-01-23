import itertools

seq = "123456"
com_seq = itertools.combinations(seq, 6)
count = 57
for c in com_seq:  
    print('case {}:  result = cross && f{} && f{} && f{} && f{} && f{} && f{};	break;'.format(count,c[0],c[1],c[2],c[3],c[4],c[5]))
    count+=1
	
print('total combination: ',count-1)

for i in range(1,7):
	print('bool f{} = macdFilter{}[0] > signalFilter{}[0] && signalFilter{}[0] < 0.0;'.format(i,i,i,i))

print('fck you')
