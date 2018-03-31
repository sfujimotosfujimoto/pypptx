import pandas as pd
import os
from pptx import Presentation

print("Where is your data?")
print("You can drag your file to this terminal.")
from_path = input().strip()
print("Where should I put your data?")
print("Don't forget to add `.pptx` to the name of the file")
to_path = input().strip()

prs = Presentation(os.path.abspath('ppt/base.pptx'))

df = pd.read_csv(os.path.abspath(from_path))
count = 0
for index, row in df.iterrows():

    slide = prs.slides.add_slide(prs.slide_layouts[2])
    try:

        slide.placeholders[0].text = row[0]
        slide.placeholders[1].text = row[1]
        if index % 10 == 0:

            print(f"Made {index+1} slides.")
        count = index
    except ValueError:
        pass
    except TypeError:
        pass

prs.save(os.path.abspath(to_path))
print(f"Saved! Made a total of {count} slides!")
