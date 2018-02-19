# Farm Planning Screen
# Using this screen, the user can select which crops to plant where and see the projected results.  When they are done, they can hit "Accept Plan".
#
# TODO: Support permanent plants, such as plums, goats?
# TODO: Use bars for displaying crop stats?
# TODO: Get some graphics and pretty this up
# TODO: show kids' ages and farm/community info

screen plan_farm:
    tag plan_farm
    style_prefix "plan_farm"
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User [his_name] has logged on." size 12 xalign 0.1 ypos 22 color "#fff"
        textbutton "Family" xpos 800 ypos 22 action Show("monthly_screen")
        textbutton "?" xpos 1077 ypos 22 action Jump("tutorial_ask")        
        textbutton "             " xpos 1085 ypos 22 action ShowMenu("preferences")
        vbox:            
            area (60, 50, 1150, 620)           
            yfill True
            hbox:                
                xfill True
                yfill True                                
                # crop details here          
                frame:
                    yfill True
                    background gray_dark                    
                    vbox:                    
                        label "Farm Plan for Year " + str(year):
                            xalign 0.5
                        
                        use crop_details_screen                         
                        
                        hbox:
                            xfill True
                            null width LEFT_COLUMN_WIDTH
                            textbutton "Auto":
                                xalign 0.5
                                action [
                                            set_default_crops,
                                            renpy.restart_interaction
                                        ]
                            textbutton "Accept Plan":
                                xalign 1.0
                                action Return()

label monthly_computer:
    call screen monthly_screen    
                                
screen monthly_screen:
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User {a=call:monthly_computer}[his_name]{/a} has logged on." size 12 xalign 0.1 ypos 15 color "#fff"
        textbutton "?" xpos 1077 ypos 15 action Jump("tutorial_ask")
        textbutton "             " xpos 1085 ypos 15 action ShowMenu("preferences")
        vbox:            
            area (60, 50, 1150, 620)           
            yfill True
            hbox:                
                xfill True
                yfill True
                vbox:                    
                    # family details here
                    frame:
                        yfill True                        
                        background gray_light
                        has vbox
                        vbox:
                            xsize LEFT_COLUMN_WIDTH
                            # TODO: Add a small family photo
                            label "Family"
                            text "[his_name]"
                            text "[her_name]"                    
                            text "[kid_name], [earth_year] earth years"
                            if (bro_birth_year != 0):
                                text "[bro_name], [bro_age] earth years"
                            # Community info
                
                        # community/reference details
                        vbox: 
                            xsize LEFT_COLUMN_WIDTH
                            label "Community" # TODO: have cute icons for these, like on a phone?
                            textbutton "Message Board" action Show("messages")
                            textbutton "Parenting Handbook" action Show("parenting_handbook")
                            
                        vbox:
                            textbutton "Return to Farm" action Hide("monthly_screen")
                    
                                
##
# Subscreen letting the user see information on crops and choose which to plant this year
##
screen crop_details_screen:
    hbox:
        xalign 0.5
        xfill True
        # Show crops that we can choose from
        vbox:
            xalign 0.0
            xsize LEFT_COLUMN_WIDTH
            label "Crops"
            use crops_available
          
        # Crop layout area
        vbox:
            xsize MIDDLE_COLUMN_WIDTH
            label "Layout"
            use crops_layout
                
        # Totals so far                                                    
        vbox:            
            xalign 0.5
            xsize RIGHT_COLUMN_WIDTH
            label "Total"
            use crops_totals
                
screen crops_available:
    vbox:
        style_prefix "crop_details"
        $ crop_name = crop_info[selected_crop_index][NAME_INDEX] 
        label crop_name.capitalize()                
        # TODO: Take out style tag and see if autodetecting of this has been fixed later.
        hbox:        
            grid 2 5:
                # TODO: Make each of these a different color and have a key so they take up less room.
                # TODO: Add Nitrogen usage (pest effect?)
                text "Calories: "
                bar value crop_info[selected_crop_index][CALORIES_INDEX] range CROP_STATS_MAX style "crop_details_bar"
                text "Nutrition: "
                bar value crop_info[selected_crop_index][NUTRITION_INDEX] range CROP_STATS_MAX style "crop_details_bar"
                if (year >= 5):
                    text "Value: "
                    bar value crop_info[selected_crop_index][VALUE_INDEX] range CROP_STATS_MAX style "crop_details_bar"
                else:
                    null
                    null
                text "Work: "
                bar value crop_info[selected_crop_index][WORK_INDEX] range CROP_STATS_MAX style "crop_details_bar"
                text "Nitrogen: "
                $ crop_nitrogen = crop_info[selected_crop_index][NITROGEN_INDEX]
                if (crop_nitrogen <= 0):
                    bar value (-crop_nitrogen) range Field.NITROGEN_FULL style "crop_details_positive_bar" 
                else:
                    bar value crop_nitrogen range Field.NITROGEN_FULL style "crop_details_bar"
                #text "Income: " + str(crop_info[crop_info_index][5]) # TODO: based on value, calories, and nutrition?
            text crop_descriptions[crop_name]
        null height 30
        vpgrid:                
            # TODO: change this based on number of enabled crops?
            cols 4
            spacing 10
            draggable True
            mousewheel True        
            #scrollbars "vertical"
            side_xalign 0.5
                    
            for j in range(0, len(crop_info)):
                # only show currently enabled crops
                if (crop_info[j][ENABLED_INDEX]):
                    $ crop_name = crop_info[j][NAME_INDEX]                            
                    $ max_crops_reached = (farm.crops.count(crop_info[j][NAME_INDEX]) >= crop_info[j][MAXIMUM_INDEX])                        
                    $ imagefile = "gui/crop icons/" + crop_name + ".png"
                    $ is_selected = (selected_crop_index == j)                    
    
                    imagebutton:
                        idle imagefile 
                        hover LiveComposite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                        selected_idle LiveComposite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                        insensitive LiveComposite((CROP_ICON_SIZE, CROP_ICON_SIZE), (0,0), imagefile, (0,0), Solid(gray_transparent))
                        xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                        anchor (0.5, 0.5)
                        align  (0.5, 0.5)
                        selected is_selected
                        sensitive (not max_crops_reached)
                        action [ SetVariable("selected_crop_index", j), renpy.restart_interaction ]
        
screen crops_layout:
    vpgrid:
        style_prefix "crop_layout"
        
        # number of columns is the square root of farm_size
        cols int(farm_size**0.5)                
        side_xalign 0.5
        for i in range(0, farm_size):
            vbox:
                hbox:
                    $ current_crop_name = farm.crops[i]
                    frame:
                        if (crop_info[get_crop_index(current_crop_name)][NITROGEN_INDEX] > farm.health[i][Field.NITROGEN_LEVEL_INDEX]):
                            background red_dark
                        else:
                            background tan_dark                                 
                        $ imagefile = "gui/crop icons/" + current_crop_name + ".png"
                        imagebutton:
                            idle imagefile 
                            hover LiveComposite((CROP_ICON_SIZE,CROP_ICON_SIZE), (0,0), imagefile, (0,0), "gui/crop icons/selected.png")
                            xysize (CROP_ICON_SIZE,CROP_ICON_SIZE)
                            anchor (0.5, 0.5)
                            align  (0.5, 0.5)
                            action [ SetCrop(i, crop_info[selected_crop_index][NAME_INDEX]), renpy.restart_interaction ]
                            
                    $ nitrogen_usage = crop_info[get_crop_index(current_crop_name)][NITROGEN_INDEX]
                    $ current_nitrogen_level = farm.health[i][Field.NITROGEN_LEVEL_INDEX] 
                    $ new_nitrogen_level = bounded_value(current_nitrogen_level - nitrogen_usage, 0, Field.NITROGEN_FULL)
                    
                    # This crop adds nitrogen; show it in a positive color
                    if (new_nitrogen_level >= current_nitrogen_level):                                    
                        $ display_value = new_nitrogen_level - current_nitrogen_level
                        $ display_range = Field.NITROGEN_FULL - current_nitrogen_level                                     
                        $ display_size = int((CROP_LAYOUT_BAR_SIZE/100.0) * (Field.NITROGEN_FULL - current_nitrogen_level))
                        $ display_style = "crop_layout_nitrogen_increased_bar"
                                                            
                    # This crop subtracts nitrogen; show it in a negative color
                    else:
                        $ display_value = current_nitrogen_level - new_nitrogen_level
                        $ display_range = Field.NITROGEN_FULL - new_nitrogen_level 
                        $ display_size = int((CROP_LAYOUT_BAR_SIZE/100.0) *  (Field.NITROGEN_FULL - new_nitrogen_level))
                        $ display_style = "crop_layout_nitrogen_decreased_bar"
                            
                    vbox:
                        bar value display_value range display_range style display_style ysize display_size 
                        bar value Field.NITROGEN_FULL range Field.NITROGEN_FULL style "crop_layout_bar" ysize (CROP_LAYOUT_BAR_SIZE - display_size)                                

                    #bar value farm.health[i][Field.NITROGEN_LEVEL_INDEX] range Field.NITROGEN_FULL style "crop_layout_bar"
                    bar value farm.health[i][Field.PEST_LEVEL_INDEX] range Field.PEST_MAX style "crop_layout_bar"
                    
                # history
                hbox:
                    $ history_icon_size = CROP_ICON_SIZE // 2
                    for past_crop in range(0, Field.HISTORY_SIZE):
                        $ past_crop_name = farm.history[i][past_crop]
                        $ imagefile = "gui/crop icons/" + past_crop_name + ".png"
                        add imagefile size (history_icon_size, history_icon_size)
    
screen crops_totals:
    vbox:
        $ calories_max = get_calories_required()
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
            if (year >= 5):
                $ total_value += crop_info[index][VALUE_INDEX]
            $ total_work += crop_info[index][WORK_INDEX]
                
        #grid 2 4
        text "Calories:     " + str(total_calories)
        bar value total_calories range calories_max style "crop_totals_bar"
        text "Nutrition:    " + str(total_nutrition)
        bar value total_nutrition range calories_max style "crop_totals_bar"
        if (year >= 5):
            text "Value:          ¤" + str(total_value)
        text "Work:         " + str(total_work)                 
        bar value total_work range get_work_available() style "crop_totals_bar"

    # TODO: add projected yield
                        
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
        
    SetCrop = renpy.curry(set_crop)
    
    # Use our default test crops
    def set_default_crops():
        global farm
        farm.crops.setDefault()
        
# Custom styles for the farm planning screen
style plan_farm_label is label:
    background tan_dark
    xfill True

style plan_farm_label_text is label_text:
    color black
    font "fonts/Questrial-Regular.otf"
    
style plan_farm_button_text is button_text:
    font "fonts/Questrial-Regular.otf"
    idle_color tan_dark
    hover_color tan_med
    
style plan_farm_text is text:
    color black
    
style plan_farm_vbox is vbox:
    spacing 5    
    
# Custom styles for the crop details part of the screen
style crop_details_vpgrid is vpgrid:
    xalign 0.5
    xfill True
    yalign 1.0
    
style crop_details_label is plan_farm_label:
    background green_dark    
    
style crop_details_label_text is plan_farm_label_text:
    color black    
    size 20
    
style crop_details_selected_label is crop_details_label:
    background tan_dark
    
style crop_details_selected_label_text is crop_details_label_text:
    color white
    
style crop_details_button_text is plan_farm_button_text:
    idle_color green_med
    hover_color green_light
    selected_color white
    
style crop_details_text is plan_farm_text:
    size 16
    yalign 0.5
    xalign 1.0
    
style crop_details_bar is bar:
    left_bar Frame(Solid(green_med))
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
    
style crop_details_vbox is vbox:
    xsize LEFT_COLUMN_WIDTH
    spacing 10
    
style crop_details_hbox is hbox:
    xsize LEFT_COLUMN_WIDTH
    xalign 0.0
    xfill True
    
style crop_details_grid is grid:
    xsize LEFT_COLUMN_WIDTH
    spacing 0
    
style crop_layout_vpgrid is vpgrid:
    spacing 16  
    xalign 0.5
    xsize MIDDLE_COLUMN_WIDTH
    xfill True
    
style crop_layout_hbox is hbox:
    spacing 5
    
style crop_layout_bar is bar:
    bar_vertical True
    xsize 5
    ysize CROP_LAYOUT_BAR_SIZE
    yalign 1.0
    spacing 1

style crop_layout_nitrogen_increased_bar is crop_layout_bar:
    top_bar Frame(Solid(gray_light))
    bottom_bar Frame(Solid(green_dark))
    
style crop_layout_nitrogen_decreased_bar is crop_layout_bar:
    top_bar Frame(Solid(gray_light))
    bottom_bar Frame(Solid(red_med))
    
style crop_totals_bar is crop_layout_bar
