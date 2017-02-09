# Farm Planning Screen
# Using this screen, the user can select which crops to plant where and see the projected results.  When they are done, they can hit "Accept Plan".
#
# TODO: Actually set crop variables.  Use screen variables and return it or something else?
# TODO: Use bars for displaying crop stats?
# TODO: Get some graphics
# TODO: Pretty this up 

screen plan_farm:
    frame:
        vbox:
            yfill True
            label "Farm Plan for Year " + str(year):
                xalign 0.5
            hbox:
                xfill True
                # crop details here
                vbox:
                    xalign 0.5
                    xsize 200
                    
                    $ crop_name = crop_info[crop_index][0]
                    label crop_name.capitalize()
                    text "Calories:     " + str(crop_info[crop_index][CALORIES_INDEX])
                    text "Nutrition:    " + str(crop_info[crop_index][NUTRITION_INDEX])
                    text "Fun:          " + str(crop_info[crop_index][FUN_INDEX])
                    text "Work:         " + str(crop_info[crop_index][WORK_INDEX])
                    #text "Income: " + str(crop_info[crop_index][5])
                  
                # Crop layout area
                vbox:
                    xalign 0.5
                    label "Layout"
                    vpgrid:
                        cols 4
                        spacing 5
                        draggable True
                        mousewheel True
                        
                        #scrollbars "vertical"
                        side_xalign 0.5
                        for i in range(0, farm_size):
                            if (crops[i] == ""):
                                textbutton "(_)":
                                    xysize (50,50)
                                    action [
                                        SetCrop(i, crop_name),
                                        renpy.restart_interaction # This makes the screen refresh
                                        ]
                            else:
                                textbutton "(" + crops[i][:2] + ")":
                                    xysize (50,50)
                                    action [
                                        SetCrop(i, ""),
                                        renpy.restart_interaction # This makes the screen refresh
                                        ]                                        

                # Totals so far                                                    
                vbox:
                    xalign 0.5
                    xsize 200
                    label "Total"
                    text "Calories:     " + str(total_calories)
                    text "Nutrition:    " + str(total_nutrition)
                    text "Fun:          " + str(total_fun)
                    text "Work:         " + str(total_work)                 
            
            # Show crops that we can choose from
            # TODO: only allow enabled crops
            vpgrid:
                xfill True
                cols 8
                spacing 2
                draggable True
                mousewheel True
                #scrollbars "horizotal"
                
                for j in range(0, len(crop_info)):
                    if (crop_info[j][ENABLED_INDEX]):
                        textbutton crop_info[j][0]:
                            xysize (50,50)
                            action [
                                    SetVariable("crop_index", j),
                                    renpy.restart_interaction # This makes the screen refresh
                            ]
                            #hovered SetVariable("crop_index", j)             
                        
            textbutton "Accept Plan":
                xalign 1.0
                action Return()
                
                
                
init python:
    
    # Set the crop in our farm array and update the total stats for the farm
    def set_crop(index, crop_name):
        crops[index] = crop_name
        update_totals()
        
        
    # TODO: Why does this think these are local variables instead of using the global ones?
    def update_totals():
        total_calories = 0
        total_nutrition = 0
        total_fun = 0
        total_work = 0        
        for i in range(0, len(crops)):
            if (crops[i] != ""):
                crop_names = [row[0] for row in crop_info]
                crop_index = crop_names.index(crops[i]) # find the crop's index in crop_info
                total_calories += crop_info[crop_index][CALORIES_INDEX]
                total_nutrition += crop_info[crop_index][NUTRITION_INDEX]
                total_fun += crop_info[crop_index][FUN_INDEX]
                total_work += crop_info[crop_index][WORK_INDEX]
        
        
    SetCrop = renpy.curry(set_crop)
