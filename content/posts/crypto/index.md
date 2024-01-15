+++
title = 'My public GPG key'
summary = 'if you want to send some encrypted e-mail!'
date = 2024-02-06T22:09:03Z
showCodeCopyButtons = true
+++

{{< codeinclude "text" "content/posts/crypto/pubkey.txt" >}}

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
