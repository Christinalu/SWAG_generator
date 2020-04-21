
import nltk
import nltk.corpus
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

virus_ref = ['covid-19', 'coronavirus', 'cov-2', 'sars-cov-2', 'sars-cov', 'hcov', '2019-ncov']
symptoms = ['weight loss','chills','shivering','convulsions','deformity','discharge','dizziness','vertigo','fatigue','malaise','asthenia','hypothermia','jaundice','muscle weakness','pyrexia','sweats','swelling','swollen','painful lymph node','weight gain','arrhythmia','bradycardia','chest pain','claudication','palpitations','tachycardia','dry mouth','epistaxis','halitosis','hearing loss','nasal discharge','otalgia','otorrhea','sore throat','toothache','tinnitus','trismus','abdominal pain','fever','bloating','belching','bleeding','blood in stool','melena','hematochezia', 'constipation','diarrhea','dysphagia','dyspepsia','fecal incontinence','flatulence','heartburn','nausea','odynophagia','proctalgia fugax','pyrosis','steatorrhea','vomiting','alopecia','hirsutism','hypertrichosis','abrasion','anasarca','bleeding into the skin','petechia','purpura','ecchymosis and bruising','blister','edema','itching','laceration','rash','urticaria','abnormal posturing','acalculia','agnosia','alexia','amnesia','anomia','anosognosia','aphasia and apraxia','apraxia','ataxia','cataplexy','confusion','dysarthria','dysdiadochokinesia','dysgraphia','hallucination','headache','akinesia','bradykinesia','akathisia','athetosis','ballismus','blepharospasm','chorea','dystonia','fasciculation','muscle cramps','myoclonus','opsoclonus','tic','tremor','flapping tremor','insomnia','loss of consciousness','syncope','neck stiffness','opisthotonus','paralysis and paresis','paresthesia','prosopagnosia','somnolence','abnormal vaginal bleeding','vaginal bleeding in early pregnancy', 'miscarriage','vaginal bleeding in late pregnancy','amenorrhea','infertility','painful intercourse','pelvic pain','vaginal discharge','amaurosis fugax','amaurosis','blurred vision','double vision','exophthalmos','mydriasis','miosis','nystagmus','amusia','anhedonia','anxiety','apathy','confabulation','depression','delusion','euphoria','homicidal ideation','irritability','mania','paranoid ideation','suicidal ideation','apnea','hypopnea','cough','dyspnea','bradypnea','tachypnea','orthopnea','platypnea','trepopnea','hemoptysis','pleuritic chest pain','sputum production','arthralgia','back pain','sciatica','Urologic','dysuria','hematospermia','hematuria','impotence','polyuria','retrograde ejaculation','strangury','urethral discharge','urinary frequency','urinary incontinence','urinary retention']
organs = ['mouth','teeth','tongue','salivary glands','parotid glands','submandibular glands','sublingual glands','pharynx','esophagus','stomach','small intestine','duodenum','Jejunum','ileum','large intestine','liver','Gallbladder','mesentery','pancreas','anal canal and anus','blood cells','respiratory system','nasal cavity','pharynx','larynx','trachea','bronchi','lungs','diaphragm','Urinary system','kidneys','Ureter','bladder','Urethra','reproductive organs','ovaries','Fallopian tubes','Uterus','vagina','vulva','clitoris','placenta','testes','epididymis','vas deferens','seminal vesicles','prostate','bulbourethral glands','penis','scrotum','endocrine system','pituitary gland','pineal gland','thyroid gland','parathyroid glands','adrenal glands','pancreas','circulatory system','Heart','patent Foramen ovale','arteries','veins','capillaries','lymphatic system','lymphatic vessel','lymph node','bone marrow','thymus','spleen','tonsils','interstitium','nervous system','brain','cerebrum','cerebral hemispheres','diencephalon','the brainstem','midbrain','pons','medulla oblongata','cerebellum','the spinal cord','the ventricular system','choroid plexus','peripheral nervous system','nerves','cranial nerves','spinal nerves','Ganglia','enteric nervous system','sensory organs','eye','cornea','iris','ciliary body','lens','retina','ear','outer ear','earlobe','eardrum','middle ear','ossicles','inner ear','cochlea','vestibule of the ear','semicircular canals','olfactory epithelium','tongue','taste buds','integumentary system','mammary glands','skin','subcutaneous tissue']

# test_text = """The covid 19 gives weight loss. And also chills. Maybe some mouth
# pain. Salivary glands pain. Salivary glands ijsofjsef"""

def stem_preprocess(sym_list, organs_list):
    
    ps = nltk.PorterStemmer()
    stemmed_sym = []
    stemmed_organs = []
    for sym in sym_list:
        sym = ps.stem(sym)
        stemmed_sym.append(sym)

    for org in organs_list:
        org = ps.stem(org)
        stemmed_organs.append(org)
        
    return stemmed_sym, stemmed_organs 

def symptom_frequency_list(text, symp_list):

    ps = nltk.PorterStemmer()
    sent_token = nltk.sent_tokenize(text)
    sym_freq_list = {}
    for sent in sent_token:
        for sym in symp_list:
            if re.search(sym, sent.lower()):
                if sym not in sym_freq_list.keys():
                    sym_freq_list[sym] = 1
                else:
                    sym_freq_list[sym] += 1
            else:
                continue
    return sym_freq_list
            
def organs_frequency_list(text, organ_list):

    ps = nltk.PorterStemmer()
    sent_token = nltk.sent_tokenize(text)
    org_freq_list = {}
    for sent in sent_token:
        for org in organ_list:
            if re.search(org,sent.lower()):
                if org not in org_freq_list.keys():
                    org_freq_list[org] = 1
                else:
                    org_freq_list[org] += 1
            else:
                continue

    return org_freq_list


def super_integrated_method(text, sympList, organsList):
    
    stemmed_s , stemmed_o = stem_preprocess(sympList, organsList)
    sym_freq = symptom_frequency_list(text,stemmed_s)
    org_freq = organs_frequency_list(text, stemmed_o)

    plot_histogram(sym_freq, org_freq)


def plot_histogram(sym_freq, org_freq):

    plt.subplot(1,2,1)
    plt.bar(sym_freq.keys(),sym_freq.values(),width = 0.8, color = 'skyblue', linewidth = 1.0)
    plt.title("Symptoms Frequency Histogram", loc = 'center')
    plt.xlabel("Symptoms")
    plt.ylabel("Frequency")
    
    plt.subplot(1,2,2)
    plt.bar(org_freq.keys(),org_freq.values(),width = 0.8, color = 'skyblue', linewidth = 1.0)
    plt.title("Organs Frequency Histogram", loc = 'center')
    plt.xlabel("Organs")
    plt.ylabel("Frequency")
    plt.show()

    
def print_analysis(text):
    super_integrated_method(text, symptoms, organs)
    
