label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")

print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")


chai = "Chai Special"

print(chai[0])    # C
print(chai[1])    # h
print(chai[2])    # a
print(chai[3])    # i
print(chai[5])    # S

# Negative indexing
print(chai[-1])   # l
print(chai[-2])   # a
print(chai[-3])   # i
print(chai[-4])   # c

chai = "Chai"

print(chai[0])   # C
print(chai[3])   # i
# print(chai[4]) # IndexError: string index out of range

chai = "Chai"

# chai[0] = "T"  # TypeError
chai = "T" + chai[1:]
print(chai)       # Thai

chai = "Chai Special"

print(chai[0:4])    # Chai
print(chai[5:12])   # Special
print(chai[:4])     # Chai
print(chai[5:])     # Special
print(chai[:])      # Chai Special


text = "ABCDEFGHIJ"

print(text[0:5])     # ABCDE
print(text[2:7])     # CDEFG
print(text[::2])     # ACEGI
print(text[1::2])    # BDFHJ
print(text[::3])     # ADGJ
print(text[-4:])     # GHIJ
print(text[:-3])     # ABCDEFG
print(text[-6:-2])   # EFGH
print(text[2:8:2])   # CEG

# Reverse the string

chai = "Chai Special"

print(chai[::-1])   # laicepS iahC
print(chai[::1])    # Chai Special
print(chai[::-2])   # lieSih

#4. String encoding and decoding

label_text = "Chai Spécial"

# Encoding
encoded_label = label_text.encode("utf-8")

print("Original:", label_text)
print("Encoded:", encoded_label)
print("Type:", type(encoded_label))

# Decoding
decoded_label = encoded_label.decode("utf-8")

print("Decoded:", decoded_label)
print("Type:", type(decoded_label))