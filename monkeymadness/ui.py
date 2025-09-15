import bpy


class MONKEYMADESS_PT_panel(bpy.types.Panel):
    bl_label = "Monkey Madness"
    bl_idname = "MONKEYMADESS_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # N-panel
    bl_category = 'Monkey'

    def draw(self, context):
        layout = self.layout
        layout.operator("monkeymadess.add_random_monkey", text="Add Random Monkey")


CLASSES = (
    MONKEYMADESS_PT_panel,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
