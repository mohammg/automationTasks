#python3 -m pip install --upgrade Pillow
from PIL import Image
import os
import shutil
fite_size=0
out_folder='output'
current_dir =os.path.dirname(os.path.realpath(__file__))
percent=0
def resize():
    if not os.path.exists(os.path.join(current_dir,out_folder)):
        os.mkdir(os.path.join(current_dir,out_folder))
    for filename in os.listdir(current_dir):
        filename=filename.lower()
        if filename.endswith(('jpg','png','jpeg')):
            ##OPen image-->get Image size-->resize
            image=Image.open(os.path.join(current_dir, filename))
            width, height = image.size
            print(f'fite size is {fite_size}')
            if width>fite_size and height >fite_size:
                    if percent>0:
                         height=int(height*percent/100)
                         width=int(width*percent/100)
                    else:
                        if width>height:
                            height=int((fite_size/width)*height)
                            width=fite_size
                        else:
                            width=int((fite_size/height)*width)
                            height=fite_size
                    image=image.resize((width,height))
                    image=image.save(os.path.join(current_dir,out_folder,filename))
            else:
                 shutil.copy(os.path.join(current_dir, filename),os.path.join(current_dir,out_folder))        
    print ("don resize")