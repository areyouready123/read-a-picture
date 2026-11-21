from PIL import Image
import json
data={}
with Image.open("photo.jpg") as img:
    data["size"]=img.size
    data["pixels"]=[]
    for i in range(img.height):
        data["pixels"].append([])
        for j in range(img.width):
            data["pixels"][i].append(img.getpixel((j,i)))

    json_string = json.dumps(data)
    with open("data.json","w") as f:
        f.write(json_string)



