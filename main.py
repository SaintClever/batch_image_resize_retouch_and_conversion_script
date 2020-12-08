from pathlib import Path
from glob import glob
from datetime import datetime
import cv2, os, time, shutil


# Get date and format to a string
date_str = datetime.today().strftime("%m-%d-%Y_%H-%M-%S")


# Get user input
convert_from = input('\nConvert from [jpg or png]: ').lower()
c_or_g = input('Color or grayscale [c or g]: ').lower()
convert_to = input('Convert to [jpg or png]: ').lower()
print('')

# Create color or grayscale image
def color_or_grayscale():
  if c_or_g == 'g':
    return 0
  else:
    return 1
  

# Produces images
def photo_retoucher(convert_from, color, convert_to):
  # create a dir for converted files and use the date as the name
  Path(date_str).mkdir(parents=True, exist_ok=True)

  p = Path('.')
  # print(p) # locate directory
  
  imgs = list(p.glob(f'*.{convert_from}'))
  # print(imgs) # create list of images

  counter = 0
  for img in imgs: 
    # change the color
    jpg = cv2.imread(f'{img}', color) # 1 is for color / 2 for grayscale
    
    # change the size
    width = int(jpg.shape[1]/2)
    height = int(jpg.shape[0]/2)
    resized_img = cv2.resize(jpg, (width, height))
    
    # write / create image and present image
    counter += 1
    file_name = 'img_{counter}.{convert_to}'.format(counter=counter, convert_to=convert_to)
    cv2.imwrite(file_name, resized_img)
    cv2.imshow(file_name, resized_img)
      
    # wait for a second and close image window
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    
    # move files to created folder
    shutil.move(file_name, date_str)
    # shutil.move(os.path.join(p, file_name), os.path.join(date_str, file_name))
      
    
color = color_or_grayscale()
photo_retoucher(convert_from, color, convert_to)
