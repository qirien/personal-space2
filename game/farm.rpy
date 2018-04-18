# Code for the crop and fields objects and functions
# relating to the farm.

init python:

    ##
    # FIELD OBJECT
    ##

    class Field(renpy.store.object):
        NITROGEN_FULL = 100
        NITROGEN_FALLOW = -50
        NITROGEN_GOATS = -95
        PEST_NONE = 2
        PEST_GOAT_REDUCTION = -2
        PEST_FALLOW_REDUCTION = -75
        PEST_MAX = 100
        HISTORY_SIZE = 3

        NITROGEN_LEVEL_INDEX = 0
        PEST_LEVEL_INDEX = 1
        def __init__(self, current_size, max_size=MAX_FARM_SIZE):
            self.current_size = current_size
            self.max_size = max_size

            # Current health of the field, with Nitrogen levels and Pest levels
            # We *cannot* do health = [[100, 5] * max_size] because then all elements of the array point to the same memory location.
            self.health = [[Field.NITROGEN_FULL, Field.PEST_NONE] for i in range(max_size)]
            [[Field.NITROGEN_FULL, Field.PEST_NONE]] * max_size
            # History of the last three crops planted in each space
            self.history = [["fallow", "fallow", "fallow"]] * max_size
            # Current crops planted in each space
            self.crops = Crops(current_size)


        # Calculate how many crops we harvested in each square and update the field_health
        def process_crops(self):
            final_yield = [100] * self.current_size
            current_nitrogen = 0
            current_pests = 0
            for i in range(0, self.current_size):
                pest_factor = 0
                nitrogen_factor = 0
                crop_name = self.crops[i]
                current_nitrogen = self.health[i][Field.NITROGEN_LEVEL_INDEX]
                current_pests = self.health[i][Field.PEST_LEVEL_INDEX]
                #print "Crop " + str(i) + " is " + crop_name + " and current_nitrogen: " + str(current_nitrogen) + ", current_pests: " + str(current_pests)
                # Decrease yield based on randomness and number of times crop has been in that spot lately.
                # Set pest level of field after crops.
                if (crop_name == "fallow"):
                    pest_factor = current_pests // Field.PEST_FALLOW_REDUCTION
                elif (crop_name == "goats"):
                    pest_factor = current_pests // Field.PEST_GOAT_REDUCTION
                else:
                    pest_factor = int(current_pests + current_pests * renpy.random.random() * self.history[i].count(crop_name))
                new_pests = self.health[i][Field.PEST_LEVEL_INDEX] + pest_factor
                new_pests = bounded_value(new_pests, Field.PEST_NONE, Field.PEST_MAX)
                self.health[i][Field.PEST_LEVEL_INDEX] = new_pests

                #print "Pest Factor[" + str(i) + "] is " + str(pest_factor)

                # Decrease yield if there's not enough nitrogen
                # Set nitrogen level of the field after crops
                new_nitrogen = current_nitrogen - crop_info[get_crop_index(crop_name)][NITROGEN_INDEX]
                #print "New Nitrogen: " + str(new_nitrogen)
                if (new_nitrogen < 0):
                    nitrogen_factor = new_nitrogen / Field.NITROGEN_FALLOW * -100

                new_nitrogen = bounded_value(new_nitrogen, 0, Field.NITROGEN_FULL)
                self.health[i][Field.NITROGEN_LEVEL_INDEX] = new_nitrogen

                #print "Nitrogen Factor[" + str(i) + "] is " + str(nitrogen_factor)

                # TODO: Use bees in calculations.
                final_yield[i] = final_yield[i] - pest_factor - nitrogen_factor

            self.update_history()
            return final_yield

        # Reset the crops for a new year.
        # TODO: keep perennials
        def reset_crops(self, size=MAX_FARM_SIZE):
            self.crops = Crops(size)

        # Update the crop history in preparation for a new year.
        def update_history(self):
            for i in range(0, len(self.crops.items)):
                self.history[i] = [self.crops.items[i]] + self.history[i][0:-1]
            return

        # Return how much work the current field takes
        def get_total_work(self):
            total_work = 0
            for i in range(0, self.crops.len()):
                crop_names = [row[NAME_INDEX] for row in crop_info]
                index = crop_names.index(self.crops[i]) # find the crop's index in crop_info
                total_work += crop_info[index][WORK_INDEX]
            return total_work

        # Return how many calories the current field gives
        def get_total_calories(self):
            total_cals = 0
            for i in range(0, self.crops.len()):
                crop_names = [row[NAME_INDEX] for row in crop_info]
                index = crop_names.index(self.crops[i]) # find the crop's index in crop_info
                total_cals += crop_info[index][CALORIES_INDEX]
            return total_cals

        # Check if the current farm layout is valid.
        # To be valid, we need no crops that would use more nitrogen than is available
        # and we need enough calories.
        # We also need all goats allocated.
        def is_valid_layout(self):
            valid_layout = True
            # Check if this nitrogen is valid
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i]
                nitrogen_usage = crop_info[get_crop_index(current_crop_name)][NITROGEN_INDEX]
                current_nitrogen_level = self.health[i][Field.NITROGEN_LEVEL_INDEX]
                if (nitrogen_usage > current_nitrogen_level):
                    valid_layout = False

            # Check goats
            if (self.crops.count("goats") != crop_info[get_crop_index("goats")][MAXIMUM_INDEX]):
                valid_layout = False

            # Check calories
            total_cals = self.get_total_calories()
            if (total_cals < get_calories_required()):
                valid_layout = False

            return valid_layout

    ##
    # CROPS OBJECT
    ##
    class Crops(renpy.store.object):
        # Initialize as an empty field of a certain size
        def __init__(self, size=MAX_FARM_SIZE):
            self.items = ["fallow"] * size

        # Set the crop at [index] to [crop_name]
        def __setitem__(self, key, value):
            self.items[key] = value

        def __getitem__(self, key):
            return self.items[key]

        def count(self, value):
            return self.items.count(value)

        def len(self):
            return len(self.items)

        # Randomly select from currently available crops, respecting maximums
        def setDefault(self):
            available_crop_names = []
            for i in range(0, len(crop_info)):
                if (crop_info[i][ENABLED_INDEX]):
                    available_crop_names.append(crop_info[i][NAME_INDEX])

            for i in range(0, farm_size):
                crop_name = renpy.random.choice(available_crop_names)
                self[i] = crop_name

                # If we've reached the max, remove this crop from the ones that can be chosen
                # TODO: This is no longer working.
                if (self.items.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX]):
                    available_crop_names.remove(crop_name)
            return

        # Return a random crop from our field
        # If weighted, then you will be more likely to get a crop the more times it is planted.
        def random_crop(self, weighted = True, include_animals = True):
            chosen_crop = ""
            while (chosen_crop == ""):
                if weighted:
                    chosen_crop = renpy.random.choice(self.items)
                else:
                    chosen_crop = renpy.random.choice(list(set(self.items)))
                if (not include_animals):
                    if (chosen_crop == "goats"):
                        chosen_crop = ""

            return chosen_crop


    # Return the index of a crop in crop_info given its name
    def get_crop_index(crop_name):
        crop_names = [row[0] for row in crop_info]
        index = crop_names.index(crop_name) # find the crop's index in crop_info
        return index
