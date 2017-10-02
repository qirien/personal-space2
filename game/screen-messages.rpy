# Screen to display messages every month        
screen messages:
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        vbox:
            area (50, 30, 1180, 660)           
            yfill True
            label "Community Message Board"
            # get monthly  messages here
            
            
            textbutton "Return" yalign 1.0 action Hide("messages")
