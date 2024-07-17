+++
title = 'My public GPG key'
summary = 'if you want to send some encrypted e-mail!'
date = 2024-02-06T22:09:03Z
showCodeCopyButtons = true
+++

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEZcKvURYJKwYBBAHaRw8BAQdAzsjqGhHZjBD1eRPV1Nl5jTwY7UbwqxQRvM1C
f0Se1V60N0NocmlzdGlhbiBGcmFudHplbiAoYSBzb2Z0d2FyZSBkZXZlbG9wZXIp
IDxjZkAweDI5YS5tZT6IjgQTFgoANgIbAwIXgBYhBDVtIJHdwGXSedjfEcr6965l
1nJ8BQJlwq+9BAsJCAcFFQoJCAsEFgIDAQIeBQAKCRDK+veuZdZyfIdLAQDA4yjp
Nuel+eSbSurSXskt9UGvjg1dWScUvjivUiqp5AEAnUoEWk+H7VSBaII+5KttPpKx
RkMAN6vGvUX/8NihOg64OARlwq9REgorBgEEAZdVAQUBAQdArQ/mgWp9dldMXz/Q
j7NxvMY8h4MIT907FmfLOMOn7iYDAQgHiHgEGBYKACAWIQQ1bSCR3cBl0nnY3xHK
+veuZdZyfAUCZcKvUQIbDAAKCRDK+veuZdZyfLNiAQDSe27IrWnQIn9JJUzDN2/O
zrVFw8hJ6XQTiMTQwS1dbgEA4ZQ6EBK722qnvjf4jx4Ob8XQlWi1N2REHMPA6Lcf
vgg=
=03/V
-----END PGP PUBLIC KEY BLOCK-----
```

You can use it to encrypt messages to me. 

To use this key, you can copy it from the code block using the button provided. Then, follow these steps:

1. **Copy the Key:** Click the button next to the public key to copy it to your clipboard.

2. **Import the Key:** Open your terminal and use the following command:

   ```bash
   gpg --import
   ```
   Press enter, then paste the copied key into the terminal. Press **CTRL+D** to signal the end of the input.

3. **Encrypt a Message:** Now you can encrypt a message to me using the following command:

   ```bash
   gpg --encrypt <recipient_email_address> <message_file>
   ```

   - Replace `<recipient_email_address>` with my email address associated with this public key.
   - Replace `<message_file>` with the name of your message file.


Remember: Only I, the holder of the corresponding private key, can decrypt messages encrypted with this public key.  This system ensures privacy and authenticity in communication.  
