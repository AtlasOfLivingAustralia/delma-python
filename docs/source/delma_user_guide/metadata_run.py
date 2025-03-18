import delma
import pandas as pd

# set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

delma.create_md(metadata_md='metadata.md',working_dir='./delma_user_guide/')
print(delma.display_as_dataframe(metadata_md='metadata.md',working_dir='./delma_user_guide/'))