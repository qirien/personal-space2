#
# Screen to show short bios of all the characters.
# TODO: Make it so you can get to this screen by clicking on someone's portrait,
#       their mini-portrait in NVL mode, or the main computer screen
#
screen biographies(name="Thuc"):
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
                null width 30

                vpgrid:
                    cols 1
                    xsize LEFT_COLUMN_WIDTH-50
                    for person in bios:
                        $ name = person.getName()
                        textbutton name action SetVariable("show_person", name)
                        #add "images/icons/" + name + "-icon.png"

                null width 5
                vbox:
                    xsize MIDDLE_COLUMN_WIDTH-32
                    yalign 0.0                    
                    label bios.getFullName(show_person) 
                    text  bios.getBio(show_person) 


############################################################################################
#
# Styles for the bio screen
#
############################################################################################
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

############################################################################################
#
# Person and Bios classes for storing people and their biographies
#
############################################################################################

init python:
    class Person(renpy.store.object):
        def __init__(self, nickname, full_name, bio):
            self.nickname = nickname
            self.full_name = full_name
            self.bio = bio
            return
        def getName(self):
            return self.nickname
        def getFullName(self):
            return self.full_name
        def getBio(self):
            return self.bio

    class Bios(renpy.store.object):
        def __init__(self):
            self.people = []
            self.index = 0            
            self.addPerson("Thuc", "Thuc Nguyen", "Thuc Nguyen is my neighbor, a farmer, and best friend (aside from [her_name] of course). We have the same sense of humor and the same lack of patience with incompetence. He raises goats and grows rice, onions, and other vegetables. He and his wife {a=showmenu:biographies(\"Julia\")}Julia{/a} have 10 kids, including Joanna (married to Tomás Perón), Miranda, Gardenia, and Van.")
            self.addPerson("Julia", "Julia Nguyen", "Julia is very particular about her farm, her kids, and... pretty much everything. She's an amazing farmer and homesteader -- you name it, she can make it five different ways. I still try to avoid her, though. She and her husband {a=showmenu:biographies(\"Thuc\")}Thuc{/a} have 9 really polite kids (including Joanna, Miranda, and Van) and 1 little stinker (Gardenia).")            
            self.addPerson("Natalia", "Natalia Perón", "Natalia is laid-back and friendly, so we get along pretty well. She farms nearby, raising chickens and growing beans, corn, squash, and other crops. She's married to Martín and they have five kids: Tomás (married to Joanna Nguyen), Isabella, Raúl, Josephina (who passed away as a child), and Mateo.")
            self.addPerson("Martín", "Martín Perón", "Martín is one of those quiet guys that you just kind of forget about most of the time. He doesn't talk much, but he's nice enough when we get a chance to hang out. He's really good with kids, too, though his kids are all older than mine. His son Tomás is married to Joanna Nguyen, and then there's Isabella, Raúl, and Mateo. Josephina was hit by a tractor when she was little and died.")
            self.addPerson("Pavel", "Mayor Pavel Grayson", "If all managers could be like Pavel, no one would mind working. He loves everyone and tries to help each person do their best. He's not the smartest or the most talented or the nicest person, but he knows who is best at what and how to keep everyone happy and productive. His wife is Sister Naomi.")

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

        def addPerson(self, nickname, full_name, bio):
            self.people.append(Person(nickname, full_name, bio))
            return

        def getPerson(self, name):
            for person in self.people:
                if (person.getName() == name):
                    return person
            return None

        def getBio(self, name):
            person = self.getPerson(name)
            if (person is None):
                return None
            else:
                return person.getBio()

        def getFullName(self, name):
            person = self.getPerson(name)
            if (person is None):
                return None
            else:
                return person.getFullName()
