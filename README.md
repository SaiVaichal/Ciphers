network_security_lab
Ceaser cipher: This code implements the Caesar Cipher, a basic encryption technique that shifts letters in the alphabet by a fixed number (k). The function ceaserCipher(st, k) encrypts a given text by shifting each letter forward by k positions while keeping uppercase and lowercase letters within their respective ranges. Non-alphabetic characters remain unchanged.
The function dceaserCipher(st, k) performs decryption by shifting the letters backward by k positions, restoring the original text. The program first takes user input for a plaintext string and a shift value (k). It then encrypts the text using ceaserCipher, decrypts it using dceaserCipher, and finally prints both the encrypted and decrypted text.
Output:
![image](https://github.com/user-attachments/assets/d1ff95f6-2729-40c5-a7b4-f41aa24d5c2a)


Fiestel Cipher: a symmetric encryption technique that splits the input into two halves and applies transformations using a key. First, the user enters a string, which is converted into an 8-bit binary representation for each character. The resulting binary string is then divided into two equal halves: left and right.
Next, the user provides a key, which is also converted into an 8-bit binary format. In the first round, the right half is added to the key in binary form, and the result is XORed with the left half to generate a new right half. The left and right halves are then swapped. In the second round, the process repeats: the new right half is added to the key, XORed with the new left half, and swapped again to form the final ciphertext.

If the length of the cipher text is shorter than the original binary string, leading zeroes are added to match the original length. Finally, the binary cipher text is converted back into characters, reconstructing the decrypted text. This implementation follows the core principles of a Feistel cipher, though a full-fledged Feistel network typically involves multiple rounds with different subkeys.
Output:
![image](https://github.com/user-attachments/assets/f09e1fb8-ff49-4ca9-aeea-fafda41c9d0c)


Hill Cipher: Hill Cipher, a polygraphic substitution cipher that encrypts blocks of letters using matrix multiplication. It requires a square key matrix and processes the plaintext in fixed-size blocks.
First, the hill_cipher_encrypt function converts the input text to uppercase and removes spaces. If the text length isn’t a multiple of the key matrix size, it appends 'X' as padding. The text is then converted into numerical form (A=0, B=1, etc.), split into blocks, and multiplied by the key matrix. The resulting numbers are converted back to letters to form the ciphertext.

The hill_cipher_decrypt function reverses the encryption by computing the modular inverse of the key matrix. It multiplies the ciphertext blocks by this inverse matrix, then converts the numerical values back into letters. The function returns only the original length of the plaintext, removing any padding.

The mod_inverse_matrix function calculates the modular inverse of the key matrix by finding its determinant, computing its adjugate, and applying modular arithmetic. This inverse matrix is crucial for decryption.

Finally, the program takes user input, encrypts the text using a predefined 3×3 key matrix, displays the ciphertext, then decrypts it to retrieve the original message.
![image](https://github.com/user-attachments/assets/42ab7bb1-f1fc-451f-b752-b10838a6090a)


MonoAlphabetic Cipher: This code implements a Monoalphabetic Cipher, a substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a randomly shuffled alphabet.
The genrate_key function generates a random key by shuffling the English alphabet and mapping each letter to a new unique letter. This key is stored as a dictionary. The inv function creates an inverse mapping of this key, which is used for decryption.

The encry function encrypts the plaintext by replacing each letter with its corresponding value from the generated key. It preserves non-alphabetic characters by leaving them unchanged. Similarly, the dencry function decrypts the ciphertext using the inverse key, mapping each encrypted letter back to its original form.

Finally, the program generates a random key, takes user input for plaintext, encrypts it, displays the ciphertext, and then decrypts it back to verify correctness.
Output:
![image](https://github.com/user-attachments/assets/a8c743d9-5062-471d-967b-2587c3543012)


Playfair Cipher: The playfair_mat function generates the Playfair matrix by removing duplicate letters from the key and filling the remaining slots with the rest of the alphabet. This matrix is used for encryption and decryption. The find_position function locates the row and column of a given letter within this matrix.
The playfair_encrypt function processes the plaintext by replacing "J" with "I" and ensuring an even length by appending "X" if needed. It encrypts two letters at a time based on Playfair Cipher rules:

If both letters are in the same row, they are replaced with the next letter in the row. If both letters are in the same column, they are replaced with the next letter in the column. Otherwise, they are replaced with letters in the opposite corners of the rectangle they form in the matrix. The playfair_decrypt function reverses this process to retrieve the original message, shifting letters backward instead of forward.
Output:
![image](https://github.com/user-attachments/assets/ef988f8b-4254-4990-8f75-fd7a0be02366)


vigenere Cipher: The generate_key function ensures that the encryption key matches the length of the plaintext by repeating its characters as needed. This extended key is then used for both encryption and decryption.
The encrypt_vigenere function encrypts the plaintext by shifting each letter according to the corresponding letter in the key. If a character is uppercase, it remains uppercase; if lowercase, it remains lowercase. Non-alphabetic characters are left unchanged.

The decrypt_vigenere function reverses the process by shifting each letter back based on the key, restoring the original message. It ensures that uppercase and lowercase letters are decrypted correctly while preserving non-alphabetic characters.
Output:
![image](https://github.com/user-attachments/assets/5fec9b19-c2c5-44cb-bd47-65a3f9a01b87)

DES:
A Symmetric-Key Block Cipher
The Data Encryption Standard (DES) is a symmetric encryption algorithm that processes 64-bit blocks of data using a 56-bit key. It follows a Feistel network structure with 16 rounds of encryption, where each round applies key-based transformations, substitutions (S-boxes), and permutations.  

The encryption begins with an initial permutation (IP), followed by splitting the data into two halves. The right half undergoes expansion, XOR with a round key, substitution, and permutation before being XORed with the left half. The halves swap, and this repeats for 16 rounds. A final permutation (FP) produces the ciphertext.  

Decryption reverses the process using the same key. While DES was once widely used, its short key length makes it vulnerable to attacks, leading to stronger alternatives like 3DES and AES.
Output:
![image](https://github.com/user-attachments/assets/bdad0506-3926-4b77-bf55-4d966b1f6523)

Diffie-Hellman :

The Diffie-Hellman Key Exchange (DHKE) allows two parties to securely establish a shared secret over an insecure channel. It relies on modular exponentiation and the difficulty of the discrete logarithm problem.

How It Works-
Public Parameters: A prime number p and a primitive root g are shared.
Key Exchange:
-Party A picks a private key a, computes A = g^a mod p, and shares A.
-Party B picks b, computes B = g^b mod p, and shares B.
Shared Secret: Both compute S = (other's value)^own key mod p, obtaining the same secret.
Security & Uses
Secure unless intercepted (vulnerable to MITM without authentication).
Used in TLS, VPNs, and secure messaging.
Output:
![image](https://github.com/user-attachments/assets/27ecd57c-7281-4e8f-87f3-ecc78177974a)

RSA :

This is a Python implementation of the RSA encryption algorithm, a widely used public-key cryptosystem. The program allows users to:
-Generate public and private keys
-Encrypt a plaintext message using the public key
-Decrypt the encrypted message using the private key
-How RSA Works

Key Generation:
-Choose two large prime numbers, p and q.
-Compute n = p * q, which forms part of the public and private keys.
-Compute Euler's totient function, φ(n) = (p-1) * (q-1).
-Select an integer e such that 1 < e < φ(n), and gcd(e, φ(n)) = 1 (public exponent).
-Compute the modular inverse d, which satisfies d * e ≡ 1 (mod φ(n)) (private exponent).

Encryption:
Convert each character of the plaintext message to its ASCII value.
Encrypt using the formula:

C = (M^e) mod n

C is the encrypted character, M is the original character.
Decryption:

Decrypt using the formula:

M = (C^d) mod n
Convert the ASCII values back to characters.

![image](https://github.com/user-attachments/assets/c98f729f-f3d2-4bd5-b943-4f66395d1217)



