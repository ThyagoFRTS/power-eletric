from nbr_tables import get_neutral_reduction_table
from nbr_tables import get_fh_factor_table
from nbr_tables import get_conduction_table
from tools import search_in_conduction_table

def get_neutral_section(phase_section, Ib, circuit_type = 'mono', index_THD3 = 0, balanced_circuit = True, installation_method = 'B1', ft=1, fg=1):
    neutral_section = 0
    if circuit_type == 'mono':
        neutral_section = phase_section
        print('Neutral Section: ', phase_section)
    elif circuit_type == 'bi':
        if index_THD3 < 0.33:
            neutral_section = phase_section
            print('Neutral Section: ', phase_section)
            pass
        else:
            data, thd3s = get_fh_factor_table()
            fh = 0
            for factor, thd3 in zip(data['Bi'],thd3s):
                if index_THD3 <= float(thd3):
                    fh = factor
                    break
            print('Harmonic factor selected: ', fh)
            Ib1 = Ib/(ft * fg)
            print('Project current modified: ', Ib * fh)
            print('Current to table: ', Ib1 * fh)
            neutral_section, current = search_in_conduction_table(Ib * fh, Ib1 * fh, ft, fg, '2', installation_method)
            print('Neutral Section: ', neutral_section)
            if fg != 1 or ft !=1:
                print("Normal conditions, cable supports "+str(current)+', but with ft and fg, the real capacity is:'+ str(current*ft*fg))
            
        
    elif circuit_type == 'tri':
        if index_THD3 < 0.15 and balanced_circuit:
            data, sections = get_neutral_reduction_table()
            for section, index in zip(data, data.index):
                if  phase_section <= int(section):
                    neutral_section = sections[index]
                    break
            if neutral_section == 'S':
                neutral_section = phase_section
            print('Neutral Section: ', neutral_section)
        elif index_THD3 < 0.33:
            neutral_section = phase_section
            print('Neutral Section: ', phase_section)
            pass
        else:
            print('THD3 over 33%')
            data, thd3s = get_fh_factor_table()
            fh = 0
            for factor, thd3 in zip(data['Tri'],thd3s):
                if index_THD3 <= float(thd3):
                    fh = factor
                    break 
            print('Harmonic factor selected: ', fh)
            Ib1 = Ib/(ft * fg)
            print('Project current modified: ', Ib * fh)
            print('Current to table: ', Ib1 * fh)
            neutral_section, current = search_in_conduction_table(Ib * fh, Ib1 * fh, ft, fg, '3', installation_method)
            print('Neutral Section: ', neutral_section)
            if fg != 1 or ft !=1:
                print("Normal conditions, cable supports "+str(current)+', but with ft and fg, the real capacity is:'+ str(current*ft*fg))
    else:
        print('Wrog circuit type')
        return -1        

    print('')
    return neutral_section