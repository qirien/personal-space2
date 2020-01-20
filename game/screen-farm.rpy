# Using this screen, the user can select which crops to plant where and see the projected results.  When they are done, they can hit "Accept Plan".
# Farm Planning Screen
#

screen plan_farm:
    tag plan_farm
    style_prefix "plan_farm"
    $ valid_layout = farm.is_valid_layout()
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User [his_name] has logged on." size 12 xalign 0.1 ypos 22 color "#fff"
        textbutton "?" xpos 1077 ypos 18 action Jump("farm_tutorial")
        textbutton "             " xpos 1085 ypos 18 action ShowMenu("preferences")
        vbox:
            area (60, 50, 1150, 620)
            yfill True
            hbox:
                xfill True
                yfill True
                # crop details here
                frame:
                    yfill True
                    background "roundrect_darkgray"

                    vbox:
                        use farm_details_screen

                        hbox:
                            frame:
                                xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH + 25
                                style "plan_farm_subframe"
                                hbox:
                                    label "Status" xsize 100
                                    # TODO: allow more than one status?
                                    if (not valid_layout):
                                        if (farm.get_total_calories() < get_calories_required(year)):
                                            text "Need more calories!" style "plan_farm_status_text"
                                        elif (farm.crops.count("goats") != crop_info[get_crop_index("goats")][MAXIMUM_INDEX]):
                                            text "Need to allocate all goats!" style "plan_farm_status_text"
                                        elif (crop_enabled("honey") and (farm.crops.count("honey") != crop_info[get_crop_index("honey")][MAXIMUM_INDEX])):
                                            text "Need to allocate all bees!"
                                            style "plan_farm_status_text"
                                        else:
                                            text "Cannot plant crops where there is insufficient nitrogen!" style "plan_farm_status_text"
                                    else:
                                        text "OK!" style "plan_farm_status_text" color green_dark
                            hbox:
                                xfill True
                                xsize RIGHT_COLUMN_WIDTH
                                textbutton "Clear":
                                    style "round_button"
                                    action [
                                            clear_crops,
                                            renpy.restart_interaction
                                            ]
                                textbutton "Random":
                                    style "round_button"
                                    action [
                                            set_default_crops,
                                            renpy.restart_interaction
                                            ]
                                textbutton "Done":
                                # TODO: What if no valid layout is possible? Have emergency help button?
                                    style "round_button"
                                    sensitive valid_layout
                                    action Jump("yearly_events")



screen colony_messages_button(read_colony_messages):
    if (not read_colony_messages):
        text "{color=#FF0}{b}NEW!{/b}{/color} " ypos 30 xalign 1.0 outlines [(1, "#000", 1, 1)]
    else:
        text "" ypos 30 xalign 0.0 # We have to have this here or it messes up all the positions

    textbutton "Message Board" action Jump("yearly_messages") xoffset 20 #Call("yearly_messages")

# To change appearance, see screens.rpy, screen nvl
label yearly_messages:
    $ message = "message" + `year`
    $ read_messages = True
    nvl clear
    call expression message
    #computer "\n(End of messages)"
    nvl clear
    call screen plan_farm
    # TODO: something weird is happening where reading the message board makes the game return to the main menu after picking crops.
    "You should never see this."
##
# Subscreen letting the user see information on crops and choose which to plant this year
##
screen farm_details_screen:
    hbox:
        xalign 0.5
        xfill True
        # Show family info
        vbox:
            xsize LEFT_COLUMN_WIDTH
            frame:
                style "plan_farm_subframe"
                vbox:
                    xalign 0.0
                    label "Family"
                    text "[his_name] & [her_name]" xoffset 20
                    if (earth_year < 2):
                        $ kid_months = int(earth_year * 12)
                        $ kid_age = str(kid_months) + " Earth months old"
                    else:
                        $ kid_age = str(int(earth_year)) + " Earth years old"
                    text "[kid_name], [kid_age]" xoffset 20
                    if (bro_birth_year != 0):
                        if (earth_year < 2):
                            $ bro_months = int(get_earth_years(bro_age) * 12)
                            $ bro_age = str(bro_months) + " Earth months old"
                        else:
                            $ bro_age = str(int(get_earth_years(bro_age))) + " Earth years old"
                        text "[bro_name], [bro_age]" xoffset 20
                    else:
                        text " "
                    text " "

                    text notifications italic True xoffset 20

            # Community info
            frame:
                style "plan_farm_subframe"
                vbox:
                    label "Community" # TODO: have cute icons for these, like on a phone?
                    # TODO: have icons for how much each group likes you?
                    use colony_messages_button(read_messages)
                    # TODO: make this have a "NEW!" icon when there's new stuff?
                    textbutton "Child Development" action Show("parenting_handbook", zoomin) xoffset 20
                    # TODO: add parenting quote

                    # TODO: Display poetry written
                    # TODO: how do I get the word_board variable here?
                    # textbutton "Poetry" action Show("poetry_display", args=word_board)

                    # TODO: show these somewhere beside previous screen?
                    # text notifications



        # Crop layout area
        frame:
            style "plan_farm_subframe"
            vbox:
                xsize MIDDLE_COLUMN_WIDTH
                ysize TOP_SECTION_HEIGHT
                hbox:
                    label "Layout" xfill False
                    null width 275
                    label "Year " + str(year) xalign 1.0
                use crops_layout

        # Totals so far
        frame:
            style "plan_farm_subframe"
            vbox:
                xalign 0.5
                xsize RIGHT_COLUMN_WIDTH
                ysize TOP_SECTION_HEIGHT
                label "Total"
                use crops_totals

# TODO: mask the rest of the screen?
screen choose_crop(crop_index=0):
    on "show" action SetVariable("selected_crop_index", get_crop_index(farm.crops[crop_index]))
    frame:
        style_prefix "crop_details"
        yalign 0.5
        xalign 0.5
        hbox:
            xsize MIDDLE_COLUMN_WIDTH + LEFT_COLUMN_WIDTH + 20
            spacing 10
            # vbox:
            #     spacing 10
            #     style_prefix "field_info"
            #     xsize LEFT_COLUMN_WIDTH
            #     label "Field Status"
            #     label "History" style "crop_details_label" text_color white
            #     use history_box(crop_index)
            #     null height 20
            #     label "Health" style "crop_details_label" text_color white
            #     text "Nitrogen Level: " + get_level_fuzzy(1 - (farm.health[crop_index][Field.NITROGEN_LEVEL_INDEX] / float(Field.NITROGEN_FULL)))
            #     if USE_PESTS:
            #         text "Pest Level: " + get_level_fuzzy(farm.health[crop_index][Field.PEST_LEVEL_INDEX] / float(Field.PEST_MAX))

            frame:
                style "plan_farm_subframe"
                vbox:
                    xfill True
                    hbox:
                        $ crop_name = crop_info[selected_crop_index][NAME_INDEX]
                        label crop_name.capitalize()
                        textbutton "X" xpos 120 ypos -2 action Hide("choose_crop", zoomout)
                    hbox:
                        style_prefix "crop_status"
                    # TODO: The text here gets cut off on the left
                        vpgrid:
                            cols 2
                            text "   Calories: " #extra spaces are needed because vpgrid takes size for ALL children from size of first child
                            frame:
                                use stat_icons(crop_info[selected_crop_index][CALORIES_INDEX], CALORIES_INDEX)
                            text "Nutrition: "
                            frame:
                                use stat_icons(crop_info[selected_crop_index][NUTRITION_INDEX], NUTRITION_INDEX)
                            text "Work: "
                            frame:
                                use stat_icons(crop_info[selected_crop_index][WORK_INDEX], WORK_INDEX)
                            text "Nitrogen: "
                            frame:
                                use stat_icons(crop_info[selected_crop_index][NITROGEN_INDEX]/5, NITROGEN_INDEX)

                            if (year >= MONEY_YEAR):
                                text "Value: "
                                use stat_icons(crop_info[selected_crop_index][VALUE_INDEX], VALUE_INDEX)
                            else:
                                null
                                null
                        text crop_descriptions[crop_name.rstrip("+")]
                    null height 30
                    vpgrid:
                        # TODO: change this based on number of enabled crops?
                        cols 5
                        spacing 10
                        draggable True
                        mousewheel True
                        #scrollbars "vertical"
                        side_xalign 0.5

                        for j in range(0, len(crop_info)):
                            # only show currently enabled crops where we haven't planted the maximum yet
                            if (crop_info[j][ENABLED_INDEX] and (crop_info[j][MAXIMUM_INDEX] > 0) and
                            (crop_temporarily_disabled != crop_info[j][NAME_INDEX])):
                                $ crop_name = crop_info[j][NAME_INDEX]
                                $ max_crops_reached = (farm.crops.count(crop_info[j][NAME_INDEX]) >= crop_info[j][MAXIMUM_INDEX])
                                $ imagefile = get_crop_filename(crop_name)
                                $ is_selected = (selected_crop_index == j)

                                imagebutton:
                                    idle imagefile
                                    hover Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                                    selected_idle Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                                    insensitive Composite((CROP_ICON_SIZE, CROP_ICON_SIZE), (0,0), imagefile, (0,0), Solid(gray_transparent))
                                    xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                                    anchor (0.5, 0.5)
                                    align  (0.5, 0.5)
                                    selected is_selected
                                    sensitive (not max_crops_reached)
                                    if (not renpy.variant("touch")):
                                        hovered SetLocalVariable("selected_crop_index", j)
                                    if renpy.variant("touch"):
                                        action If((selected_crop_index == j), [ SetCrop(crop_index,    crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", zoomout)], SetLocalVariable("selected_crop_index", j))
                                    else:
                                        action [ SetCrop(crop_index,    crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", zoomout)]

screen stat_icons(stat_value, stat_index):
    hbox:
        style "stat_icon_hbox"
        # must be a nitrogen-giving thing
        if (stat_value < 0):
            $ stat_icon_name = "nitrogen-add"
            $ stat_value = -stat_value/2
        else:
            $ stat_icon_name = CROP_INFO_INDEX_NAMES[stat_index].lower()

        for i in range(0, stat_value//2):
            add STAT_ICON_BASE + stat_icon_name + ".png"
        if (stat_value%2 > 0):
            add STAT_ICON_BASE + stat_icon_name + "-half.png"

# TODO: show bee boosting while laying out crops
screen crops_layout:
    frame:
        yfill True
        background "soil"
        #background brown_dark
        vpgrid:
            yalign 0.5
            style_prefix "crop_layout"

            # number of columns is the square root of farm_size
            cols round(farm_size**0.5)
            side_xalign 0.5
            for i in range(0, farm_size):
                vbox:
                    xalign 0.5
                    hbox:
                        $ current_crop_name = farm.crops[i]
                        $ selected_crop_index = get_crop_index(current_crop_name)
                        $ nitrogen_usage = crop_info[get_crop_index(current_crop_name)][NITROGEN_INDEX]
                        $ current_nitrogen_level = farm.health[i][Field.NITROGEN_LEVEL_INDEX]
                        $ new_nitrogen_level = bounded_value(current_nitrogen_level - nitrogen_usage, 0, Field.NITROGEN_FULL)
                        $ tint_factor = 1 - (current_nitrogen_level / float(Field.NITROGEN_FULL))
                        $ tint_factor = tint_factor / 2.0

                        if (USE_PESTS):
                            $ current_pest_level = farm.health[i][Field.PEST_LEVEL_INDEX]
                            $ pest_factor = (current_pest_level / float(Field.PEST_MAX))
                        frame:
                            if (nitrogen_usage > current_nitrogen_level):
                                background red_dark
                            else:
                                #background Frame(im.MatrixColor("gui/crop icons/background.png", im.matrix.tint(tint_factor, tint_factor, tint_factor))) #make poor soils darker
                                # make poor soils lighter and
                                # (optionally) put the pests on top
                                background Frame(Composite(
                                    (CROP_ICON_SIZE, CROP_ICON_SIZE),
                                    (0,0), im.MatrixColor("gui/crop icons/background.png",    im.matrix.brightness(tint_factor))
                                    #(0,0), get_pest_image(pest_factor)
                                    ))

                            if (current_crop_name == "fallow"):
                                $ imagefile = "gui/crop icons/blank.png"
                            else:
                                $ imagefile = get_crop_filename(current_crop_name)
                            imagebutton:
                                idle Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/idle.png")
                                hover Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                                xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                                anchor (0.5, 0.5)
                                align  (0.5, 0.5)
                                action [If(
                                (current_crop_name[-1] == "+"),
                                    Confirm("Are you sure you want to destroy this perennial plant? You can't get it back.", ShowTransient("choose_crop", zoomin, i)),
                                    ShowTransient("choose_crop", zoomin, i))
                                    ]

# Shows past three years of the crop at specified index.
screen history_box(index):
    style_prefix "crop_history"
    hbox:
        $ history_icon_size = CROP_ICON_SIZE // 1.5
        for past_crop in range(0, Field.HISTORY_SIZE):
            $ past_crop_name = farm.history[index][past_crop]
            $ imagefile = get_crop_filename(past_crop_name)
            add imagefile size (history_icon_size, history_icon_size)

style crop_history_hbox is crop_details_hbox:
    xsize LEFT_COLUMN_WIDTH-10
    xalign 0.5

screen crops_totals:
    vbox:
        $ calories_needed = get_calories_required(year)
        $ nutrition_needed = get_nutrition_required(year)
        $ total_max = farm_size * CROP_STATS_MAX
        $ total_calories = 0
        $ total_nutrition = 0
        $ total_value = 0
        $ total_work = 0
        # Totaling crops attributes
        for i in range(0, farm.crops.len()):
            $ crop_names = [row[NAME_INDEX] for row in crop_info]
            $ index = crop_names.index(farm.crops[i]) # find the crop's index in crop_info
            $ total_calories += crop_info[index][CALORIES_INDEX]
            $ total_nutrition += crop_info[index][NUTRITION_INDEX]
            if (year >= MONEY_YEAR):
                $ total_value += get_credits_from_value(crop_info[index][VALUE_INDEX])
                # TODO: Need to take into account pests if using, so the user is not surprised.

            $ total_work += crop_info[index][WORK_INDEX]

        #grid 2 4
        text "Calories:     " + str(total_calories)
        use tricolor_bar(calories_needed, total_calories, total_max, RIGHT_COLUMN_WIDTH, CROP_LAYOUT_BAR_WIDTH*5, False)
        text "Nutrition:    " + str(total_nutrition)
        use tricolor_bar(nutrition_needed, total_nutrition, total_max, RIGHT_COLUMN_WIDTH, CROP_LAYOUT_BAR_WIDTH*5, False)
        text "Work:         " + str(total_work) + " / " + str(get_work_available())
        use tricolor_bar(total_work, get_work_available(), total_max, RIGHT_COLUMN_WIDTH, CROP_LAYOUT_BAR_WIDTH*5, False)

        if (year >= MONEY_YEAR):
            text "Current Balance: [credits] credits"
            $ total_expenses = get_expenses_required(year) - KELLY_SALARY
            if (crop_enabled("wheat")):
                $ total_expenses += WHEAT_COST # TODO: Change depending on how much wheat you plant?
            if (total_expenses > total_value):
                text "Value:    " + str(total_value) + " credits" color red_med
            else:
                text "Value:    " + str(total_value) + " credits"
            text "Expenses: " + str(total_expenses) + " credits"
            text "Expected Balance: " + str(credits + total_value - total_expenses) + " credits"
            # TODO: ability to click on "Expenses" or "Value" and see itemized list.
            # TODO: make this look prettier
            # TOdO: show bee boosting

        text " "
        if (year >= KID_WORK_YEAR):
            label "Kids' Assignment"
            bar value kid_work_slider range 100 style "work_slider" changed set_kid_work
            hbox:
                xfill True
                text "Free Time"
                text "Work" xalign 1.0


# Screen to show a bar with three values. Show the values in a different color
# depending on whether the new value is greater than or less than the current
# value.
# TODO: This gets wonky when the value is close to the max? Or maybe the maximum needs to be adjusted?
screen tricolor_bar(current_value, new_value, max_value, display_max_size, display_min_size=CROP_LAYOUT_BAR_WIDTH, display_vertical=True):
    # we have an increase; show it in a positive color
    if (new_value >= current_value):
        $ display_value = new_value - current_value
        $ display_range = max_value - current_value
        $ display_size = int((display_max_size/float(max_value)) * (max_value - current_value))
        $ display_style = "increased_bar"

    # we have a decrease; show it in a negative color
    else:
        $ display_value = current_value - new_value
        $ display_range = max_value - new_value
        $ display_size = int((display_max_size/float(max_value)) *  (max_value - new_value))
        $ display_style = "decreased_bar"

    if (display_vertical):
        vbox:
            spacing 0
            bar value display_value range display_range style display_style xsize display_min_size ysize display_size
            bar value max_value range max_value style "normal_bar" xsize display_min_size ysize (display_max_size - display_size)
    else:
        hbox:
            spacing 0
            bar value max_value range max_value style "normal_bar_horizontal" xsize (display_max_size - display_size) ysize display_min_size bar_invert True
            $ display_style += "_horizontal"
            bar value display_value range display_range style display_style xsize display_size ysize display_min_size

init python:

    # Set the crop in our farm array and update the total stats for the farm
    def set_crop(index, crop_name):
        global farm
        global selected_crop_index
        farm.crops[index] = crop_name
        max_crops_reached = (farm.crops.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX])
        # if we have put in the max of this crop, select something else.
        if (max_crops_reached):
            selected_crop_index = 0
        return

    SetCrop = renpy.curry(set_crop)

    # Use our default test crops
    def set_default_crops():
        global farm
        farm.crops.setDefault()
        return

    def clear_crops():
        global farm
        farm.reset_crops()
        return

    def set_kid_work(new_value):
        global kid_work_slider
        kid_work_slider = new_value
        renpy.restart_interaction()
        return


# Custom styles for the farm planning screen
style plan_farm_label is label:
    xpadding 5
    ypadding 5
    xfill True

style plan_farm_label_text is label_text:
    color black
    font "fonts/Questrial-Regular.otf"

style plan_farm_button is button

style plan_farm_button_text is button_text:
    font "fonts/Questrial-Regular.otf"
    idle_color green_dark
    hover_color green_med

style round_button is plan_farm_button:
    background "roundrect_medgreen"
    xalign 1.0

style round_button_text is plan_farm_button_text:
    idle_color gray_light
    hover_color white
    insensitive_color gray_dark

style plan_farm_text is text:
    color black

style plan_farm_status_text is plan_farm_text:
    yalign 0.5
    italic True
    xoffset 15
    color red_med

style plan_farm_vbox is vbox:
    spacing 5

style plan_farm_subframe is frame:
    background "roundrect_lightgray"
    xpadding 8
    ypadding 8

# Custom styles for the crop details part of the screen

# STYLE COMPUTER_SUB used for subwindows of the main computer screen
style computer_sub_frame is frame:
    background "roundrect_darkgray"
    xpadding 8
    ypadding 8

style computer_sub_label is plan_farm_label

style computer_sub_label_text is plan_farm_label_text:
    color green_light

style computer_sub_text is plan_farm_text:
    size 16
    color white

style computer_sub_grid is grid

style computer_sub_hbox is hbox:
    xalign 0.0
    xfill True

style computer_sub_vbox is vbox:
    spacing 10

style computer_sub_button is plan_farm_button

style computer_sub_button_text is plan_farm_button_text:
    idle_color black
    hover_color white
    selected_idle_color white

# STYLE CROP_DETAILS_ used for when you click on a space to choose a crop
style crop_details_frame is computer_sub_frame


style crop_details_vpgrid is vpgrid:
    xalign 0.5
    xfill True
    yalign 1.0

style crop_details_label is computer_sub_label

style crop_details_label_text is computer_sub_label_text:
    size 26
    xalign 0.0
    color green_dark

style crop_details_selected_label is crop_details_label:
    background tan_dark

style crop_details_selected_label_text is crop_details_label_text:
    color white

style crop_details_button_text is computer_sub_button_text

style crop_details_text is computer_sub_text:
    yalign 0.5
    xalign 1.0
    font "DejaVuSans.ttf"

style crop_details_bar is bar:
    left_bar Frame(Solid(red_dark))
    right_bar Frame(Solid(tan_light))
    xsize 50
    ysize 5
    yalign 0.5

style crop_details_positive_bar is bar:
    left_bar Frame(Solid(green_dark))
    right_bar Frame(Solid(tan_light))
    xsize 50
    ysize 5
    yalign 0.5

style crop_details_vbox is computer_sub_vbox:
    xsize MIDDLE_COLUMN_WIDTH+LEFT_COLUMN_WIDTH

style crop_details_hbox is computer_sub_hbox:
    xsize MIDDLE_COLUMN_WIDTH-10
    spacing 10
    xalign 0.5

style crop_details_grid is computer_sub_grid:
    xsize MIDDLE_COLUMN_WIDTH
    spacing 0

# STYLE FIELD_INFO_ used for displaying the details of a field when you click on one
style field_info_hbox is computer_sub_hbox
style field_info_label is computer_sub_label
style field_info_label_text is computer_sub_label_text
style field_info_text is computer_sub_text:
    xoffset 20
    color black


# STYLE CROP_LAYOUT_ used for displaying the field of crops
style crop_layout_vpgrid is vpgrid:
    spacing 16
    xalign 0.5
    xsize MIDDLE_COLUMN_WIDTH
    xfill True

style crop_layout_hbox is hbox:
    spacing 5

style crop_layout_bar is bar:
    bar_vertical True
    xsize CROP_LAYOUT_BAR_WIDTH
    ysize CROP_LAYOUT_BAR_SIZE
    yalign 1.0
    spacing 1

style increased_bar is crop_layout_bar:
    top_bar Frame(Solid(gray_light))
    bottom_bar Frame(Solid(green_dark))

style decreased_bar is crop_layout_bar:
    top_bar Frame(Solid(gray_light))
    bottom_bar Frame(Solid(red_dark))

style increased_bar_horizontal is crop_layout_bar:
    right_bar Frame(Solid(gray_light))
    left_bar Frame(Solid(green_dark))
    bar_vertical False

style decreased_bar_horizontal is crop_layout_bar:
    left_bar Frame(Solid(red_dark))
    right_bar Frame(Solid(gray_light))
    bar_vertical False

style normal_bar is crop_layout_bar

style normal_bar_horizontal is crop_layout_bar:
    bar_vertical False

style crop_totals_bar is crop_layout_bar

style work_slider is slider

style crop_status_vpgrid:
    xsize CROP_STATUS_ICON_SIZE*5*2
    xspacing 5
    yspacing 10

style crop_status_frame is frame:
    background None

style crop_status_hbox is hbox:
    xsize CROP_STATUS_ICON_SIZE*5*2*2
    xalign 0.5

style crop_status_text is text:
    xfill True
    xalign 1.0
