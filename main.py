from PIL import Image
import json
data={}
def to_hex(t: tuple) -> str:
    string = "#"
    for i in t:        
        hex_val = hex(i)[2:].zfill(2) 
        string += hex_val
    return string

with Image.open("photo.jpg") as img:
    data["width"]=img.width
    data["height"]=img.height
    data["mode"]=img.mode
    data["pixels"]=[]
    for i in range(img.height):
        data["pixels"].append([])
        for j in range(img.width):
            data["pixels"][i].append(img.getpixel((j,i)))
    json_string = json.dumps(data)
    with open("data.json","w") as f:
        f.write(json_string)

data={}

with Image.open("photo.jpg") as img:
    data["width"]=img.width
    data["height"]=img.height
    data["mode"]=img.mode
    data["pixels"]=[]
    for i in range(img.height):
        data["pixels"].append([])
        for j in range(img.width):
            data["pixels"][i].append(to_hex(img.getpixel((j,i))))
    json_string = json.dumps(data)
    with open("data_hex.json","w") as f:
        f.write(json_string)

print("Done.")

