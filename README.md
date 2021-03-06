# Parkinson Disease Classification
Title: Parkinsons Disease Data Set <br>
Abstract: Oxford Parkinson's Disease Detection Dataset <br>

## Summary of Dataset
Data Set Characteristics: Multivariate <br>
Number of Instances: 197 <br>
Area: Life <br>
Attribute Characteristics: Real <br>
Number of Attributes: 23 <br>
Date Donated: 2008-06-26 <br>
Associated Tasks: Classification <br>
Missing Values? N/A <br>

## Data Set Information:

This dataset is composed of a range of biomedical voice measurements from
31 people, 23 with Parkinson's disease (PD). Each column in the table is a
particular voice measure, and each row corresponds one of 195 voice
recording from these individuals ("name" column). The main aim of the data
is to discriminate healthy people from those with PD, according to "status"
column which is set to 0 for healthy and 1 for PD. <br>
<br>
The data is in ASCII CSV format. The rows of the CSV file contain an
instance corresponding to one voice recording. There are around six
recordings per patient, the name of the patient is identified in the first
column.<br>

## Source:

The dataset was created by Max Little of the University of Oxford, in
collaboration with the National Centre for Voice and Speech, Denver,
Colorado, who recorded the speech signals. The original study published the
feature extraction methods for general voice disorders.


## Attribute Information:

name - ASCII subject name and recording number <br>
MDVP:Fo(Hz) - Average vocal fundamental frequency <br>
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency <br>
MDVP:Flo(Hz) - Minimum vocal fundamental frequency <br>
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several
measures of variation in fundamental frequency <br>
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude <br>
NHR,HNR - Two measures of ratio of noise to tonal components in the voice <br>
status - Health status of the subject (one) - Parkinson's, (zero) - healthy <br>
RPDE,D2 - Two nonlinear dynamical complexity measures <br>
DFA - Signal fractal scaling exponent <br>
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation <br>

## Reference
'Exploiting Nonlinear Recurrence and Fractal Scaling Properties for Voice Disorder Detection', <br>
Little MA, McSharry PE, Roberts SJ, Costello DAE, Moroz IM. <br>
BioMedical Engineering OnLine 2007, 6:23 (26 June 2007) <br>
