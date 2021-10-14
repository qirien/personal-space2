#
# Screen to show short bios of all the characters.
#
screen biographies(name):
    on "show" action SetVariable("show_person", name)
    modal True
    zorder 1
    style_prefix "bio"
    key "x" action Hide("biographies")

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            hbox:
                label "Community Bios"
                textbutton "X" xalign 0.97 text_font "fonts/Questrial-Regular.otf" text_bold True text_size 42 focus_mask None action Hide("biographies", irisin) xfill False
            hbox:
                null width 10

                vpgrid:
                    cols 1
                    xsize LEFT_COLUMN_WIDTH + 40
                    mousewheel True
                    edgescroll (70, 50)
                    pagekeys True
                    scrollbars "vertical"
                    yinitial bios.getPosition(name) #Scroll to where the current person is in the list
                    for person in bios:
                        $ name = person.getName()
                        $ fname = person.getFullName()
                        $ read = person.getRead()
                        $ active = person.getActive()
                        if (active):
                            hbox:
                                showif (not read):
                                    text " {b}!{/b} " xalign 1.0 yalign 0.0 alt "" style "alert_text" at tiny_bounce
                                else:
                                    text "" xalign 0.0 alt ""
                                textbutton fname action SetVariable("show_person", name)

                null width 10
                vbox:
                    #xsize MIDDLE_COLUMN_WIDTH-32-50 #we gave up 50px for the left section to be bigger.
                    yalign 0.0                    
                    hbox:
                        $ iconname = bios.getIconName(show_person)
                        add "images/icons/" + iconname + "-icon.png"
                        label bios.getFullName(show_person) xalign 0.9 yalign 1.0
                    text bios.getBio(show_person) 


###############################################################################
#
# Styles for the bio screen
#
###############################################################################
style bio_hbox is parenting_hbox
style bio_vbox is parenting_vbox
style bio_frame is parenting_frame:
    ysize COMPUTER_SUB_HEIGHT
style bio_button is parenting_button
style bio_button_text is parenting_button_text

style bio_text is parenting_text:
    yalign 0.0
    yfill True

style bio_label is parenting_label:
    ypadding 0
    xpadding 0
    xfill False
style bio_label_text is parenting_label_text

###############################################################################
#
# Person and Bios classes for storing people and their biographies
#
###############################################################################

init python:
    class Person(renpy.store.object):
        def __init__(self, nickname, full_name, bio):
            self.nickname = nickname
            self.full_name = full_name
            self.bio = bio
            self.activated = False
            self.read = False
            return
        def getName(self):
            return self.nickname
        def getFullName(self):
            return self.full_name
        def getBio(self):
            self.read = True
            return self.bio
        def getRead(self):
            return self.read
        def getActive(self):
            return self.activated
        def activate(self):
            self.activated = True
            return
        def changeName(self, newName):
            self.nickname = newName            
        def addToBio(self, addition):
            self.activated = True
            self.bio = addition + "\n-------------------------------------------------------\n" + self.bio
            self.read = False
            return

    class Bios(renpy.store.object):
        def __init__(self):
            self.people = []
            self.index = 0   
            self.initialize()        
            return

        def __iter__(self):
            return iter(self.people)

        def __next__(self):
            if (index <= len(self.people)):
                person = self.people[self.index]
                self.index += 1
                return person
            else:
                raise StopIteration

        def getIconName(self, name):
            global his_name, her_name, kid_name, bro_name
            if ("his_name" in name) or (his_name in name) or ("Jack" in name):
                return "him"
            elif ("her_name" in name) or (her_name in name) or ("Kelly" in name):
                return "her"
            elif ("kid_name" in name) or (kid_name in name) or ("Terra" in name):
                return "kid"
            elif ("bro_name" in name) or (bro_name in name) or ("Aeron" in name):
                return "bro"
            elif ("Martín" in name):
                return "martin"
            else:
                return name.lower()

        def hasUnread(self):
            for person in self.people:
                if (person.getActive() and (person.getRead() == False)):
                    return True
            return False

        def activate(self, name):
            person = self.getPerson(name)
            if (person is None):
                return
            else:
                person.activate()
            return

        def changeName(self, oldName, newName):
            for person in self.people:
                if (person.getName() == oldName):
                    person.changeName(newName)
                    return
            return

        # Add a person to the list of people. Optionally, give the name of a person to insert them after.        
        # If they already exist, do nothing.
        def addPerson(self, nickname, full_name, bio):
            if (self.getPerson(nickname) is None):
                newPerson = Person(nickname, full_name, bio)
                self.people.insert(0, newPerson)
            return

        def getPerson(self, name):
            for person in self.people:
                if (person.getName() == name):
                    return person
            return None

        def getFirstUnreadPersonName(self):
            for person in self.people:
                if (person.getActive() and (person.getRead() == False)):
                    return person.getName()
            return self.people[0].getName()

        def addToBio(self, name, addition):
            changePerson = "None"
            for person in self.people:
                if (person.getName() == name):
                    changePerson = person
            if (changePerson == "None"):
                return
            else:
                changePerson.addToBio(addition)

        def getBio(self, name):
            person = self.getPerson(name)
            if (person is None):
                return ""
            else:
                return person.getBio()

        def getFullName(self, name):
            person = self.getPerson(name)
            if (person is None):
                return ""
            else:
                return person.getFullName()

        # Return a float identifying how far this person is down the list. Used to scroll to someone we clicked on.
        def getPosition(self, name):         
            i = 0   
            for i in range(0, len(self.people)):
                if (self.people[i].getName() == name):
                    return (float(i) / len(self.people))

        # Content for all the bios
        def initialize(self):
            self.addPerson("Chaco", "Chaco Acosta", "Chaco is one of the miners. We were assigned to help him feel welcome. I still don't know much about him, except that he doesn't like to talk about himself.")
            self.addPerson("Brennan", "Brennan Callahan", "When we first arrived on Talaam, Brennan was assigned to assist [her_name] at the clinic. But the real reason he was here was to report back to RET about our planet's value for mining. His favorite things are wine, women, and being smug and condescending. I thought I would never have to deal with him again, but now he's back as the manager for RET's mining operation.")

            self.addPerson("Zaina", "Zaina Shirazi", "Zaina arrived from Earth around the time [kid_name] was born. She's a geologist helping to scout out the planet for RET so that they know where the best mining sites will be. She and {a=action:SetVariable('show_person', 'Kevin')}Kevin{/a} got married right before they came here. They also have their own garden. And she has a great sense of humor (well, she laughs at my jokes anyway).")
            self.addPerson("Kevin", "Kevin Washington", "As a mining engineer, Kevin is making plans for future mining by RET. He has a real head for numbers, but he sometimes takes things too literally and wants everything to be quantifiable like math is. In that way he and his wife {a=action:SetVariable('show_person', 'Zaina')}Zaina{/a} are kind of opposites, but they are both curious and fast learners.")

            self.addPerson("Pavel", "Mayor Pavel Grayson", "If all managers could be like Pavel, no one would mind working. He loves everyone and tries to help each person do their best. He's not the smartest or the most talented or the nicest person, but he knows how to keep everyone happy and productive. His wife is {a=action:SetVariable('show_person', 'Naomi')}Sister Naomi{/a}; their kids and grandkids all live on Earth.")
            self.addPerson("Naomi", "Sister Naomi Grayson", "She's an older woman who specializes in helping people deal with life, whether through therapy, religion, or just being a good friend. Whenever someone's having a hard time, chances are you'll find her helping out. She and {a=action:SetVariable('show_person', 'Pavel')}Pavel{/a} have been married for like fifty years and have a bunch of kids and grandkids back on Earth.")            

            self.addPerson("Lily", "Dr. Lily Kealoha", "Dr. Lily was part of the first group of scientists to come to the planet, study it, and approve it for colonization. She applies her precision problem-solving skills to Talaam's biology and geology, like with her edible plant guide and solar flare warning system. She tends to keep to herself unless rocks or plants are involved.")

            self.addPerson("Natalia", "Natalia Perón", "Natalia is laid-back and friendly, so we get along pretty well. She farms nearby, raising chickens and growing beans, corn, squash, and other crops. She's married to {a=action:SetVariable('show_person', 'Martín')}Martín{/a} and they have five kids: Tomás (married to Joanna Nguyen), Isabella, Raúl, Josephina (who passed away as a child), and Mateo.")
            self.addPerson("Martín", "Martín Perón", "Martín is one of those quiet guys that you just kind of forget about most of the time. But he's dependable, and honest, and he doesn't deserve the cancer he's been fighting for years. He's really good with the kids he and {a=action:SetVariable('show_person', 'Natalia')}Natalia{/a} have, though his kids are all older than mine. His son Tomás is married to Joanna Nguyen, and then there's Isabella, Raúl, and Mateo. Josephina was hit by a tractor when she was little and died.")

            self.addPerson("Travis", "Travis Jennings", "Travis is a wild, mischievous kid that never seems to stay still or stay quiet. Maybe it's because he was born on the shuttle from Earth? {a=action:SetVariable('show_person', 'Pete')}Pete{/a} and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} sure have their hands full with him!")            
            self.addPerson("Pete", "Pete Jennings", "Pete loves the extremes. He's a tough, independent cowboy with a soft spot for history books and classic novels. He and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} have a farm that makes the best butter on the planet! He has a {a=action:SetVariable('show_person', 'Travis')}son{/a} just a little bit older than [kid_name].")
            self.addPerson("Helen", "Helen Jennings", "Helen Jennings used to be so shy, she'd barely say more than two words to me. I don't know if she changed or just feels more comfortable around me now, but she's actually a real tough cowgirl. And she's the best painter we have. Maybe also the only painter? She and {a=action:SetVariable('show_person', 'Pete')}Pete{/a} have a couple kids; the oldest, {a=action:SetVariable('show_person', 'Travis')}Travis{/a}, is the same age as our daughter.")

            self.addPerson("Thuc", "Thuc Nguyen", "Thuc Nguyen has a great sense of humor and is a dedicated farmer. We have the same sense of humor and the same lack of patience with incompetence. He met his wife {a=action:SetVariable('show_person', 'Julia')}Julia{/a} when they were both working for the Peace Corps in Cambodia, and now they have like ten kids, including Joanna (married to Tomás Perón), Miranda, Gardenia, and Van.")
            self.addPerson("Julia", "Julia Nguyen", "Julia is very particular about her farm, her kids, and... pretty much everything. She's a really organized and knowledgeable farmer, midwife, and crafter -- you name it, she can make it five different ways.  She and her husband {a=action:SetVariable('show_person', 'Thuc')}Thuc{/a} have 9 really polite kids (including Joanna, Miranda, and Van) and 1 little stinker (Gardenia).")  

            self.addPerson("Oleg", "Oleg Andrevski", "He's {a=action:SetVariable('show_person', 'Sara')}Sara{/a} and {a=action:SetVariable('show_person', 'Ilian')}Ilian{/a}'s son, about the same age as {a=action:SetVariable('show_person', '[[kid_name]')}[kid_name]{/a}. He doesn't talk much but I get the feeling he's really smart. Everyone dotes on him but somehow he's not spoiled, just sweet.")
            self.addPerson("Sara", "Sara Hill-Andrevski", "Sara helps {a=action:SetVariable('show_person', 'Pavel')}Mayor Grayson{/a} stay organized and get things done around the colony. She's friendly and has a good sense of humor and is also good friends with [her_name]. She and {a=action:SetVariable('show_person', 'Ilian')}Ilian{/a} have a son named {a=action:SetVariable('show_person', 'Oleg')}Oleg{/a}.")
            self.addPerson("Ilian", "Ilian Andrevski", "I'm guessing Ilian wasn't always the grumpy control freak he is now... but it's hard to imagine. He runs the storehouse with an iron fist, which is probably good for increasing our food stores, but doesn't make him well-liked. Maybe he needs more fresh air? He and {a=action:SetVariable('show_person', 'Sara')}Sara{/a} have a son named {a=action:SetVariable('show_person', 'Oleg')}Oleg{/a}.")
                        
            self.addPerson("[bro_name]", "[bro_name] Ventura", "[bro_name] is our second child. He was born with a cleft lip, which made it difficult to feed him for the first few months. He has a lot going on inside his head, even though he doesn't say much. He's [bro_age] Earth years old.")
            self.addPerson("[kid_name]", "[kid_name] Ventura", "We made a person! She was one of the first babies to be born here. She's smart and determined and definitely has her own ideas about who she wants to become. She's [earth_year] Earth years old.")            
            self.addPerson("[her_name]", "[her_name] Ventura", "My wife, lover, and best friend forever, [her_name]. She's the colony doctor as well as being a level-headed mom. She had a hard time adjusting to life away from Earth, but we've stuck together even when I forgot our anniversary, and when she got really homesick, and when she got pregnant and had to make her own maternity clothes.... She's an amazing woman.")            
            self.addPerson("[his_name]", "[his_name] Ventura", "All right, finally someone I actually know something about! I'm a farmer and husband to {a=action:SetVariable('show_person', '[her_name]')}[her_name]{/a}. I love my family, my horse Lettie, the outdoors, growing things, playing games, and writing poetry. I'm also {a=action:SetVariable('show_person', '[kid_name]')}[kid_name]{/a}'s father.")
