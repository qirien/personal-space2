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
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    for person in bios:
                        $ name = person.getFullName()
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
        def addToBio(self, addition):
            self.bio = self.bio + "\n-----------------------------------\n" + addition

    class Bios(renpy.store.object):
        def __init__(self):
            self.people = []
            self.index = 0

            # Initial bios from the beginning of the game.
            self.addPerson("Thuc", "Thuc Nguyen", "Thuc Nguyen is my neighbor, a farmer, and best friend (aside from [her_name] of course). We have the same sense of humor and the same lack of patience with incompetence. He raises goats and grows rice, onions, and other vegetables. He and his wife {a=showmenu:biographies(\"Julia\")}Julia{/a} have 10 kids, including Joanna (married to Tomás Perón), Miranda, Gardenia, and Van.")
            self.addPerson("Julia", "Julia Nguyen", "Julia is very particular about her farm, her kids, and... pretty much everything. She's an amazing farmer and homesteader -- you name it, she can make it five different ways. I still try to avoid her, though. She and her husband {a=showmenu:biographies(\"Thuc\")}Thuc{/a} have 9 really polite kids (including Joanna, Miranda, and Van) and 1 little stinker (Gardenia).")            
            self.addPerson("Natalia", "Natalia Perón", "Natalia is laid-back and friendly, so we get along pretty well. She farms nearby, raising chickens and growing beans, corn, squash, and other crops. She's married to Martín and they have five kids: Tomás (married to Joanna Nguyen), Isabella, Raúl, Josephina (who passed away as a child), and Mateo.")
            self.addPerson("Martín", "Martín Perón", "Martín is one of those quiet guys that you just kind of forget about most of the time. He doesn't talk much, but he's nice enough when we get a chance to hang out. He's really good with kids, too, though his kids are all older than mine. His son Tomás is married to Joanna Nguyen, and then there's Isabella, Raúl, and Mateo. Josephina was hit by a tractor when she was little and died.")
            self.addPerson("Pavel", "Mayor Pavel Grayson", "If all managers could be like Pavel, no one would mind working. He loves everyone and tries to help each person do their best. He's not the smartest or the most talented or the nicest person, but he knows who is best at what and how to keep everyone happy and productive. His wife is Sister Naomi, but their kids and grandkids all live on Earth.")
            self.addPerson("Naomi", "Sister Naomi Grayson", "She's and older woman who specializes in helping people deal with life, whether through therapy, religion, or just being a good friend. Whenever someone's having a hard time, chances are you'll find her helping out. She and Pavel have been married for like fifty years and have a bunch of kids and grandkids back on Earth.")
            self.addPerson("[his_name]", "[his_name] Ventura", "All right, finally someone I actually know something about! I'm a farmer and husband to [her_name]. I love my horse Lettie, the outdoors, games, and writing poetry. I'm also [kid_name]'s father.")
            self.addPerson("[her_name]", "[her_name] Ventura", "My wife, lover, and best friend forever, [her_name]. We got married right before coming to Talaam as colonists. Our first year was kind of rough, living on our own on a new planet, but we made it work. She is a capable doctor and a caring mother, and there's no one I'd rather live in the middle of nowhere with!")
            self.addPerson("[kid_name]", "[kid_name] Ventura", "We made a person! She definitely has her own ideas about who she wants to become.")
            # TODO: add bro when he's born?
            self.addPerson("Pete", "Pete Jennings", "Pete loves the extremes. He's a tough, independent cowboy with a soft spot for history books and classic novels. His farm makes the best butter on the planet! He has a son about the same age as our daughter.")
            self.addPerson("Helen", "Helen Jennings", "I mostly know Helen from game night. She seems quiet and sweet, but then she'll pull the deadliest moves out of nowhere! She and Pete have a couple kids; the oldest, Travis, is the same age as our daughter.")
            self.addPerson("Travis", "Travis Jennings", "Travis is a wild, mischievous kid that never seems to stay still or stay quiet. Pete and Helen sure have their hands full with him!")
            self.addPerson("Lily", "Dr. Lily Kealoha", "Dr. Lily has lived on Talaam longer than anyone else. She was part of the first group of scientists to come to the planet, study it, and approve it for colonization. She applies her level-headed problem-solving skills to Talaam's biology and geology, like with her edible plant guide.")
            self.addPerson("Sara", "Sara Andrevski", "Sara helps Mayor Grayson stay organized and get things done around the colony. She's friendly and has a good sense of humor and is also good friends with [her_name]. She and Ilian have a son named Oleg.")
            self.addPerson("Ilian", "Ilian Andrevski", "I'm guessing Ilian wasn't always the grumpy control freak he is now... but it's hard to imagine. He runs the storehouse with an iron fist, which is probably good for increasing our food stores, but doesn't make him well-liked. He and Sara have a son named Oleg.")
            self.addPerson("Oleg", "Oleg Andrevski", "He's Sara and Ilian's son, about the same age as [her_name]. He doesn't talk much but I get the feeling he's really smart.")
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

        def addPerson(self, nickname, full_name, bio, afterName=None):
            if (afterName is not None):
                afterIndex = self.people.index(afterName)
            else:
                afterIndex = len(self.people)
            newPerson = Person(nickname, full_name, bio)
            self.people.insert(afterIndex, newPerson)
            return

        def getPerson(self, name):
            for person in self.people:
                if (person.getName() == name):
                    return person
            return None

        def addToBio(self, name, addition):
            person = self.getPerson(name)
            if (person is None):
                return
            else:
                person.addToBio(addition)

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
