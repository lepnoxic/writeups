# Level 27: Secret Weapon

## Problem

After having identified the location of the enemy, you all assess the damage that has been dealt to the planet. Spock connects itself to the planet's mainframe, to go through the history of the planet. Where he finds a long-lost file about a hidden weapon under the planet's surface.
You must locate the secret weapon to turn the tides in your favor. 

**Locating the secret weapon**
```
The long lost file has this riddle..
Look up to the heavens and contemplate,
Not all stars, in brilliance, equate, it's fate.
Seek the ones that gleam pure and white,
And once that quest is complete,
Seek amongst them the brightest light.
You look at starry night sky and ponder what it means
``````
Flag format: sctf{lowercasetext} 

## Writeup

We are given an image with black and white pattern. We are told that not all stars equate, this means not all white blocks might be having perfect 255,255,255 rgb value. And they are telling us to seek amongst the brightest, so we just need to focus on the pixels that are 255,255,255.

we can make a script for this using pillows and replace the true white ones as red.

```python
from PIL import Image
import numpy as np

def convert_white_to_red_and_black(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Convert the image to a NumPy array for easier manipulation
    img_array = np.array(image)

    # Define the RGB value to replace (255,255,255) with (255,0,0)
    white_color = np.array([255, 255, 255])
    red_color = np.array([255, 0, 0])
    black_color = np.array([0, 0, 0])

    # Find pixels with the white color and replace them with red, all others with black
    white_pixels = np.all(img_array == white_color, axis=-1)
    img_array[white_pixels] = red_color
    img_array[~white_pixels] = black_color

    # Convert the NumPy array back to an image
    modified_image = Image.fromarray(img_array)

    # Save the modified image
    modified_image.save(output_path)

if __name__ == "__main__":
    input_file = "starry_night_sky.png"  # Replace with your input file path
    output_file = "output.png"  # Replace with your desired output file path

    convert_white_to_red_and_black(input_file, output_file)
```

![Alt text](image.png)

This is a constellation for the big dipper. We are asked what is the brightest star among this which comes to be Alioth.

`sctf{alioth}`