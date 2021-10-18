# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def mmbb_to_float(l):
    new_l = []
    for i in l:
        if i == 'Damages not recorded':
            i == i
        elif 'M' in i:
            i = float(i.strip('M')) * 1000000.0
        elif 'B' in i:
            i = float(i.strip('B')) * 1000000000.0
        new_l.append(i)
    return new_l

damages_clean = mmbb_to_float(damages)
#print(damages_clean)

# write your construct hurricane dictionary function here:
def hurricane_dict(name_list, month_list, year_list, wind_list, area_list, damage_list, death_list):
    hurricanes = {}  
    for i in range(len(name_list)):
        details = {}
        details['Name'] = name_list[i]
        details['Month'] = month_list[i]
        details['Year'] = year_list[i]
        details['Max Sustained Wind'] = wind_list[i]
        details['Areas Affected'] = area_list[i]
        details['Damage'] = damage_list[i]
        details['Death'] = death_list[i]
        hurricanes[name_list[i]] = details
    return hurricanes

hurricane_data = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_clean, deaths)
#print(hurricane_data)

# write your construct hurricane by year dictionary function here:
def hurricane_year(hurricane_dict):
    year_dict = {}
    for name in hurricane_data:
        y = hurricane_data[name]['Year']
        
        if year_dict.get(y) == None:
            l = [hurricane_data[name]]
            year_dict[y] = l
        
        else:
            e = year_dict[y]
            e.append(hurricane_data[name])
            year_dict[y] = e
    return year_dict

hurricane_data_by_year = hurricane_year(hurricane_data)
#print(hurricane_data_by_year)

# write your count affected areas function here:
def count_areas(hurricane_dictionary):
    area_counts = {}
    for hurricane in hurricane_dictionary:
        for area in hurricane_dictionary[hurricane]['Areas Affected']:
            area_counts[area] = area_counts.get(area,0) + 1
    return area_counts

area_counts = count_areas(hurricane_data)
#print(area_counts)

# write your find most affected area function here:
def area_most_affected(area_count_dict):
    maxval = 0
    for key in area_count_dict:
        if area_count_dict[key] > maxval:
            maxval = area_count_dict[key]
            maxkey = key
    return {maxkey : area_count_dict[maxkey]}

area_max = area_most_affected(area_counts)
#print(area_max)

# write your greatest number of deaths function here:
def max_deaths(hurricane_dict):
    maxval = 0
    for hurricane in hurricane_dict:
        if hurricane_dict[hurricane]['Death'] > maxval:
            maxval = hurricane_dict[hurricane]['Death']
            maxkey = hurricane
    return {maxkey : hurricane_dict[maxkey]['Death']}

deadliest = max_deaths(hurricane_data)
#print(deadliest)

# write your catgeorize by mortality function here:
def mortality_categories(h_dict):
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
        
    mort_cat = {'0':list0,'1':list1,'2':list2,'3':list3,'4':list4,'5':list5}
    h_dict = hurricane_data
    
    for hurricane in h_dict:
        deaths = h_dict[hurricane]['Death']
        #print(deaths)
        if deaths <= 0:
            mort_cat[0] = list0.append(h_dict[hurricane])
            #print("added to 0")
        elif deaths <= 100:
            mort_cat[1] = list1.append(h_dict[hurricane])
            #print("added to 1")
        elif deaths <= 500:
            mort_cat[2] = list2.append(h_dict[hurricane])
            #print("added to 2")
        elif deaths <= 1000:
            mort_cat[3] = list3.append(h_dict[hurricane])
            #print("added to 3")
        elif deaths <= 10000:
            mort_cat[4] = list4.append(h_dict[hurricane])
            #print("added to 4")
        elif deaths > 10000:
            mort_cat[5] = list5.append(h_dict[hurricane])
            #print("added to 5")
    return mort_cat

mort = mortality_categories(hurricane_data)
#print(mort['5'])

# write your greatest damage function here:
def greatest_damage(h_dict):
    maxval = 0
    for hurricane in h_dict:
        if type(h_dict[hurricane]['Damage']) == float:
            if h_dict[hurricane]['Damage'] > maxval:
                maxval = h_dict[hurricane]['Damage']
                maxkey = hurricane
    return {maxkey:maxval}

max_damage = greatest_damage(hurricane_data)
#print(max_damage)
            
# write your catgeorize by damage function here:
def damage_categories(h_dict):
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
        
    damage_cat = {'0':list0,'1':list1,'2':list2,'3':list3,'4':list4,'5':list5}
    h_dict = hurricane_data
    
    for hurricane in h_dict:
        damage = h_dict[hurricane]['Damage']
        if damage == 'Damages not recorded':
            damage_cat[0] = list0.append(h_dict[hurricane])
        elif damage <= 100000000:
            damage_cat[1] = list1.append(h_dict[hurricane])
        elif damage <= 1000000000:
            damage_cat[2] = list2.append(h_dict[hurricane])
        elif damage <= 10000000000:
            damage_cat[3] = list3.append(h_dict[hurricane])
        elif damage <= 50000000000:
            damage_cat[4] = list4.append(h_dict[hurricane])
        elif damage > 50000000000:
            damage_cat[5] = list5.append(h_dict[hurricane])
    return damage_cat
damage = damage_categories(hurricane_data)
#print(damage)