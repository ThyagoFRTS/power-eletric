
def conduit(phases_section, number_cables_per_section):
    area = 0
    for section, number_cables in zip(phases_section, number_cables_per_section):
        area =+ number_cables * (section)/4
    
