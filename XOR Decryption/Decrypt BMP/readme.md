# XOR Decryption of a BMP file

A BMP file has been accidentally xor-encrypted and we don't know the key nor the key size.


## How to proceed

To understand how to proceed, you must first know the architecture of the bmp file.

![Bits to Bitmaps: A simple walkthrough of BMP Image Format | by Uday  Hiwarale | System Failure | Medium](https://miro.medium.com/v2/resize:fit:1400/1*2ohsW8Chn2QsTcSyVcTZcw.png)

![BMP Header open in Hex Editor | Download Scientific Diagram](https://www.researchgate.net/publication/319105105/figure/fig2/AS:527239752421376@1502715160714/BMP-Header-open-in-Hex-Editor.png)

I used Kasiski's method to get an idea of the size of the key and thank to that you can guess that the key size is 6 bytes.

We look at what the first 6 encrypted bytes correspond to and what those are supposed to look like.

The first two are supposed to be "BM", the other 4 bytes are the file size.
We know the real size of the file and the encrypted size

We check on 256 bytes which keys correspond to each encrypted byte

If the byte found resulting from the xor of the encrypted byte and the tested byte corresponds to the byte target (for example for the first two the targets are 0x42, and 0x4d which represent BM in hexadecimal) then I store the key byte by byte

Once we found that, we just have to use the key to decrypt the file by xor decrypting byte by byte with the key that we got until the end of the file. So, the process is to going trough each byte of the key while going through the file and looping the key until we reached the end of the file