import gzip

parent_file="III BA PROJECT -SRI SABARISH.(21UENG017).pdf"
output_file="comp.txt"

with open(parent_file,'rb')as inp_file, gzip.open(output_file,"wb") as out_file:
    out_file.writelines(inp_file)

print("Process Completed")