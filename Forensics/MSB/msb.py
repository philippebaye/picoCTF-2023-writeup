from PIL import Image


with Image.open('Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png', 'r') as image:
    print(image.mode)
    pixels = image.load()

    extracted = ''
    for y in range(0, image.height):
        for x in range(0, image.width):
            r,g,b = pixels[x,y]
            extracted += str(r >> 7)
            extracted += str(g >> 7)
            extracted += str(b >> 7)
    
    chars = []
    for i in range(len(extracted)//8):
        byte = extracted[i*8:(i+1)*8]
        chars.append(chr(int(byte, 2)))
    
    open('Ninja.extraction', 'w').write(''.join(chars))
