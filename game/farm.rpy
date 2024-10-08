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

                # If we have a composting outhouse, and this square lost nitrogen,
                # then we get a nitrogen bonus.
                if (new_nitrogen < current_nitrogen):
                    if (work8_choice == "improve"):
                        new_nitrogen += 5
                new_nitrogen = bounded_value(new_nitrogen, 0, Field.NITROGEN_FULL)
                self.health[i][Field.NITROGEN_LEVEL_INDEX] = new_nitrogen

                pest_factor = 0 # how pests affect yield
                pest_growth = 0 # how much pests increase/decrease this year
                # If pest calculation is on (which it's not; might cause bugs, no pun intended, or something)               
                # still runaway pests on perennials...
                if USE_PESTS:
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

                if (crop_name == "honey"):
                    boosted_squares = self.get_boosted_squares()
                    for curr_index in boosted_squares:
                        final_yield[curr_index] = final_yield[curr_index] + Field.BEE_BOOST

                # Subtract pests and nitrogen deficiency from final yield
                #print "Pest Factor is " + str(pest_factor)
                final_yield[i] = final_yield[i] - pest_factor

            self.update_history()
            return final_yield

        # Given the percentage yield of each crop square, calculate
        # how much money will be made
        def calculate_income(self, crop_yield):
            income = 0
            for i in range(0, self.crops.len()):
                crop_name = self.crops[i]
                crop_value = get_credits_from_value(crop_info[get_crop_index(crop_name)][VALUE_INDEX])
                final_value = (crop_yield[i]/100.0) * crop_value
                # print "crop_yield " + str(crop_yield[i]) + " crop_value " + str(crop_value) + " final_value " + str(final_value)
                income += roundint(final_value)
            return income

        # Set all crops to fallow except for already-planted perennials
        def clear_crops(self):
            for i in range(0, self.crops.len()):
                crop_index = get_crop_index(self.crops[i])
                crop_name = self.crops[i]
                if (crop_info[crop_index][PERENNIAL_INDEX]):
                    if (crop_name[-1] != "+"):
                        self.crops[i] = "fallow"
                else:
                    self.crops[i] = "fallow"

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
                # keep crop names for next year
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
            total_calories = 0
            boosted_squares = self.get_boosted_squares()
            # Totaling crops attributes
            for i in range(0, self.crops.len()):
                multiplier = 1.0
                if (i in boosted_squares):
                    multiplier += (self.BEE_BOOST/100.0)
                crop_names = [row[NAME_INDEX] for row in crop_info]
                index = crop_names.index(self.crops[i]) # find the crop's index in crop_info
                crop_name = self.crops[i].rstrip("+")
                total_calories += roundint(crop_info[index][CALORIES_INDEX] * multiplier)

            return total_calories

        # Check if the current farm layout is valid.
        # To be valid, we need no crops that would use more nitrogen than is available
        # We also need all goats and bees allocated.
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
            if (crop_enabled("honey") and (self.crops.count("honey") != crop_info[get_crop_index("honey")][MAXIMUM_INDEX])):
                valid_layout = False

            # Check calories
            # if self.low_calories():
            #    valid_layout = False

            return valid_layout

        # If we're checking for vitamins, return if we have enough vitamins.
        # Otherwise, we can't have low vitamins yet
        def low_vitamins(self):
            if (year > NUTRITION_YEAR):
                return (self.low_vitamin_a() or self.low_vitamin_c() or self.low_magnesium())
            else:
                return False

        def low_vitamin_a(self):
            vitA = 0
            boosted_squares = self.get_boosted_squares()
            for i in range(0, self.crops.len()):
                multiplier = 1.0
                if (i in boosted_squares):
                    multiplier += (farm.BEE_BOOST/100.0)
                current_crop_name = self.crops[i].rstrip("+")
                vitA += multiplier * crop_info[get_crop_index(current_crop_name)][VITA_INDEX]
            return (vitA < get_vitamins_required(year))

        def low_vitamin_c(self):
            vitC = 0
            boosted_squares = self.get_boosted_squares()
            for i in range(0, self.crops.len()):
                multiplier = 1.0
                if (i in boosted_squares):
                    multiplier += (farm.BEE_BOOST/100.0)
                current_crop_name = self.crops[i].rstrip("+")
                vitC += multiplier * crop_info[get_crop_index(current_crop_name)][VITC_INDEX]
            return (vitC < get_vitamins_required(year))

        def low_magnesium(self):
            vitM = 0
            boosted_squares = self.get_boosted_squares()
            for i in range(0, self.crops.len()):
                multiplier = 1.0
                if (i in boosted_squares):
                    multiplier += (farm.BEE_BOOST/100.0)
                current_crop_name = self.crops[i].rstrip("+")
                vitM += multiplier * crop_info[get_crop_index(current_crop_name)][VITM_INDEX]
            return (vitM < get_vitamins_required(year))

        def low_calories(self):
            return (self.get_total_calories() < get_calories_required(year))

        def most_frequent_crop(self):
            return self.crops.most_frequent_crop()

        # Return a set of indexes that are currently boosted
        def get_boosted_squares(self):
            indices = set()
            for i in range(0, self.crops.len()):
                crop_name = self.crops[i]
                if (crop_name == "honey"):
                    potential_indices = get_adjacent(i, self.crops.len())
                    for curr_index in potential_indices:
                        # if it's a pollinated crop
                        if crop_info[get_crop_index(self.crops[curr_index])][POLLINATED_INDEX]:
                            indices.add(curr_index)
            return indices

        # Delete all instances of crop_name in crops
        def delete_crop(self, crop_name):
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i]
                if (current_crop_name == crop_name):
                    self.crops[i] = "fallow"

        # Delete the instance of this crop that has the highest nitrogen
        def delete_one_crop(self, crop_name):
            delete_index = -1
            delete_nitro = -Field.NITROGEN_FULL
            for i in range(0, self.crops.len()):
                current_crop_name = self.crops[i]
                if (current_crop_name == crop_name):
                    field_nitro = self.health[i][Field.NITROGEN_LEVEL_INDEX] 
                    if (field_nitro >= delete_nitro):
                        delete_index = i
                        delete_nitro = field_nitro 

            self.crops[delete_index] = "fallow"
            return

        # Calculate how much income we lose if we only get
        # a certain percentage of our crops.
        def income_loss(self, percentage):
            high_yield = [100] * self.crops.len()
            low_yield = [percentage] * self.crops.len()
            difference = self.calculate_income(low_yield) - self.calculate_income(high_yield)
            return difference

        
        def autoPlace(self):
            self.clear_crops()

            # Place goats and honey
            goats_needed = crop_info[get_crop_index("goats")][MAXIMUM_INDEX]
            if (crop_info[get_crop_index("honey")][ENABLED_INDEX]):
                honey_needed = crop_info[get_crop_index("honey")][MAXIMUM_INDEX]
            else:
                honey_needed = 0

            while (goats_needed):
                self.crops[self.min_nitrogen_index()] = "goats"
                goats_needed -= 1

            while (honey_needed):
                self.crops[self.min_nitrogen_index()] = "honey"
                honey_needed -= 1

            available_crop_names = set(self.crops.getAvailableCrops())
            for i in range(0, self.crops.len()):
                crop_name = "beans"
                # If it's a perennial, keep it.
                # Otherwise, fill it with what makes sense
                if (self.crops[i] == "fallow"):
                    if (self.health[i][Field.NITROGEN_LEVEL_INDEX] < 50):
                        crop_name = renpy.random.choice(list(available_crop_names.intersection(["beans", "peanuts"])))
                    elif self.low_vitamin_c():
                        crop_name = renpy.random.choice(list(available_crop_names.intersection(["potatoes", "peppers", "turnips", "broccoli", "spinach", "garlic"])))
                    elif self.low_vitamin_a():
                        crop_name = renpy.random.choice(list(available_crop_names.intersection(["squash", "carrots", "spinach"])))
                    elif self.low_magnesium():
                        crop_name = renpy.random.choice(list(available_crop_names.intersection(["beans", "peanuts"])))
                    elif (self.low_calories()):
                        crop_name = renpy.random.choice(list(available_crop_names.intersection(["wheat", "corn", "onions", "potatoes"])))
                    else:
                        crop_name = "fallow"
                    
                    self.crops[i] = crop_name

                    # If we've reached the max, remove this crop from the ones that can be chosen
                    if (self.crops.items.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX]):
                        available_crop_names.remove(crop_name)

                    # If we have enough calories and nutrition and don't have work left, break out and return
                    if (not self.low_calories() and not self.low_vitamins()):
                    #if (self.get_total_work() >= get_work_available()):
                        return
            return

        # Return the index of the empty square that has the least nitrogen
        def min_nitrogen_index(self):
            min_so_far = 500
            index = 0
            for i in range(0, self.crops.len()):
                if (self.health[i][Field.NITROGEN_LEVEL_INDEX] < min_so_far):
                    if (self.crops[i] == "fallow"):
                        index = i
                        min_so_far = self.health[i][Field.NITROGEN_LEVEL_INDEX]
            return index

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

        def getAvailableCrops(self):
            available_crop_names = []
            for i in range(0, len(crop_info)):
                if (crop_info[i][ENABLED_INDEX] and (crop_info[i][MAXIMUM_INDEX] > 0) and
                (crop_temporarily_disabled != crop_info[i][NAME_INDEX])):
                    available_crop_names.append(crop_info[i][NAME_INDEX])
            return available_crop_names

        # Randomly select from currently available crops, respecting maximums
        def setDefault(self):
            available_crop_names = self.getAvailableCrops()

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
            crops_selection = []

            # Build a list of possible crops
            for curr_crop in self.items:
                if (not include_animals):
                    if not ((curr_crop == "goats") or (curr_crop == "honey") or (curr_crop == "fallow")):
                        crops_selection.append(curr_crop)
                else:
                    if (curr_crop != "fallow"):
                        crops_selection.append(curr_crop)

            # If we have any to choose from, choose randomly.
            if (len(crops_selection) > 0):
                if weighted:
                    chosen_crop = renpy.random.choice(crops_selection)
                else:
                    chosen_crop = renpy.random.choice(list(set(crops_selection)))

                chosen_crop = chosen_crop.rstrip("+")
            else: # otherwise just use the generic word "crops"
                chosen_crop = "crops"
            return chosen_crop

        def most_frequent_crop(self):
            most_frequent_crop = ""
            most_frequent_count = 0
            for i in range(0, len(self.items)):
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
        if (crop_info[crop_index][ENABLED_INDEX]):
            if (crop_info[crop_index][MAXIMUM_INDEX] < 100):
                crop_info[crop_index][MAXIMUM_INDEX] += 1
                if notify:
                    notify_change("{image=gui/crop icons/" + crop_name + ".png} " + crop_name.capitalize() + " + 1!")    
        if (notify and not crop_info[crop_index][ENABLED_INDEX]):
            notify_change("{image=gui/crop icons/" + crop_name + ".png} " + crop_name.capitalize() + " unlocked!")
        crop_info[crop_index][ENABLED_INDEX] = True
        #Check for all crops unlocked achievement
        if (all_crops_unlocked()):
            achieved("Super Farmer")
        return

    def disable_crop(crop_name, notify=True):
        crop_index = get_crop_index(crop_name)        
        if (notify and crop_info[crop_index][ENABLED_INDEX]):
            notify_change("{image=gui/crop icons/" + crop_name + ".png} " + crop_name.capitalize() + " disabled")
        crop_info[crop_index][ENABLED_INDEX] = False
        return
    
    # Check all the crops. If any are disabled, return False. Otherwise, return True.
    def all_crops_unlocked():
        for i in range(0, len(crop_info)):
            if (crop_info[i][NAME_INDEX][-1] != "+"):
                if (not crop_info[i][ENABLED_INDEX]):
                    return False
        return True


    # Return indices of what is 'adjacent' - -1 and +1 for horizontal,
    # and -num_columns and +num_columns for vertical
    def get_adjacent(crop_index, max_size):
        num_columns = 5 #We no longer use the square root. roundint(max_size**0.5)
        # left edge
        if ((crop_index % num_columns) == 0):
            potential_indices = [crop_index-num_columns, crop_index+1, crop_index+num_columns]
        # right edge
        elif ((crop_index % num_columns) == (num_columns - 1)):
            potential_indices = [crop_index-num_columns, crop_index-1, crop_index+num_columns]
        # middle column somewhere
        else:
            potential_indices = [crop_index-num_columns, crop_index-1, crop_index+1, crop_index+num_columns]

        for curr_index in potential_indices[:]: #iterate over a copy of the list to avoid bugs
            # if it's out of bounds, delete it
            if ((curr_index < 0) or (curr_index >= max_size)):
                potential_indices.remove(curr_index)

        return potential_indices
