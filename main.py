"""
Bank transactions visualization project
Leon Nijenhuis
Edit: 2023-06-21

WEB functies moeten geen berekeningen doen, die voeg je in script toe
"""
import file_management

files = file_management.Files()

df_data, df_name = files.read()
print(df_data.info(verbose=True))
files.save(df_data, df_name)

# process_data.process_directory()
# figures.plot_data()

