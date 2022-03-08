import os 
import base64 

def image_as_base64(img_file, format='jpeg'):
    encoded_string = ''
    encoded_string = base64.b64encode(img_file.open(mode='rb').read()).decode('utf-8')
    return 'data:image/%s;base64, %s' %(format, encoded_string)
