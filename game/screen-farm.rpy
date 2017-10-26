# Farm Planning Screen
# Using this screen, the user can select which crops to plant where and see the projected results.  When they are done, they can hit "Accept Plan".
#
# TODO: Support permanent plants, such as plums, goats?
# TODO: Use bars for displaying crop stats?
# TODO: Get some graphics and pretty this up
# TODO: show kids' ages and farm/community info

screen plan_farm:
    style_prefix "plan_farm"
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User {color=#888}[his_name]{/color} has logged on." size 12 xalign 0.1 ypos 22 color "#fff"
        textbutton "?" xpos 1077 ypos 22 action Jump("tutorial_ask")
        textbutton "             " xpos 1085 ypos 22 action ShowMenu("preferences")
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
                            label "[his_name] and [her_name]'s Family"
                            text "Kids:"                         
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
                    
                # crop details here          
                frame:
                    yfill True
                    background gray_dark
                    style_prefix "crop_details"                    
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
                                            Return()
                                        ]
                            textbutton "Accept Plan":
                                xalign 1.0
                                action Return()

##
# Subscreen letting the user see information on crops and choose which to plant this year
##
screen crop_details_screen():
    hbox:
        xalign 0.5
        xfill True
        vbox:
            xalign 0.5
            xsize 200
            
            $ crop_name = crop_info[crop_info_index][NAME_INDEX]
            $ imagefile = "gui/crop icons/" + crop_name + ".png" 
            label crop_name.capitalize()
            add imagefile
            text "Calories:     " + str(crop_info[crop_info_index][CALORIES_INDEX])
            text "Nutrition:    " + str(crop_info[crop_info_index][NUTRITION_INDEX])
            text "Fun:          " + str(crop_info[crop_info_index][FUN_INDEX])
            text "Work:         " + str(crop_info[crop_info_index][WORK_INDEX])
            #text "Income: " + str(crop_info[crop_info_index][5])
          
        # Crop layout area
        vbox:
            xalign 0.5
            xsize 400
            label "Layout"
            vpgrid:
                if (farm_size <= 16):
                    cols 4
                else:
                    cols 8
                spacing 5
                draggable True
                mousewheel True
                
                #scrollbars "vertical"
                side_xalign 0.5
                for i in range(0, farm_size):
                    $ max_crops_reached = (crops.count(crop_info[crop_info_index][NAME_INDEX]) >= crop_info[crop_info_index][MAXIMUM_INDEX])          
                    if (crops[i] == ""):
                        $ imagefile = "gui/crop icons/blank.png" 
                        textbutton "(_)":
                            xysize (50,50)
                            action [
                                SetCrop(i, crop_name),
                                renpy.restart_interaction # This makes the screen refresh
                                ]
                            sensitive (not max_crops_reached)
                    else:
                        $ imagefile = "gui/crop icons/" + crops[i] + ".png"
                        imagebutton:
                            idle imagefile 
                            xysize (50,50)
                            anchor (0.5, 0.5)
                            align  (0.5, 0.5)
                            action [ SetCrop(i, ""), renpy.restart_interaction ] 
                            at highlight_imagebutton
                             
            # Show crops that we can choose from
            vpgrid:
                # TODO: change this based on number of enabled crops?
                cols 4
                spacing 2
                draggable True
                mousewheel True        
                #scrollbars "horizotal"
                
                for j in range(0, len(crop_info)):
                    if (crop_info[j][ENABLED_INDEX]):
                        $ max_crops_reached = (crops.count(crop_info[j][NAME_INDEX]) >= crop_info[j][MAXIMUM_INDEX])
                        $ imagefile = "gui/crop icons/" + crop_info[j][NAME_INDEX] + ".png"
                        imagebutton:
                            idle imagefile 
                            xysize (50,50)
                            anchor (0.5, 0.5)
                            align  (0.5, 0.5)
                            sensitive (not max_crops_reached)
                            selected ((crop_info_index == j) and (not max_crops_reached))
                            action [ SetVariable("crop_info_index", j), renpy.restart_interaction ] 
                            at highlight_imagebutton
                            
                            # TODO: Add alternate action to get more crop info?            
                        
    
        # Totals so far                                                    
        vbox:
            xalign 0.5
            xsize 200
            
            $ total_calories = 0
            $ total_nutrition = 0
            $ total_fun = 0
            $ total_work = 0
            # Totaling crops attributes        
            for i in range(0, crops.len()):
                if (crops[i] != ""):
                    $ crop_names = [row[NAME_INDEX] for row in crop_info]
                    $ index = crop_names.index(crops[i]) # find the crop's index in crop_info                
                    $ total_calories += crop_info[index][CALORIES_INDEX]
                    $ total_nutrition += crop_info[index][NUTRITION_INDEX]
                    $ total_fun += crop_info[index][FUN_INDEX]
                    $ total_work += crop_info[index][WORK_INDEX]
                    
            label "Total"
            text "Calories:     " + str(total_calories)
            text "Nutrition:    " + str(total_nutrition)
            text "Fun:          " + str(total_fun)
            text "Work:         " + str(total_work)                 
    
    
    
init python:
    
    # Set the crop in our farm array and update the total stats for the farm
    def set_crop(index, crop_name):
        crops[index] = crop_name
        
    SetCrop = renpy.curry(set_crop)
    
    # Use our default test crops
    def set_default_crops():
        global crops
        crops.setDefault()
        
# Custom styles for the farm planning screen
style plan_farm_label is label:
    background green_dark
    xfill True

style plan_farm_label_text is label_text:
    color white
    font "fonts/Questrial-Regular.otf"
    
style plan_farm_button_text is button_text:
    font "fonts/Questrial-Regular.otf"
    idle_color green_med
    hover_color green_dark
    
style plan_farm_text is text:
    color black
    
# Custom styles for the crop details part of the screen
style crop_details_vpgrid is vpgrid:
    xalign 0.5
    
style crop_details_label is plan_farm_label:
    background tan_dark
    
style crop_details_label_text is plan_farm_label_text:
    color black    
    
style crop_details_button_text is plan_farm_button_text:
    idle_color tan_med
    hover_color tan_light
