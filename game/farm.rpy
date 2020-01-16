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
        PEST_GOAT_REDUCTION = -1.1
        PEST_BEE_REDUCTION = -1.5
        PEST_FALLOW_REDUCTION = -1.5
        PEST_OTHER_CROP_REDUCTION = -5.0
        PEST_MAX = 100
        BEE_BOOST = 15
        HISTORY_SIZE = 3

        NITROGEN_LEVEL_INDEX = 0
        PEST_LEVEL_INDEX = 1
        def __init__(self, current_size, max_size=FARM_SIZE_MAXIMUM):
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
            final_yield = [100] * self.crops.len()
            current_nitrogen = 0
            current_pests = 0
            for i in range(0, self.crops.len()):
                crop_name = self.crops[i]
                current_nitrogen = self.health[i][Field.NITROGEN_LEVEL_INDEX]
                # Decrease yield if there's not enough nitrogen
                # Set nitrogen level of the field after crops
                new_nitrogen = current_nitrogen - crop_info[get_crop_index(crop_name)][NITROGEN_INDEX]
                # print "New Nitrogen: " + str(new_nitrogen)

                new_nitrogen = bounded_value(new_nitrogen, 0, Field.NITROGEN_FULL)
                self.health[i][Field.NITROGEN_LEVEL_INDEX] = new_nitrogen

                pest_factor = 0 # how pests affect yield
                pest_growth = 0 # how much pests increase/decrease this year
                # If pest calculation is on
                # TODO: Set difficulty level? Remove completely?
                if USE_PESTS:
                    current_pests = self.health[i][Field.PEST_LEVEL_INDEX]
                    #print "Crop " + str(i) + " is " + crop_name + " and current_nitrogen: " + str(current_nitrogen) + ", current_pests: " + str(current_pests)
                    # Decrease yield based on randomness and number of times crop has been in that spot lately.
                    # Set pest level of field after crops.
                    if (crop_info[get_crop_index(crop_name)][PERENNIAL_INDEX]):
                        pest_growth = 0
                        pest_factor = 0 # not PEST_NONE because otherwise pests will slowly increase
                    elif (crop_name == "fallow"):
                        pest_growth = current_pests / Field.PEST_FALLOW_REDUCTION
                        pest_factor = 0
                    elif (crop_name == "goats"):
                        pest_growth = current_pests / Field.PEST_GOAT_REDUCTION
                        pest_factor = 0
                    elif (crop_name == "honey"):
                        pest_growth = current_pests / Field.PEST_BEE_REDUCTION
                        pest_factor = 0
                    elif (self.history[i].count(crop_name) == 0):
                        pest_growth = current_pests / Field.PEST_OTHER_CROP_REDUCTION
                        pest_factor = 0
                    else:
                        pest_growth = pest_factor = int(current_pests * renpy.random.random() * (1.5 * self.history[i].count(crop_name)))

                    # Update pests for that field
                    new_pests = self.health[i][Field.PEST_LEVEL_INDEX] + pest_growth
                    new_pests = bounded_value(new_pests, Field.PEST_NONE, Field.PEST_MAX)
                    self.health[i][Field.PEST_LEVEL_INDEX] = new_pests

                    # At most you can lose half your yield from pests
                    pest_factor = bounded_value(pest_factor, 0, Field.PEST_MAX/2)
                    # print "Pest Factor[" + str(i) + "] is " + str(pest_factor) + ", pest_growth= " + str(pest_growth)

                # Bee Calculation
                # Boost what is adjacent - -1 and +1 for horizontal,
                # and -num_columns and +num_columns for vertical
                if (crop_name == "honey"):
                    num_columns = int(self.crops.len()**0.5)
                    # left edge
                    if ((i % num_columns) == 0):
                        indices = [i-num_columns, i+1, i+num_columns]
                    # right edge
                    elif ((i % num_columns) == (num_columns - 1)):
                        indices = [i-num_columns, i-1, i+num_columns]
                    # middle column somewhere
                    else:
                        indices = [i-num_columns, i-1, i+1, i+num_columns]
                    #print "Bee boosting: " + str(indices)
                    for curr_index in indices:
                        # if it's not out of bounds
                        if ((curr_index >= 0) and (curr_index < len(final_yield))):
                            # if it's a pollinated crop
                            if crop_info[get_crop_index(self.crops[curr_index])][POLLINATED_INDEX]:
                                final_yield[curr_index] = final_yield[curr_index] + Field.BEE_BOOST

                # TODO: still runaway pests on perennials...
                # Subtract pests and nitrogen deficiency from final yield
                #print "Pest Factor is " + str(pest_factor)
                final_yield[i] = final_yield[i] - pest_factor

            self.update_history()
            return final_yield

        # Given the percentage yield of each crop square, calculate
        # how much money will be made
        # TODO: tweak this
        def calculate_income(self, crop_yield):
            income = 0
            for i in range(0, self.crops.len()):
                crop_name = self.crops[i]
                crop_value = get_credits_from_value(crop_info[get_crop_index(crop_name)][VALUE_INDEX])
                final_value = (crop_yield[i]/100.0) * crop_value
                print "crop_yield " + str(crop_yield[i]) + " crop_value " + str(crop_value) + " final_value " + str(final_value)
                income += int(final_value)
            return income

        # Reset the crops for a new year.
        def reset_crops(self, size=FARM_SIZE_MAXIMUM):
            new_crops = Crops(size)
            for i in range(0, self.crops.len()):
                crop_index = get_crop_index(self.crops[i])
                crop_name = self.crops[i]
                #print str("resetting crop: " + crop_name)
                if (crop_info[crop_index][PERENNIAL_INDEX]):
                    if (crop_name[-1] != "+"):
                        new_crops[i] = crop_name + "+"

                        # subtract one from the no +
                        crop_info[crop_index][MAXIMUM_INDEX] -= 1

                        # Add one to +
                        plus_index = get_crop_index(new_crops[i])
                        crop_info[plus_index][MAXIMUM_INDEX] += 1
                    else:
                        new_crops[i] = crop_name
            self.crops = new_crops

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

            # Check bees
            if (crop_enabled("honey") and (self.crops.count("honey") != crop_info[get_crop_index("goats")][MAXIMUM_INDEX])):
                valid_layout = True

            # Check calories
            total_cals = self.get_total_calories()
            if (total_cals < get_calories_required(year)):
                valid_layout = False

            return valid_layout

        def low_vitamin_a(self):
            vitA = 0
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i].rstrip("+")
                vitA += VITAMIN_A_CROPS[current_crop_name]
            return (vitA <= VITAMIN_A_LOW)

        def low_vitamin_c(self):
            vitC = 0
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i].rstrip("+")
                vitC += VITAMIN_C_CROPS[current_crop_name]
            return (vitC <= VITAMIN_C_LOW)

        def low_magnesium(self):
            magn = 0
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i].rstrip("+")
                magn += MAGNESIUM_CROPS[current_crop_name]
            return (magn <= MAGNESIUM_LOW)

        def most_frequent_crop(self):
            return self.crops.most_frequent_crop()

    ##
    # CROPS OBJECT
    ##
    class Crops(renpy.store.object):
        # Initialize as an empty field of a certain size
        def __init__(self, size=FARM_SIZE_MAXIMUM):
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
                if (crop_info[i][ENABLED_INDEX] and (crop_info[i][MAXIMUM_INDEX] > 0) and
                (crop_temporarily_disabled != crop_info[i][NAME_INDEX])):
                    available_crop_names.append(crop_info[i][NAME_INDEX])

            for i in range(0, self.len()):
                # If it's a perennial, keep it.
                # Otherwise, fill it randomly
                if (self[i][-1] != "+"):
                    crop_name = renpy.random.choice(available_crop_names)
                    self[i] = crop_name

                    # If we've reached the max, remove this crop from the ones that can be chosen
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
                    if ((chosen_crop == "goats") or (chosen_crop == "honey")):
                        chosen_crop = ""

                # an empty field is not a valid choice
                if (chosen_crop == "fallow"):
                    chosen_crop = ""

            chosen_crop = chosen_crop.rstrip("+")
            return chosen_crop

        def most_frequent_crop(self):
            most_frequent_crop = ""
            most_frequent_count = 0
            for i in range(0, len(self)):
                current_crop_name = self.items[i]
                current_crop_count = self.count(current_crop_name)
                if ((current_crop_count >=  most_frequent_count) and (current_crop_name != "fallow")):
                    most_frequent_crop = current_crop_name
                    most_frequent_count = current_crop_count
            most_frequent_crop = most_frequent_crop.rstrip("+")
            return most_frequent_crop


    # Return the index of a crop in crop_info given its name
    def get_crop_index(crop_name):
        crop_names = [row[0] for row in crop_info]
        index = crop_names.index(crop_name) # find the crop's index in crop_info
        return index

    def get_crop_filename(crop_name):
        return "gui/crop icons/" + crop_name.rstrip("+") + ".png"

    def crop_enabled(crop_name):
        crop_index = get_crop_index(crop_name)
        return crop_info[crop_index][ENABLED_INDEX]

    def enable_crop(crop_name, notify=True):
        crop_index = get_crop_index(crop_name)
        crop_info[crop_index][ENABLED_INDEX] = True
        if (notify):
            renpy.say(tutorial,"You can now grow " + crop_name + " on your farm.")

    def disable_crop(crop_name, notify=True):
        crop_index = get_crop_index(crop_name)
        crop_info[crop_index][ENABLED_INDEX] = False
        if (notify):
            renpy.say(tutorial,"You can no longer grow " + crop_name + " on your farm.")

    # Delete all instances of crop_name in crops
    def delete_crop(crop_name):
        for i in range(0, crops.len()):
            current_crop_name = self.items[i]
            if (current_crop_name == crop_name):
                self.items[i] = "fallow"
