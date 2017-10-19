def brute_pattern(pattern, string):
	occ = []
	p_len = len(pattern)
	s_len = len(string)

	if p_len == 0 or s_len == 0:
		return occ

	i = 0
	# for i in range(s_len): #recorre el string
	while(i < s_len):
		# print("i"+ str(i))
		if string[i] == pattern[0] : # si el caracter es igual al primer caracter del patron	
			p_count = 1
			j = 1
			# for j in range(1,p_len):
			while(j < p_len):
				i += 1
				if i < s_len:
					# print("j" + str(j))
					b = string[i]
					b = pattern[j]
					if string[i] == pattern[j]:
						p_count +=1
					else:
						break
				j+=1
			if p_count == p_len:
				occ.append(i - (p_len-1))
		i += 1
	# for i in range(10):
	# 	print(i)
	# 	i+=3
	return occ

# pat = "bla"
# txt = "blablablabla"
# txt = """ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC
# 		CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC
# 		CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG
# 		AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCC
# 		CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG
# 		TTTAATTACAGACCTGAA"""

# pat = "ACA"
# occ = brute_pattern(pat,txt)

# Caso 4 palabras iguales con un k = 18
# pat = "blaquenaitormaster"
# txt = pat*1000000
# txt = txt[:700000]
# # print(len(txt))
pat3 = "b"*1000000
txt3 = pat3
occ = brute_pattern(pat3,txt3)
print(occ)
