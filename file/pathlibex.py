from pathlib import Path

pp = Path(__file__) # E:\Dropbox\Dev\Notes\python\nicegui_slideshow\pathlibex.py

### Parents ###
pa = Path(__file__).parent
pas = Path(__file__).parents
print(pa)      # E:\Dropbox\Dev\Notes\python\nicegui_slideshow
print(pas)     # <WindowsPath.parents>
print(pas[0])  # E:\Dropbox\Dev\Notes\python\nicegui_slideshow
print(pas[1])  # E:\Dropbox\Dev\Notes\python

### NAME PARTS ###
# name, suffix, stem, anchor, parts
print(pp.name) # pathlibex.py
print(pp.suffix)  # .py
print(pp.anchor) # e:\
print(pp.stem)  # pathlibex
print(pp.parts[2]) #Dev

### TESTS ###
# is_absolute, exists, if_file, is_dir, with_name, with_stem, with_suffix

# is_absolute
print(Path("nicegui_slideshow\\pathlibex.py").is_absolute) #False
print(Path("E:\\Dropbox\\Dev\\Notes\\python\\nicegui_slideshow\\pathlibex.py").is_absolute)  # True

# with_name & with_stem & with_suffix
print(pp.with_name('newscript.py'))
print(pp.with_stem("newscript"))
print(pp.with_suffix(".py"))

# is_dir & is_file
pp = Path(__file__)
pa = pp.parent
print(pp.is_file()) # True
print(pa.is_dir())  # True

# exists
print(Path('missingfile.py').exists()) #False



# iterdir(), glob(), rglob()
# glob uses ??? and [aaa]
# you can cast to a list... list(pa.rglob('*.md'))
# you can use list comprehensions
pp = Path(__file__)
pa = pp.parent
for child in pa.iterdir():
    print(child.name)

for child in pa.glob('*.py'):
    print(child.name)



# joinpath
pp = Path(__file__)
pa = pp.parent
print(pa.joinpath('scripts', 'newscript.py'))
# E:\Dropbox\Dev\Notes\python\nicegui_slideshow\scripts\newscript.py

# match
pp = Path(__file__)
print(pp.match('*.py')) #True
print(pp.match("python/*.py"))  # False
print(pp.match("python/*/*.py"))  # True


# cwd & home
print(Path.cwd())
print(Path.home())


# mkdir
pp = Path(__file__)
pa = pp.parent
newdir = pa.joinpath('newdir')
Path.mkdir(newdir, exist_ok=False, parents=)

# touch
# exists_ok...
# True: If the file already exists, no action is taken. The function returns `None`.
# False: If the file already exists, an `FileExistsError` exception is raised.
file_name = r'newfile.txt'
Path.touch(file_name, exist_ok=True)

# rename

# read_text(), write_text(), open

# replace (a rename and move alt)
original_path = Path("old_file.txt")
new_path = Path("new_file.txt")
new_path = original_path.replace(new_path)
print(new_path)  # Output: new_file.txt

# stat -> 
pp.stat().st_mtime()
pp.stat().st_ctime()
pp.stat().st_size()