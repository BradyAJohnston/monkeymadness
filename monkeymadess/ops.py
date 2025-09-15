import bpy
import random


class MONKEYMADESS_OT_add_random_monkey(bpy.types.Operator):
    bl_idname = "monkeymadess.add_random_monkey"
    bl_label = "Add Random Monkey"
    bl_description = "Add a Suzanne at a random location in (-10, 10)"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        loc = (
            random.uniform(-10.0, 10.0),
            random.uniform(-10.0, 10.0),
            random.uniform(-10.0, 10.0),
        )
        bpy.ops.mesh.primitive_monkey_add(location=loc)
        return {"FINISHED"}


CLASSES = (
    MONKEYMADESS_OT_add_random_monkey,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
