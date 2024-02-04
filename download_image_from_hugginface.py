import os
if not os.path.exists('./dress_images'):
    os.mkdir('./dress_images')

from tqdm.auto  import tqdm
for i in tqdm(range(len(dataset)-43380)):
    dataset[i]['image'].save(f'./dress_images/{i}.jpg')

#for generating prompt

import pandas as pd
import os
from tqdm.auto import tqdm

# Assuming your text files are stored in a directory, for example, './text_files/'
text_files_directory = './prompt/'

# Get a list of all text files in the directory
text_files = [f for f in os.listdir(text_files_directory) if f.endswith('.txt')]

# Create an empty DataFrame
df = pd.DataFrame(columns=['index', 'text'])

# Iterate through the text files
for i, text_file in tqdm(enumerate(text_files)):
    file_path = os.path.join(text_files_directory, text_file)
    
    # Read the content of the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
    
    # Append the data to the DataFrame
    df = df.append({'index': i, 'text': text_content}, ignore_index=True)

# Save the DataFrame to a CSV file
df.to_csv('./prompt.csv', index=False)
