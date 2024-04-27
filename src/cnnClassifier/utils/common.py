import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
"""
read_yaml(path_to_yaml: Path) -> ConfigBox:
This function is used to read a YAML file and return its contents as a ConfigBox object. A ConfigBox is a dictionary-like object that provides access to its keys via attribute syntax (dot notation) as well as dictionary-style access.

The function takes a single argument path_to_yaml of type Path, which represents the path to the YAML file that needs to be read.
It uses the @ensure_annotations decorator from the ensure library, which helps in enforcing type annotations and handling type-related errors.
Inside the function, it opens the YAML file using the open() function and passes the file object to yaml.safe_load() from the yaml library. This function safely loads the YAML content while preventing potential security issues.
If the YAML file is empty, it raises a ValueError with the message "yaml file is empty". This is handled using a try-except block and the BoxValueError exception from the box library.
If any other exception occurs, it raises that exception.
If the YAML file is loaded successfully, it converts the loaded content to a ConfigBox object and returns it.
It also logs a success message using the logger.info() function, indicating that the YAML file has been loaded successfully.
"""
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

"""create_directories(path_to_directories: list, verbose=True):
This function is used to create a list of directories, ensuring that they exist.

The function takes two arguments:
path_to_directories: a list of paths representing the directories to be created.
verbose: an optional boolean parameter (defaulting to True) that controls whether log messages are printed or not.

It also uses the @ensure_annotations decorator to enforce type annotations.
Inside the function, it iterates over the list of paths using a for loop.
For each path, it uses the os.makedirs() function to create the directory (and any intermediate directories) if they don't exist. The exist_ok=True argument ensures that no error is raised if the directory already exists.
If the verbose parameter is True, it logs a message using logger.info() for each directory that is created."""


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

"""save_json(path: Path, data: dict):

This function saves a Python dictionary as a JSON file.
It takes two arguments: path (a Path object representing the file path to save the JSON file) and data (the dictionary to be saved as JSON).
It opens the file in write mode using open(path, "w") and uses json.dump(data, f, indent=4) from the json module to write the dictionary as a JSON string to the file, with 4 spaces for indentation.
It also logs a message indicating the path where the JSON file was saved."""


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)
"""load_json(path: Path) -> ConfigBox:

This function loads data from a JSON file and returns it as a ConfigBox object.
It takes one argument: path (a Path object representing the file path of the JSON file to be loaded).
It opens the file using open(path) and uses json.load(f) from the json module to load the JSON data as a Python dictionary.
It then converts the dictionary to a ConfigBox object using ConfigBox(content) and returns it.
It also logs a message indicating that the JSON file was loaded successfully."""


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

"""save_bin(data: Any, path: Path):

This function saves data as a binary file using the joblib library.
It takes two arguments: data (the data object to be saved, which can be of any type) and path (a Path object representing the file path to save the binary file).
It uses joblib.dump(value=data, filename=path) to save the data object as a binary file at the specified path.
It logs a message indicating the path where the binary file was saved."""


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

"""load_bin(path: Path) -> Any:

This function loads data from a binary file using the joblib library.
It takes one argument: path (a Path object representing the file path of the binary file to be loaded).
It uses joblib.load(path) to load the data object from the binary file.
It returns the loaded data object, which can be of any type.
It also logs a message indicating that the binary file was loaded successfully."""

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

"""get_size(path: Path) -> str:

This function returns the size of a file in kilobytes (KB) as a string.
It takes one argument: path (a Path object representing the file path).
It uses os.path.getsize(path) to get the size of the file in bytes and then divides it by 1024 to convert it to kilobytes.
It rounds the size to the nearest integer using round() and returns a string formatted as "~ {size_in_kb} KB"."""


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

"""decodeImage(imgstring, fileName):

This function decodes a base64-encoded image string and saves it as a file.
It takes two arguments: imgstring (the base64-encoded image string) and fileName (the name of the file to save the decoded image).
It uses base64.b64decode(imgstring) to decode the base64-encoded string into a bytes object.
It opens a file in binary write mode using open(fileName, 'wb') and writes the decoded bytes object to the file using f.write(imgdata).
It closes the file using f.close()."""


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
