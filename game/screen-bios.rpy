#
# Screen to show short bios of all the characters.
# TODO: Make it so you can get to this screen by clicking on someone's portrait,
#       their mini-portrait in NVL mode, or the main computer screen
# TODO: Have all bios from the beginning, but only activate them when you meet someone OR when you click on someone's portrait
#
screen biographies(name):
    modal True
    zorder 1
    style_prefix "bio"
    on "show" action SetVariable("show_person", name)

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            hbox:
                label "Community Bios"
                textbutton "X" xalign 0.97 action Hide("biographies", irisin) xfill False
            hbox:
                null width 20

                vpgrid:
                    cols 1
                    xsize LEFT_COLUMN_WIDTH-50
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    for person in bios:
                        $ name = person.getName()
                        $ fname = person.getFullName()
                        $ read = person.getRead()
                        $ active = person.getActive()
                        if (active):
                            hbox:
                                showif (not read):
                                    text " {b}!{/b} " xalign 1.0 yalign 0.0 style "alert_text" at tiny_bounce
                                else:
                                    text "" xalign 0.0
                                textbutton fname action SetVariable("show_person", name)
                            #TODO: add icons somewhere in here add "images/icons/" + name + "-icon.png"

                null width 5
                vbox:
                    xsize MIDDLE_COLUMN_WIDTH-32
                    yalign 0.0                    
                    label bios.getFullName(show_person) 
                    text  bios.getBio(show_person) 


###############################################################################
#
# Styles for the bio screen
#
###############################################################################
style bio_hbox is parenting_hbox
style bio_vbox is parenting_vbox
style bio_frame is parenting_frame
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
            self.bio = self.bio + "\n-----------------------------------\n" + addition
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

        def getFirstPersonName(self):
            return self.people[0].getName()

        def addToBio(self, name, addition):
            person = self.people.remove(name)
            if (person is None):
                return
            else:
                person.addToBio(addition)
            self.people.insert(len(self.people), person)

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

        # Content for all the bios
        def initialize(self):
            self.addPerson("Chaco", "Chaco Acosta", "Chaco is one of the miners. We were assigned to help him feel welcome. He's not very expressive, so it's hard to know what he's feeling, but he seems like a solid guy.")
            self.addPerson("Brennan", "Brennan Callahan", "When we first arrived on Talaam, Brennan was assigned to assist [her_name] at the clinic. But the real reason he was here was to report back to RET about our planet's value for mining. Something about him always bugged me... actually, lots of things about him bug me -- his arrogance, his total lack of practical skills, and his winks and smiles towards every woman on the planet between 15 and 50. Now he's back as the manager for RET's mining operation.")

            self.addPerson("Zaina", "Zaina Shirazi", "Zaina arrived from Earth around the time [kid_name] was born. She's a geologist helping to scout out the planet for RET so that they know where the best mining sites will be. She and Kevin got married right before they came here. They also have their own garden.")
            self.addPerson("Kevin", "Kevin Washington", "As a mining engineer, Kevin is making plans for future mining by RET. He has a real head for numbers, but he sometimes takes things too literally and wants everything to be quantifiable like math is. In that way he and his wife Zaina are kind of opposites, but they are both curious and fast learners.")

            self.addPerson("Pavel", "Mayor Pavel Grayson", "If all managers could be like Pavel, no one would mind working. He loves everyone and tries to help each person do their best. He's not the smartest or the most talented or the nicest person, but he knows who is best at what and how to keep everyone happy and productive. His wife is {a=action:SetVariable('show_person', 'Naomi')}Sister Naomi{/a}, but their kids and grandkids all live on Earth.")
            self.addPerson("Naomi", "Sister Naomi Grayson", "She's and older woman who specializes in helping people deal with life, whether through therapy, religion, or just being a good friend. Whenever someone's having a hard time, chances are you'll find her helping out. She and {a=action:SetVariable('show_person', 'Pavel')}Pavel{/a} have been married for like fifty years and have a bunch of kids and grandkids back on Earth.")            

            self.addPerson("Lily", "Dr. Lily Kealoha", "Dr. Lily has lived on Talaam longer than anyone else. She was part of the first group of scientists to come to the planet, study it, and approve it for colonization. She applies her precision problem-solving skills to Talaam's biology and geology, like with her edible plant guide and solar flare warning system.")

            self.addPerson("Natalia", "Natalia Perón", "Natalia is laid-back and friendly, so we get along pretty well. She farms nearby, raising chickens and growing beans, corn, squash, and other crops. She's married to {a=action:SetVariable('show_person', 'Martín')}Martín{/a} and they have five kids: Tomás (married to Joanna Nguyen), Isabella, Raúl, Josephina (who passed away as a child), and Mateo.")
            self.addPerson("Martín", "Martín Perón", "Martín is one of those quiet guys that you just kind of forget about most of the time. He doesn't talk much, but he's nice enough when we get a chance to hang out with him and his wife {a=action:SetVariable('show_person', 'Natalia')}Natalia{/a}. He's really good with kids, too, though his kids are all older than mine. His son Tomás is married to Joanna Nguyen, and then there's Isabella, Raúl, and Mateo. Josephina was hit by a tractor when she was little and died.")

            self.addPerson("Travis", "Travis Jennings", "Travis is a wild, mischievous kid that never seems to stay still or stay quiet. {a=action:SetVariable('show_person', 'Pete')}Pete{/a} and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} sure have their hands full with him!")            
            self.addPerson("Pete", "Pete Jennings", "Pete loves the extremes. He's a tough, independent cowboy with a soft spot for history books and classic novels. He and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} have a farm that makes the best butter on the planet! He has a {a=action:SetVariable('show_person', 'Travis')}son{/a} about the same age as our daughter.")
            self.addPerson("Helen", "Helen Jennings", "I mostly know Helen from game night. She seems quiet and sweet, but then she'll pull the deadliest moves out of nowhere! She and {a=action:SetVariable('show_person', 'Pete')}Pete{/a} have a couple kids; the oldest, {a=action:SetVariable('show_person', 'Travis')}Travis{/a}, is the same age as our daughter.")

            self.addPerson("Thuc", "Thuc Nguyen", "Thuc Nguyen is my neighbor, a farmer, and best friend (aside from [her_name] of course). We have the same sense of humor and the same lack of patience with incompetence. He raises goats and grows rice, onions, and other vegetables. He and his wife {a=action:SetVariable('show_person', 'Julia')}Julia{/a} have 10 kids, including Joanna (married to Tomás Perón), Miranda, Gardenia, and Van.")
            self.addPerson("Julia", "Julia Nguyen", "Julia is very particular about her farm, her kids, and... pretty much everything. She's an amazing farmer and homesteader -- you name it, she can make it five different ways. I still try to avoid her, though. She and her husband {a=action:SetVariable('show_person', 'Thuc')}Thuc{/a} have 9 really polite kids (including Joanna, Miranda, and Van) and 1 little stinker (Gardenia).")  

            self.addPerson("Oleg", "Oleg Andrevski", "He's {a=action:SetVariable('show_person', 'Sara')}Sara{/a} and {a=action:SetVariable('show_person', 'Ilian')}Ilian{/a}'s son, about the same age as {a=action:SetVariable('show_person', '[[kid_name]')}[kid_name]{/a}. He doesn't talk much but I get the feeling he's really smart.")
            self.addPerson("Sara", "Sara Andrevski", "Sara helps {a=action:SetVariable('show_person', 'Pavel')}Mayor Grayson{/a} stay organized and get things done around the colony. She's friendly and has a good sense of humor and is also good friends with [her_name]. She and {a=action:SetVariable('show_person', 'Ilian')}Ilian{/a} have a son named {a=action:SetVariable('show_person', 'Oleg')}Oleg{/a}.")
            self.addPerson("Ilian", "Ilian Andrevski", "I'm guessing Ilian wasn't always the grumpy control freak he is now... but it's hard to imagine. He runs the storehouse with an iron fist, which is probably good for increasing our food stores, but doesn't make him well-liked. He and {a=action:SetVariable('show_person', 'Sara')}Sara{/a} have a son named {a=action:SetVariable('show_person', 'Oleg')}Oleg{/a}.")
                        
            self.addPerson("[bro_name]", "[bro_name] Ventura", "[bro_name] is our second child. He was born with a cleft lip, which made it difficult to feed him for the first few months.")
            self.addPerson("[kid_name]", "[kid_name] Ventura", "We made a person! She definitely has her own ideas about who she wants to become.")            
            self.addPerson("[her_name]", "[her_name] Ventura", "My wife, lover, and best friend forever, [her_name]. We got married right before coming to Talaam as colonists. Our first year was kind of rough, living on our own on a new planet, but we made it work. She is a capable doctor and a caring mother, and there's no one I'd rather live in the middle of nowhere with!")            
            self.addPerson("[his_name]", "[his_name] Ventura", "All right, finally someone I actually know something about! I'm a farmer and husband to {a=action:SetVariable('show_person', '[her_name]')}[her_name]{/a}. I love my horse Lettie, the outdoors, games, and writing poetry. I'm also {a=action:SetVariable('show_person', '[kid_name]')}[kid_name]{/a}'s father.")
