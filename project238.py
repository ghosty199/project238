import hashlib
text="fewjgrfvuisrbnmtnhbgvcdsvfgbtrhbvfcdfvrgbvdgrbgfbf"
result=hashlib.sha3_256(text.encode())
print("the sha3_256 is:",result.hexdigest())

text2="ji"
result2=hashlib.sha3_256(text2.encode())
print("the sha3_256 is:",result2.hexdigest())




filename="screenshotcry.png"
with open (filename, "rb") as f:
	file_data = f.read()

image_hash=hashlib.sha3_256(filename.encode())
print("the sha3_256 is:",image_hash.hexdigest())
