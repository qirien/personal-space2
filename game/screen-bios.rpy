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
        def addToBio(self, addition):
            self.bio = self.bio + "\n-----------------------------------\n" + addition
            self.read = False

    class Bios(renpy.store.object):
        def __init__(self):
            self.people = []
            self.index = 0           
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
                if (person.getRead() == False):
                    return True
            return False

        # Add a person to the list of people. Optionally, give the name of a person to insert them after.        
        # If they already exist, do nothing.
        def addPerson(self, nickname, full_name, bio, afterName=None):
            if (self.getPerson(nickname) is None):
                if (afterName is not None):
                    afterIndex = self.people.index(afterName)
                else:
                    afterIndex = 0
                newPerson = Person(nickname, full_name, bio)
                self.people.insert(afterIndex, newPerson)
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

# Activate all bios after a certain point
label activate_bios:
    $ bios.addPerson("Pavel", "Mayor Pavel Grayson", "If all managers could be like Pavel, no one would mind working. He loves everyone and tries to help each person do their best. He's not the smartest or the most talented or the nicest person, but he knows who is best at what and how to keep everyone happy and productive. His wife is {a=action:SetVariable('show_person', 'Naomi')}Sister Naomi{/a}, but their kids and grandkids all live on Earth.")
    $ bios.addPerson("Naomi", "Sister Naomi Grayson", "She's and older woman who specializes in helping people deal with life, whether through therapy, religion, or just being a good friend. Whenever someone's having a hard time, chances are you'll find her helping out. She and {a=action:SetVariable('show_person', 'Pavel')}Pavel{/a} have been married for like fifty years and have a bunch of kids and grandkids back on Earth.")            

    $ bios.addPerson("Lily", "Dr. Lily Kealoha", "Dr. Lily has lived on Talaam longer than anyone else. She was part of the first group of scientists to come to the planet, study it, and approve it for colonization. She applies her level-headed problem-solving skills to Talaam's biology and geology, like with her edible plant guide.")            

    $ bios.addPerson("Natalia", "Natalia Perón", "Natalia is laid-back and friendly, so we get along pretty well. She farms nearby, raising chickens and growing beans, corn, squash, and other crops. She's married to {a=action:SetVariable('show_person', 'Martín')}Martín{/a} and they have five kids: Tomás (married to Joanna Nguyen), Isabella, Raúl, Josephina (who passed away as a child), and Mateo.")
    $ bios.addPerson("Martín", "Martín Perón", "Martín is one of those quiet guys that you just kind of forget about most of the time. He doesn't talk much, but he's nice enough when we get a chance to hang out with him and his wife {a=action:SetVariable('show_person', 'Natalia')}Natalia{/a}. He's really good with kids, too, though his kids are all older than mine. His son Tomás is married to Joanna Nguyen, and then there's Isabella, Raúl, and Mateo. Josephina was hit by a tractor when she was little and died.")

    $ bios.addPerson("Travis", "Travis Jennings", "Travis is a wild, mischievous kid that never seems to stay still or stay quiet. {a=action:SetVariable('show_person', 'Pete')}Pete{/a} and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} sure have their hands full with him!")            
    $ bios.addPerson("Pete", "Pete Jennings", "Pete loves the extremes. He's a tough, independent cowboy with a soft spot for history books and classic novels. He and {a=action:SetVariable('show_person', 'Helen')}Helen{/a} have a farm that makes the best butter on the planet! He has a {a=action:SetVariable('show_person', 'Travis')}son{/a} about the same age as our daughter.")
    $ bios.addPerson("Helen", "Helen Jennings", "I mostly know Helen from game night. She seems quiet and sweet, but then she'll pull the deadliest moves out of nowhere! She and {a=action:SetVariable('show_person', 'Pete')}Pete{/a} have a couple kids; the oldest, {a=action:SetVariable('show_person', 'Travis')}Travis{/a}, is the same age as our daughter.")

return