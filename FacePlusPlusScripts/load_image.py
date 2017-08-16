# hexadecimal and binary dump of image file data
# modified to work with Python30
import binascii
try:
    # pick an image file you have in the working directory
    # or give the full file path ...
    image_file = 'firas1.png'
    fin = open(image_file, "rb")
    data = fin.read()
    fin.close()
except IOError:
    print("Image file %s not found" % image_file)
    raise SystemExit
# convert every byte of data to the corresponding 2-digit hexadecimal
hex_str = str(binascii.hexlify(data))
# now create a list of 2-digit hexadecimals
hex_list = []
bin_list = []
for ix in range(2, len(hex_str)-1, 2):
    hex = hex_str[ix]+hex_str[ix+1]
    hex_list.append(hex)
    bin_list.append(bin(int(hex, 16))[2:])
#print(bin_list)
bin_str = "".join(bin_list)
print(bin_str)