import os
from os.path import exists
import re
import click
from pathlib import Path
from appdirs import user_config_dir
from shutil import copy
import platform
import pyperclip
import subprocess
import pdf2image as p2i


# syntax: python -m illustrator-figures crear-editar "nombre_fig" directorio_figure
@click.group()
def cli():
   pass

@cli.command(help='Convert PDF to PNG')
@click.argument('directorio')
def convert(directorio):
    directorio = Path(directorio.strip()).with_suffix('.pdf')
    print(directorio.stem)
    if directorio.stem == "formulario":
        copy(directorio, "/mnt/c/Users/heber/Documents/obs config/")
    else:
        page = p2i.convert_from_path(directorio, 500)
        page[0].save('/mnt/c/Users/heber/Documents/obs config/stremingpregunta.jpg', 'JPEG')

if __name__ == "__main__":
    cli()
