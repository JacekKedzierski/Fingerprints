import os
import stat
import subprocess

file_type = '.sdf'
similarity_threshold = 0.82
fp_type = 'MACCS'
#fp_type = 'fFP2'

template_dir =  os.getcwd() + '/template/'
cpd_dir = os.getcwd() + '/cpds/'


templates = []
for file in os.listdir(template_dir):
	if file_type in file:
		templates.append(template_dir + file)
templates.sort()

cpds = []
for file in os.listdir(cpd_dir):
	if file_type in file:
		cpds.append(cpd_dir + file)
cpds.sort()

out_csv = open('output' + fp_type + '.csv','w')
header = '   ,'
for inputcpd in cpds:
	cpd_name = os.path.basename(inputcpd)
	cpd_name = cpd_name[:-4]
	header = header + cpd_name + ','
header=header[:-1]
out_csv.write(header + '\n')


outfile = open('outfile_' + fp_type + '.res','w')
outfile.write('HIGH SIMILARITY DETECTED FOR THE FOLLOWING COMBINATIONS:' + '\n')

for template in templates:
	print(template)
	temp_base = os.path.basename(template)
	csv_string_per_temp = temp_base[:-4] + ','
	print(csv_string_per_temp)
	for cpd in cpds:
		cpd_base = os.path.basename(cpd)
		cpd_base = cpd_base[:-4]

		command = "obabel " + template + " " + cpd + " -ofpt -x" + fp_type
		print(command)
		p = subprocess.Popen(command, shell=True, bufsize=0, stdout=subprocess.PIPE, universal_newlines=True)
		p.wait()

		output = p.stdout.read()
		for element in output.split('\n'):
			if '=' in element:
				es = element.split('=')
				value = es[1].strip()
				print(value)
				csv_string_per_temp = csv_string_per_temp + str(value) + ','
			
				if float(value) >= similarity_threshold: 
					outfile.write(temp_base[:-4] + ' vs ' + cpd_base + ' ' + str(value) + '\n')
		#print(output)
		p.stdout.close()

	out_csv.write(csv_string_per_temp + '\n')

	

