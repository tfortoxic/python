import os

# Get the current working directory
current_directory = os.getcwd()

# Get a list of entries in the specified directory
directory_entries = os.listdir(path)

# Create a new directory
os.mkdir(path)

# Create directories recursively
os.makedirs(path)

# Join one or more path components intelligently
joined_path = os.path.join(path, *paths)

# Check if a path exists
path_exists = os.path.exists(path)

# Check if a path points to a regular file
is_file = os.path.isfile(path)

# Check if a path points to a directory
is_directory = os.path.isdir(path)

# Rename a file or directory
os.rename(src, dst)

# Remove a file
os.remove(path)

# Get the normalized absolute path of a file or directory
normalized_path = os.path.abspath(path)

# Split the pathname into root and extension
root, ext = os.path.splitext(path)

# Get the directory name of a file or directory
dirname = os.path.dirname(path)

# Get the base name of a file or directory
basename = os.path.basename(path)

# Get the size of a file in bytes
file_size = os.path.getsize(path)

