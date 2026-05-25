[[PAGE:1]]

 1 / 35 
 Title   1 
Transmission and strate gy analysis of Chikungunya among  demographic groups: Proposing an  2 
optimal control framework based on a vector -borne model 3 
 4 
Authors  5 
Jiahui Li1†, Zeyu Zhao1 2 3†, Jia Rui2 4 5†, Jianguo Zhao1, Qixuan Luo1, Kangguo Li1, Wentao  6 
Song6, Sandra  Perez7 8, Roger F rutos1 2 9 10, Yanhua Su1, Tianxin Xiang6*, Qiuping Chen1 2* ＆ 7 
Tianmu Chen1* 8 
 9 
Affiliations   10 
1 State Key Laboratory of Vaccines for Infectious Diseases, Xiang An Biomedicine  Laboratory, 11 
National Innovation  Platform for Industry ‑Education Integration  in Vaccine Research, School of 12 
Public Health, Xiamen  University, 4221 ‑117 South Xiang’an Road, Xiang’an District, Xiamen 13 
City, Fujian Province  361102,  China ;  14 
2 CIRAD, URM 17, Intertryp, Montpellier, France ;  15 
3 WorldPop, Scho ol of Geography and Environmental Science, University of Southampton, 16 
Southampton, UK;  17 
4 Department of Epidemiology and Health Statistics, Xiangya School of Public Health, Central 18 
South ; 19 
5 Aix-Marseille University, IHU Méditerranée -Infection, Marseille, France ; 20 
6 Jiangxi Provincial Key Laboratory of Prevention and Treatment of Infectious Diseases, Jiangxi 21 
Medical Center for Critical Public Health Events, The First Affiliated Hospital, Jiangx i Medical 22 
College, Nanchang University, Nanchang, China ; 23 
7 University Nice Côte d'Azur, UMR 7300 ESPACE, France ; 24 
8 Universitas AIRLANGGA (UNAIR), Department of Epidemiology, Biostatistics, Population 25 
Studies and Health Promotion, Faculty of Public Health, Indonesia ; 26 
9 Department of Pathology, Faculty of Medicine -Ramathibodi Hospital, Mahidol University, 27 
Bangkok, Thailand ; 28 
10 Department of Health, Faculty of Vocational Studies, Universitas Airlangga, Surabaya, 29 
Indonesia ; 30 
† These authors contributed equally:  Jiahui Li; Zeyu Zhao ; Jia Rui . 31 
* Correspondence:  Tianmu Chen , chentianmu@xmu.edu.cn ; Qiuping Chen,  32 
chenqp241@xmu.edu.cn ; Tianxin Xiang , ndyfy02258@ncu.edu.cn . 33 
 34 
Abstract  35 
The global spread of chikungunya in 2025, driven by climate warming, has increased the 36 
difficulty of controlling tropical mosquito -borne diseases. To enhance the precision of 37 
interventions, this study developed an age - and sex -structured human -mosquito interaction 38 
dynamic model and established an analytical framework for optimizing control strategies. The 39 
framework was empirically validated using data from the largest chikungunya ou tbreak in China 40 
in 2025. Decomposition of the reproduction number identified asymptomatic males aged 15 –59 41 
years as the core transmission group. Optimal control analysis indicates that mosquito population 42 
suppression should be prioritized as a universal st rategy, although its weaker effectiveness in 43 
females aged 60+ requires attention. The study further confirmed that asymmetric intensity 44 
combinations, such as “10%/90%/90%” or “60%/80%/90%”, can effectively control outbreaks. 45 
This research elucidates popula tion-specific transmission patterns and key intervention pathways, 46 
providing a theoretical and strategic foundation for the precise control of mosquito -borne 47 
diseases.  48 
 49 
MAIN  TEXT  50 

[[PAGE:2]]

 2 / 35 
  51 
Introduction  52 
Chikungunya fever (CHIK) is an acute infectious disease caused by the chikungunya virus 53 
(CHIKV) and transmitted through the bites of  Aedes  mosquitoes, primarily  Aedes 54 
aegypti  and Aedes albopictus  [1-2]. The disease has an incubation period typically ranging from 3 55 
to 7 days.  The general population is susceptible to CHIKV, and infection is thought to confer 56 
long-lasting immunity. Sources of transmission include acute -phase patients, asymptomatic 57 
individuals, and virus -carrying mosquitoes, with most patients remaining contagiou s within the 58 
first week symptom onset  (3). In 2025, a local clustered outbreak of CHIK, triggered by imported 59 
cases, occurred again in Foshan City, Guangdong Province, representing the largest epidemic 60 
event of its kind recorded in China to date.  In the early stage of the outbreak, the local 61 
government responded promptly by issuing "A Letter to All Citizens" on July 18, calling for 62 
public participatio n in mosquito prevention and control activities. This announcement marked the 63 
official transition from routine prevention and control measures to an emergency response state, 64 
initiating a comprehensive containment phase.  65 
By the end of 2024, more than 110 c ountries had reported local or imported cases of CHIK. 66 
In the first seven months of 2025 alone, over 240,000 cases and 90 deaths were recorded globally 67 
(4). Modeling studies project a long -term global average annual infection risk of 0.012 (95% UI: 68 
0.007 –0.019), corresponding to approximately 14.4 million (95% UI: 11.0 –17.8 million) annual 69 
infections worldwide (5), underscoring both the persistent transmission pressure and the urgency 70 
of control efforts.  As a region with extensive distribution of  Aedes alb opictus  and prolonged 71 
mosquito activity seasons, China possesses natural conditions conducive to rapid virus spread, 72 
facing a long -term potential risk of "imported cases triggering local transmission." Since the first 73 
imported case from Sri Lanka was detec ted in 2008 (6), a total of 61 CHIK public health 74 
emergencies were reported nationwide from 2010 to 2019, 56 of which involved single imported 75 
cases  (7). However, local clustered outbreaks —such as those in Dongguan, Guangdong in 2010 76 
(8) and Ruili, Yunnan in 2019 (9)—highlight that the risk of indigenous transmission cannot be 77 
overlooked.  78 
Mathematical models play a crucial role in elucidating the transmission dynamics of vector - 79 
borne diseases and guiding  precision control strategies. During the first CHIK outbreak in 80 
Guangdong Province in 2010, simulation studies based on ordinary differential equations 81 
demonstrated that comprehensive interventions focusing on mosquito control were significantly 82 
more effe ctive than strategies relying solely on human -to-mosquito transmission control (10).  In 83 
the early stage of the 2025 outbreak in Foshan, Guangdong, which was triggered by an imported 84 
case and led to local transmission, Zhao et al. (11) employed mathematical modeling to estimate 85 
the basic reprodu ction number as 7.28, indicating extremely high transmission potential. Further 86 
model -based dissection of the transmission chain revealed that the "human -to-mosquito" pathway 87 
contributed substantially more than the "mosquito -to-human" pathway, serving as t he primary 88 
driver of the outbreak. Among different types of infected individuals, symptomatic cases played a 89 
particularly prominent role in transmission. A cohort study on CHIK  outbreaks in Europe 90 
indicated that the 45 –64 age group faces the highest infect ion risk, with female cases consistently 91 
outnumbering males (12). This gender disparity may be linked to differences in social activities, 92 
exposure  opportunities, and immune responses between sexes.  93 
Age- and sex -structured dynamic models have been widely applied in animal population 94 
studies  (13-14), with most models utilizing partial differential equations to characterize 95 
population structure (15-17). In the field of vector -borne diseases, such structured models are also 96 
progressively developing. Forouzannia et al. (18) developed an age -structu red deterministic 97 
model to evaluate the impact of antimalarial drugs on transmission dynamics. Their results 98 
indicated that, in the absence of drug -induced resistance, the model exhibited competitive 99 
exclusion —where Plasmodium  strains with higher basic rep roduction numbers suppressed others, 100 

[[PAGE:3]]

 3 / 35 
 driving them toward extinction. Aimée Uwineza et al. (19) further established a malaria 101 
transmission dynamic m odel incorporating both age and sex structures, highlighting that to 102 
control malaria transmission in Rwanda, it is essential to focus on reducing mosquito biting and 103 
infection rates. They also emphasized the active participation of women in government -led 104 
interventions and strengthening malaria prevention education for children.  Recent modeling 105 
research on CHIK V in Brazil by Cortes -Azuero et al. (20) also indicates that increasing age and 106 
female sex are significant risk factors for symptom occurrence, further underscoring the necessity 107 
of incorporating demographic structure into transmission models.  However, existing research still 108 
shows a deficiency i n simultaneously integrating age and sex structures into CHIK transmission 109 
dynamic models. This gap limits the ability to quantify the specific roles of different demographic 110 
groups in transmission, thereby constraining the development of targeted control strategies.  111 
To address the gaps in existing research, this study proposes an analytical framework for 112 
optimizing prevention and control strategies, building upon prior work. This framework was then 113 
validated and subjected to empirical analysis using data f rom the largest CHIK outbreak recorded 114 
in China. We developed a vector -borne transmission dynamic model that incorporates both age 115 
and sex structures, dividing the total population into multiple subgroups with distinct 116 
epidemiological characteristics. Base d on this model framework, we analytically decomposed the 117 
basic reproduction number to quantitatively assess the heterogeneous contributions of different 118 
sexes, age groups, and infection statuses (symptomatic/asymptomatic) to disease transmission. 119 
Furtherm ore, we introduced optimal control theory to construct a Hamiltonian system with 120 
control variables representing mosquito -to-human transmission control, mosquito population 121 
suppression, and human -to-mosquito transmission control. By numerically solving this  system, 122 
we identified the optimal implementation pathways for each intervention under realistic outbreak 123 
conditions and comprehensively evaluated the effectiveness of different intervention 124 
combinations in controlling epidemic progression.  125 
 126 
 127 
Results   128 
Epid emiological Characteristics  129 
Since the first imported case of CHIK was reported in Foshan City on June 16, 2025, a total 130 
of 9,929 confirmed cases had been recorded by September 18. Among these, 5,171 (52.08%) 131 
were male and 4,758 (47.92%) were female, indica ting a slightly higher proportion of cases 132 
among males (Fig. 1d–e). In terms of age distribution, the 15 –59 age group was the most affected 133 
across both sexes, representing the highest number of infections in each gender subgroup.  134 
Driven by the implementation of control policies, the epidemic progression exhibited distinct 135 
phases and clear intervention -response characteristics (Fig. 1a). The first minor peak in daily 136 
incidence occurred on July 18, with 405 new cases reported. Follow ing the implementation of 137 
containment measures, case numbers were temporarily suppressed . However, after a plateau 138 
period reflecting the incubation lag, infections resurged, reaching a peak of 493 new cases on July 139 
28—the highest daily count recorded durin g the outbreak. Subsequently, the number of new cases 140 
declined consistently, indicating that control measures had gradually taken effect and the outbreak 141 
had entered a phase of effective containment.  142 
Stratified analysis by phase revealed that during the pr eparedness phase (June 16 –July 18), 143 
males accounted for 51.09% of cases. Among all cases in this phase, the 15 –59 age group 144 
constituted 32.46%, making it the predominant demographic, while individuals aged 60 and 145 
above accounted for 11.06%. Females represe nted 48.91% of cases in this phase, with the 15 –59 146 
age group comprising 30.03% of all cases.  After transitioning to the containment phase (July 19 – 147 
September 18), the proportion of male cases slightly increased to 52.39%, with the 15 –59 age 148 
group remaining the most affected, constituting 32.31% of all cases during this period. This 149 

[[PAGE:4]]

 4 / 35 
 pattern highlights the consistently higher exposure risk and disease burden shouldered by the 15 – 150 
59 age group throughout the entire epidemic (Fig. 1b–c). 151 
 152 
Fig. 1 Temporal dynamics and demographic characteristics of the largest recorded CHIK  153 
outbreak in China.  (a) Daily reported cases by containment phase. The timeline is segmented 154 
into distinct phases, annotated with black text and arrows, with colors indicating t emporal 155 
progression. (b–c) Age and sex distribution of incident cases during the preparedness phase (b) 156 
and containment phase (c). (d –e) Daily cases by age group among females (d) and males (e). 157 
Colors represent sex (blue: male; orange: female) and age gro ups (light to dark shades: 0 –14, 15 – 158 
59, and 60+ years, respectively).  159 
 160 
Basic Reproduction Number with Sex -Age Structure  161 
The disease -free equilibrium (DFE)  represented by  162 


[[PAGE:5]]

 5 / 35 
 𝐸0=(𝑆𝑚10,0,0,0,0,𝑆𝑓10,0,0,0,0,…,𝑆𝑚𝑘0,0,0,0,0,𝑆𝑓𝑘0,0,0,0,0,𝑆𝑎0,0,𝑆𝑣0,0,0)1×(10𝑘+5), 163 
in which 𝑁𝑝=∑(𝑆𝑚𝑗0+𝑆𝑓𝑗0)𝑘
𝑗=1  and 𝑁𝑣=𝑆𝑎0+𝑆𝑣0. We calculate d the basic  reproduction  164 
number ℛ0 using the next -generation matrix approach described in (30). The nonlinear terms with 165 
new infection ℱ and the  outflow term 𝒱 are given by  166 
ℱ=
(                 𝛽𝑣𝑝𝐼𝑅𝑅𝑚1𝑆𝑚1𝐼𝑣
𝑁𝑝𝑖
0
0
𝛽𝑣𝑝𝐼𝑅𝑅𝑓1𝑆𝑓1𝐼𝑣
𝑁𝑝
0
0
⋮
𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑘𝑆𝑚𝑘𝐼𝑣
𝑁𝑝
0
0
𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑘𝑆𝑓𝑘𝐼𝑣
𝑁𝑝
0
0
𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝
0 )                 
(6𝑘+2)×1, and 𝒱=
(              𝑞𝜔′𝐸𝑚1+(1−𝑞)𝜔𝐸𝑚1
−(1−𝑞)𝜔𝐸𝑚1+𝛾𝐼𝑚1
−𝑞𝜔′𝐸𝑚1+𝛾′𝐴𝑚1
𝑞𝜔′𝐸𝑓1+(1−𝑞)𝜔𝐸𝑓1
−(1−𝑞)𝜔𝐸𝑓1+𝛾𝐼𝑓1
−𝑞𝜔′𝐸𝑓1+𝛾′𝐴𝑓1
⋮
𝑞𝜔′𝐸𝑚𝑘+(1−𝑞)𝜔𝐸𝑚𝑘
−(1−𝑞)𝜔𝐸𝑚𝑘+𝛾𝐼𝑚𝑘
−𝑞𝜔′𝐸𝑚𝑘+𝛾′𝐴𝑚𝑘
𝑞𝜔′𝐸𝑓𝑘+(1−𝑞)𝜔𝐸𝑓𝑘
−(1−𝑞)𝜔𝐸𝑓𝑘+𝛾𝐼𝑓𝑘
−𝑞𝜔′𝐸𝑓𝑘+𝛾′𝐴𝑓𝑘
(𝑑+𝜛)𝐸𝑣
−𝜆𝐼𝑎− 𝜛𝐸𝑣+𝑑𝐼𝑣)              
(6𝑘+2)×1, 167 
The Jacobian matrice s of ℱ and 𝒱 at the DFE 𝐸0 are 168 
𝐹(𝐸0)=(06𝑘×6𝑘𝐹1
𝐹202×2), 169 
and 170 
𝑉(𝐸0)=(𝑉106𝑘×2
02×6𝑘𝑉2), 171 
respectively , of which  172 
𝐹1=
(              0𝛽𝑣𝑝𝐼𝑅𝑅𝑚1𝑆𝑚10
𝑁𝑝
0 0
0 0
0𝛽𝑣𝑝𝐼𝑅𝑅𝑓1𝑆𝑓10
𝑁𝑝
0 0
0 0
⋮ ⋮
0𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑘𝑆𝑚𝑘0
𝑁𝑝
0 0
0 0
0𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑘𝑆𝑓𝑘0
𝑁𝑝
0 0
0 0)              
6𝑘×2, 𝐹2=11×3𝑘⊗(0𝛽𝑝𝑣𝑆𝑣0
𝑁𝑝𝛽𝑝𝑣𝑆𝑣0
𝑁𝑝
000), 173 

[[PAGE:6]]

 6 / 35 
 𝑉1=𝐼2𝑘⊗(𝑞𝜔′+(1−𝑞)𝜔00
−(1−𝑞)𝜔𝛾0
−𝑞𝜔′0𝛾′), 𝑉2=((𝑑+𝜛)0
− 𝜛𝑑). 174 
Then, the basic reproduction number ℛ0 of model (1) is the spectral radius of the next  175 
generation matrix 𝐹𝑉−1(𝐸0). Direct calculation gives  176 
ℛ0=√ℛ0(𝑣𝑝)×ℛ0(𝑝𝑣), 177 
in which,  178 
ℛ0(𝑣𝑝)=∑(𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗0
𝑁𝑝(1−𝑞)𝜔)𝑘
𝑗=1
[𝑞𝜔′+(1−𝑞)𝜔]𝛾+∑(𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗0
𝑁𝑝𝑞𝜔′)𝑘
𝑗=1
[𝑞𝜔′+(1−𝑞)𝜔]𝛾′179 
+∑(𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗0
𝑁𝑝(1−𝑞)𝜔)𝑘
𝑗=1
[𝑞𝜔′+(1−𝑞)𝜔]𝛾+∑(𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗0
𝑁𝑝𝑖𝑞𝜔′)𝑘
𝑗=1
[𝑞𝜔′+(1−𝑞)𝜔]𝛾′180 
=ℛ0(𝑣𝑝𝐼𝑚)+ℛ0(𝑣𝑝𝐴𝑚)+ℛ0(𝑣𝑝𝐼𝑓)+ℛ0(𝑣𝑝𝐴𝑓), 181 
ℛ0(𝑝𝑣)=𝛽𝑝𝑣𝑆𝑣0
𝑁𝑝𝜛
(𝑑+𝜛)𝑑. 182 
ℛ0(𝑝𝑣) represents the average number of secondary human infections produced by a single 183 
infected mosquito per unit time in a fully susceptible human population. Specifically,  this value 184 
can be disaggregated into the sum of four components: the number of secondary symptomatic 185 
male infections  ℛ0(𝑣𝑝𝐼𝑚), asymptomatic male infections  ℛ0(𝑣𝑝𝐴𝑚), symptomatic female infections  186 
ℛ0(𝑣𝑝𝐼𝑓), and asymptomatic female infections  ℛ0(𝑣𝑝𝐴𝑓). Each of thes e components is further 187 
stratified by  𝑗(𝑗=1,…,𝑘) age groups.  Similarly , ℛ0(𝑝𝑣) represents the average number of 188 
secondary infected mosquitoes produced by a susceptible mosquito, per unit time, through biting 189 
the infect ed population.   190 
 191 
Fig. 2 Demographi c decomposition  and relative risk analysis  of the basic reproduction 192 
number ( 𝓡𝟎) in the largest  CHIK  outbreak in China.  (a) ℛ0 stratified by sex, age group, and 193 
infection status (asymptomatic/symptomatic) across different containment phases. The horizontal 194 
axis represents age groups, the vertical axis indicates time periods, and point size corresponds to 195 


[[PAGE:7]]

 7 / 35 
 ℛ0 values (each hollow ci rcle represents 0.1). (b) Relative risk of other population subgroups 196 
compared to the reference group (asymptomatic males aged 0 –14 years). The solid red line marks 197 
the baseline. The vertical position and area of each circle denote the magnitude of relativ e risk. 198 
Blue and orange colors denote male and female cases, respectively, while light and dark blue 199 
shades represent asymptomatic and symptomatic infections.  200 
In the decomposition analysis of the basic reproduction number, ℛ0 was disaggregated into 201 
two tra nsmission pathways: "human -to-mosquito" and "mosquito -to-human," with their geometric 202 
mean representing the overall ℛ0 of the model (specific values are provided in Table 1). For 203 
demographic analysis, the population was divided into three age groups ( 𝑘 = 3). The "mosquito - 204 
to-human" component was further decomposed into 12 subcomponents, with detailed 205 
contributions illustrated in Fig. 2. 206 
During the preparedness phase, the overall ℛ0 remained at a relatively high level. The 207 
contribution of "human -to-mosquito" transmission was significantly greater than that of 208 
"mosquito -to-human" transmission. The population -wide ℛ0 during this phase was 3.6197, 209 
exceeding 1, indicating a trend of epid emic expansion. In terms of infection status, asymptomatic 210 
individuals contributed more to transmission than symptomatic cases. Among age groups, the 15 – 211 
59 years group played the most prominent role in transmission. The ℛ0 contribution from 212 
asymptomatic in dividuals in this age group reached 0.9929 for males and 0.9183 for females. This 213 
was followed by individuals aged 60 and above, among whom the ℛ0 contribution from 214 
asymptomatic infections was higher in females (0.4102) than in males (0.3383).  215 
During the  containment phase, although "human -to-mosquito" transmission remained 216 
stronger than "mosquito -to-human" transmission, the overall population ℛ0 decreased to 0.8665, 217 
falling below 1. This suggests that control measures were effective and the outbreak was bro ught 218 
under improved control. In this phase, asymptomatic individuals in the 15 –59 years age group 219 
remained the primary contributors to ℛ0, with slightly higher values in males (0.2377) than in 220 
females (0.2199).  When the containment phase was further divide d by the  incubation lag, the 221 
overall model ℛ0 during the lag period was slightly lower than in the subsequent period. Further 222 
decomposition revealed that although "human -to-mosquito" transmission was lower during the 223 
lag period than later, both "mosquito -to-human" transmission and the ℛ0 contribution s across 224 
population subgroups were higher  during the lag period. The analysis also reaffirmed that 225 
asymptomatic individuals aged 15 –59 consistently represented the group with the highest ℛ0 226 
contribution throughout.  227 
Table 1. Contribution of cross -species tr ansmission pathways to the basic reproduction 228 
number ( 𝓡𝟎) in the largest CHIK outbreak in China  229 
Time  𝓡𝟎 𝓡𝟎(𝒗𝒑) 𝓡𝟎(𝒑𝒗) 
11 Jun -18 Jul  10.1235  3.6197  28.3132  
19 Jul -18 Sep  1.386 5 0.8665  2.2185  
19 Jul-25 Jul  1.2934  1.0341  1.6178  
26 Jul -18 Sep  1.3243  0.8122  2.1593  
 230 
HMC -Optimized Strategy Validation  231 
To evaluate the effectiveness of intervention strategies for CHIK, we incorporated  three 232 
distinct control pathways —controlling mosquito -to-human transmission, controlling human -to- 233 
mosquito transmission, and suppressing mosquito populations through net deployment —into 234 
Model (1) as control functions  𝑢(𝑡)=(𝑢1(𝑡),𝑢2(𝑡),𝑢3(𝑡)) (see Table 2). A Hamiltonian system 235 
was formulated to quantitatively assess the optimal initiation timing and imp lementation intensity 236 
of each intervention in controlling the outbreak.  237 
Table 2. Parameterization of Intervention Measures  238 
Intervention pathway  Control function s Parameter adjustment  

[[PAGE:8]]

 8 / 35 
 ① Mosquito -to-human transmission control  𝑢1(𝑡) 𝛽𝑣𝑝≜(1−𝑢1(𝑡))𝛽𝑣𝑝 
② Human -to-mosquito transmission control  𝑢2(𝑡) 𝛽𝑝𝑣≜(1−𝑢2(𝑡))𝛽𝑝𝑣 
③ Mosquito population suppression  𝑢3(𝑡) 𝑁𝑣=(1−𝑢3(𝑡))𝑥𝑁𝑝 
The structure of system by incorporating the above control measures was given below:  239 
{                          𝑑𝑆𝑚𝑗
𝑑𝑡=−(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗𝐼𝑣
𝑁𝑝,
𝑑𝐸𝑚𝑗
𝑑𝑡=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗𝐼𝑣
𝑁𝑝−𝑞𝜔′𝐸𝑚𝑗−(1−𝑞)𝜔𝐸𝑚𝑗,
𝑑𝐼𝑚𝑗
𝑑𝑡=(1−𝑞)𝜔𝐸𝑚𝑗−𝛾𝐼𝑚𝑗,
𝑑𝐴𝑚𝑗
𝑑𝑡=𝑞𝜔′𝐸𝑚𝑗−𝛾′𝐴𝑚𝑗,
𝑑𝑅𝑚𝑗
𝑑𝑡=𝛾𝐼𝑚𝑗+𝛾′𝐴𝑚𝑗,
𝑑𝑆𝑓𝑗
𝑑𝑡=−(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗𝐼𝑣
𝑁𝑝,
𝑑𝐸𝑓𝑗
𝑑𝑡=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗𝐼𝑣
𝑁𝑝−𝑞𝜔′𝐸𝑓𝑗−(1−𝑞)𝜔𝐸𝑓𝑗,
𝑑𝐼𝑓𝑗
𝑑𝑡=(1−𝑞)𝜔𝐸𝑓𝑗−𝛾𝐼𝑓𝑗,
𝑑𝐴𝑓𝑗
𝑑𝑡=𝑞𝜔′𝐸𝑓𝑗−𝛾′𝐴𝑓𝑗,
𝑑𝑅𝑓𝑖𝑗
𝑑𝑡=𝛾𝐼𝑓𝑗+𝛾′𝐴𝑓𝑗,
𝑑𝑆𝑎
𝑑𝑡=𝑎𝑐[(1−𝑢3(𝑡))𝑥𝑁𝑝−𝑛𝐼𝑎]−𝜆𝑆𝑎,
𝑑𝐼𝑎
𝑑𝑡=𝑎𝑐𝑛𝐼𝑎−𝜆𝐼𝑎,
𝑑𝑆𝑣
𝑑𝑡=𝜆𝑆𝑎−(1−𝑢2(𝑡))𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝−𝑑𝑆𝑣,
𝑑𝐸𝑣
𝑑𝑡=(1−𝑢2(𝑡))𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝−(𝑑+𝜛)𝐸𝑣,
𝑑𝐼𝑣
𝑑𝑡=𝜆𝐼𝑎+ 𝜛𝐸𝑣−𝑑𝐼𝑣.                           (2) 240 
Our main objective was to minimize the number of new case s in symptomatic classes and the 241 
costs required  to control epidemic.  Consequently,  the objective functional was defined as  242 
𝐺(𝑢(𝑡))=∫[∑(𝑝𝑚𝑗𝐼𝑚𝑗+𝑝𝑓𝑗𝐼𝑓𝑗)𝑘
𝑗=1 +𝑝𝑘+1
2𝑢12(𝑡)+𝑝𝑘+2
2𝑢22(𝑡)+𝑝𝑘+3
2𝑢32(𝑡)]𝑑𝑡𝑇
0,     (3) 243 
where, t he constants  𝑝𝑚𝑗,𝑝𝑓𝑗,(𝑗=1,…,𝑘) are the weight factors for the symptomatic classes 244 
𝐼𝑚𝑗,𝐼𝑓𝑗,(𝑗=1,…,𝑘), respectively , while 𝑝𝑘+1,𝑝𝑘+2, and 𝑝𝑘+3 are the corresponding cost factors.  245 
The core task was to determine  the optimal controls for  𝑢∗=(𝑢1∗,𝑢2∗,𝑢3∗) based on the Pontryagin 246 
maximum principle, such that  247 
𝐺(𝑢∗)=𝑚𝑖𝑛Θ𝐺(𝑢(𝑡)),                                                     (4) 248 
where, Θ={𝑢(𝑡)∈𝐿3(0,𝑇)|𝑢𝑚𝑖𝑛≤𝑢1(𝑡),𝑢2(𝑡),𝑢3(𝑡)≤𝑢𝑚𝑎𝑥,𝑡∈(0,𝑇)} is the control set , T 249 
is represented the final step size , and 𝐿3(0,𝑇) is the set of integrable functions defined on the 250 
interval (0,𝑇).  251 
To begin solving the optimal problem, we focus ed on the Lagrangian and Hamiltonian for 252 
Eqs. (2) to ( 4). The Lagrangian for the optimal problem is defined as follows:  253 
ℒ=∑(𝑝𝑚𝑗𝐼𝑚𝑗+𝑝𝑓𝑗𝐼𝑓𝑗)𝑘
𝑗=1 +𝑝𝑘+1
2𝑢12(𝑡)+𝑝𝑘+2
2𝑢22(𝑡)+𝑝𝑘+3
2𝑢32(𝑡).               (5) 254 
To find the minimum value of Eq.  (5), we introduce d the Hamiltonian function ℋ defined as 255 
follows:  256 

[[PAGE:9]]

 9 / 35 
 ℋ=𝐿+∑𝜂𝑖𝑓𝑖10𝑘+5
𝑖=1,                                                     (6) 257 
where, 𝑓𝑖 is the right -hand side of the dif ferential Eq.  (2) of the i-th state variable , and 𝜂𝑖 is the 258 
adjoint -vector.  Based on t he existence of an optimal solution for the control problem , the 259 
following  Theorem  1 can be obtained .  260 
Theorem 1  Let 𝑆𝑚𝑗∗,𝐸𝑚𝑗∗,𝐼𝑚𝑗∗,𝐴𝑚𝑗∗,𝑅𝑚𝑗∗,𝑆𝑓𝑗∗,𝐸𝑓𝑗∗,𝐼𝑓𝑗∗,𝐴𝑓𝑗∗,𝑅𝑓𝑗∗,𝑆𝑎∗,𝐼𝑎∗,𝑆𝑣∗,𝐸𝑣∗,𝐼𝑣∗,(𝑗=1,…,𝑘) 261 
represent the state solutions associated with the optimal control measures  𝑢1∗, 𝑢2∗,𝑢3∗ for the 262 
optimum control system stat ed in ( 2) and (3). Then, we derive the adjoint variables 𝜂𝑖(𝑖= 263 
1,…,10𝑘+5) that satisfy:  264 
{                        𝑑𝜂10(𝑗−1)+1
𝑑𝑡=𝜂10(𝑗−1)+1𝐶1𝑚−𝜂10(𝑗−1)+2𝐶1𝑚,
𝑑𝜂10(𝑗−1)+2
𝑑𝑡=𝜂10(𝑗−1)+2[𝑞𝜔′+(1−𝑞)𝜔]−𝜂10(𝑗−1)+3(1−𝑞)𝜔−𝜂10(𝑗−1)+4𝑞𝜔′,
𝑑𝜂10(𝑗−1)+3
𝑑𝑡=−𝑝𝑚𝑗+𝑝𝜂10(𝑗−1)+3𝛾−𝜂10(𝑗−1)+5𝛾+𝜂10𝑘+3𝐶2−𝜂10𝑘+4𝐶2,
𝑑𝜂10(𝑗−1)+4
𝑑𝑡=𝜂10(𝑗−1)+4𝛾′−𝜂10(𝑗−1)+5𝛾′+𝜂10𝑘+3𝐶2−𝜂10𝑘+4𝐶2,
𝑑𝜂10(𝑗−1)+5
𝑑𝑡=0,
𝑑𝜂10(𝑗−1)+6
𝑑𝑡=𝜂10(𝑗−1)+6𝐶1𝑓−𝜂10(𝑗−1)+7𝐶1𝑓,
𝑑𝜂10(𝑗−1)+7
𝑑𝑡=𝜂10(𝑗−1)+7[𝑞𝜔′+(1−𝑞)𝜔]−𝜂10(𝑗−1)+8(1−𝑞)𝜔−𝜂10(𝑗−1)+9𝑞𝜔′,
𝑑𝜂10(𝑗−1)+8
𝑑𝑡=−𝑝𝑓𝑗+𝑝𝜂10(𝑗−1)+8𝛾−𝜂10𝑗𝛾+𝜂10𝑘+3𝐶2−𝜂10𝑘+4𝐶2,
𝑑𝜂10(𝑗−1)+9
𝑑𝑡=𝜂10(𝑗−1)+𝛾′−𝜂10𝑗𝛾′+𝜂10𝑘+3𝐶2−𝜂10𝑘+4𝐶2,
𝑑𝜂10𝑗
𝑑𝑡=0,
𝑑𝜂10𝑘+1
𝑑𝑡=𝜂10𝑘+1𝜆−𝜂10𝑘+3𝜆,
𝑑𝜂10𝑘+2
𝑑𝑡=𝜂10𝑘+1𝑎𝑐𝑛−𝜂10𝑘+2(𝑎𝑐𝑛−𝜆)−𝜂10𝑘+5𝜆,
𝑑𝜂10𝑘+3
𝑑𝑡=𝜂10𝑘+3[𝐶3+𝑑]−𝜂10𝑘+4𝐶3,
𝑑𝜂10𝑘+4
𝑑𝑡=𝜂10𝑘+4(𝑑+𝜛)−𝜂10𝑘+5 𝜛,
𝑑𝜂10𝑘+5
𝑑𝑡=∑[(𝜂10(𝑗−1)+1−𝜂10(𝑗−1)+2)𝐶4𝑚+(𝜂10(𝑗−1)+6−𝜂10(𝑗−1)+7)𝐶4𝑓]𝑘
𝑗=1 +𝜂10𝑘+5𝑑,(7) 265 
with boundary conditions or transversality conditions  266 
𝜂𝑖(𝑇)=0, 267 
where,  268 
𝐶1𝑚=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝐼𝑣
𝑁𝑝,𝐶1𝑓=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝐼𝑣
𝑁𝑝, 269 
𝐶2=(1−𝑢2(𝑡))𝛽𝑝𝑣𝑆𝑣
𝑁𝑝,𝐶3=(1−𝑢2(𝑡))𝛽𝑝𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝, 270 
𝐶4𝑚=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗
𝑁𝑝,𝐶4𝑓=(1−𝑢1(𝑡))𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗
𝑁𝑝. 271 
Moreover, the control measures  𝑢1∗,𝑢2∗,𝑢3∗ are given by  272 

[[PAGE:10]]

 10 / 35 
 {        𝑢1∗(𝑡)=𝑚𝑎𝑥{𝑚𝑖𝑛{𝑢𝑚𝑖𝑛,∑{[𝜂10(𝑗−1)+2−𝜂10(𝑗−1)+1]𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗𝐼𝑣
𝑁𝑝+[𝜂10(𝑗−1)+7−𝜂10(𝑗−1)+6]𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗𝐼𝑣
𝑁𝑝}𝑘
𝑗=1
𝑝𝑘+1},𝑢𝑚𝑎𝑥},
𝑢2∗(𝑡)=𝑚𝑎𝑥{𝑚𝑖𝑛{𝑢𝑚𝑖𝑛,(𝜂10𝑘+4−𝜂10𝑘+3)𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝
𝑝𝑘+1},𝑢𝑚𝑎𝑥},
𝑢3∗(𝑡)=𝑚𝑎𝑥{𝑚𝑖𝑛{𝑢𝑚𝑖𝑛,𝜂10𝑘+1𝑎𝑐𝑥𝑁𝑝
𝑝𝑘+2},𝑢𝑚𝑎𝑥}.273 
(8) 274 
Proof  Based on the Pontryagin maximum principle and the Hamiltonian function (Eq.(6)), the 275 
adjoint equation is obtained as follows : 276 
𝑑𝜂10(𝑗−1)+1
𝑑𝑡=−𝜕𝐻
𝜕𝑆𝑚𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑆𝑚𝑗10𝑘+5
𝑖=1, 277 
𝑑𝜂10(𝑗−1)+2
𝑑𝑡=−𝜕𝐻
𝜕𝐸𝑚𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐸𝑚𝑗10𝑘+5
𝑖=1, 278 
𝑑𝜂10(𝑗−1)+3
𝑑𝑡=−𝜕𝐻
𝜕𝐼𝑚𝑗=−𝑝𝑚𝑗−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐼𝑚𝑗10𝑘+5
𝑖=1, 279 
𝑑𝜂10(𝑗−1)+4
𝑑𝑡=−𝜕𝐻
𝜕𝐴𝑚𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐴𝑚𝑗10𝑘+5
𝑖=1, 280 
𝑑𝜂10(𝑗−1)+5
𝑑𝑡=−𝜕𝐻
𝜕𝑅𝑚𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑅𝑚𝑗10𝑘+5
𝑖=1, 281 
𝑑𝜂10(𝑗−1)+6
𝑑𝑡=−𝜕𝐻
𝜕𝑆𝑓𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑆𝑓𝑗10𝑘+5
𝑖=1, 282 
𝑑𝜂10(𝑗−1)+7
𝑑𝑡=−𝜕𝐻
𝜕𝐸𝑓𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐸𝑓𝑗10𝑘+5
𝑖=1, 283 
𝑑𝜂10(𝑗−1)+8
𝑑𝑡=−𝜕𝐻
𝜕𝐼𝑓𝑗=−𝑝𝑓𝑗−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐼𝑓𝑗10𝑘+5
𝑖=1, 284 
𝑑𝜂10(𝑗−1)+9
𝑑𝑡=−𝜕𝐻
𝜕𝐴𝑓𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐴𝑓𝑗10𝑘+5
𝑖=1, 285 
𝑑𝜂10𝑗
𝑑𝑡=−𝜕𝐻
𝜕𝑅𝑓𝑗=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑅𝑓𝑗10𝑘+5
𝑖=1, 286 
𝑑𝜂10𝑘+1
𝑑𝑡=−𝜕𝐻
𝜕𝑆𝑎=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑆𝑎10𝑘+5
𝑖=1, 287 
𝑑𝜂10𝑘+2
𝑑𝑡=−𝜕𝐻
𝜕𝐼𝑎=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐼𝑎10𝑘+5
𝑖=1, 288 
𝑑𝜂10𝑘+3
𝑑𝑡=−𝜕𝐻
𝜕𝑆𝑣=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝑆𝑣10𝑘+5
𝑖=1, 289 

[[PAGE:11]]

 11 / 35 
 𝑑𝜂10𝑘+4
𝑑𝑡=−𝜕𝐻
𝜕𝐸𝑣=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐸𝑣10𝑘+5
𝑖=1, 290 
𝑑𝜂10𝑘+5
𝑑𝑡=−𝜕𝐻
𝜕𝐼𝑣=−∑𝜂𝑖𝜕𝑓𝑖
𝜕𝐼𝑣10𝑘+5
𝑖=1, 291 
subject to boundary time conditions (i.e. final)  𝜂𝑖(𝑇)=0,𝑖=1,…,10𝑘+5. In order to achieve  292 
the desired problem ( 8), we utilize d the following equations:  293 
𝜕𝐻
𝜕𝑢1=0, 294 
𝜕𝐻
𝜕𝑢2=0, 295 
𝜕𝐻
𝜕𝑢3=0. 296 
By utilizing the property of the control space Θ being in the interior of the control set, we 297 
obtain ed the desired result . 298 
The theoretical framework was applied to analyze the largest recorded CHIK outbreak  in 299 
China. Considering that human interventions cannot completely interrupt transmission, the 300 
control parameters were bounded between  𝑢min=0.2 and 𝑢max=0.8. First, Model (1) was used 301 
to fit infection data from the preparedness phase, stratified into six population groups by sex and 302 
age (male: 0 –14, 15 –59, 60+; female: 0 –14, 15 –59, 60+). Model parameters were estimated using 303 
the PMCMC method (Supplementary Table S2). The estimated parameters were then applied to 304 
Model (2) for fitting the containment phase and numerically solving the control functions. 305 
Goodness -of-fit comparisons indicated that segmenting the containment phase by the incubation 306 
lag significantly improved model performance (Supplementary Fig. S1 and Table S3). 307 
Based on the fitting results of actual epidemic data and the control intensity curves derived 308 
from Eqs. (8) (Supplementary Fig. S1), the analysis reveals that mosquito population suppression 309 
was maintained at the highest intensity ( 𝑢3=0.8) starting from July 19. However, it was also the  310 
first measure to begin decreasing in intensity, gradually declining from September 8 and 311 
remaining at the minimum control level ( 𝑢3=0.2) after September 1 1, with an average intensity 312 
of 𝑢3=0.7086 . In comparison, both mosquito -to-human transmission contr ol and human -to- 313 
mosquito transmission control reached their peak control intensities ( 𝑢1=𝑢2=0.8) on July 20. 314 
Human -to-mosquito transmission control began to gradually decrease from September 13, 315 
dropping to its minimum ( 𝑢2=0.2) by September 1 5, with an average intensity of 𝑢2=0.7444 . 316 
In contrast, mosquito -to-human transmission control started to decline from September 1 5 and 317 
reached its lowest influence level ( 𝑢1=0.2) during September 1 7, with an average intensity of 318 
𝑢1=0.7086 . 319 
 320 
Evaluation of Combination Strategies  321 
In this study, we systematically evaluated the effectiveness of three intervention measures — 322 
mosquito -to-human transmission control, human -to-mosquito transmission control, and mosquito 323 
population suppression —under different implement ation strategies. Using "no intervention" and 324 
"full implementation of all three measures" as reference scenarios, we simulated changes in 325 
infection numbers under single or pairwise combinations of interventions  (Fig. 3). Across all six 326 
population groups, t he effectiveness of the strategies, ranked from highest to lowest, was as 327 
follows: “ mosquito -to-human transmission control + human -to-mosquito transmission control  + 328 
mosquito population suppression ” (Strategy 8)  > “mosquito -to-human transmission control  + 329 
mosquito population suppression ” (Strategy 6) > “human -to-mosquito transmission control  + 330 
mosquito population suppression ” (Strategy 7) > “mosquito population suppression ” (Strategy 4) 331 
> “mosquito -to-human transmission control  + human -to-mosquito transmissi on control ” (Strategy 332 

[[PAGE:12]]

 12 / 35 
 5) > “human -to-mosquito transmission control ” (Strategy 3)  > “mosquito -to-human transmission 333 
control ” (Strategy 2) > “no control ” (Strategy 1). Under the no -intervention scenario, the final 334 
epidemic size was the largest, whereas the combined implementation of all three measures 335 
resulted in the smallest final size, with an average reduction of 95.7586% in infections compared 336 
to the no -intervention scenario. The greatest reduction was observed among males aged 15 –59 337 
years (95.7620%), while the smallest reduction was seen in females aged 0 –14 years (95.7518%).  338 
Among the single -intervention strategies, mosquito population suppression was the most 339 
effec tive, reducing the final epidemic size by an average of 78.4695% (range: 78.4611% – 340 
78.4764%) compared to the no -intervention scenario. This was followed by human -to-mosquito 341 
transmission control, which led to an average reduction of 25.6044% (25.5899% –25.61 02%). 342 
Mosquito -to-human transmission control alone had the lowest impact, with an average reduction 343 
of 17.8302% (17.8170% –17.8365%). In terms of demographic variations, mosquito population 344 
suppression and human -to-mosquito transmission control were most ef fective for males aged 15 – 345 
59 years, whereas mosquito -to-human transmission control performed best for females aged 0 –14 346 
years. All single measures showed the weakest effects for females aged 60 years and above.  347 
Among the two -measure combinations, mosquito -to-human transmission control + mosquito 348 
population suppression was the most effective, reducing the final epidemic size by an average of 349 
81.5226% (81.5135% –81.5285%). This was followed by human -to-mosquito transmission control 350 
+ mosquito population suppre ssion, with an average reduction of 80.7287% (80.7208% – 351 
80.7352%). The combination of mosquito -to-human transmission control + human -to-mosquito 352 
transmission control had the lowest impact, with an average reduction of 35.7960% (35.7772% – 353 
35.7772%), which was  even lower than that of mosquito population suppression alone. In terms 354 
of demographic responses, mosquito -to-human transmission control + mosquito population 355 
suppression and human -to-mosquito transmission control + mosquito population suppression 356 
were mo st effective for males aged 15 –59 years, while mosquito -to-human transmission control + 357 
human -to-mosquito transmission control worked best for females aged 0 –14 years. All two - 358 
measure combinations continued to show the weakest effects for females aged 60 y ears and 359 
above.  360 
Table 3. Design of Intervention Strategy Combinations Based on Transmission Pathway 361 
Analysis  362 
Strategy  Mosquito -to-human 
transmission control 𝒖𝟏 Human -to-mosquito 
transmission control 𝒖𝟐 Mosquito population 
suppression 𝒖𝟑 
Strategy 10 0 0 0 
Strategy 2  HMC -Estimated  0 0 
Strategy 3  0 HMC -Estimated  0 
Strategy 4  0 0 HMC -Estimated  
Strategy 5  HMC -Estimated  HMC -Estimated  0 
Strategy 6  HMC -Estimated  0 HMC -Estimated  
Strategy 7  0 HMC -Estimated  HMC -Estimated  
Strategy 81 HMC -Estimated  HMC -Estimated  HMC -Estimated  
Note:  0 represents the blank control group with no intervention applied to any transmission pathway; 1 
represents the control group where interventions are applied to all transmission pathways at the actually 
observed intensity.  

[[PAGE:13]]

 13 / 35 
  363 
Fig. 3 Simulated infection counts by population group under different control strategies in 364 
the largest recorded CHIK outbreak  in China.  (a–f) Temporal dynamics of infections for six 365 
population groups: males 0 –14 years (a), males 15 –59 years (b), males 60+ years (c), females 0 – 366 
14 years (d), females 15 –59 years (e), and females 60+ years (f). Dark gray bars represent 367 
observed infe ctions. The dark red curve (Strategy 1) represents the no -intervention control group 368 
based on segmented fitting of Model (1), while the dark gray curve (Strategy 8) corresponds to 369 
the actual control group based on segmented fitting of Model (2).  370 
 371 
Dose -Resp onse Effects of Interventions  372 
We conducted parameter sweeps for three control measures —mosquito -to-human 373 
transmission control ( 𝑢1), human -to-mosquito transmission control ( 𝑢2), and mosquito population 374 
suppression ( 𝑢3)—by varying each within the range (0, 1) and systematically evaluated the 375 
impact of 1,331 control combinations on the effective reproduction number ( ℛ𝑒𝑓𝑓). Results 376 
showed that across all scenarios, the ℛ𝑒𝑓𝑓 for the "human -to-mosquito" transmission pathway 377 
(ℛ𝑒𝑓𝑓(𝑝𝑣)) was consistentl y and significantly higher than that for the "mosquito -to-human" 378 
pathway ( ℛ𝑒𝑓𝑓(𝑣𝑝)). 379 
Theoretically, setting any single control parameter to 1 (i.e., implementing extreme -intensity 380 
isolation or vector control) would reduce the overall system ℛ𝑒𝑓𝑓 to zero, achieving complete 381 
transmission interruption. However, such extreme intensity is often impractical in real -world 382 
interventions. To identify feasible control strategies, we fixed one parameter at its actual value 383 
based on empirical data and adjust ed the other two, identifying multiple non -extreme control 384 
combinations capable of reducing ℛ𝑒𝑓𝑓 below 1  (Fig. 4a-c): 385 
 With 𝑢1 fixed at its actual value, settings of ( 𝑢2=0.6, 𝑢3=0.9), (𝑢2= 0.8, 𝑢3=0.8), or ( 𝑢2= 386 
0.9, 𝑢3=0.6) all achieved ℛ𝑒𝑓𝑓=0.9737.  387 
 With 𝑢2 fixed at its actual value, combinations ( 𝑢1= 0.7, 𝑢3=0.9) or (𝑢1= 0.9, 𝑢3=0.7) 388 
reduced ℛ𝑒𝑓𝑓=0.8865.  389 
 With 𝑢3 fixed at its actual value, combinations ( 𝑢1= 0.7, 𝑢2=0.9) or (𝑢1= 0.9, 𝑢2=0.7) 390 
resulted in ℛ𝑒𝑓𝑓=0.9465.  391 


[[PAGE:14]]

 14 / 35 
 All the above outcomes satisfy ℛ𝑒𝑓𝑓< 1, indicating that the outbreak can be effectively controlled.  392 
Further analysis revealed that beyond these threshold combinations, increasing the intensity of 393 
any control measure further reduced ℛ𝑒𝑓𝑓 and enhanced control effect iveness.  394 
Based on the mathematical structure of the basic reproduction number ( ℛ0) and simulation 395 
results, mosquito -to-human transmission control ( 𝑢1) had a relatively limited impact on the 396 
effective reproduction number for human -to-mosquito transmission (ℛ𝑒𝑓𝑓(𝑝𝑣)) (Fig. 4d). 397 
Specifically, when 𝑢2=0.7 and 𝑢3=0.9, or 𝑢2=0.9 and 𝑢3=0.7, ℛ𝑒𝑓𝑓(𝑝𝑣) remained constant at 398 
0.8494 regardless of the value of 𝑢1. Systematically increasing the intensity of any control 399 
measure beyond these combinations furthe r reduced the ℛ𝑒𝑓𝑓(𝑝𝑣) value.  On the other hand, 400 
human -to-mosquito transmission control ( 𝑢2) and mosquito population suppression ( 𝑢3) exhibited 401 
limited influence on the effective reproduction number for mosquito -to-human transmission 402 
(ℛ𝑒𝑓𝑓(𝑣𝑝)) (Fig. 4e). When u₁ reached the actual implementation level, ℛ𝑒𝑓𝑓(𝑣𝑝) could be stably 403 
controlled below 1. Further simulations demonstrated that when either 𝑢2 or 𝑢3 was fixed at its 404 
actual value, increasing 𝑢1 to 0.8 was sufficient to reduce ℛ𝑒𝑓𝑓(𝑣𝑝) to 0.7239, even with 405 
fluctuations in the other parameter. This indicates that transmission within the human population 406 
was effectively contained under such conditions.  407 
Under scenarios where the intensities of all three control measures were adjusted 408 
simult aneously, the study identified multiple asymmetric strategy combinations capable of 409 
reducing ℛ𝑒𝑓𝑓 below the epidemic threshold. Specifically, when the intensity of one measure was 410 
maintained at 0.1 while the other two were set to 0.9, the system ℛ𝑒𝑓𝑓 decreased to 0.9604. 411 
Similarly, when one measure was increased to 0.9 while the other two remained at 0.7, the same 412 
control effect was achieved.  More notably, when the three control intensities were specifically 413 
allocated as 0.6, 0.8, and 0.9 (excluding o ther numerical combinations), the system ℛ𝑒𝑓𝑓 was 414 
further reduced to 0.9055, indicating significant synergistic and complementary effects among the 415 
different interventions.  It is important to highlight that, beyond achieving the control effects 416 
describe d above, further increasing the intensity of any single measure continued to lower the 417 
ℛ𝑒𝑓𝑓 value, demonstrating that each intervention retains potential for continuously enhancing 418 
outbreak control effectiveness.  419 
 420 


[[PAGE:15]]

 15 / 35 
 Fig. 4 Heatmap analysis of the impact of control strategy combinations on the effective 421 
reproduction number ( 𝓡𝒆𝒇𝒇). (a)–(c) Effects on the overall  ℛ𝑒𝑓𝑓 when altering combinations of 422 
the other two control measures while fixing one strategy at its actual im plementation value. (d) 423 
Variation of the human -to-mosquito effective reproduction number ( ℛ𝑒𝑓𝑓(𝑝𝑣)) with changes in 𝑢2 424 
and 𝑢3. (e) Variation of the mosquito -to-human effective reproduction number ( ℛ𝑒𝑓𝑓(𝑣𝑝)) and its 425 
subcomponents with changes in 𝑢1. The axes correspond to the intensities of controlling 426 
mosquito -to-human transmission ( 𝑢1), human -to-mosquito transmission ( 𝑢2), and mosquito 427 
population suppression ( 𝑢3). Each row of subplots employs a different value range and colormap 428 
standard.  429 
 430 
Discussion   431 
This study developed a structural vector -borne model. The model system encompasses two 432 
main populations: the human population, structured using an age - and sex -stratified SEIAR 433 
compartmental framework, and the mosquito population, which includes both larval (aquatic) and 434 
adult stages. The total number o f compartments in the system reaches 10𝑘+5, where 𝑘 435 
represents the number of age groups.  Through theoretical analysis of this high -dimensional 436 
system of ordinary differential equations, the basic reproduction number ( ℛ0) was derived. Its 437 
mathematical str ucture reveals that the transmission contributions from infectious individuals 438 
within the same species combine additively to form ℛ0, whereas the contributions from cross - 439 
species transmission (e.g., between humans and mosquitoes) are represented by their g eometric 440 
mean. This finding elucidates the coupling mechanism governing interspecies transmission from a 441 
dynamical perspective.  442 
Existing studies indicate significant age -specific disparities in the global infection burden of 443 
CHIK. One modeling estimate sug gests approximately 14.4 million annual infections worldwide, 444 
with a relatively higher burden among individuals aged 40 –60 years, while extreme age groups 445 
(e.g., under 10 and over 80 years) exhibit elevated mortality risks (5). Furthermore, a systematic 446 
analysis of European outbreaks also identified the 45 –64 age group as high -risk, with female 447 
cases generally outnumbering males (12). However, our analysis of  the largest CHIK outbreak in 448 
China  reveals a distinct pattern: cases were slightly more prevalent among males than females, 449 
and the 15 –59 age group constituted the most affected population. This discrepancy may be 450 
attributed to the relatively broad age categorization used in the current study, which led to the 15 – 451 
59 group —comprising a large share of the working -age population —dominating the demographic 452 
composition. Additionally, individuals in this age range tend to have wider daily mobility and 453 
greater exposure to mosquito habitats, further elevating their infection risk. Moreover, this study 454 
found that asymptomatic infections within this gr oup contributed substantially to transmission, 455 
suggesting their potential role as key drivers of the outbreak, which may partly explain why this 456 
demographic emerged as the core affected population in the local epidemic.  457 
In the study of intervention strateg ies for vector -borne diseases, although specialized 458 
mathematical models for CHIK remain relatively limited, research on diseases with similar 459 
transmission mechanisms, such as dengue fever, provides an important reference. Existing studies 460 
on vector -borne d isease modeling have indicated that rapid containment can be achieved when 461 
surveillance, research, community engagement, and governance operate as an integrated and 462 
adaptive system (45). Further analysis suggests that vector control is a critical component for 463 
achieving rapid outbreak containment (46), and integrated approaches combining case 464 
management, community protection, and mosquito elimination have been demonstrated as the 465 
optimal strategy for interrupting virus transmission (47-48). The optimal control model developed 466 
in this study, based on the largest CHIK outbreak in China  data, validates these perspectives: the 467 
combined implementation of all three control measures reduced the total number of infections by 468 
an average of 95.7586%, demonstrating the significant advantage of synergistic interventi ons. 469 
Mosquito population suppression, as a core intervention, reached and maintained the highest 470 

[[PAGE:16]]

 16 / 35 
 intensity earliest during the containment phase and, as a single measure, led to an average 471 
reduction in infections of 78.4695%. However, relevant studies have  pointed out that unless 472 
sustained at very high implementation intensity, the effectiveness of vector control measures may 473 
gradually diminish over time, potentially leading to a resurgence of the outbreak during later 474 
phases. Premature reduction in control  intensity may undermine the sustainability of intervention 475 
outcomes (49). 476 
Regarding the synergistic implementation of multiple measures, this study  found that the 477 
dual strategy of "mosquito -to-human transmission control + mosquito population suppression" 478 
was the most effective (reducing infection size by 81.5226%), outperforming other two -measure 479 
combinations and single interventions. This aligns wit h findings from dengue fever research 480 
indicating that "the combined use of mosquito nets and insecticides yields the highest infection 481 
avoidance rate" (49). It is noteworthy that although human -to-mosquito transmission control as a 482 
standalone measure had limited effectiveness (25.6044% reduction), its combination with 483 
mosquito population suppression significantly enhanced overall containment efficacy (80.7287% 484 
reduction). This suggests that multi -pathway transmission blocking is key to improving 485 
intervention quality when resources permit. Furthermore, the effects of different measures varied 486 
across population groups: mosquito population suppression and  human -to-mosquito transmission 487 
control were most effective for males aged 15 –59 years, while mosquito -to-human transmission 488 
control provided better protection for females aged 0 –14 years, indicating that intervention 489 
strategies should be tailored to popul ation -specific behavioral and exposure characteristics.  The 490 
findings support the integration of surveillance -response systems, vector control, and community 491 
engagement into an adaptive framework to facilitate rapid outbreak containment.   492 
In the phase -based  analysis of epidemic control, this study divided the containment period 493 
into incubation lag and post -incubation lag subphases, revealing distinct stage -specific differences 494 
in transmission dynamics. The analysis indicated that the overall effective reprod uction number 495 
(ℛ𝑒𝑓𝑓) during the incubation lag subphase was slightly lower than that in the subsequent 496 
subphase, with both "mosquito -to-human" transmission and population -specific contributions 497 
remaining relatively low in the earlier subphase. It is noteworthy that asymptomatic individuals 498 
aged 15 –59 years consistently served as the core transmission group across both subphases, 499 
underscoring their pivotal role in outbreak control.  These findings align with transmission models 500 
that incorporate time -delay effects (50), suggesting that the transmission delay induced by the 501 
incubation period should be fully considered in intervention assessments. The  study further 502 
revealed that during the post -incubation lag subphase, the overall system ℛ𝑒𝑓𝑓 was 1.3243 —still 503 
above the epidemic threshold —yet the "mosquito -to-human" transmission intensity (0.8122) had 504 
fallen below 1, indicating a potential gradual de cline in human transmission. However, the 505 
"human -to-mosquito" transmission intensity remained elevated at 2.1593, reflecting persistent 506 
viral activity in mosquito populations and a continued risk of outbreak resurgence.  507 
To effectively contain the spread of  the outbreak, this study systematically evaluated the 508 
effectiveness of different control strategies, demonstrating that multiple non -extreme control 509 
combinations could reduce ℛ𝑒𝑓𝑓 below the epidemic threshold. When fixing one intervention at 510 
its actual  implementation level while optimizing the other two, effective strategies consistently 511 
achieved ℛ𝑒𝑓𝑓<1 across scenarios: with u₁ fixed, combinations such as ( 𝑢2=60%, 𝑢3=90%), 512 
(𝑢2=80%, 𝑢3=80%), or ( 𝑢2=90%, 𝑢3=60%) yielded ℛ𝑒𝑓𝑓=0.9737; with u₂ f ixed, combinations 513 
like (u₁=70%, u₃=90%) reduced ℛ𝑒𝑓𝑓 to 0.8865; and with 𝑢3 fixed, configurations such as 514 
(𝑢1=70%, 𝑢2=90%) lowered ℛ𝑒𝑓𝑓 to 0.9465. Further analysis revealed distinct pathway -specific 515 
effects: mosquito -to-human transmission control  (𝑢1) exhibited limited influence on human -to- 516 
mosquito transmission ( ℛ𝑒𝑓𝑓(𝑝𝑣)), which remained stable at 0.8494 when 𝑢2 and 𝑢3 were set to 517 
70% and 90% respectively, whereas mosquito -to-human transmission ( ℛ𝑒𝑓𝑓(𝑣𝑝)) was primarily 518 
controlled by 𝑢1, reaching 0.7239 when its intensity attained 80% even under variations in the 519 

[[PAGE:17]]

 17 / 35 
 other measures. When simultaneously adjusting all three interventions, specific asymmetric 520 
intensity allocations —such as single -measure intensity at 10% paired with dual -measure  intensity 521 
at 90%, or a triple -measure profile of 60%/80%/90% —achieved ℛ𝑒𝑓𝑓 values as low as 0.9055. 522 
All control measures demonstrated continuous effectiveness enhancement, where increasing 523 
intensity beyond baseline levels consistently yielded further r eduction in transmission risk.  524 
This study has several limitations. First, with the recent approval and rollout of the world's 525 
first CHIK vaccine, Ixchiq, by the U.S. FDA in 2023 and its subsequent authorization in multiple 526 
countries (51), vaccination has become an important intervention strategy. However, the model 527 
developed in this study only considers non -pharmaceutical interventions and does not in corporate 528 
the role of immunization strategies within the overall control framework.  Second, the current 529 
model does not fully account for the potential impact of climate change on mosquito distribution 530 
and virus transmission. Studies have shown that global warming and altered precipitation patterns 531 
are significantly expanding the suitable habitats for  Aedes  mosquitoes (52-54), increasing 532 
transmission risks in temperate regions (55). Yet, the present model does not integrate 533 
meteorological variables to reflect this dynamic process.  Furthermore, the model inadequately 534 
addresses the role of human mobility. In the context of globalization, international travel and  535 
cross -regional movement accelerate virus spread (56-57). However, the model is primarily based 536 
on local transmission dynamics and does not systematically analyze the impact of imported cases 537 
on local outbreaks.  Future research should aim to integ rate vaccination strategies, climate 538 
variables, and human mobility data, combined with genomic approaches, to establish a more 539 
comprehensive risk assessment framework.  540 
 541 
Methods  542 
Structural Vector -born e Model development  543 
This study developed an age - and sex -structured human -vector transmission dynamic model 544 
for CHIK. The human population is stratified into 10𝑘 compartments, where  𝑘 denotes the 545 
number of age groups. Specifically, for each age group  𝑗 (𝑗=1 ,…,𝑘), the model includes the 546 
following compartments:  547 
 𝑆𝑚𝑗/𝑆𝑓𝑗: Susceptible males / females in age group  𝑗; 548 
 𝐸𝑚𝑗/𝐸𝑓𝑗: Exposed males / females in age group  𝑗; 549 
 𝐼𝑚𝑗/𝐼𝑓𝑗: Symptomatically infectious males / females in age group  𝑗; 550 
 𝐴𝑚𝑗/𝐴𝑓𝑗: Asymptomatically infectious males / females in age group  𝑗; 551 
 𝑅𝑚𝑗/𝑅𝑓𝑗: Recovered males / females in age group  𝑗. 552 
And, t he vector component comprises five compartments:  553 
 𝑆𝑎: Susceptible larval mosquitoes  ; 554 
 𝐼𝑎: Infected larval mosquitoes  ; 555 
 𝑆𝑣: Susceptible adult mosquitoes ; 556 
 𝐸𝑣: Exp osed adult mosquitoes ; 557 
 𝐼𝑣: Infectious adult mosquitoes . 558 
The model is based on the following assumptions:  559 
Ⅰ. CHIKV  transmission occurs exclusively through cross -species interactions, specifically 560 
between vectors and humans (vector -to-human or human -to-vector). Direct human -to-human or 561 
vector -to-vector transmission is not considered.  562 
Ⅱ. The effective transmission rate varies across age and sex groups. The rate for the first 563 
male age group (𝑚1), denoted as  𝛽𝑣𝑝, serves as the baseline. The effec tive transmission rates for 564 
all other groups are derived by multiplying this baseline by the corresponding Incidence Rate 565 
Ratio (IRR)  (Supplementary Table  S1). 566 
Ⅲ. Upon infection, susceptible individuals enter a latent period during which they are not 567 
infec tious. Subsequently, with probability  𝑞, they progress after an average latency period of 1
ω′ to 568 

[[PAGE:18]]

 18 / 35 
 become asymptomatic infections, eventually recovering at a rate 𝛾′. Alternatively, with 569 
probability (1−𝑞), they undergo a latency period of 1
𝜔 to become symp tomatically infectious, 570 
then recover at rate 𝛾. 571 
Ⅳ. A proportion  (𝑛) of mosquitoes acquire the virus through vertical transmission, 572 
influenced by the per capita birth rate of mosquitoes (𝑎). This process is modulated by a seasonal 573 
effect factor (𝑐), making the  effective vertical transmission rate  𝑎∙𝑐∙𝑛. Infected larval 574 
mosquitoes then develop into infectious adult mosquitoes after an average emergence period of 1
𝜆, 575 
gaining the ability to transmit the virus.  576 
Ⅴ. Newly reproduced larval mosquitoes, except thos e vertically infected, enter the 577 
susceptible larval  mosquito compartment. They develop into susceptible adult mosquitoes  after an 578 
average emergence period of 1
𝜆. Susceptible adult mosquitoes acquire the virus by biting infectious 579 
humans, entering the expo sed class. After an average extrinsic incubation period of 1
𝜛, they 580 
transition to the infectious class, capable of transmitting the virus.  581 
The model defines the total human population as  582 
𝑁𝑝=∑(𝑆𝑚𝑗+𝐸𝑚𝑗+𝐼𝑚𝑗+𝐴𝑚𝑗+𝑅𝑚𝑗+𝑆𝑓𝑗+𝐸𝑓𝑗+𝐼𝑓𝑗+𝐴𝑓𝑗+𝑅𝑓𝑗)𝑘
𝑗=1, 583 
and the total mosquito population as:  584 
𝑁𝑣=𝑆𝑎+𝐼𝑎+𝑆𝑣+𝐼𝑣+𝑅𝑣=𝑥∙𝑁𝑝. 585 
For simplicity in subsequent computations, 𝑁𝑝is treated as constant based on its demographic 586 
interpretation.  Furthermore,  the seasonal effect function is defined a s: 587 
𝑐≜𝑐(𝑡)=𝑐𝑜𝑠(𝑡−𝜏
𝑇). 588 
The model structure is illustrated in Fig . 5, and the corresponding system of equations is 589 
given as follows:  590 

[[PAGE:19]]

 19 / 35 
 {                          𝑑𝑆𝑚𝑗
𝑑𝑡=−𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗𝐼𝑣
𝑁𝑝,
𝑑𝐸𝑚𝑗
𝑑𝑡=𝛽𝑣𝑝𝐼𝑅𝑅𝑚𝑗𝑆𝑚𝑗𝐼𝑣
𝑁𝑝−𝑞𝜔′𝐸𝑚𝑗−(1−𝑞)𝜔𝐸𝑚𝑗,
𝑑𝐼𝑚𝑗
𝑑𝑡=(1−𝑞)𝜔𝐸𝑚𝑗−𝛾𝐼𝑚𝑗,
𝑑𝐴𝑚𝑗
𝑑𝑡=𝑞𝜔′𝐸𝑚𝑗−𝛾′𝐴𝑚𝑗,
𝑑𝑅𝑚𝑗
𝑑𝑡=𝛾𝐼𝑚𝑗+𝛾′𝐴𝑚𝑗,
𝑑𝑆𝑓𝑗
𝑑𝑡=−𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗𝐼𝑣
𝑁𝑝,
𝑑𝐸𝑓𝑗
𝑑𝑡=𝛽𝑣𝑝𝐼𝑅𝑅𝑓𝑗𝑆𝑓𝑗𝐼𝑣
𝑁𝑝−𝑞𝜔′𝐸𝑓𝑗−(1−𝑞)𝜔𝐸𝑓𝑗,
𝑑𝐼𝑓𝑗
𝑑𝑡=(1−𝑞)𝜔𝐸𝑓𝑗−𝛾𝐼𝑓𝑗,
𝑑𝐴𝑓𝑗
𝑑𝑡=𝑞𝜔′𝐸𝑓𝑗−𝛾′𝐴𝑓𝑗,
𝑑𝑅𝑓𝑖𝑗
𝑑𝑡=𝛾𝐼𝑓𝑗+𝛾′𝐴𝑓𝑗,
𝑑𝑆𝑎
𝑑𝑡=𝑎𝑐(𝑁𝑣−𝑛𝐼𝑎)−𝜆𝑆𝑎,
𝑑𝐼𝑎
𝑑𝑡=𝑎𝑐𝑛𝐼𝑎−𝜆𝐼𝑎,
𝑑𝑆𝑣
𝑑𝑡=𝜆𝑆𝑎−𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝−𝑑𝑆𝑣,
𝑑𝐸𝑣
𝑑𝑡=𝛽𝑝𝑣𝑆𝑣∑(𝐼𝑚𝑗+𝐼𝑓𝑗+𝐴𝑚𝑗+𝐴𝑓𝑗)𝑘
𝑗=1
𝑁𝑝−(𝑑+𝜛)𝐸𝑣,
𝑑𝐼𝑣
𝑑𝑡=𝜆𝐼𝑎+ 𝜛𝐸𝑣−𝑑𝐼𝑣.                                        (1) 591 

[[PAGE:20]]

 20 / 35 
  592 
Fig. 5 Compartmental structure of the CHIK V transmission model.  593 
 594 
Data and Parameter Collection  595 
The data for this study were sourced from the 2025 CHIK outbreak records released by the 596 
World Health Organization (WHO) (21) and relevant literature  (22). To conduct an in -depth 597 
analysis of transmission heterogeneity and intervention effectiveness across population groups, 598 
Foshan City was selected as the study site due to its experience with the largest local outbreak in 599 
Asia during 2025. As a typical area with active  Aedes  mosquito populations, its vector ecology 600 
and climatic conditions are representative of southern China and even Sou theast Asia. Moreover, 601 
the city's epidemic data are systematic and complete, effectively reflecting human infection 602 
patterns in a vector -borne transmission context.  603 


[[PAGE:21]]

 21 / 35 
  604 
Fig. 6 Geographic distribution of suspected and confirmed CHIK cases and deaths reported 605 
to WHO or shared publicly by national ministries of health by region, as of September 2025.  606 
(a) Burden distribution map by region: color intensity represents case severity, while pie charts 607 
show the proportion of suspected versus confirmed cases within each region. (b)–(d) Statistics of 608 
confirmed cases, suspected cases, and deaths by region, respectively.  609 
During data preprocessing, the epidemic time series was constructed bas ed on the date of 610 
symptom onset. According to the available structured data, all cases were stratified by sex (male, 611 
female) and age group (children and adolescents: 0 –14 years; adults: 15 –59 years; older adults: 612 
≥60 years). According to the key phases of the outbreak, the study period was divided into two 613 
main intervals for model fitting: a preparedness phase (16 June –18 July 2025) and a containment 614 
phase (19 July –18 September 2025). To account for transmission characteristics, the first 7 days 615 
of the cont ainment phase (19 –25 July) were further defined as an incubation lag phase, allowing 616 
assessment of the potential impact of the latent period on outbreak control.  617 
Demographic parameters for the model were derived from population statistics published by 618 
the Foshan Municipal Bureau of Statistics  (23). The parameters IRR were calculated based on the 619 
actual number of infections during the model fitting pe riod. Key transmission parameters, 620 
including 𝛽𝑣𝑝, 𝛽𝑝𝑣, and  𝑥, were estimated using the Particle Markov Chain Monte Carlo 621 
(PMCMC) algorithm  (Supplementary Table  S2). The remaining parameter values were obtained 622 
from published literature. Detailed descriptions, values, and sources of all model parameters are 623 
provided in Table 4. 624 
Table 4. Definition and value of parameters in the transmission dynamics model  625 
Parameters  Definition  Unit  Value  Range  Source  
𝛽𝑣𝑝 Effective transmission rate from 
mosquitoes to human s 1 - 0-1 Fitting  
𝛽𝑝𝑣 Effective transmission rate from 
human s to mosquito  1 - 0-1 Fitting  
𝑥 The ratio of mosquitoes to 
human s total number  1 - 5-15 Fitting  
𝑎 Per capita birth rate of 
mosquitoes  Day-1 0.145  0.02-0.27 Ref. (24-25) 


[[PAGE:22]]

 22 / 35 
 𝜏 Simulation delay in the initial 
time in the whole season day  Day 30 - Estimation  
𝑇 Duration of the daily cycle  Day 365 - Estimation  
𝑛 The minimum infection rate for 
vertical transmiss ion 1 0.0181  0.0076 -
0.0286  Ref. (26-27) 
𝜆 Rate of mosquito emergence  Day-1 0.0902  0.0691 -
0.1296  Ref. (28) 
𝑑 Natural mortality rate of 
mosquitoes  Day-1 1/7.4  1/9.8 -1/4.5  Ref. (29) 
𝜛 Transition rate of infection in 
mosquitoes from exposed to 
infectious  Day-1 1/5.5  1/8.2 -1/3 Ref. (30-33) 
𝑞 Proportion of exposed 
individuals progressing to 
asymptomatic individuals  1 0.155  0.03-0.28 Ref. (34-35) 
𝜔 Transition rate of exposed 
individuals to the symptomatic 
individuals  Day-1 1/4.5  1/7-0.5 Ref. (34-35) 
𝜔′ Transition rate of exposed 
individuals to the asymptomatic 
individuals  Day-1 1/4.5  1/7-0.5 Ref. (34-35) 
𝛾 Recovery rate of symptomatic 
individuals  Day-1 1/7 - Ref. (36) 
𝛾′ Recovery rate of asymptomatic 
individuals  Day-1 1/7 - Ref. (36) 
 626 
Parameter Estimation  627 
This study employs the Particle Markov Chain Monte Carlo (PMCMC) method to perform 628 
Bayesian inference for the unknown parameter vector 𝜃 in the dynamic model. The PMCMC 629 
framework integrates Particle Filtering (PF) with Markov Chain Monte Carlo (MCMC) sampling, 630 
making it particularly suitable for parameter estimation in state -space models characterized by 631 
partial observational noise and com plex nonlinear dynamics. This approach effectively addresses 632 
the challenge of intractable likelihood evaluation inherent in such models (37). 633 
The methodological foundation lies in reformulating parameter estimation as the exploration 634 
of the posterior distribution  𝑝(𝜃|𝑦1:𝑇), where  𝑦1:𝑇 represents the time -series observational d ata. 635 
According to Bayes’ theorem, the posterior distribution is proportional to the product of the 636 
likelihood function  𝑝(𝑦1:𝑇|𝜃) and the prior distribution  𝑝(𝜃): 637 
𝑝(𝜃|𝑦1:𝑇)∝𝑝(𝑦1:𝑇|𝜃)𝑝(𝜃). 638 
Within this framework, the goodness -of-fit of parameters is define d by their probability density 639 
under the posterior distribution. Regions of higher probability density correspond to parameter 640 
values that are more consistent with prior knowledge and demonstrate better compatibility with 641 
the observed data.  642 

[[PAGE:23]]

 23 / 35 
 The posterior d istribution of parameters is sampled using a constructive Metropolis -Hastings 643 
(M-H) algorithm. This method explores the parameter space sequentially by constructing a 644 
Markov chain whose stationary distribution is the target posterior distribution  (38). At each 645 
iteration  𝑘, a candidate parameter value  𝜃∗ is first generated from a proposal 646 
distribution  𝑞(𝜃|𝜃(𝑘−1)), typically configured as a Gaussian random walk. To evaluate this 647 
candidate, a particle filter is invoked to compute its corresponding marginal likelihood 648 
estimate  𝑝̂(𝑦1:𝑇|𝜃∗). The particle filter sequentially approximates the filtering distribution of the 649 
latent states by maintaining a set of weighted particles  {𝑥𝑡(𝑖),𝑤𝑡(𝑖)}
𝑖=1𝑁
, ultimately providing an 650 
unbiased estimate of the marginal likelihood:  651 
𝑝̂(𝑦1:𝑇|𝜃)=∏(𝑁−1∑𝑤𝑡(𝑖)𝑁
𝑖=1)𝑇
𝑡=1. 652 
This estimate is embedded within the MCMC sampler, linking parameters to the observed data 653 
and driving the e xploration of the parameter space.  654 
Based on the output of the particle filter, the algorithm performs an accept -reject step to 655 
update the parameters. The acceptance probability  𝛼 for the candidate point  𝜃∗ is determined by:  656 
𝛼=𝑚𝑖𝑛{1,𝑝̂(𝑦1:𝑇|𝜃∗)𝑝(𝜃∗)
𝑝̂(𝑦1:𝑇|𝜃𝑘−1)𝑝(𝜃𝑘−1),𝑞(𝜃(𝑘−1)|𝜃∗)
𝑞(𝜃∗|𝜃(𝑘−1))}. 657 
This mechanism ensures that the Markov chain visits regions of higher posterior probability with 658 
frequency proportional to their probability density. After a predefined burn -in period, the 659 
sequence of samples  {𝜃(𝑘)} generated by the Markov chain can be regarded as an approximation 660 
of independent and identically distributed samples from the target posterior distribution. Finally, 661 
based on this sample set, statistical inference and uncertainty quantification of the p arameter 662 
values are completed by calculating the posterior mean  E[𝜃|𝑦1:𝑇] or posterior mode as a point 663 
estimate, and using quantiles to construct credible intervals (39). 664 
 665 
Optimal Control  666 
This study first analyzed the key factors influencing epidemic transmission based on the 667 
global regional disease burden data up to September 2025 (Supplementary  Text). Building on 668 
this, and focusing on human -controllable interventions, we developed an intervention 669 
transmission dynamics model that incorporates both human population and vector structural 670 
features. The model targets three critical pathways: blocking mosq uito-to-human transmission, 671 
controlling human -to-mosquito transmission, and suppressing the mosquito population. Guided 672 
by Pontryagin's Maximum Principle (40), we formulated an optimal control theoretical model, 673 
establishing an analytical framework for optimizing disease control strategies (Fig. 7). 674 
To validate this framework, we selected the largest CHIK outbreak recorded in China —the 675 
2025 Foshan ep idemic —as a case study for empirical analysis. The Hamiltonian Monte Carlo 676 
(HMC) method was employed to derive both analytical and numerical solutions for control 677 
strategies within the human -mosquito transmission system, enabling a systematic evaluation of  678 
the effectiveness of different intervention combinations. The theoretical core of this method lies 679 
in constructing a Hamiltonian function, which transforms the original optimal control problem 680 
into solving a coupled system of state and costate equations. This process identifies the optimal 681 
control variables that minimize the predefined objective function (41-42). 682 

[[PAGE:24]]

 24 / 35 
  683 
Fig. 7 Framework for analyzing intervention optimal disease control strategie s. 684 
The Hamiltonian function integrates the state equations, costate variables (Lagrange 685 
multipliers), and the integrand of the objective function as follows:  686 
ℋ(𝑥,𝜆,𝑢,𝑡)=𝐿(𝑥(𝑡),𝑢(𝑡),𝑡)+𝜆𝑇(𝑡)×𝑓(𝑥(𝑡),𝑢(𝑡),𝑡), 687 
where  𝑥(𝑡) represents the vector of state variables,  𝑢(𝑡) denotes the control variables to be 688 
determined,  𝐿(⋅) corresponds to the integrand (running cost) of the objective 689 
function,  𝑓(⋅) describes the system dynamics, and  𝜆(𝑡) refers to the costate variables (also known 690 
as adjoint variables), with  𝑡=0,…,𝑇. According to Pontryagin’s Maximum Principle, the 691 
optimal control  𝑢∗(𝑡) must minimize (or maximize) the Hamiltonian  ℋ over the entire time 692 
horizon. By taking the partial derivative of  ℋ with respect to the control variable  𝑢 and setting it 693 
to zero, i.e.,  694 
∂ℋ
∂𝑢=0, 695 
an explicit expression for the optimal control exists and can be derived as a function of the state 696 
variables  𝑥(𝑡) and costate variables  𝜆(𝑡), yielding  𝑢∗=𝑢∗(𝑥,𝜆) (43-44). 697 
Solving the aforementioned optimal control system requires simultaneously satisfying both 698 
the state equations and the costate equations. The state equation  699 
𝑥̇=𝑓(𝑥,𝑢,𝑡), 700 
is integrated forw ard in time with the initial condition  𝑥(0)=𝑥0, while the costate equation  701 
𝜆̇=−∂ℋ
∂𝑥, 702 


[[PAGE:25]]

 25 / 35 
 is integrated backward with the terminal condition  𝜆(𝑇)=0. To numerically solve this coupled 703 
system, we employ the forward -backward sweep method, which iteratively perf orms the 704 
following steps:  First, given the current estimate of the control variables, the state equations are 705 
integrated forward to obtain the state trajectory ; Second, using the current state trajectory, the 706 
costate equations are integrated backward to determine the costate trajectory ; Finally, the control 707 
variables are updated according to the Hamiltonian minimization condition  𝑢∗=𝑢∗(𝑥,𝜆). 708 
To ensure algorit hm stability and convergence, a relaxation update strategy is introduced:  709 
𝑢𝑛𝑒𝑤=(1−𝜔)𝑢𝑜𝑙𝑑+𝜔𝑢𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑡𝑒𝑑 , 710 
where  𝜔∈(0,1) is the relaxation (or damping) factor. The updated control variables are then 711 
projected onto the admissible control set  𝑈 (e.g.,  𝑢min≤𝑢(𝑡)≤𝑢max), which essentially 712 
implements a form of the projected gradient method.  The iteration continues until the relative 713 
change in the control variables falls below a preset tolerance or the maximum number of 714 
iterations is reached.  715 
 716 
References  717 
1. Bartholomeeusen, K., Daniel, M. & LaBeaud, D. A.  et al. Chikungunya fever.  Nat. Rev. Dis. 718 
Primers  9, 17 (2023).  719 
2. Vairo, F., Haider, N. & Kock, R.  et al . Chikungunya: epidemiology, pathogenesis, clinical 720 
features, management, and prevention.  Infect. Dis. Clin. North Am.  33, 1003 –1025 (2019).  721 
3. Powers, A. M. & Logue, C. H. Changing patterns of chikungunya virus: re -emergence of a 722 
zoonotic arbovirus.  J. Gen. Virol.  88, 2363 –2377 (2007).  723 
4. European Centre for Disease Prevention and Control (ECDC). Ch ikungunya virus disease 724 
worldwide overview. Available from:  https://www.ecdc.europa.eu/en/chikungunya - 725 
monthly  (cited 13 Nov 2025).  726 
5. Kang, H., Lim, A. & Auzenbergs, M.  et al . Globa l, regional and national burden of 727 
chikungunya: force of infection mapping and spatial modelling study.  BMJ Glob. Health  10, 728 
e018598 (2025).  729 
6. Lin, B. L., Xie, D. Y . & Zhai, J. Q.  et al. Investigation of confirmed cases with chikungunya 730 
fever in Dongguan.  J. Sun Yat -sen Univ.: Med. Sci. Ed.  32, 208 –212 (2011).  731 
7. Chen, B., Chen, Q. L. & Li, Y .  et al. Epidemiological characteristics of imported chikungunya 732 
fever cases in China, 2010 –2019.  Dis. Surveill.  36, 539 –543 (2021).  733 
8. Wu, D., Wu, J. & Zhang, Q.  et al . Chikun gunya outbreak in Guangdong Province, China, 734 
2010.  Emerg. Infect. Dis.  18, 493 –495 (2012).  735 
9. Yin, X., Hu, T. S. & Zhang, H.  et al. Emergent chikungunya fever and vertical transmission in 736 
Yunnan Province, China, 2019.  Arch. Virol.  166, 1455 –1462 (2021).  737 
10. Zhao,  J., Liu, R. C. & Chen, S. L. et al. A model for evaluation of key measures for control of 738 
chikungunya fever outbreak in China.  Chin. J. Epidemiol.  36, 1253 –1257 (2015).  739 
11. Zhao, Y ., Li, J. & Zhao, Z.  et al. Estimating the transmissibility of the 2025 chikung unya fever 740 
outbreak in Foshan, China: a modelling study.  Infect. Dis. Poverty  14, 106 (2025).  741 
12. Liu, Q., Shen, H. & Gu, L.  et al. Chikungunya virus in Europe: a retrospective epidemiology 742 
study from 2007 to 2023.  PLoS Negl. Trop. Dis.  19, e0012904 (2025).  743 
13. Simoy, M. I., Simoy, M. V . & Canziani, G. A. Herd dynamics age and sex structured model 744 
considering management practices and animal movements among districts. Appl. Math. Model . 745 
96, 53–65 (2021).  746 
14. Mukhopadhyay, S. & Piepho, H. P., Bhattacharya, S. et al. Hier archical Bayesian integrated 747 
modeling of age - and sex -structured wildlife population dynamics. J. Agric. Biol. Environ. Stat.  748 
30, 1068 –1093 (2025).  749 
15. Wu, P., Feng, Z. & Zhang, X. Global dynamics of an age –space structured HIV/AIDS model 750 
with viral load -depen dent infection and conversion rates.  J. Comput. Appl. Math . 412, 114309 751 
(2022).  752 

[[PAGE:26]]

 26 / 35 
 16. Zhang, J., Wang, L. & Jin, Z. Global stability for age -infection -structured human 753 
immunodeficiency virus model with heterogeneous transmission. Infect. Dis. Model . 9, 437 – 754 
457 ( 2024).  755 
17. Huo, J., Huo, Q. & Yuan, R. Threshold dynamics for infection age -structured epidemic models 756 
with spatial diffusion and degenerate diffusion. J. Dyn. Differ. Equ . 37, 251 –296 (2025).  757 
18. Forouzannia, F. & Gumel, A. B. Dynamics of an age -structured two -strain model for malaria 758 
transmission. Appl. Math. Comput . 250, 860 –886 (2015).  759 
19. Uwineza, M. A., Nzabanita, J. & Ngaruye, I.  et al.  A deterministic analysis of an age -sex- 760 
structured model for malaria transmission dynamics. IJID Reg.  13, 100478 (2024).  761 
20. Cortes -Azuero, O., O'Driscoll, M.  & Ribeiro Dos Santos, G.  et al . The epidemiology of 762 
chikungunya virus in Brazil and the potential impact of vaccines: a mathematical modelling 763 
study.  Lancet Infect. Dis.  Published online (2025).  764 
21. World Health Organization (WHO). C hikungunya virus disease – Global situation.  Disease 765 
Outbreak News  (23 Oct 2025). Available from:  https://www.who.int/emergencies/disease - 766 
outbreak -news/item/2025 -DON581  (cited 12 Dec 2025).  767 
22. Zhang, M., Li, Y . & Huang, X. et al . Epidemiological characteristics and transmission 768 
dynamics of the early stage Chikungunya fever outbreak in Foshan City, Guangdo ng Province, 769 
China in 2025. Infect . Dis. Poverty . 14, 93 (2025) . 770 
23. Foshan Municipal Bureau of Statistics. Available 771 
from:  https://www.foshan.gov.cn/gzjg/stjj/tjnj_1110962/  (cited 1 0 Oct 2025).  772 
24. Li, Y . & Liu, L. The impact of Wolbachia on dengue transmission dynamics in an SEI -SIS 773 
model.  Nonlinear Anal. Real World Appl.  62, 103363 (2021).  774 
25. Chitnis, N., Hyman, J. M. & Cushing, J. M. Determining important parameters in the spread 775 
of mala ria through the sensitivity analysis of a mathematical model.  Bull. Math. Biol.  70, 776 
1272 –1296 (2008).  777 
26. Agarwal, A., Bhardwaj, N. & Sharma, S. K.  et al . Evidence of experimental vertical 778 
transmission of emerging novel ECSA genotype of chikungunya virus in Ae des aegypti.  PLoS 779 
Negl. Trop. Dis.  8, e2990 (2014).  780 
27. Honório, N. A., Wiggins, K. & Eastmond, B.  et al . Experimental vertical transmission of 781 
chikungunya virus by Brazilian and Florida Aedes albopictus populations.  Viruses  11, 353 782 
(2019).  783 
28. Cai, X., Li, Z. & L iu, Y .  et al. Effects of temperature, relative humidity, and illumination on 784 
the entomological parameters of Aedes albopictus: an experimental study.  Int. J. 785 
Biometeorol.  67, 687 –694 (2023).  786 
29. Yang, D., Li, C. & Li, M.  et al . Semi -field life -table studies of  Aedes albopictus (Diptera: 787 
Culicidae) in Guangzhou, China.  PLoS One  15, e0229829 (2020).  788 
30. Jourdain, F., Lambert, G. & Roux, J.  et al . Estimating chikungunya virus transmission 789 
parameters and vector control effectiveness highlights key factors to mitigate a rboviral disease 790 
outbreaks.  PLoS Negl. Trop. Dis.  16, e0010259 (2022).  791 
31. Dumont, Y ., Chiroleu, F. & Domerg, C. On a temporal model for the Chikungunya disease: 792 
modeling, theory and numerics.  Math. Biosci.  213, 80–91 (2008).  793 
32. Christofferson, R. C., Chisenhall,  D. M. & Wearing, H. J. et al . Chikungunya viral fitness 794 
measures within the vector and subsequent transmission potential.  PLoS One . 9, e110538 795 
(2014).  796 
33. González -Parra, G. C., Aranda, D. F. & Chen -Charpentier, B.  et al. Mathematical modeling 797 
and characterization of the spread of chikungunya in Colombia.  Math. Comput. Appl.  24, 6 798 
(2019).  799 
34. de Lima Cavalcanti, T. Y . V ., Pereira, M. R. & de Paula, S. O.  et al. A review on chikungunya 800 
virus epidemiology, pathogenesis and current vaccine development.  Viruses 14, 969 (2022).  801 

[[PAGE:27]]

 27 / 35 
 35. Alade, T. O., Alnegga, M. & Olaniyi, S.  et al . Mathematical modelling of within -host 802 
Chikungunya virus dynamics with adaptive immune response.  Model. Earth Syst. Environ.  9, 803 
3837 –3849 (2023).  804 
36. Ribeiro dos Santos, G., Jawed, F. & Mukanda vire, C.  et al. Global burden of chikungunya virus 805 
infections and the potential benefit of vaccination campaigns.  Nat. Med.  31, 2342 –2349 (2025).  806 
37. Andrieu, C., Doucet, A. & Holenstein, R. Particle Markov chain Monte Carlo methods.  J. R. 807 
Stat. Soc. B.  72, 269–342 (2010).  808 
38. Doucet, A. & Johansen, A. M. A tutorial on particle filtering and smoothing: fifteen years later. 809 
in The Oxford Handbook of Nonlinear Filtering  656–704 (Oxford University Press, Oxford, 810 
2011).  811 
39. Gelman, A., Carlin, J. B. & Stern, H. S.  et al. Bayesian Data Analysis  3rd edn (Chapman and 812 
Hall/CRC, Boca Raton, 2013).  813 
40. Zhang, C. R. & Zheng, B. D.  Biomathematics - Dynamic Models, Methods and 814 
Applications  (Science Press, Beijing, 2018).  815 
41. Pontryagin, L. S.  Mathematical Theory of Optimal Processes  (Routle dge, New York, 1987).  816 
42. Lenhart, S. & Workman, J. T.  Optimal Control Applied to Biological Models  (Chapman and 817 
Hall/CRC, Boca Raton, 2007).  818 
43. Area, I., Ndaïrou, F. & Nieto, J. J.  et al. Ebola model and optimal control with vaccination 819 
constraints.  J. Ind. Mana g. Optim.  14, 427 –466 (2018).  820 
44. Tadmon, C. & Kengne, J. N. Mathematical analysis of a model of Ebola disease with control 821 
measures.  Int. J. Biomath.  07, 2250048 (2022).  822 
45. Nama, N., Ma, Y . & Zhou, J.  et al. The outbreak, response, and reflections on the chikung unya 823 
fever epidemic in Foshan City, China.  Glob. Health Res. Policy  10, 59 (2025).  824 
46. Saha, P., Sikdar, G. C. & Ghosh, U. Transmission dynamics and control strategy of single - 825 
strain dengue disease.  Int. J. Dyn. Control  11, 1396 –1414 (2023).  826 
47. Khatua, A. & Kar, T. K. Dynamical behavior and control strategy of a dengue epidemic 827 
model.  Eur. Phys. J. Plus  135, 643 (2020).  828 
48. Abidemi, A. & Peter, O. J. Host -vector dynamics of dengue with asymptomatic, isolation and 829 
vigilant compartments: insights from modelling.  Eur. Ph ys. J. Plus  138, 199 (2023).  830 
49. Sun, H., Koo, J. & Dickens, B. L.  et al. Short -term and long -term epidemiological impacts of 831 
sustained vector control in various dengue endemic settings: a modelling study.  PLoS Comput. 832 
Biol.  18, e1009979 (2022).  833 
50. Raj, M. P., Ve nkatesh, A. & Kumar, K. A.  et al . Dengue transmission model in an age - 834 
structured population using delay differential equations.  Discov. Public Health  22, 91 (2025).  835 
51. Maure, C., Khazhidinov, K. & Kang, H.  et al. Chikungunya vaccine development, challenges, 836 
and pathway toward public health impact.  Vaccine  42, 126483 (2024).  837 
52. Ryan, S. J., Carlson, C. J. & Mordecai, E. A.  et al. Global expansion and redistribution of 838 
Aedes -borne virus transmission risk with climate change.  PLoS Negl. Trop. Dis.  13, e0007213 839 
(2019). 840 
53. Tjaden, N. B., Suk, J. E. & Fischer, D.  et al. Modelling the effects of global climate change on 841 
Chikungunya transmission in the 21st century.  Sci. Rep.  7, 3813 (2017).  842 
54. Kraemer, M. U. G., Reiner, R. C. & Brady, O. J.  et al. Past and future spread of th e arbovirus 843 
vectors Aedes aegypti and Aedes albopictus.  Nat. Microbiol.  4, 854 –863 (2019).  844 
55. European Centre for Disease Prevention and Control (ECDC). Mosquito -borne diseases: an 845 
emerging threat. Available from:  https://www.ecdc.europa.eu/en/publications -data/mosquito - 846 
borne -diseases -emerging -threat  (cited 13 Nov 2025).  847 
56. Abdul -Ghani, R., Fouque, F. & Mahdy, M. A. K.  et al . Multisectoral approach  to address 848 
chikungunya outbreaks driven by human mobility: a systematic review and meta -analysis.  J. 849 
Infect. Dis.  222, S709 –S716 (2020).  850 

[[PAGE:28]]

 28 / 35 
 57. Staples , J. E. & Fischer , M. Chikungunya virus in the Americas --what a vector  borne pathogen 851 
can do.  N Engl J Med . 371(10), 887–9 (2014 ).  852 
 853 
Acknowledgments  854 
This work is supported by the Self -supporting Program of Guangzhou Laboratory 855 
(GZNL2024A01004 and SRPG22 -007), the National Key Research and Development Program of 856 
China (2024YFC2311404), the China Postdoctoral Science  Foundation (K2825002) , the 857 
Postdoctoral Fellowship Program of CPSF (GZC20250516) , and the Prevention and Control of 858 
Emerging and Major Infectious Diseases -National Science and Technology Major Projec t 859 
(2025ZD01900406 ). 860 
 861 
Author contributions  862 
Conceptualizat ion: T. M. C., J. H. L ., Z. Y. Z ., J. R. Investigation:  J. H. L. , Z. Y. Z ., J. R., J. G. 863 
Z., Q. X. L, W. T. S., Q. P. C. Methodology:  J. H. L. , Z. Y. Z ., J. R., S. P., R. F . Software:  J. H. 864 
L., J. G. Z., Q. X. L . Validation: Z. Y. Z ., J. R., K. G. L., S. P., R. F., Y. H. S.,  X. T. X . Writing — 865 
original  draft: J. H. L., J. G. Z., Q. X. L., K. G. L. Writing —review & editing: J. H. L. , Z. Y. Z ., J. 866 
R., S. P., R. F., Y. H. S., Q. P. C., X. T. X., T. M. C. All authors read and approved the final  867 
manuscript.  868 
 869 
Competing interests  870 
The authors declare no competing interests.  871 
 872 
Figures  and Tables  873 

[[PAGE:29]]

 29 / 35 
  874 
Fig. 1 Temporal dynamics and demographic characteristics of the largest recorded CHIK  875 
outbreak in China.  (a) Daily reported cases by containment phase. The t imeline is segmented 876 
into distinct phases, annotated with black text and arrows, with colors indicating temporal 877 
progression. (b–c) Age and sex distribution of incident cases during the preparedness phase (b) 878 
and containment phase (c). (d –e) Daily cases by  age group among females (d) and males (e). 879 
Colors represent sex (blue: male; orange: female) and age groups (light to dark shades: 0 –14, 15 – 880 
59, and 60+ years, respectively).  881 


[[PAGE:30]]

 30 / 35 
  882 
Fig. 2 Demographic decomposition  and relative risk analysis  of the basic reproduction 883 
number ( 𝓡𝟎) in the largest CHIK  outbreak in China.  (a) ℛ0 stratified by sex, age group, and 884 
infection status (asymptomatic/symptomatic) across different containment phases. The horizontal 885 
axis represents age groups, the vertical axis indicat es time periods, and point size corresponds to 886 
ℛ0 values (each hollow circle represents 0.1). (b) Relative risk of other population subgroups 887 
compared to the reference group (asymptomatic males aged 0 –14 years). The solid red line marks 888 
the baseline. The v ertical position and area of each circle denote the magnitude of relative risk. 889 
Blue and orange colors denote male and female cases, respectively, while light and dark blue 890 
shades represent asymptomatic and symptomatic infections.  891 
 892 
Fig. 3 Simulated infect ion counts by population group under different control strategies in 893 
the largest recorded CHIK outbreak in China.  (a–f) Temporal dynamics of infections for six 894 
population groups: males 0 –14 years (a), males 15 –59 years (b), males 60+ years (c), females 0 – 895 


[[PAGE:31]]

 31 / 35 
 14 years (d), females 15 –59 years (e), and females 60+ years (f). Dark gray bars represent 896 
observed infections. The dark red curve (Strategy 1) represents the no -intervention control group 897 
based on segmented fitting of Model (1), while the dark gray curve ( Strategy 8) corresponds to 898 
the actual control group based on segmented fitting of Model (2).  899 
 900 
Fig. 4 Heatmap analysis of the impact of control strategy combinations on the effective 901 
reproduction number ( 𝓡𝒆𝒇𝒇). (a)–(c) Effects on the overall  ℛ𝑒𝑓𝑓 when altering combinations of 902 
the other two control measures while fixing one strategy at its actual implementation value. (d) 903 
Variation of the human -to-mosquito effective reproduction number ( ℛ𝑒𝑓𝑓(𝑝𝑣)) with changes in 𝑢2 904 
and 𝑢3. (e) Variation of the  mosquito -to-human effective reproduction number ( ℛ𝑒𝑓𝑓(𝑣𝑝)) and its 905 
subcomponents with changes in 𝑢1. The axes correspond to the intensities of controlling 906 
mosquito -to-human transmission ( 𝑢1), human -to-mosquito transmission ( 𝑢2), and mosquito 907 
populat ion suppression ( 𝑢3). Each row of subplots employs a different value range and colormap 908 
standard.  909 


[[PAGE:32]]

 32 / 35 
  910 
Fig. 5 Compartmental structure of the CHIK V transmission model.  911 
 912 
Fig. 6 Geographic distribution of suspected and confirmed CHIK cases and deaths reported 913 
to WHO or shared publicly by national ministries of health by region, as of September 2025.  914 
(a) Burden distribution map by region: color intensity represents case severity, while pie charts 915 
show the proportion of suspected versus confirmed cases within each region. (b)–(d) Statistics of 916 
confirmed cases, suspected cases, and deaths by region, respectively.  917 


[[PAGE:33]]

 33 / 35 
  918 
Fig. 7 Framework for analyzing intervention optimal disease control strategies.  919 
 920 
Table 1. Contribution of cross -species transmission pathways to the basic reproduction 921 
number ( 𝓡𝟎) in the largest CHIK outbreak in China  922 
Time  𝓡𝟎 𝓡𝟎(𝒗𝒑) 𝓡𝟎(𝒑𝒗) 
11 Jun -18 Jul  10.1235  3.6197  28.3132  
19 Jul -18 Sep  1.386 5 0.8665  2.2185  
19 Jul-25 Jul  1.2934  1.0341  1.6178  
26 Jul -18 Sep  1.3243  0.8122  2.1593  
 923 
Table 2. Parameterization of Intervention Measures  924 
Intervention pathway  Control function s Parameter adjustment  
① Mosquito -to-human transmission control  𝑢1(𝑡) 𝛽𝑣𝑝≜(1−𝑢1(𝑡))𝛽𝑣𝑝 
② Human -to-mosquito transmission control  𝑢2(𝑡) 𝛽𝑝𝑣≜(1−𝑢2(𝑡))𝛽𝑝𝑣 
③ Mosquito population suppression  𝑢3(𝑡) 𝑁𝑣=(1−𝑢3(𝑡))𝑥𝑁𝑝 
 925 
Table 3. Design of Intervention Strategy Combinations Based  on Transmission Pathway 926 
Analysis  927 
Strategy  Mosquito -to-human 
transmission control 𝒖𝟏 Human -to-mosquito 
transmission control 𝒖𝟐 Mosquito population 
suppression 𝒖𝟑 


[[PAGE:34]]

 34 / 35 
 Strategy 
10 0 0 0 
Strategy 
2 HMC -Estimated  0 0 
Strategy 
3 0 HMC -Estimated  0 
Strategy  
4 0 0 HMC -Estimated  
Strategy 
5 HMC -Estimated  HMC -Estimated  0 
Strategy 
6 HMC -Estimated  0 HMC -Estimated  
Strategy 
7 0 HMC -Estimated  HMC -Estimated  
Strategy 
81 HMC -Estimated  HMC -Estimated  HMC -Estimated  
 928 
Table 4. Definition and value of parameters in the transmission dynamics model  929 
Parameters  Definition  Unit  Value  Range  Source  
𝛽𝑣𝑝 Effective transmission rate from 
mosquitoes to human  1 - 0-1 Fitting  
𝛽𝑝𝑣 Effective transmission rate from 
human to mosquito  1 - 0-1 Fitting  
𝑥 The ratio of mosquitoes to human 
total number  1 - 5-15 Fitting  
𝑎 Per capita birth rate of mosquitoes  Day-
1 0.145  0.02-0.27 Ref. (24-
25) 
𝜏 Simulation delay in the initial time in 
the whole season day  Day 30 - Estimation  
𝑇 Duration of the daily cycle  Day 365 - Estimation  
𝑛 The minimum infection rate for 
vertical transmiss ion 1 0.0181  0.0076 -
0.0286  Ref. (26-
27) 
𝜆 Rate of mosquito emergence  Day-
1 0.0902  0.0691 -
0.1296  Ref. (28) 
𝑑 Natural mortality rate of mosquitoes  Day-
1 1/7.4  1/9.8 -
1/4.5  Ref. (29) 
𝜛 Transition rate of infection in 
mosquitoes from exposed to 
infectious  Day-
1 1/5.5  1/8.2 -1/3 Ref. (30-
33) 

[[PAGE:35]]

 35 / 35 
 𝑞 Proportion of exposed individuals 
progressing to asymptomatic 
individuals  1 0.155  0.03-0.28 Ref. (34-
35) 
𝜔 Transition rate of exposed individuals 
to the symptomatic individuals  Day-
1 1/4.5  1/7-0.5 Ref. (34-
35) 
𝜔′ Transition rate of exposed individuals 
to the asymptomatic individuals  Day-
1 1/4.5  1/7-0.5 Ref. (34-
35) 
𝛾 Recovery rate of symptomatic 
individuals  Day-
1 1/7 - Ref. (36) 
𝛾′ Recovery rate of asymptomatic 
individuals  Day-
1 1/7 - Ref. (36) 