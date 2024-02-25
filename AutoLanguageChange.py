import bpy

class LanguageSwitchOperator(bpy.types.Operator):
    bl_idname = "wm.language_switch"
    bl_label = "Switch Language"
    
    def execute(self, context):
        # 获取当前语言
        current_language = bpy.context.preferences.view.language
        
        # 切换语言
        if current_language == 'en_US':
            bpy.context.preferences.view.language = 'zh_HANS'
        else:
            bpy.context.preferences.view.language = 'en_US'
        
        return {'FINISHED'}

def draw_menu(self, context):
    layout = self.layout
    layout.operator("wm.language_switch")

# 注册插件
def register():
    bpy.utils.register_class(LanguageSwitchOperator)
    bpy.types.TOPBAR_HT_upper_bar.append(draw_menu)

# 注销插件
def unregister():
    bpy.utils.unregister_class(LanguageSwitchOperator)
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_menu)

if __name__ == "__main__":
    register()
