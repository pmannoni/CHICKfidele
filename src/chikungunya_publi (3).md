# Transmission and Strategy Analysis of Chikungunya Among Demographic Groups: Proposing an Optimal Control Framework Based on a Vector-Borne Model

## Authors

Jiahui Li, Zeyu Zhao, Jia Rui, Jianguo Zhao, Qixuan Luo, Kangguo Li, Wentao Song, Sandra Perez, Roger Frutos, Yanhua Su, Tianxin Xiang, Qiuping Chen & Tianmu Chen

**Correspondence:** Tianmu Chen (chentianmu@xmu.edu.cn); Qiuping Chen (chenqp241@xmu.edu.cn); Tianxin Xiang (ndyfy02258@ncu.edu.cn)

---

## Abstract

The global spread of chikungunya in 2025, driven by climate warming, has increased the difficulty of controlling tropical mosquito-borne diseases. To enhance the precision of interventions, this study developed an age- and sex-structured human-mosquito interaction dynamic model and established an analytical framework for optimizing control strategies. The framework was empirically validated using data from the largest chikungunya outbreak in China in 2025. Decomposition of the reproduction number identified asymptomatic males aged 15–59 years as the core transmission group. Optimal control analysis indicates that mosquito population suppression should be prioritized as a universal strategy, although its weaker effectiveness in females aged 60+ requires attention. The study further confirmed that asymmetric intensity combinations, such as "10%/90%/90%" or "60%/80%/90%", can effectively control outbreaks. This research elucidates population-specific transmission patterns and key intervention pathways, providing a theoretical and strategic foundation for the precise control of mosquito-borne diseases.

---

## Introduction

Chikungunya fever (CHIK) is an acute infectious disease caused by the chikungunya virus (CHIKV) and transmitted through the bites of *Aedes* mosquitoes, primarily *Aedes aegypti* and *Aedes albopictus* [1-2]. The disease has an incubation period typically ranging from 3 to 7 days. The general population is susceptible to CHIKV, and infection is thought to confer long-lasting immunity. Sources of transmission include acute-phase patients, asymptomatic individuals, and virus-carrying mosquitoes, with most patients remaining contagious within the first week of symptom onset [3].

In 2025, a local clustered outbreak of CHIK, triggered by imported cases, occurred in Foshan City, Guangdong Province, representing the largest epidemic event of its kind recorded in China to date. By the end of 2024, more than 110 countries had reported local or imported cases of CHIK. In the first seven months of 2025 alone, over 240,000 cases and 90 deaths were recorded globally [4]. Modeling studies project a long-term global average annual infection risk of 0.012 (95% UI: 0.007–0.019), corresponding to approximately 14.4 million (95% UI: 11.0–17.8 million) annual infections worldwide [5].

Mathematical models play a crucial role in elucidating the transmission dynamics of vector-borne diseases and guiding precision control strategies. Age- and sex-structured dynamic models have been widely applied in population studies. To address the gaps in existing research, this study proposes an analytical framework for optimizing prevention and control strategies, building upon prior work, validated using data from the largest CHIK outbreak recorded in China.

---

## Results

### Epidemiological Characteristics

Since the first imported case of CHIK was reported in Foshan City on June 16, 2025, a total of 9,929 confirmed cases had been recorded by September 18. Among these, 5,171 (52.08%) were male and 4,758 (47.92%) were female. In terms of age distribution, the 15–59 age group was the most affected across both sexes.

The epidemic progression exhibited distinct phases:
- **First peak:** July 18 (405 new cases)
- **Highest daily count:** July 28 (493 new cases)
- **Subsequent decline:** control measures gradually took effect

Stratified analysis revealed:
- **Preparedness phase (June 16 – July 18):** males 51.09%, females 48.91%; the 15–59 group constituted 32.46% of all cases
- **Containment phase (July 19 – September 18):** males 52.39%; the 15–59 group remained at 32.31% of all cases

---

### Basic Reproduction Number with Sex-Age Structure

The disease-free equilibrium (DFE) is represented by:

$$E_0 = (S_{m1}^0, 0,0,0,0, S_{f1}^0, 0,0,0,0, \ldots, S_{mk}^0, 0,0,0,0, S_{fk}^0, 0,0,0,0, S_a^0, 0, S_v^0, 0,0)_{1\times(10k+5)}$$

where $N_p = \sum_{j=1}^{k}(S_{mj}^0 + S_{fj}^0)$ and $N_v = S_a^0 + S_v^0$.

The basic reproduction number $\mathcal{R}_0$ is calculated using the next-generation matrix approach. The nonlinear terms with new infection $\mathcal{F}$ and the outflow term $\mathcal{V}$ are given by:

$$\mathcal{F} = \begin{pmatrix} \frac{\beta_{vp}IRR_{m1}S_{m1}I_v}{N_p} \\ 0 \\ 0 \\ \frac{\beta_{vp}IRR_{f1}S_{f1}I_v}{N_p} \\ 0 \\ 0 \\ \vdots \\ \frac{\beta_{vp}IRR_{mk}S_{mk}I_v}{N_p} \\ 0 \\ 0 \\ \frac{\beta_{vp}IRR_{fk}S_{fk}I_v}{N_p} \\ 0 \\ 0 \\ \frac{\beta_{pv}S_v \sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p} \\ 0 \end{pmatrix}_{(6k+2)\times 1}$$

$$\mathcal{V} = \begin{pmatrix} q\omega'E_{m1} + (1-q)\omega E_{m1} \\ -(1-q)\omega E_{m1} + \gamma I_{m1} \\ -q\omega' E_{m1} + \gamma' A_{m1} \\ q\omega'E_{f1} + (1-q)\omega E_{f1} \\ -(1-q)\omega E_{f1} + \gamma I_{f1} \\ -q\omega' E_{f1} + \gamma' A_{f1} \\ \vdots \\ q\omega'E_{mk} + (1-q)\omega E_{mk} \\ -(1-q)\omega E_{mk} + \gamma I_{mk} \\ -q\omega' E_{mk} + \gamma' A_{mk} \\ q\omega'E_{fk} + (1-q)\omega E_{fk} \\ -(1-q)\omega E_{fk} + \gamma I_{fk} \\ -q\omega' E_{fk} + \gamma' A_{fk} \\ (d+\varpi)E_v \\ -\varpi E_v + d \cdot I_v \end{pmatrix}_{(6k+2)\times 1}$$

The Jacobian matrices of $\mathcal{F}$ and $\mathcal{V}$ at the DFE $E_0$ are:

$$F(E_0) = \begin{pmatrix} 0_{6k\times 6k} & F_1 \\ F_2 & 0_{2\times 2} \end{pmatrix}$$

$$V(E_0) = \begin{pmatrix} V_1 & 0_{6k\times 2} \\ 0_{2\times 6k} & V_2 \end{pmatrix}$$

where:

$$F_1 = \begin{pmatrix} 0 & \frac{\beta_{vp}IRR_{m1}S_{m1}^0}{N_p} & 0 & 0 & 0 & 0 \\ 0 & \frac{\beta_{vp}IRR_{f1}S_{f1}^0}{N_p} & 0 & 0 & 0 & 0 \\ \vdots & \vdots & & & & \\ 0 & \frac{\beta_{vp}IRR_{mk}S_{mk}^0}{N_p} & 0 & 0 & 0 & 0 \\ 0 & \frac{\beta_{vp}IRR_{fk}S_{fk}^0}{N_p} & 0 & 0 & 0 & 0 \end{pmatrix}_{6k\times 2}$$

$$F_2 = \mathbf{1}_{1\times 3k} \otimes \begin{pmatrix} 0 & \frac{\beta_{pv}S_v^0}{N_p} & \frac{\beta_{pv}S_v^0}{N_p} & 0 & 0 & 0 \end{pmatrix}$$

$$V_1 = I_{2k} \otimes \begin{pmatrix} q\omega' + (1-q)\omega & 0 & 0 \\ -(1-q)\omega & \gamma & 0 \\ -q\omega' & 0 & \gamma' \end{pmatrix}, \quad V_2 = \begin{pmatrix} (d+\varpi) & 0 \\ -\varpi & d \end{pmatrix}$$

The basic reproduction number $\mathcal{R}_0$ of model (1) is the spectral radius of the next-generation matrix $FV^{-1}(E_0)$:

$$\mathcal{R}_0 = \sqrt{\mathcal{R}_{0(vp)} \times \mathcal{R}_{0(pv)}}$$

where:

$$\mathcal{R}_{0(vp)} = \frac{\sum_{j=1}^{k}\left(\frac{\beta_{vp}IRR_{mj}S_{mj}^0}{N_p}(1-q)\omega\right)}{[q\omega'+(1-q)\omega]\gamma} + \frac{\sum_{j=1}^{k}\left(\frac{\beta_{vp}IRR_{mj}S_{mj}^0}{N_p}q\omega'\right)}{[q\omega'+(1-q)\omega]\gamma'}$$

$$+ \frac{\sum_{j=1}^{k}\left(\frac{\beta_{vp}IRR_{fj}S_{fj}^0}{N_p}(1-q)\omega\right)}{[q\omega'+(1-q)\omega]\gamma} + \frac{\sum_{j=1}^{k}\left(\frac{\beta_{vp}IRR_{fj}S_{fj}^0}{N_p}q\omega'\right)}{[q\omega'+(1-q)\omega]\gamma'}$$

$$= \mathcal{R}_{0(vpI_m)} + \mathcal{R}_{0(vpA_m)} + \mathcal{R}_{0(vpI_f)} + \mathcal{R}_{0(vpA_f)}$$

$$\mathcal{R}_{0(pv)} = \frac{\beta_{pv}S_v^0}{N_p} \cdot \frac{\varpi}{(d+\varpi)d}$$

**Table 1. Contribution of cross-species transmission pathways to $\mathcal{R}_0$**

| Time | $\mathcal{R}_0$ | $\mathcal{R}_{0(vp)}$ | $\mathcal{R}_{0(pv)}$ |
|------|--------|------------|------------|
| 11 Jun–18 Jul | 10.1235 | 3.6197 | 28.3132 |
| 19 Jul–18 Sep | 1.3865 | 0.8665 | 2.2185 |
| 19 Jul–25 Jul | 1.2934 | 1.0341 | 1.6178 |
| 26 Jul–18 Sep | 1.3243 | 0.8122 | 2.1593 |

---

### HMC-Optimized Strategy Validation

Three control pathways were incorporated into Model (1) as control functions $u(t) = (u_1(t), u_2(t), u_3(t))$:

**Table 2. Parameterization of Intervention Measures**

| Intervention pathway | Control function | Parameter adjustment |
|---------------------|-----------------|---------------------|
| ① Mosquito-to-human transmission control | $u_1(t)$ | $\beta_{vp} \triangleq (1-u_1(t))\beta_{vp}$ |
| ② Human-to-mosquito transmission control | $u_2(t)$ | $\beta_{pv} \triangleq (1-u_2(t))\beta_{pv}$ |
| ③ Mosquito population suppression | $u_3(t)$ | $N_v = (1-u_3(t))xN_p$ |

The controlled system is $\quad (2)$:

$$\frac{dS_{mj}}{dt} = -\frac{(1-u_1(t))\beta_{vp}IRR_{mj}S_{mj}I_v}{N_p}$$

$$\frac{dE_{mj}}{dt} = \frac{(1-u_1(t))\beta_{vp}IRR_{mj}S_{mj}I_v}{N_p} - q\omega'E_{mj} - (1-q)\omega E_{mj}$$

$$\frac{dI_{mj}}{dt} = (1-q)\omega E_{mj} - \gamma I_{mj}$$

$$\frac{dA_{mj}}{dt} = q\omega'E_{mj} - \gamma'A_{mj}$$

$$\frac{dR_{mj}}{dt} = \gamma I_{mj} + \gamma'A_{mj}$$

$$\frac{dS_{fj}}{dt} = -\frac{(1-u_1(t))\beta_{vp}IRR_{fj}S_{fj}I_v}{N_p}$$

$$\frac{dE_{fj}}{dt} = \frac{(1-u_1(t))\beta_{vp}IRR_{fj}S_{fj}I_v}{N_p} - q\omega'E_{fj} - (1-q)\omega E_{fj}$$

$$\frac{dI_{fj}}{dt} = (1-q)\omega E_{fj} - \gamma I_{fj}$$

$$\frac{dA_{fj}}{dt} = q\omega'E_{fj} - \gamma'A_{fj}$$

$$\frac{dR_{fj}}{dt} = \gamma I_{fj} + \gamma'A_{fj}$$

$$\frac{dS_a}{dt} = ac[(1-u_3(t))xN_p - nI_a] - \lambda S_a$$

$$\frac{dI_a}{dt} = acnI_a - \lambda I_a$$

$$\frac{dS_v}{dt} = \lambda S_a - \frac{(1-u_2(t))\beta_{pv}S_v\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p} - dS_v$$

$$\frac{dE_v}{dt} = \frac{(1-u_2(t))\beta_{pv}S_v\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p} - (d+\varpi)E_v$$

$$\frac{dI_v}{dt} = \lambda I_a + \varpi E_v - dI_v$$

The objective functional to minimize is $(3)$:

$$G\bigl(u(t)\bigr) = \int_0^T \left[\sum_{j=1}^{k}\bigl(p_{mj}I_{mj} + p_{fj}I_{fj}\bigr) + \frac{p_{k+1}}{2}u_1^2(t) + \frac{p_{k+2}}{2}u_2^2(t) + \frac{p_{k+3}}{2}u_3^2(t)\right]dt$$

The optimal control problem is $(4)$:

$$G(u^*) = \min_{\Theta}\, G\bigl(u(t)\bigr)$$

where:

$$\Theta = \Bigl\{u(t) \in L^3(0,T) \;\Big|\; u_{min} \leq u_1(t),\, u_2(t),\, u_3(t) \leq u_{max},\; t \in (0,T)\Bigr\}$$

The Lagrangian for the optimal problem is $(5)$:

$$\mathcal{L} = \sum_{j=1}^{k}\bigl(p_{mj}I_{mj} + p_{fj}I_{fj}\bigr) + \frac{p_{k+1}}{2}u_1^2(t) + \frac{p_{k+2}}{2}u_2^2(t) + \frac{p_{k+3}}{2}u_3^2(t)$$

The Hamiltonian function $\mathcal{H}$ is defined as $(6)$:

$$\mathcal{H} = \mathcal{L} + \sum_{i=1}^{10k+5} \eta_i f_i$$

**Theorem 1.** The adjoint variables $\eta_i$ $(i=1,\ldots,10k+5)$ satisfy $\quad (7)$:

$$\frac{d\eta_{10(j-1)+1}}{dt} = \eta_{10(j-1)+1}C_{1m} - \eta_{10(j-1)+2}C_{1m}$$

$$\frac{d\eta_{10(j-1)+2}}{dt} = \eta_{10(j-1)+2}[q\omega'+(1-q)\omega] - \eta_{10(j-1)+3}(1-q)\omega - \eta_{10(j-1)+4}q\omega'$$

$$\frac{d\eta_{10(j-1)+3}}{dt} = -p_{mj} + p\eta_{10(j-1)+3}\gamma - \eta_{10(j-1)+5}\gamma + \eta_{10k+3}C_2 - \eta_{10k+4}C_2$$

$$\frac{d\eta_{10(j-1)+4}}{dt} = \eta_{10(j-1)+4}\gamma' - \eta_{10(j-1)+5}\gamma' + \eta_{10k+3}C_2 - \eta_{10k+4}C_2$$

$$\frac{d\eta_{10(j-1)+5}}{dt} = 0$$

$$\frac{d\eta_{10(j-1)+6}}{dt} = \eta_{10(j-1)+6}C_{1f} - \eta_{10(j-1)+7}C_{1f}$$

$$\frac{d\eta_{10(j-1)+7}}{dt} = \eta_{10(j-1)+7}[q\omega'+(1-q)\omega] - \eta_{10(j-1)+8}(1-q)\omega - \eta_{10(j-1)+9}q\omega'$$

$$\frac{d\eta_{10(j-1)+8}}{dt} = -p_{fj} + p\eta_{10(j-1)+8}\gamma - \eta_{10j}\gamma + \eta_{10k+3}C_2 - \eta_{10k+4}C_2$$

$$\frac{d\eta_{10(j-1)+9}}{dt} = \eta_{10(j-1)+}\gamma' - \eta_{10j}\gamma' + \eta_{10k+3}C_2 - \eta_{10k+4}C_2$$

$$\frac{d\eta_{10j}}{dt} = 0$$

$$\frac{d\eta_{10k+1}}{dt} = \eta_{10k+1}\lambda - \eta_{10k+3}\lambda$$

$$\frac{d\eta_{10k+2}}{dt} = \eta_{10k+1}acn - \eta_{10k+2}(acn-\lambda) - \eta_{10k+5}\lambda$$

$$\frac{d\eta_{10k+3}}{dt} = \eta_{10k+3}[C_3+d] - \eta_{10k+4}C_3$$

$$\frac{d\eta_{10k+4}}{dt} = \eta_{10k+4}(d+\varpi) - \eta_{10k+5}\varpi$$

$$\frac{d\eta_{10k+5}}{dt} = \sum_{j=1}^{k}\left[(\eta_{10(j-1)+1}-\eta_{10(j-1)+2})C_{4m} + (\eta_{10(j-1)+6}-\eta_{10(j-1)+7})C_{4f}\right] + \eta_{10k+5}d$$

with boundary conditions $\eta_i(T) = 0$, where:

$$C_{1m} = \frac{(1-u_1(t))\beta_{vp}IRR_{mj}I_v}{N_p}, \quad C_{1f} = \frac{(1-u_1(t))\beta_{vp}IRR_{fj}I_v}{N_p}$$

$$C_2 = \frac{(1-u_2(t))\beta_{pv}S_v}{N_p}, \quad C_3 = \frac{(1-u_2(t))\beta_{pv}\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p}$$

$$C_{4m} = \frac{(1-u_1(t))\beta_{vp}IRR_{mj}S_{mj}}{N_p}, \quad C_{4f} = \frac{(1-u_1(t))\beta_{vp}IRR_{fj}S_{fj}}{N_p}$$

The optimal control measures $u_1^*, u_2^*, u_3^*$ are given by $(8)$:

$$u_1^*(t) = \max\left\{\min\left\{u_{min},\; \frac{\displaystyle\sum_{j=1}^{k}\left[(\eta_{10(j-1)+2}-\eta_{10(j-1)+1})\frac{\beta_{vp}IRR_{mj}S_{mj}I_v}{N_p} + (\eta_{10(j-1)+7}-\eta_{10(j-1)+6})\frac{\beta_{vp}IRR_{fj}S_{fj}I_v}{N_p}\right]}{p_{k+1}}\right\},\; u_{max}\right\}$$

$$u_2^*(t) = \max\left\{\min\left\{u_{min},\; \frac{\displaystyle(\eta_{10k+4}-\eta_{10k+3})\,\frac{\beta_{pv}S_v\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p}}{p_{k+1}}\right\},\; u_{max}\right\}$$

$$u_3^*(t) = \max\left\{\min\left\{u_{min},\; \frac{\eta_{10k+1}\,a\,c\,x\,N_p}{p_{k+2}}\right\},\; u_{max}\right\}$$

---

### Evaluation of Combination Strategies

**Table 3. Design of Intervention Strategy Combinations**

| Strategy | $u_1$ (Mosquito-to-human) | $u_2$ (Human-to-mosquito) | $u_3$ (Mosquito suppression) |
|----------|--------------------------|--------------------------|------------------------------|
| Strategy 1 | 0 | 0 | 0 |
| Strategy 2 | HMC-Estimated | 0 | 0 |
| Strategy 3 | 0 | HMC-Estimated | 0 |
| Strategy 4 | 0 | 0 | HMC-Estimated |
| Strategy 5 | HMC-Estimated | HMC-Estimated | 0 |
| Strategy 6 | HMC-Estimated | 0 | HMC-Estimated |
| Strategy 7 | 0 | HMC-Estimated | HMC-Estimated |
| Strategy 8 | HMC-Estimated | HMC-Estimated | HMC-Estimated |

Effectiveness ranked from highest to lowest: Strategy 8 > 6 > 7 > 4 > 5 > 3 > 2 > 1.

- Combined implementation of all three measures: average reduction of **95.7586%**
- Mosquito population suppression alone: **78.4695%** reduction
- Human-to-mosquito control alone: **25.6044%** reduction
- Mosquito-to-human control alone: **17.8302%** reduction
- Best two-measure combination (Strategy 6): **81.5226%** reduction

All measures showed weakest effects for **females aged 60+**.

---

### Dose-Response Effects of Interventions

1,331 control combinations were evaluated. Key findings:

- With $u_1$ fixed: $(u_2=0.6, u_3=0.9)$, $(u_2=0.8, u_3=0.8)$, or $(u_2=0.9, u_3=0.6)$ → $\mathcal{R}_{eff}=0.9737$
- With $u_2$ fixed: $(u_1=0.7, u_3=0.9)$ or $(u_1=0.9, u_3=0.7)$ → $\mathcal{R}_{eff}=0.8865$
- With $u_3$ fixed: $(u_1=0.7, u_2=0.9)$ or $(u_1=0.9, u_2=0.7)$ → $\mathcal{R}_{eff}=0.9465$

Asymmetric combinations: intensities of **60%/80%/90%** → $\mathcal{R}_{eff}=0.9055$

---

## Discussion

This study developed a structural vector-borne model encompassing two main populations: the human population (age- and sex-stratified SEIAR framework) and the mosquito population (larval and adult stages). The total number of compartments reaches $10k+5$.

Key findings:
- The 15–59 age group constituted the most affected population, with asymptomatic infections contributing substantially to transmission
- Mosquito population suppression is the most effective single intervention, but must be sustained at high intensity to avoid resurgence
- The dual strategy of "mosquito-to-human control + mosquito population suppression" was the most effective two-measure combination (81.5226% reduction)
- Intervention effects varied across demographic groups, supporting population-targeted strategies

**Limitations:**
- Vaccination (Ixchiq, approved 2023) not incorporated
- Climate change impacts on mosquito distribution not modeled
- Human mobility and imported cases not systematically analyzed

---

## Methods

### Structural Vector-Borne Model Development

The model stratifies the human population into $10k$ compartments. For each age group $j$ $(j=1,\ldots,k)$:

**Human compartments:**
- $S_{mj}/S_{fj}$: Susceptible males/females
- $E_{mj}/E_{fj}$: Exposed males/females
- $I_{mj}/I_{fj}$: Symptomatically infectious males/females
- $A_{mj}/A_{fj}$: Asymptomatically infectious males/females
- $R_{mj}/R_{fj}$: Recovered males/females

**Vector compartments:**
- $S_a$: Susceptible larval mosquitoes
- $I_a$: Infected larval mosquitoes
- $S_v$: Susceptible adult mosquitoes
- $E_v$: Exposed adult mosquitoes
- $I_v$: Infectious adult mosquitoes

**Model assumptions:**
1. CHIKV transmission occurs exclusively through vector-human cross-species interactions
2. Effective transmission rate varies across age and sex groups via IRR
3. Upon infection, individuals enter latency; with probability $q$ they become asymptomatic (rate $\omega'$, recovery $\gamma'$); with probability $(1-q)$ they become symptomatic (rate $\omega$, recovery $\gamma$)
4. A proportion $n$ of mosquitoes acquire the virus through vertical transmission at effective rate $a \cdot c \cdot n$
5. Newly reproduced larvae enter $S_a$; adult mosquitoes have extrinsic incubation period $1/\varpi$

Total populations:

$$N_p = \sum_{j=1}^{k}(S_{mj}+E_{mj}+I_{mj}+A_{mj}+R_{mj}+S_{fj}+E_{fj}+I_{fj}+A_{fj}+R_{fj})$$

$$N_v = S_a + I_a + S_v + E_v + I_v = x \cdot N_p$$

Seasonal effect function:

$$c \triangleq c(t) = \cos\left(\frac{t-\tau}{T}\right)$$

**Full model system $\quad (1)$:**

$$\frac{dS_{mj}}{dt} = -\frac{\beta_{vp}IRR_{mj}S_{mj}I_v}{N_p}$$

$$\frac{dE_{mj}}{dt} = \frac{\beta_{vp}IRR_{mj}S_{mj}I_v}{N_p} - q\omega'E_{mj} - (1-q)\omega E_{mj}$$

$$\frac{dI_{mj}}{dt} = (1-q)\omega E_{mj} - \gamma I_{mj}$$

$$\frac{dA_{mj}}{dt} = q\omega'E_{mj} - \gamma'A_{mj}$$

$$\frac{dR_{mj}}{dt} = \gamma I_{mj} + \gamma'A_{mj}$$

$$\frac{dS_{fj}}{dt} = -\frac{\beta_{vp}IRR_{fj}S_{fj}I_v}{N_p}$$

$$\frac{dE_{fj}}{dt} = \frac{\beta_{vp}IRR_{fj}S_{fj}I_v}{N_p} - q\omega'E_{fj} - (1-q)\omega E_{fj}$$

$$\frac{dI_{fj}}{dt} = (1-q)\omega E_{fj} - \gamma I_{fj}$$

$$\frac{dA_{fj}}{dt} = q\omega'E_{fj} - \gamma'A_{fj}$$

$$\frac{dR_{fj}}{dt} = \gamma I_{fj} + \gamma'A_{fj}$$

$$\frac{dS_a}{dt} = ac(N_v - nI_a) - \lambda S_a$$

$$\frac{dI_a}{dt} = acnI_a - \lambda I_a$$

$$\frac{dS_v}{dt} = \lambda S_a - \frac{\beta_{pv}S_v\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p} - dS_v$$

$$\frac{dE_v}{dt} = \frac{\beta_{pv}S_v\sum_{j=1}^{k}(I_{mj}+I_{fj}+A_{mj}+A_{fj})}{N_p} - (d+\varpi)E_v$$

$$\frac{dI_v}{dt} = \lambda I_a + \varpi E_v - dI_v$$

---

### Data and Parameter Collection

Data sourced from WHO 2025 CHIK outbreak records and relevant literature. Study site: Foshan City, Guangdong Province. Cases stratified by sex and age (0–14, 15–59, ≥60 years). Study period divided into preparedness phase (June 16 – July 18) and containment phase (July 19 – September 18), with incubation lag subphase (July 19–25).

**Table 4. Definition and value of parameters**

| Parameter | Definition | Unit | Value | Range | Source |
|-----------|-----------|------|-------|-------|--------|
| $\beta_{vp}$ | Transmission rate mosquito→human | — | — | 0–1 | Fitting |
| $\beta_{pv}$ | Transmission rate human→mosquito | — | — | 0–1 | Fitting |
| $x$ | Mosquito-to-human ratio | — | — | 5–15 | Fitting |
| $a$ | Per capita birth rate of mosquitoes | Day⁻¹ | 0.145 | 0.02–0.27 | Ref. (24-25) |
| $\tau$ | Simulation delay initial time | Day | 30 | — | Estimation |
| $T$ | Duration of daily cycle | Day | 365 | — | Estimation |
| $n$ | Minimum vertical transmission rate | — | 0.0181 | 0.0076–0.0286 | Ref. (26-27) |
| $\lambda$ | Rate of mosquito emergence | Day⁻¹ | 0.0902 | 0.0691–0.1296 | Ref. (28) |
| $d$ | Natural mortality rate of mosquitoes | Day⁻¹ | 1/7.4 | 1/9.8–1/4.5 | Ref. (29) |
| $\varpi$ | Transition rate exposed→infectious mosquito | Day⁻¹ | 1/5.5 | 1/8.2–1/3 | Ref. (30-33) |
| $q$ | Proportion exposed→asymptomatic | — | 0.155 | 0.03–0.28 | Ref. (34-35) |
| $\omega$ | Transition rate exposed→symptomatic | Day⁻¹ | 1/4.5 | 1/7–0.5 | Ref. (34-35) |
| $\omega'$ | Transition rate exposed→asymptomatic | Day⁻¹ | 1/4.5 | 1/7–0.5 | Ref. (34-35) |
| $\gamma$ | Recovery rate symptomatic | Day⁻¹ | 1/7 | — | Ref. (36) |
| $\gamma'$ | Recovery rate asymptomatic | Day⁻¹ | 1/7 | — | Ref. (36) |

---

### Parameter Estimation

The PMCMC (Particle Markov Chain Monte Carlo) method is used for Bayesian inference of unknown parameters $\theta$. The posterior distribution is:

$$p(\theta|y_{1:T}) \propto p(y_{1:T}|\theta) \cdot p(\theta)$$

The marginal likelihood estimate from the particle filter:

$$\hat{p}(y_{1:T}|\theta) = \prod_{t=1}^{T}\left(N^{-1}\sum_{i=1}^{N}w_t^{(i)}\right)$$

The acceptance probability for candidate $\theta^*$:

$$\alpha = \min\left\{1, \frac{\hat{p}(y_{1:T}|\theta^*)p(\theta^*)}{\hat{p}(y_{1:T}|\theta^{k-1})p(\theta^{k-1})} \cdot \frac{q(\theta^{(k-1)}|\theta^*)}{q(\theta^*|\theta^{(k-1)})}\right\}$$

---

### Optimal Control

The Hamiltonian function:

$$\mathcal{H}(x,\lambda,u,t) = L(x(t),u(t),t) + \lambda^T(t) \times f(x(t),u(t),t)$$

According to Pontryagin's Maximum Principle, the optimal control $u^*(t)$ satisfies:

$$\frac{\partial\mathcal{H}}{\partial u} = 0$$

The state equation is integrated forward:

$$\dot{x} = f(x,u,t), \quad x(0) = x_0$$

The costate equation is integrated backward:

$$\dot{\lambda} = -\frac{\partial\mathcal{H}}{\partial x}, \quad \lambda(T) = 0$$

A relaxation update strategy ensures convergence:

$$u_{new} = (1-\omega)u_{old} + \omega \cdot u_{calculated}$$

where $\omega \in (0,1)$ is the relaxation factor.

---

## References

1. Bartholomeeusen K, Daniel M & LaBeaud DA et al. Chikungunya fever. *Nat Rev Dis Primers* 9, 17 (2023).
2. Vairo F, Haider N & Kock R et al. Chikungunya: epidemiology, pathogenesis, clinical features, management, and prevention. *Infect Dis Clin North Am* 33, 1003–1025 (2019).
3. Powers AM & Logue CH. Changing patterns of chikungunya virus. *J Gen Virol* 88, 2363–2377 (2007).
4. ECDC. Chikungunya virus disease worldwide overview. https://www.ecdc.europa.eu/en/chikungunya-monthly (2025).
5. Kang H, Lim A & Auzenbergs M et al. Global, regional and national burden of chikungunya. *BMJ Glob Health* 10, e018598 (2025).
6–57. [See full reference list in original article]

---

## Acknowledgments

This work is supported by the Self-supporting Program of Guangzhou Laboratory (GZNL2024A01004 and SRPG22-007), the National Key Research and Development Program of China (2024YFC2311404), the China Postdoctoral Science Foundation (K2825002), the Postdoctoral Fellowship Program of CPSF (GZC20250516), and the Prevention and Control of Emerging and Major Infectious Diseases — National Science and Technology Major Project (2025ZD01900406).

---

## Author Contributions

**Conceptualization:** T.M.C., J.H.L., Z.Y.Z., J.R. | **Investigation:** J.H.L., Z.Y.Z., J.R., J.G.Z., Q.X.L., W.T.S., Q.P.C. | **Methodology:** J.H.L., Z.Y.Z., J.R., S.P., R.F. | **Software:** J.H.L., J.G.Z., Q.X.L. | **Validation:** Z.Y.Z., J.R., K.G.L., S.P., R.F., Y.H.S., X.T.X. | **Writing — original draft:** J.H.L., J.G.Z., Q.X.L., K.G.L. | **Writing — review & editing:** J.H.L., Z.Y.Z., J.R., S.P., R.F., Y.H.S., Q.P.C., X.T.X., T.M.C.

---

*Competing interests: The authors declare no competing interests.*
