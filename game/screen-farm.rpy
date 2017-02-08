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
                    text "Calories: " + str(crop_info[crop_index][1])
                    text "Nutrition: " + str(crop_info[crop_index][2])
                    text "Fun: " + str(crop_info[crop_index][3])
                    text "Work: " + str(crop_info[crop_index][4])
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
                            if (current_crops[i] == ""):
                                textbutton "(_)":
                                    xysize (50,50)
                                    #action SetVariable("current_crops[i]", crop_name)
                            else:
                                textbutton "(" + current_crops[i][:2] + ")":
                                    xysize (50,50)
                                    #action SetField("current_crops", str(i), "")

                # Totals so far                                                    
                vbox:
                    xalign 0.5
                    xsize 200
                    label "Total"
                    text "Calories"
                    text "Nutrition"
                    text "Fun"
                    text "Work"
                    text "Income"                    
            
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
                    textbutton crop_info[j][0]:
                        xysize (50,50)
                        action Return(j) 
                        hovered SetVariable("crop_index", j)             
                        
            textbutton "Accept Plan":
                xalign 1.0
                action Return()
