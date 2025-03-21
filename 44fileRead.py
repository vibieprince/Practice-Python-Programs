def revrseFormatFile(filename):
    with open (filename,'r') as file:
        content = file.read().strip()
        new_content = ','.join(content)

        with open(filename,'w') as file:
            file.write(new_content)
        

filename = "44sample.txt"
revrseFormatFile(filename)

print(f"File {filename} has been updated")