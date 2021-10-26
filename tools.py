from nbr_tables import get_conduction_table


def search_in_conduction_table(Ib,Ib1, ft, fg, charged_conductors, installation_method):
    methods, sections = get_conduction_table()
    for electric_current, section in zip(methods[installation_method][charged_conductors],sections):
        current = float(electric_current)
        if current >= Ib1:
            selected_section = section
            if (current*ft*fg < Ib):
                print("Normal conditions, cable with sectinon "+str(selected_section)+" supports "+str(current)+', but with ft and fg, the real capacity is:'+ str(current*ft*fg))
                continue
            #print('Section by Conduction Capacity: ', selected_section)
            break
    return selected_section, current