# XOR Decryption of a WEBP file

A WEBP file has been accidentally xor-encrypted and we don't know the key nor the key size.


## How to proceed

To understand how to proceed, you must first know the architecture of the WEBP file. And in particular the header


0                   1                   2                   3

 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|      'R'      |      'I'      |      'F'      |      'F'      |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|                           File Size                           |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|      'W'      |      'E'      |      'B'      |      'P'      |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


<br> 

 0                   1                   2                   3<br> 
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1<br> 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+<br> 
|                                                               |<br> 
|                    WebP file header (12 bytes)                |<br> 
|                                                               |<br> 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+<br> 
:                        'VP8 ' Chunk                           :<br> 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+<br> 
<br> 

I used Kasiski's method to get an idea of the size of the key and thank to that you can guess that the key size is 15 bytes.

We look at what the first 15 encrypted bytes correspond to and what those are supposed to look like.

The first two are supposed to be "RIFF", then 4 bytes are for the file size, 4 bytes for "WEBP" and 4 bytes for "VP8 "

We know the real size of the file and the encrypted size

We check on 256 bytes which keys correspond to each encrypted byte

If the byte found resulting from the xor of the encrypted byte and the tested byte corresponds to the byte target (for example for the first two the targets are 0x42, and 0x4d which represent BM in hexadecimal) then I store the key byte by byte

Once we found that, we just have to use the key to decrypt the file by xor decrypting byte by byte with the key that we got until the end of the file. So, the process is to going trough each byte of the key while going through the file and looping the key until we reached the end of the file
