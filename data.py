import pandas as pd
data = pd.read_csv('all_secure_8.csv')

data_dict = {} #column name meanings
data_dict['anon_id'] = 'anonimized patient identifier'
data_dict['gender'] = 'male of female'
data_dict['age_radiation_start'] = '?age at which radiation was started'
data_dict['bmi'] = 'body mass index'
data_dict['smoking_now'] = 'smoking_now'
data_dict['pack_years'] = 'pack years'
data_dict['kps'] = '?A standard way of measuring the ability of cancer patients to perform ordinary tasks ranging from 0 to 100 where higher scores mean the patient is better able to carry out daily activities.'
data_dict['hgb_baseline'] = '?baseline hemoglobin level'
data_dict['charlson_age'] = '?Charlson Age-Comorbidity Index (CACI) Charlson et al. 1994 Charlson Age-Comorbidity Index (CACI) Scores 0 point. Each decade of age ≥50 years is equivalent to a 1-point increase in comorbidity (ie, 50–59 years=1 point; 60–69 years=2 points).' 
# i think that this may need to be removed as it is (maybe linearly) correlated with age?
data_dict['total_points'] = '?'
data_dict['cci'] = '?CCI771 A drug used to treat advanced renal cell carcinoma (a type of kidney cancer).'
data_dict['pet_scan'] = '?pet scan done or not?'
data_dict['side'] = '?'
data_dict['impac_diagnosis'] = '?'
data_dict['central'] = '?central'
data_dict['ct_size_cm'] = '?ct_size_cm'
data_dict['pet_suv'] = '?'
data_dict['T'] = '?'
data_dict['N'] = '?'
data_dict['M'] = '?'
data_dict['overall_stage'] = '?'
data_dict['biopsy'] = '?'
data_dict['histology'] = '?'
data_dict['if_other'] = ''
data_dict['reason_for_inoperability'] = '?'
data_dict['intent'] = ''
data_dict['total_dose'] = ''
data_dict['fractions'] = ''
data_dict['bed'] = ''
data_dict['motion_control'] = ''
data_dict['delivery_type'] = ''
data_dict['delivery_machine'] = ''
data_dict['planning_system'] = ''
data_dict['heterogeneity_correction'] = ''
data_dict['alive'] = ''
data_dict['months_fu'] = ''
data_dict['months_OS'] = ''
data_dict['months_lc'] = ''
data_dict['months_lobar_failure'] = ''
data_dict['months_nodal_failure'] = ''
data_dict['months_distant_failure'] = ''
data_dict['months_pfs'] = ''
data_dict['Local'] = ''
data_dict['Lobar'] = ''
data_dict['Nodal'] = ''
data_dict['Distant'] = ''
