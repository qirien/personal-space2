# Using this screen, the user can select which crops to plant where and see the projected results.  When they are done, they can hit "Accept Plan".
# Farm Planning Screen
#

screen plan_farm():
    tag plan_farm
    style_prefix "plan_farm"
    $ valid_layout = farm.is_valid_layout()
    if (not valid_layout):
        if (farm.crops.count("goats") != crop_info[get_crop_index("goats")][MAXIMUM_INDEX]):
            $ info_msg = "Need to allocate all goats!"
        elif (crop_enabled("honey") and (farm.crops.count("honey") != crop_info[get_crop_index("honey")][MAXIMUM_INDEX])):
            $ info_msg = "Need to allocate all bees!"
        else:
            $ info_msg = "Need to fix crops needing more nitrogen!"
    else:
        $ info_msg = "OK!"
    frame:
        background  "computer_pad_with_screen"
        text "User {color=#888}[his_name]{/color} has logged on." size 12 xalign 0.1 ypos 30 color "#fff" alt "Farm status: " + info_msg # read the info_msg first if in self-voicing mode
        imagebutton auto "gui/computerpadbutton_%s.png" action ShowMenu("save") alt "Game Menu" xpos 1233 yalign 0.5 focus_mask None
        vbox:
            area (60, 50, 1150, 620)
            yfill True
            hbox:
                xfill True
                yfill True
                # crop details here
                frame:
                    yfill True
                    #background None
                    background "roundrect_darkgray"

                    vbox:
                        use farm_details_screen

                        hbox:
                            spacing 10
                            frame:
                                xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH + 20
                                style "plan_farm_subframe"
                                hbox:
                                    label "Status" xsize 100
                                    if (not valid_layout):
                                        # if (farm.get_total_calories() < get_calories_required(year)):
                                        #     text "Need more energy!" style "alert_text"
                                        text info_msg style "alert_text"
                                    else:
                                        text info_msg style "plan_farm_status_text" color green_dark
                            hbox:
                                xsize RIGHT_COLUMN_WIDTH
                                textbutton "Clear":
                                    action [
                                            clear_crops,
                                            renpy.restart_interaction
                                            ]
                                showif persistent.times_beaten:
                                    textbutton "Auto":
                                        action[ auto_place_crops, renpy.restart_interaction]
                                textbutton "Done":
                                    sensitive valid_layout
                                    action If((farm.get_total_calories() < get_calories_required(year)), Confirm("Do you really want to continue without enough energy?", Jump("yearly_events")), Jump("yearly_events"))


# To change appearance, see screens.rpy, screen nvl
label yearly_messages:
    $ year_string = repr(year)
    $ message = "message" + year_string
    $ read_messages = True
    nvl clear
    call expression message from _call_expression_4
    #computer "\n(End of messages)"
    nvl clear
    call screen plan_farm
    "You should never see this."
##
# Subscreen letting the user see information on crops and choose which to plant this year
##
screen farm_details_screen():
    key 'p' action [auto_place_crops, renpy.restart_interaction]
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
                        $ kid_months = roundint(earth_year * 12)
                        $ kid_age = str(kid_months) + " Earth mos"
                    else:
                        $ kid_age = str(roundint(earth_year)) + " Earth years"
                    text "[kid_name], [kid_age]" xoffset 20
                    if (bro_birth_year != 0):
                        if (bro_years < 2):
                            $ bro_months = roundint(get_earth_years(bro_years) * 12)
                            $ bro_age_str = str(bro_months) + " Earth mos"
                        else:
                            $ bro_age_str = str(roundint(get_earth_years(bro_years))) + " Earth years"
                        text "[bro_name], [bro_age_str]" xoffset 20
                    else:
                        text " "
                    text " "

            # Community info
            frame:
                ysize 305
                style "plan_farm_subframe"
                #background None
                xfill True
                vbox: 
                    label " "
                    grid 2 2:
                        xspacing 30
                        xalign 0.5
                        vbox:
                            imagebutton auto "gui/messages_%s.png" action Jump("yearly_messages") alt "Messages"
                            text "Messages" style "tiny_text"

                            if (not read_messages):
                                text " {b}!{/b} " ypos -40 style "alert_text" alt "New" at tiny_bounce
                            else:
                                text " " ypos -40 style "alert_text" xalign 0.0 # We have to have this here or it messes up all the positions
                        vbox:
                            imagebutton auto "gui/parenting_%s.png" action Show("parenting_handbook", transition=irisout) alt "Parenting"
                            text "Parenting" style "tiny_text"
                            if ((year in TRANSITION_YEARS) and (not read_handbook)):
                                text " {b}!{/b} " ypos -40 style "alert_text" alt "New" at tiny_bounce
                            else:
                                text " " ypos -40 alt "" style "alert_text" # We have to have this here or it messes up all the positions

                        vbox:
                            imagebutton auto "gui/bios_%s.png" action Show("biographies", irisout, bios.getFirstUnreadPersonName()) alt "Bios"
                            text "Bios" style "tiny_text"
                            if (bios.hasUnread()):
                                text " {b}!{/b} " ypos -40 style "alert_text" alt "New" at tiny_bounce
                            else:
                                text " " ypos -40 style "alert_text"
                        vbox:
                            if(len(word_board.poems) > 0):
                                imagebutton auto "gui/poetry_%s.png" action Show("poetry_display", irisout, word_board) alt "Poetry"
                                text "Poetry" style "tiny_text"
                            else:
                                text "" xalign 0.0

        # Crop layout area
        frame:
            style "plan_farm_subframe"
            vbox:
                xsize MIDDLE_COLUMN_WIDTH
                ysize TOP_SECTION_HEIGHT
                hbox:
                    label "Year " + str(year) + " of " + str(MAX_YEARS) text_xalign 0.5
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

screen choose_crop(crop_index=0):
    on "show" action SetVariable("selected_crop_index", get_crop_index(farm.crops[crop_index]))
    modal True
    default show_sort = False
    add "gui/overlay/confirm.png"
    key "x" action Hide("choose_crop")
    frame:
        style_prefix "crop_details"
        yalign 0.5
        xalign 0.5
        hbox:
            xsize MIDDLE_COLUMN_WIDTH + LEFT_COLUMN_WIDTH + 20
            spacing 10

            frame:
                style "plan_farm_subframe"
                vbox:
                    xfill True
                    hbox:
                        $ crop_name = crop_info[selected_crop_index][NAME_INDEX]
                        label crop_name.capitalize() 

                        textbutton "X":                         
                            xpos 105
                            ypos -2
                            text_size 40
                            text_font "fonts/Questrial-Regular.otf"
                            text_bold True
                            focus_mask None
                            if not renpy.variant("touch"):
                                action Hide("choose_crop", irisin)
                            if renpy.variant("touch"):
                                action [ SetCrop(crop_index, crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", irisin) ]

                    # Display info about the selected crop
                    hbox:
                        style_prefix "crop_status"
                        vpgrid:
                            cols 2
                            text "    Energy: " #extra spaces are needed because vpgrid takes size for ALL children from size of first child
                            frame:
                                use stat_icons(crop_info[selected_crop_index][CALORIES_INDEX], CALORIES_INDEX)
                            if ((year > NUTRITION_YEAR) and (bad_nutrition_count > 0)):
                                text "Nutrition: "
                                frame:
                                    use nutrition_icons(selected_crop_index)
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
                        vbox:
                            text crop_descriptions[crop_name.rstrip("+")]

                            $ num_avail = crop_info[selected_crop_index][MAXIMUM_INDEX]
                            if (num_avail != 100):
                                text "x[num_avail]" italic True 
                            else:
                                text "unlimited" italic True

                    # Buttons to sort by different stats
                    hbox:
                        spacing 10
                        textbutton "Sort By" xalign 0.0 style "plan_farm_button" action ToggleScreenVariable("show_sort")

                        showif show_sort:
                            hbox:
                                at popside
                                use sort_buttons

                    $ crop_columns = count_enabled_crops()//4 + 2   #more columns with more enabled crops
                    # Available crops to choose from
                    vpgrid:
                        cols crop_columns
                        spacing 10
                        side_xalign 0.5

                        # Sort by proper key 
                        if (sortby == "name"):
                            $ crops_to_show = sorted(crop_info)
                        else:
                            $ crops_to_show = sorted(crop_info,key= lambda x: x[eval(sortby.upper() + "_INDEX")], reverse=True)
                        for j in range(0, len(crop_info)):
                            # only show currently enabled crops where we haven't planted the maximum yet
                            if (crops_to_show[j][ENABLED_INDEX] and (crops_to_show[j][MAXIMUM_INDEX] > 0) and
                            (crop_temporarily_disabled != crops_to_show[j][NAME_INDEX])):
                                $ crop_name = crops_to_show[j][NAME_INDEX]
                                $ crop_info_index = get_crop_index(crop_name)
                                $ imagefile = get_crop_filename(crop_name)
                                $ is_selected = (selected_crop_index == crop_info_index)                            
                                imagebutton:
                                    idle Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (CROP_ICON_SIZE//2,0), get_boosted_image(crop_name, crop_index))
                                    hover Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (CROP_ICON_SIZE//2,0), get_boosted_image(crop_name, crop_index), (0,0), "gui/crop icons/selected.png")
                                    selected_idle Composite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (CROP_ICON_SIZE//2,0), get_boosted_image(crop_name, crop_index), (0,0), "gui/crop icons/selected.png")
                                    insensitive Composite((CROP_ICON_SIZE, CROP_ICON_SIZE), (0,0), imagefile, (CROP_ICON_SIZE//2,0), get_boosted_image(crop_name, crop_index), (0,0), Solid(gray_transparent))
                                    xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                                    focus_mask None
                                    anchor (0.5, 0.5)
                                    alt crop_name
                                    align  (0.5, 0.5)
                                    selected is_selected
                                    sensitive (crop_info[crop_info_index][NITROGEN_INDEX] < farm.health[crop_index][Field.NITROGEN_LEVEL_INDEX])
                                    if (not renpy.variant("touch")):
                                        hovered SetLocalVariable("selected_crop_index", crop_info_index)
                                    if renpy.variant("touch"):
                                        action If((selected_crop_index == crop_info_index), [ SetCrop(crop_index,    crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", irisin)], SetLocalVariable("selected_crop_index", crop_info_index))
                                    else:
                                        action [ SetCrop(crop_index,    crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", irisin)]

                    if renpy.variant("touch"):
                        textbutton "Done":
                            style "plan_farm_button"
                            xalign 1.0
                            action [ SetCrop(crop_index, crop_info[selected_crop_index][NAME_INDEX]), Hide("choose_crop", irisin) ]
                                

screen sort_buttons():
    $ show_buttons = ["calories"]
    if ((year > NUTRITION_YEAR) and (bad_nutrition_count > 0)):
        $ show_buttons.append("vita")
        $ show_buttons.append("vitc")
        $ show_buttons.append("vitm")
    $ show_buttons.append("work")
    $ show_buttons.append("nitrogen")
    if (year >= MONEY_YEAR):
        $ show_buttons.append("value")

    for this_button in show_buttons:
        $ imagefile =  STAT_ICON_BASE + this_button + ".png"
        imagebutton:
            idle imagefile
            alt this_button
            hover Composite((CROP_STATUS_ICON_SIZE,CROP_STATUS_ICON_SIZE), (0,0), imagefile,
            (0,0), im.FactorScale("gui/crop icons/selected.png", 0.5))
            selected_idle Composite((CROP_STATUS_ICON_SIZE,CROP_STATUS_ICON_SIZE), (0,0), imagefile,
            (0,0), im.FactorScale("gui/crop icons/selected.png", 0.5))
            at highlight_imagebutton
            xysize (CROP_STATUS_ICON_SIZE,CROP_STATUS_ICON_SIZE)
            focus_mask None
            anchor (0.5, 0.5)
            align  (0.5, 0.5)
            action SetVariable("sortby", this_button)

screen stat_icons(stat_value, stat_index):
    hbox:
        style "stat_icon_hbox"
        # must be a nitrogen-giving thing
        if (stat_value < 0):
            $ stat_icon_name = "nitrogen-add"
            $ stat_value = -stat_value//2
        else:
            $ stat_icon_name = CROP_INFO_INDEX_NAMES[stat_index].lower()

        for i in range(0, int(stat_value//2)):
            add STAT_ICON_BASE + stat_icon_name + ".png"
        if (stat_value%2 > 0):
            add STAT_ICON_BASE + stat_icon_name + "-half.png"

screen nutrition_icons(crop_index):
    hbox:
        style "stat_icon_hbox"
        $ heart_count = 0
        $ crop_name = crop_info[crop_index][NAME_INDEX]
        for i in range(0, crop_info[crop_index][VITA_INDEX]//2):
            add STAT_ICON_BASE + "vitA.png"
            $ heart_count += 1
        for i in range(0, crop_info[crop_index][VITC_INDEX]//2):
            add STAT_ICON_BASE + "vitC.png"
            $ heart_count += 1
        for i in range(0, crop_info[crop_index][VITM_INDEX]//2):
            add STAT_ICON_BASE + "vitM.png"
            $ heart_count += 1
        if (crop_name != "fallow"):
            for i in range(heart_count, 6):
                add STAT_ICON_BASE + "nutrition.png"

screen crops_layout():
    frame:
        yfill True
        background "soil"
        #background brown_dark
        vpgrid:
            yalign 0.05
            style_prefix "crop_layout"

            # number of columns is the square root of farm_size
            cols 5#round(farm_size**0.5)
            side_xalign 0.5
            for i in range(0, farm_size):
                $ alt_add = ""
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
                                $ alt_add = " low nitrogen"
                            else:
                                # make poor soils lighter,
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
                                # image file, then boosting, then any selection box
                                alt current_crop_name + alt_add
                                idle Composite((CROP_ICON_SIZE,CROP_ICON_SIZE),
                                (0,0), imagefile,
                                (CROP_ICON_SIZE//2,0), get_boost_image(i),
                                (0,0), "gui/crop icons/idle.png")
                                hover Composite((CROP_ICON_SIZE,CROP_ICON_SIZE),
                                (0,0), imagefile,
                                (CROP_ICON_SIZE//2,0), get_boost_image(i),
                                (0,0), "gui/crop icons/selected.png")
                                xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                                anchor (0.5, 0.5)
                                align  (0.5, 0.5)
                                focus_mask None
                                action [If(
                                (current_crop_name[-1] == "+"),
                                    Confirm("Are you sure you want to destroy this perennial plant? You can't get it back.", ShowTransient("choose_crop", irisout, i)),
                                    ShowTransient("choose_crop", irisout, i))
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

screen crops_totals():
    vbox:
        yalign 0.0
        $ calories_needed = get_calories_required(year)
        $ vitamins_needed = get_vitamins_required(year)
        $ total_max = calories_needed * 2# absolute maximum: farm_size * CROP_STATS_MAX
        $ vitMax = vitamins_needed * 2
        $ total_calories = 0
        $ vitA = 0
        $ vitC = 0
        $ vitM = 0
        $ total_value = 0
        $ total_work = 0
        $ boosted_squares = farm.get_boosted_squares()
        # Totaling crops attributes
        for i in range(0, farm.crops.len()):
            $ multiplier = 1.0
            if (i in boosted_squares):
                $ multiplier += (farm.BEE_BOOST/100.0)
            $ crop_names = [row[NAME_INDEX] for row in crop_info]
            $ index = crop_names.index(farm.crops[i]) # find the crop's index in crop_info
            $ crop_name = farm.crops[i].rstrip("+")
            $ total_calories += roundint(crop_info[index][CALORIES_INDEX] * multiplier)
            $ vitA += crop_info[index][VITA_INDEX] * multiplier
            $ vitC += crop_info[index][VITC_INDEX] * multiplier
            $ vitM += crop_info[index][VITM_INDEX] * multiplier
            if (year >= MONEY_YEAR):
                $ total_value += multiplier * get_credits_from_value(crop_info[index][VALUE_INDEX])

            $ total_work += crop_info[index][WORK_INDEX]
        # Round after totalling, otherwise multiplier doesn't doo much.
        $ vitA = roundint(vitA)
        $ vitC = roundint(vitC)
        $ vitM = roundint(vitM)
        $ total_value = roundint(total_value)

        #grid 2 4
        hbox:
            text "Energy     "# + str(total_calories) + " / " + str(calories_needed)
            if (total_calories < calories_needed):
                text "{b}!{/b}" style "alert_text" alt "low" at tiny_bounce
        hbox:
            use stat_icons(2, CALORIES_INDEX)
            text " "
            use tricolor_bar(calories_needed, total_calories, total_max, RIGHT_COLUMN_WIDTH-CROP_STATUS_ICON_SIZE, CROP_LAYOUT_BAR_WIDTH*5, False)
        if ((year > NUTRITION_YEAR) and (bad_nutrition_count > 0)):
            hbox:
                text "Nutrition  "# + str(vitA) + " | " + str(vitC) + " | " + str(vitM) + "/" + str(vitamins_needed)
                if ((vitA < vitamins_needed) or (vitC < vitamins_needed) or (vitM < vitamins_needed)):
                    text "{b}!{/b}" style "alert_text" alt "low" at tiny_bounce
            hbox:
                yalign 0.5
                add "gui/emoji/vitA.png"
                use tricolor_bar(vitamins_needed+1, vitA, vitMax, (RIGHT_COLUMN_WIDTH-CROP_STATUS_ICON_SIZE*3)//3, CROP_STATUS_ICON_SIZE, False)
                add "gui/emoji/vitC.png"
                use tricolor_bar(vitamins_needed+1, vitC, vitMax, (RIGHT_COLUMN_WIDTH-CROP_STATUS_ICON_SIZE*3)//3, CROP_STATUS_ICON_SIZE, False)
                add "gui/emoji/vitM.png"
                use tricolor_bar(vitamins_needed+1, vitM, vitMax, (RIGHT_COLUMN_WIDTH-CROP_STATUS_ICON_SIZE*3)//3, CROP_STATUS_ICON_SIZE, False)

        hbox:
            text "Work          "# + str(total_work) + " / " + str(get_work_available())
            showif (total_work > get_work_available()):
                text "{b}!{/b}" style "alert_text" alt "high" at tiny_bounce
        hbox:
            use stat_icons(2, WORK_INDEX)
            text " "
            use tricolor_bar(total_work, get_work_available(), total_max, RIGHT_COLUMN_WIDTH-CROP_STATUS_ICON_SIZE, CROP_LAYOUT_BAR_WIDTH*5, False)
        if (year >= KID_WORK_YEAR):
            hbox:
                null width 50
                vbox:
                    text "Kids' Assignment"
                    bar value kid_work_slider range 100 style "work_slider" changed set_kid_work alt "Kids' Work" + str(kid_work_slider) + "percent"
                    hbox:
                        xfill True
                        text "Free Time" italic True
                        text "Work" italic True xalign 1.0

        if (year >= MONEY_YEAR):
            $ total_expenses = get_expenses_required(year) - KELLY_SALARY
            if (crop_enabled("wheat")):
                $ total_expenses += WHEAT_COST
            hbox:
                text "Finances  "
                use stat_icons(2, VALUE_INDEX)
            hbox:
                style_prefix "plan_farm_total"
                xfill True
                vbox:
                    text "Current Balance"
                    text "Projected Change"
                    #text "Value"
                    #text "Expenses"
                    text "{font=fonts/OpenSansEmoji.otf}_____________________{/font}"
                    text "Expected Balance"
                vbox:
                    xalign 1.0
                    text str(credits) xalign 1.0
                    $ year_net = total_value - total_expenses
                    if (year_net < 0):
                        text str(year_net) color red_med xalign 1.0
                    else:
                        text "+" + str(year_net) xalign 1.0    
                    #if (total_expenses > total_value):
                    #    text "+" + str(total_value) color red_med xalign 1.0
                    #else:
                    #    text "+" + str(total_value) xalign 1.0
                    #text "-" + str(total_expenses) xalign 1.0
                    text "{font=fonts/OpenSansEmoji.otf}_____{/font}" xalign 1.0
                    text str(credits + total_value - total_expenses) xalign 1.0

# Screen to show a bar with three values. Show the values in a different color
# depending on whether the new value is greater than or less than the current
# value.
screen tricolor_bar(current_value, new_value, max_value, display_max_size, display_min_size=CROP_LAYOUT_BAR_WIDTH, display_vertical=True):
    # we have an increase; show it in a positive color
    if (new_value > current_value):
        $ display_value = new_value - current_value
        $ display_range = max_value - current_value
        $ display_size = roundint((display_max_size/float(max_value)) * (max_value - current_value))
        $ display_style = "increased_bar"

    # we have a decrease; show it in a negative color
    else:
        $ display_value = current_value - new_value
        $ display_range = max_value - new_value
        $ display_size = roundint((display_max_size/float(max_value)) *  (max_value - new_value))
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
        # If we would go over the maximum, remove old one(s) instead until we have room for the selected crop
        while (farm.crops.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX]):
            farm.delete_one_crop(crop_name)

        farm.crops[index] = crop_name
        max_crops_reached = (farm.crops.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX])
        # if we have put in the max of this crop, select something else.
        if (max_crops_reached):
            selected_crop_index = 0
        renpy.retain_after_load()
        return

    SetCrop = renpy.curry(set_crop)

    # Use our default test crops
    def set_default_crops():
        global farm
        farm.crops.setDefault()
        return

    def clear_crops():
        global farm

        farm.clear_crops()
        return

    def set_kid_work(new_value):
        global kid_work_slider
        kid_work_slider = new_value
        renpy.restart_interaction()
        return

    def auto_place_crops():
        global farm
        farm.autoPlace()

#############################################################################
#
# STYLES
# Custom styles for the farm planning screen
# 
#############################################################################

style plan_farm_label is label:
    xpadding 5
    ypadding 5
    xfill True

style plan_farm_label_text is label_text:
    color black
    font "fonts/Questrial-Regular.otf"

style plan_farm_button_text is button_text:
    font "fonts/Questrial-Regular.otf"
    idle_color green_dark
    hover_color green_med
    size 36

style plan_farm_total_text is text:
    font "fonts/FreeMono.ttf"
    color black

style plan_farm_button is button:
    background "roundrect_medgreen"
    xpadding 10
    ypadding 10

style plan_farm_button_text is button_text:
    idle_color gray_light
    hover_color white
    insensitive_color gray_dark

style plan_farm_text is text:
    yalign 0.5
    color black
    font "fonts/RobotoSlab-Regular.ttf"

style alert_text is plan_farm_text:
    outlines [(1, "#000", 1, 1)]
    color yellow
    yalign 0.5

style plan_farm_status_text is plan_farm_text:
    yalign 0.5
    italic True
    xoffset 15
    color red_med

style plan_farm_vbox is vbox:
    spacing 5

style plan_farm_subframe is frame:
    background "roundrect_lightgray"
    xpadding 10
    ypadding 10

# Custom styles for the crop details part of the screen

style computer_button is button

style computer_button_text is plan_farm_text:
    idle_color white
    hover_color gray_light
    selected_idle_color gray_light

# STYLE COMPUTER_SUB used for subwindows of the main computer screen
style computer_sub_frame is frame:
    background "roundrect_darkgray"
    xpadding 8
    ypadding 8

style computer_sub_label is plan_farm_label

style computer_sub_label_text is plan_farm_label_text:
    color green_light

style computer_sub_text is plan_farm_text:
    size 18
    color white

style computer_sub_grid is grid

style computer_sub_hbox is hbox:
    xalign 0.0
    xfill True

style computer_sub_vbox is vbox:
    spacing 10

style computer_sub_button is computer_button

style computer_sub_button_text is computer_button_text:
    size 20
    idle_color black
    hover_color gray_light
    selected_idle_color white

# STYLE CROP_DETAILS_ used for when you click on a space to choose a crop
style crop_details_frame is computer_sub_frame


style crop_details_vpgrid is vpgrid:
    xalign 0.5
    xfill True
    yalign 1.0

style crop_details_label is computer_sub_label

style crop_details_label_text is computer_sub_label_text:
    size 30
    xalign 0.0
    color black

style crop_details_selected_label is crop_details_label:
    background tan_dark

style crop_details_selected_label_text is crop_details_label_text:
    color white

style crop_details_button is computer_sub_button
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

style crop_details_window is window

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
    bottom_bar Frame(Solid(red_med))

style increased_bar_horizontal is crop_layout_bar:
    right_bar Frame(Solid(gray_light))
    left_bar Frame(Solid(green_dark))
    bar_vertical False

style decreased_bar_horizontal is crop_layout_bar:
    left_bar Frame(Solid(red_med))
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

style tiny_text is plan_farm_label_text:
    size 16
    xalign 0.5