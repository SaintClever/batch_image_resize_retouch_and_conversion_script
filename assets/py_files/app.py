from pathlib import Path
import cv2


def photo_retoucher():
  p = Path('.')
  # print(p) # locate directory
  
  imgs = list(p.glob('*.jpg'))
  # print(imgs) # create list of images

  counter = 0
  for img in imgs:
    # change the color
    jpg = cv2.imread(f'{img}', 0) # 1 is for color / 2 for grayscale
    
    # change the size
    width = int(jpg.shape[1]/2)
    height = int(jpg.shape[0]/2)
    resized_img = cv2.resize(jpg, (width, height))
    
    # write / create image and present image
    counter += 1
    file_name = 'img_{}.jpg'.format(counter)
    cv2.imwrite(file_name, resized_img)
    cv2.imshow(file_name, resized_img)
    
    # wait for a second and close image window
    cv2.waitKey(2500)
    cv2.destroyAllWindows()


photo_retoucher()