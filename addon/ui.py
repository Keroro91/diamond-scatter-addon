import bpy
import importlib
import sys

class DIAMOND_OT_reload_addon(bpy.types.Operator):
    """Recharge l'addon sans redémarrer Blender"""
    bl_idname = "diamond.reload_addon"
    bl_label = "Reload Addon"

    def execute(self, context):
        # Get the addon module
        addon_name = "diamond_scatter_addon"  # Name of your addon folder
        if addon_name in sys.modules:
            # Unregister all classes
            bpy.utils.unregister_class(DIAMOND_PT_main_panel)
            bpy.utils.unregister_class(DIAMOND_OT_reload_addon)

            # Reload the addon module
            addon_module = sys.modules[addon_name]
            importlib.reload(addon_module)

            # Re-register all classes
            addon_module.register()

            self.report({'INFO'}, "Addon reloaded successfully!")
        else:
            self.report({'ERROR'}, "Addon module not found!")
        return {'FINISHED'}

class DIAMOND_PT_main_panel(bpy.types.Panel):
    """Panneau principal de l'addon"""
    bl_label = "Diamond Scatter"
    bl_idname = "DIAMOND_PT_main_panel"
    bl_space_type = 'VIEW_3D'  # Interface dans le viewport 3D
    bl_region_type = 'UI'  # Dans la barre latérale "N"
    bl_category = "Diamond Scatter"  # Nom de l'onglet

    def draw(self, context):
        layout = self.layout

        # Ajouter un bouton pour recharger l'addon
        layout.operator("diamond.reload_addon", text="Reload Addon", icon='FILE_REFRESH')

        # Ajouter un label de bienvenue
        layout.label(text="Bienvenue dans Diamond Scatter 1!")

def register():
    bpy.utils.register_class(DIAMOND_OT_reload_addon)
    bpy.utils.register_class(DIAMOND_PT_main_panel)

def unregister():
    bpy.utils.unregister_class(DIAMOND_PT_main_panel)
    bpy.utils.unregister_class(DIAMOND_OT_reload_addon)