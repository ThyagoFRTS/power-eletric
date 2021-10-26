from nbr_tables import get_conduction_table

def get_conductor_protection_section(phase_section):
    section = 0
    if phase_section <= 16:
        section = phase_section
        print('Protection: ', section)
    elif phase_section <= 35:
        section = 16
        print('Protection: ', section)

    else:
        _, sections = get_conduction_table()
        section = phase_section/2
        print('Phase/2:', section)
        for selected_section in sections:
            if float(selected_section) >= section:
                section = selected_section
                break
        print('Protection: ', section)
    print('')
    return section