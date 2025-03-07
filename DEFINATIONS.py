# install UV python   
'''powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"''' # run in cmd
#go to UV PYTTHON WESITE
#uv --version to check
# UV is python package manager like npm in typscript
# tools like dependecies

# initialize with generate password
#means create a folder through UV
#example
'''uv init generate-password''' # folder created with some files

#add streamlit 
'''uv add streamlit'''
#virtual environment created

# now activate
'''.venv\script\activate'''
#used for activate virtual environment on cli

# we have installed streamlit, so it will run web application 
# stramlit run main.py
#Local URL: http://localhost:8501
#just run
