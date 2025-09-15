import bpy


class MONKEYMADESS_MT_menu(bpy.types.Menu):
    bl_label = "Monkey Madness"
    bl_idname = "MONKEYMADESS_MT_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("monkeymadess.add_random_monkey", text="Add Random Monkey")


def draw_menu(self, context):
    self.layout.menu(MONKEYMADESS_MT_menu.bl_idname)


CLASSES = (
    MONKEYMADESS_MT_menu,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_editor_menus.append(draw_menu)


def unregister():
    bpy.types.VIEW3D_MT_editor_menus.remove(draw_menu)
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
