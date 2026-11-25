import bpy
from .. import __package__ as base_package


class YukkublendPreferences(bpy.types.AddonPreferences):
    bl_idname = base_package or "yukkublend"

    characters_path: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="characters_path",
        description="characters_path_desc",
        subtype="FILE_PATH",
        default="",
    )

    scripts_path: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="scripts_path",
        description="scripts_path_desc",
        subtype="FILE_PATH",
        default="",
    )

    aq1_usr_key: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="aq1_usr_key",
        description="aq1_usr_key_desc",
        subtype="PASSWORD",
        default="",
    )

    aq2_usr_key: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="aq2_usr_key",
        description="aq2_usr_key_desc",
        subtype="PASSWORD",
        default="",
    )

    aq10_usr_key: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="aq10_usr_key",
        description="aq10_usr_key_desc",
        subtype="PASSWORD",
        default="",
    )

    aqk2k_usr_key: bpy.props.StringProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="aqk2k_usr_key",
        description="aqk2k_usr_key_desc",
        subtype="PASSWORD",
        default="",
    )

    wasmtime_debug: bpy.props.BoolProperty(  # pyright: ignore[reportInvalidTypeForm]
        name="wasmtime_debug",
        description="wasmtime_debug_desc",
        default=False,
    )

    def draw(self, _context):
        layout = self.layout
        layout.label(text="path_options", icon="FOLDER_REDIRECT")
        layout.prop(self, "characters_path")
        layout.prop(self, "scripts_path")
        layout.separator(type="LINE")
        layout.label(text="lincense_options", icon="KEYINGSET")
        layout.label(text="license_options_desc", icon="INFO")
        layout.prop(self, "aq1_usr_key")
        layout.prop(self, "aq2_usr_key")
        layout.prop(self, "aq10_usr_key")
        layout.prop(self, "aqk2k_usr_key")
        layout.separator(type="LINE")
        layout.label(text="debug_options", icon="MOD_BUILD")
        layout.prop(self, "wasmtime_debug")
        
