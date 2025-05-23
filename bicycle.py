import pandas as pd
import itertools
import json

def bikes(excel_file):
    idd = pd.read_excel(excel_file, sheet_name='ID', dtype=str).fillna('')
    g   = pd.read_excel(excel_file, sheet_name='GENERAL', dtype=str).fillna('')
    b   = pd.read_excel(excel_file, sheet_name='1', dtype=str).fillna('')
    w   = pd.read_excel(excel_file, sheet_name='2', dtype=str).fillna('')
    f   = pd.read_excel(excel_file, sheet_name='3', dtype=str).fillna('')
    gr  = pd.read_excel(excel_file, sheet_name='4', dtype=str).fillna('')
    s   = pd.read_excel(excel_file, sheet_name='5', dtype=str).fillna('')
    c   = pd.read_excel(excel_file, sheet_name='6', dtype=str).fillna('')


    model = list(idd['Model number'].unique())
    brakes = list(idd['Brakes'].unique())
    wheels = list(idd['Wheels'].unique())
    frames = list(idd['Frame size'].unique())
    groups = list(idd['Groupset'].unique())
    sus = list(idd['Suspension'].unique())
    col = list(idd['Color'].unique())

    model = [x for x in model if x != '']
    brakes = [x for x in brakes if x != '']
    wheels = [x for x in wheels if x != '']
    frames = [x for x in frames if x != '']
    groups = [x for x in groups if x != '']
    sus = [x for x in sus if x != '']
    col = [x for x in col if x != '']

    b_dict = b.set_index('Brakes').to_dict('index')
    w_dict = w.set_index('Wheels').to_dict('index')
    f_dict = f.set_index('Frame size').to_dict('index')
    g_dict = gr.set_index('Groupset').to_dict('index')
    s_dict = s.set_index('Suspension').to_dict('index')
    c_dict = c.set_index('Color').to_dict('index')

    g_all = g.iloc[0].to_dict()

    combs = itertools.product(model, brakes, wheels, frames, groups, sus, col)

    result = []

    for i in combs:
        m = i[0]
        br = i[1]
        wh = i[2]
        fr = i[3]
        grr = i[4]
        ss = i[5]
        clr = i[6]

        fullid = m + br + wh + fr + grr + ss + clr


        bike = {}
        bike['ID'] = fullid

        for k in g_all:
            bike[k] = g_all[k]
        for k in b_dict[br]:
            bike[k] = b_dict[br][k]
        for k in w_dict[wh]:
            bike[k] = w_dict[wh][k]
        for k in f_dict[fr]:
            bike[k] = f_dict[fr][k]
        for k in g_dict[grr]:
            bike[k] = g_dict[grr][k]
        for k in s_dict[ss]:
            bike[k] = s_dict[ss][k]
        for k in c_dict[clr]:
            bike[k] = c_dict[clr][k]

        if 'Has suspension' in bike:
            if bike['Has suspension'] == '1':
                bike['Has suspension'] = 'TRUE'
            else:
                bike['Has suspension'] = 'FALSE'

        if 'Logo' in bike:
            if bike['Logo'] == '1':
                bike['Logo'] = 'TRUE'
            else:
                bike['Logo'] = 'FALSE'

        result.append(bike)

    with open("output.json", "w") as js:
        json.dump(result, js, indent=4)

bikes("Bicycle.xlsx")



