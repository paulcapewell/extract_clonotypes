
clonotypes_file0 = open('d0-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')
clonotypes_file1 = open('d10-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')
clonotypes_file2 = open('d17-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')

current_line = clonotypes_file0.readlines()
split_line = current_line[1].split("\t")

overall_dict = {}

for x in range (1, len(current_line)):
	split_line = current_line[x].split("\t")
	
	if split_line[1] == "TRGC":
		if split_line[2] in overall_dict:
			overall_dict[split_line[2]]=0.0
		else:
			overall_dict[split_line[2]]=0.0
			
current_line2 = clonotypes_file1.readlines()
split_line = current_line2[1].split("\t")
print(overall_dict.keys())

for x in range (1, len(current_line2)):
	split_line = current_line2[x].split("\t")
	if split_line[1] == "TRGC":
		overall_dict[split_line[2]]=0.0
			
current_line3 = clonotypes_file2.readlines()
split_line = current_line3[1].split("\t")
print(overall_dict.keys())

for x in range (1, len(current_line3)):
	split_line = current_line3[x].split("\t")
	if split_line[1] == "TRGC":
		overall_dict[split_line[2]]=0.0
			

my_dict1 = dict(overall_dict);
my_dict2 = dict(overall_dict);
my_dict3 = dict(overall_dict);

clonotypes_file0.seek(0)
current_line = clonotypes_file0.readlines()

for x in range (1, len(current_line)):
	split_line = current_line[x].split("\t")
	
	if split_line[1] == "TRGC":
		if split_line[2] in my_dict1:
			my_dict1[split_line[2]]=my_dict1[split_line[2]]+float(split_line[6])
		else:
			my_dict1[split_line[2]]=0

#print (my_dict1.items())

output_file = open("d0_freq_TRGC.txt", mode="w")
for key in my_dict1:
	output_file.write(str(key)+"\t"+str(my_dict1[key])+"\n")

output_file.close()
clonotypes_file0.close()
print (my_dict2.items())
clonotypes_file1.seek(0)
current_line = clonotypes_file1.readlines()

for x in range (1, len(current_line)):
	split_line = current_line[x].split("\t")
	
	if split_line[1] == "TRGC":
		if split_line[2] in my_dict2:
			my_dict2[split_line[2]]=my_dict2[split_line[2]]+float(split_line[6])
		else:
			my_dict2[split_line[2]]=0

#print (my_dict1.items())

output_file = open("d10_freq_TRGC.txt", mode="w")
for key in my_dict2:
	output_file.write(str(key)+"\t"+str(my_dict2[key])+"\n")

output_file.close()	
clonotypes_file1.close()

clonotypes_file2.seek(0)

current_line = clonotypes_file2.readlines()

for x in range (1, len(current_line)):
	split_line = current_line[x].split("\t")
	
	if split_line[1] == "TRGC":
		if split_line[2] in my_dict3:
			my_dict3[split_line[2]]=my_dict3[split_line[2]]+float(split_line[6])
		else:
			my_dict3[split_line[2]]=0

#print (my_dict1.items())

output_file = open("d17_freq_TRGC.txt", mode="w")
for key in my_dict3:
	output_file.write(str(key)+"\t"+str(my_dict3[key])+"\n")

output_file.close()	
clonotypes_file2.close()
	



