from sys import argv
from os.path import exists

script, filename, to_file = argv

print "Copying from %s to %s " % ( filename, to_file);

# opening the file
in_file = open(filename)
in_data = in_file.read()


print "The input file is %d bytes long" % len(in_data)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input("> ")

out_file = open(to_file,'w')
out_file.write(in_data)

print "Alright, all done"

out_file.close()
in_file.close()

