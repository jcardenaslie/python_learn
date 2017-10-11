def brute_pattern(pattern, string):
	occ = []
	p_len = len(pattern)
	s_len = len(string)

	if p_len == 0 or s_len == 0:
		return occ

	for i in range(0,s_len-1): #recorre el string
		if string[i] == pattern[0]: # si el caracter es igual al primer caracter del patron
			p_count = 1
			for j in range(1,p_len):
				i += 1
				if string[i] == pattern[j]:
					p_count +=1
				else:
					break
			if p_count == p_len:
				occ.append(i - (p_len-1))

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
# print(occ)
