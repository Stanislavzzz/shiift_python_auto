img_file = open('data/cat.jpg', 'rb')
content = img_file.read(50)
img_file.close()
print(content)
