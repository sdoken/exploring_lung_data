from abazeedomics_access import listdir_nohidden
import os
import pandas as pd
import numpy as np
# from data import data, data_dict
# import pandas_profiling
from radiomics import featureextractor
import sys

params = os.path.join('..', 'examples', 'exampleSettings', 'Params.yaml')
extractor = featureextractor.RadiomicsFeaturesExtractor(params)

patient_to_features = {}
def calculate_features(dir_of_patient_dirs = '/Volumes/AbazeedOmics/Shared_HPC/dokens/to_convert/',
        excel_patients_structures ='Users/semihcandoken/code/abazeed/test2.xlsx' ):
    chosen_structure_sheet = pd.read_excel(excel_patients_structures)
    list_of_patients_to_study = list(chosen_structure_sheet['anon_id'])
    chosen_structure_sheet.set_index('anon_id', inplace=True)
    patients_attempted_failed = []
    count = 0
    data = []
    featured_patients = []

    for patient in list_of_patients_to_study:
        structure_name = chosen_structure_sheet.loc[patient, 'chosen_structure']
        try: #  radiomics.extractdir_of_patient_folders + patient + '/' + structure_name)
            maskName = dir_of_patient_dirs + patient + '/structures/' + structure_name
            imageName = dir_of_patient_dirs + patient + '/images.nrrd'
        
            featureVector = extractor.execute(imageName, maskName)
            patient_to_features[patient] = featureVector
            count = count + 1
            print(patient + ' calculated  ' + str(count) + ' out of ' + str(len(list_of_patients_to_study)))
            data.append(list(featureVector.values()))
            featured_patients.append(patient)


        except :
           patients_attempted_failed.append(patient)
           count = count + 1
           print(patient + ' failed')
           # print(patient + ' calculated  ' + str(count) + ' out of ' + str(len(list_of_patients_to_study)))
           continue

    features_df = pd.DataFrame( data, columns = list(featureVector.keys()), index = featured_patients)
      
    return features_df


if __name__ == '__main__':
    print(sys.argv[0])
    features_df = calculate_features(sys.argv[1], sys.argv[2])
    features_df.to_csv('results_4_with_names.csv')
