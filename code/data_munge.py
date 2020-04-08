import pickle

def extract_davis(filename):
  """separate the filename from the data in davis.dat"""
  with open(filename,'r') as davis:
    davis_lines = [line.split('.csv:') for line in davis]
  return davis_lines

def get_index(filename,var_name='UGDS'):
  """get the index of the variable of interest"""
  with open(filename,'r') as file: 
    header = file.readline() 
  header = header.strip().split(',')
  var_index = header.index(var_name)
  return var_index

def extract_var(line, var_index):
  """Extract the var from line (variable at UG_index)"""
  line_split = line.strip().split(',')
  if line_split[var_index] == 'NULL':
    return 'NA'
  else:
    return int(line_split[var_index])

def extract_year(line):
  """extract the year from line"""
  year_str = line[-10:-6]
  return int(year_str)

if __name__=="__main__":
  data_dir = "../data/"
  first_file = data_dir + "CollegeScorecard_Raw_Data/MERGED1996_97_PP.csv"

  UG_index = get_index(first_file)
  davis_lines = extract_davis(data_dir + 'davis.dat')
  UG = [extract_var(dav_rec[1],UG_index) for dav_rec in davis_lines]
  years = [extract_year(dav_rec[0]) for dav_rec in davis_lines]

  removed_missing = [(ugd, yr) for ugd, yr in zip(UG,years) if ugd!="NA"]
  UG, years = [list(a) for a in zip(*removed_missing)]

  munged_file = "Davis_UG.dat"
  with open(data_dir + munged_file,'wb') as mdfile:
    pickle.dump((years,UG), mdfile)


