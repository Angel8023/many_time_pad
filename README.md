# ManyTimePad

A One Time Pad is secure when the key is used once. If we intercept multiple messages encoded with the same key, it is possible to retrieve the original text.
Let us see what goes wrong when a "one-time" pad is used more than once.

The file "ciphertexts.txt" contains some hex-encoded ciphertexts that are the result of encrypting some ASCII messages with the same pad.
Your goal is to decrypt these ciphertexts, and submit the secret message and the program you've written to crack the code, along with its documentation.

This is what this code does. Given some ciphertexts in input, that you find inside the ciphertext.txt file, the cracker.py decodes them.

## Getting Started

To download my repo:

```
git clone https://github.com/jjcomline/many_time_pad.git
```

Then just run the cracker.py with a ciphertext.txt file with some chipertext in it. You will find the decoded message on the terminal but you can also export it into a txt output file.

## Note

1) Cleartext messages contain only letters and spaces
2) As explained during lecture, the key idea to crack this code is considering what happens when a space is XORed with a (uppercase/lowercase) letter

If you use Python to tackle the challenge, you may find the following resources useful:
https://docs.python.org/3/library/argparse.html
https://docs.python.org/3/library/binascii.html
https://docs.python.org/3/library/stdtypes.html#string-methods
https://docs.python.org/3/library/functions.html#func-range
https://docs.python.org/3/library/functions.html#enumerate
https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations

## Authors

* **Gianluca Gambari** - *Università degli studi di Genova*
