"""For Penguins ana menusu icin FancyMenu dosyalarini uretir: <cikti>/config/fancymenu/..."""
import os, random, sys, time, uuid
from PIL import Image, ImageDraw, ImageFilter

IMG = "/tmp/claude-1000/-home-burak/b105034c-d86a-4a81-89df-530aa606386c/scratchpad/images"
OUT = os.path.join(sys.argv[1], "config", "fancymenu")
ASSETS = os.path.join(OUT, "assets")
SERVER = "play.burakdeyirmenci.com:25565"
os.makedirs(ASSETS, exist_ok=True)
os.makedirs(os.path.join(OUT, "customization"), exist_ok=True)

# --- gorseller ---
bg = Image.open(f"{IMG}/menu_b.png").convert("RGBA").resize((1920, 1080))
shade = Image.new("L", bg.size, 0)
ImageDraw.Draw(shade).ellipse((560, 330, 1360, 1000), fill=120)
bg = Image.composite(Image.new("RGBA", bg.size, (8, 14, 30, 255)), bg,
                     shade.filter(ImageFilter.GaussianBlur(90)).point(lambda v: int(v * 0.8)))
bg.convert("RGB").save(f"{ASSETS}/forpenguins_bg.png")
Image.open(f"{IMG}/title.png").save(f"{ASSETS}/forpenguins_title.png")


def button_texture(name, fill, edge, highlight):
    """200x20 nine-slice buton dokusu (kenar 3px)."""
    im = Image.new("RGBA", (200, 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 199, 19), fill=edge)
    d.rectangle((1, 1, 198, 18), fill=fill)
    d.line((2, 2, 197, 2), fill=highlight)  # ust parlama
    d.line((2, 17, 197, 17), fill=(0, 0, 0, 90))  # alt golge
    im.save(f"{ASSETS}/{name}.png")


button_texture("btn_normal", (18, 28, 52, 205), (120, 160, 210, 230), (60, 80, 120, 230))
button_texture("btn_hover", (36, 62, 104, 225), (200, 235, 255, 255), (110, 150, 200, 240))
button_texture("btn_accent", (40, 110, 170, 225), (170, 225, 255, 255), (90, 165, 220, 240))
button_texture("btn_accent_hover", (62, 145, 210, 240), (235, 250, 255, 255), (130, 200, 240, 250))

# --- layout ---
NOW = int(time.time() * 1000)


def uid():
    return f"{uuid.uuid4()}-{NOW + random.randint(0, 9999)}"


def req():
    i = uid()
    return i, f"[loading_requirement_container_meta:{i}] = [groups:][instances:]"


def common(element_type, ident, anchor, x, y, w, h, extra=""):
    ri, rl = req()
    return f"""  element_type = {element_type}
  instance_identifier = {ident}
  appearance_delay = no_delay
  appearance_delay_seconds = 1.0
  fade_in_v2 = no_fading
  fade_in_speed = 1.0
  fade_out = no_fading
  fade_out_speed = 1.0
  base_opacity = 1.0
  auto_sizing = false
  auto_sizing_base_screen_width = 0
  auto_sizing_base_screen_height = 0
  sticky_anchor = false
  anchor_point = {anchor}
  x = {x}
  y = {y}
  width = {w}
  height = {h}
  stretch_x = false
  stretch_y = false
  stay_on_screen = true
  element_loading_requirement_container_identifier = {ri}
  {rl}
  enable_parallax = false
  parallax_intensity_v2 = 0.5
  invert_parallax = false
  animated_offset_x = 0
  animated_offset_y = 0
  load_once_per_session = false
  in_editor_color = #FFC800FF
  layer_hidden_in_editor = false
{extra}"""


def button_props(block_line, actions, normal, hover, label=None):
    ai, al = req()
    lab = f"  label = {label}\n" if label is not None else ""
    return f"""{block_line}
{actions}  backgroundnormal = [source:local]/config/fancymenu/assets/{normal}.png
  backgroundhovered = [source:local]/config/fancymenu/assets/{hover}.png
  restartbackgroundanimations = true
  nine_slice_custom_background = true
  nine_slice_border_x = 3
  nine_slice_border_y = 3
{lab}  navigatable = true
  widget_active_state_requirement_container_identifier = {ai}
  {al}
  is_template = false
  template_apply_width = false
  template_apply_height = false
  template_apply_posx = false
  template_apply_posy = false
  template_apply_opacity = false
  template_apply_visibility = false
  template_apply_label = false
  template_share_with = buttons
  nine_slice_slider_handle = false
  nine_slice_slider_handle_border_x = 5
  nine_slice_slider_handle_border_y = 5
"""


def vanilla(ident, x=0, y=0, w=200, h=20, hidden=False):
    b = uid()
    props = button_props(f"  button_element_executable_block_identifier = {b}\n"
                         f"  [executable_block:{b}][type:generic] = [executables:]", "", "btn_normal", "btn_hover")
    anchor = "vanilla" if hidden else "mid-centered"
    extra = f"  is_hidden = {'true' if hidden else 'false'}\n  automated_button_clicks = 0\n"
    return "vanilla_button {\n" + props + common("vanilla_button", ident, anchor, x, y, w, h, extra) + "}\n"


def join_button(label, x, y, w, h):
    b, a = uid(), uid()
    block = (f"  button_element_executable_block_identifier = {b}\n"
             f"  [executable_action_instance:{a}][action_type:joinserver] = {SERVER}\n"
             f"  [executable_block:{b}][type:generic] = [executables:{a};]")
    props = button_props(block, "", "btn_accent", "btn_accent_hover", label)
    return "element {\n" + props + common("custom_button", uid(), "mid-centered", x, y, w, h) + "}\n"


def image(src, anchor, x, y, w, h):
    head = f"""  source = [source:local]/config/fancymenu/assets/{src}
  repeat_texture = false
  nine_slice_texture = false
  nine_slice_texture_border_x = 5
  nine_slice_texture_border_y = 5
  image_tint = #FFFFFF
  restart_animated_on_menu_load = false
"""
    return "element {\n" + head + common("image", uid(), anchor, x, y, w, h) + "}\n"


meta_i, meta_l = req()
layout = f"""type = fancymenu_layout

layout-meta {{
  identifier = title_screen
  render_custom_elements_behind_vanilla = false
  last_edited_time = {NOW}
  is_enabled = true
  randommode = false
  randomgroup = 1
  randomonlyfirsttime = false
  layout_index = 0
  {meta_l}
}}

menu_background {{
  image_path = [source:local]/config/fancymenu/assets/forpenguins_bg.png
  slide = false
  repeat_texture = false
  parallax = false
  parallax_intensity = 0.02
  invert_parallax = false
  restart_animated_on_menu_load = false
  instance_identifier = {uid()}
  background_type = image
}}

customization {{
  action = backgroundoptions
  keepaspectratio = true
}}

layout_action_executable_blocks {{
}}

"""
# GUI birimleri, ekran merkezine gore (taslaktaki 1080p / olcek 3 yerlesimi)
layout += image("forpenguins_title.png", "top-centered", -160, 22, 320, 69) + "\n"
layout += join_button("Sunucuya Katıl", -100, -37, 200, 20) + "\n"
layout += vanilla("mc_titlescreen_singleplayer_button", -102, -9, 98, 20) + "\n"
layout += vanilla("mc_titlescreen_multiplayer_button", 4, -9, 98, 20) + "\n"
for mods_id in ("forge_titlescreen_mods_button", "titlescreen_mods_button"):  # 3.10'da id degismis olabilir
    layout += vanilla(mods_id, -100, 15, 200, 20) + "\n"
layout += vanilla("mc_titlescreen_options_button", -102, 39, 98, 20) + "\n"
layout += vanilla("mc_titlescreen_quit_button", 4, 39, 98, 20) + "\n"
for hidden in ("mc_titlescreen_realms_button", "minecraft_realms_notification_icons_widget",
               "minecraft_logo_widget", "minecraft_splash_widget"):
    layout += vanilla(hidden, hidden=True) + "\n"

open(os.path.join(OUT, "customization", "forpenguins_title_screen.txt"), "w").write(layout)
open(os.path.join(OUT, "customizablemenus.txt"), "w").write(
    "type = customizablemenus\n\nnet.minecraft.client.gui.screens.TitleScreen {\n}\n")
open(os.path.join(OUT, "options.txt"), "w").write("""##[customization]

B:modpack_mode = 'true';
B:show_customization_overlay = 'false';
B:advanced_customization_mode = 'false';


##[window]

S:custom_window_title = 'For Penguins';


##[debug_overlay]

B:show_debug_overlay = 'false';


##[tutorial]

B:show_welcome_screen = 'false';
""")
print(OUT)
