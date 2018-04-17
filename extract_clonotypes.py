import os.path

clonotypes_file0 = open('d0-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')
clonotypes_file1 = open('d10-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')
clonotypes_file2 = open('d17-QIAseqRNA-immune-repertoire-TCR.clonotypes.txt')

current_line = []
current_line.append(clonotypes_file0.readlines())
current_line.append(clonotypes_file1.readlines())
current_line.append(clonotypes_file2.readlines())

split_line = current_line[0][1].split("\t")

overall_dict = {}

#Establish all possible V regions in the supplied files
for k in range (0, len(current_line)):
    for x in range (1, len(current_line[k])):
        split_line = current_line[k][x].split("\t")
        if split_line[1] == "TRBC":
            if split_line[2] in overall_dict:
                overall_dict[split_line[2]]=0.0
            else:
                overall_dict[split_line[2]]=0.0
print(overall_dict.keys())

#Scan through supplied files and extract relevant proportion details
for k in range (0, len(current_line)):
    sample_dict = dict(overall_dict);
    for x in range (1, len(current_line[k])):
        split_line = current_line[k][x].split("\t")
        
        if split_line[1] == "TRBC":
            if split_line[2] in sample_dict:
                sample_dict[split_line[2]]=sample_dict[split_line[2]]+float(split_line[6])
            else:
                sample_dict[split_line[2]]=0

        if os.path.isfile('d'+str(k)+'_freq_TRBC.txt'): 
            output_file = open('d'+str(k)+'_freq_TRBC.txt', mode='r')
            output_line = output_file.readlines()
            output_file.close()

            output_file = open('d'+str(k)+'_freq_TRBC.txt', mode='w')
        
            for key in sample_dict:
                output_file.write(output_line[0][:-2]+str(key)+"\t"+str(sample_dict[key])+"\n")
        else:
            output_file = open('d'+str(k)+'_freq_TRBC.txt', mode='w')   
            for key in sample_dict:
                output_file.write(str(key)+"\t"+str(sample_dict[key])+"\n")

output_file.close()
clonotypes_file0.close()
clonotypes_file1.close()
clonotypes_file2.close()

	



