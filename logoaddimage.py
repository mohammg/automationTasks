import os
from PIL import Image

logo_file='logo.png'
out_folder='output'
position='dr'
current_dir =os.path.dirname(os.path.realpath(__file__))

def add_logo_image():
    if not os.path.exists(os.path.join(current_dir,out_folder)):
        os.mkdir(os.path.join(current_dir,out_folder))
    image_logo=Image.open(os.path.join(current_dir,logo_file))
    for filename in os.listdir(current_dir):
        filename=filename.lower()
        

        if filename==logo_file:
            continue
        if filename.endswith(('jpg','png','jpeg')):
            image=Image.open(os.path.join(current_dir,filename))
            width,height=image.size
            n_logo_width=int(width*20/100)
            n_logo_height= int(height*20/100)
            n_logo=image_logo.resize((n_logo_width,n_logo_height))
            
            match position:
                case "dr":
                    image.paste(n_logo,(width-n_logo_width,height-n_logo_height))
                    image.save(os.path.join(current_dir,out_folder,filename))
                case "dl":
                    image.paste(n_logo,(0,height-n_logo_height))
                    image.save(os.path.join(current_dir,out_folder,filename))
                case "tr":
                    image.paste(n_logo,(width-n_logo_width,0))
                    image.save(os.path.join(current_dir,out_folder,filename))
                case "tl":
                    image.paste(n_logo,(0,0))
                    image.save(os.path.join(current_dir,out_folder,filename))
                case _:
                    print("Postion Must be on of (tr-tl-dr-dl1)")
                    break
    print("done put logo on all image")

    
