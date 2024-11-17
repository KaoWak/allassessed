def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    decrypted_text = ""
    for char in encrypted_text :
        ascii_code = ord(char)
        new_ascii_code = ( ascii_code - key) % 256
        decrypted_text += chr(new_ascii_code)
    return decrypted_text


print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu" , 3 ))