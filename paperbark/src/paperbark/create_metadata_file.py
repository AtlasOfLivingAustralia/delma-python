import os

def create_metadata_file(self):
        """
        Creates a markdown file containing the metadata information needed for the DwCA.  The user can edit this 
        markdown, and use it to generate the metadata files.

        Parameters
        ----------
            ``filename`` : ``str``
                Option whether to return a dictionary object containing full taxonomic information on your species.  Default to ``False``. 
            ``path`` : ``str``
                File path to your working directory.  Default is directory you are currently in.

        Returns
        -------
            ``None``
        """
        
        if not os.path.exists(self.metadata_md):
            os.system("cp {} {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'metadata_template.md'),os.path.join(self.metadata_md)))
        else:
            pass