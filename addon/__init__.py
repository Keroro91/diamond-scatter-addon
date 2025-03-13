bl_info = {
    "name": "Diamond Scatter Addon",
    "description": "Addon to scatter diamonds on a surface with different patterns",
    "author": "Hugo Tubiana",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > N Panel > Diamond Scatter",
    "category": "Object",
}

import bpy
from . import ui  # Importe le fichier ui.py

def register():
    ui.register()

def unregister():
    ui.unregister()

if __name__ == "__main__":
    register()