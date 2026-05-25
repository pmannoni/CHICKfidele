# ANALYSE MÉTHODOLOGIQUE EXHAUSTIVE
## PARTIE 3 : PIPELINE COMPLET, PSEUDO-CODE ET IMPLÉMENTATION

---

## PARTIE 23 : PIPELINE MÉTHODOLOGIQUE EXACT

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    CHIKUNGUNYA MODEL PIPELINE                             ║
╚════════════════════════════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 0 : COLLECTE ET NETTOYAGE DONNÉES                                │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Source 1 : WHO Global Surveillance (16 Jun - 18 Sep 2025)
    ├─ Source 2 : Ministry of Health Foshan (Confirmés/Suspects)
    ├─ Source 3 : Bureau Statistiques Foshan (Population âge-sexe)
    └─ Source 4 : Littérature (Paramètres biologiques)
    
    PROCESSING :
    ├─ [Filtrage] Retirer records incomplètes (date symptôme, sexe, âge)
    ├─ [QA Masks] Vérifier dates cohérentes, âges plausibles, pas doublons
    ├─ [Stratification] Grouper par (sexe ∈ {M,F}, âge ∈ {0-14,15-59,60+})
    ├─ [Normalisation dates] Aligner date symptôme (diagnostic offset -1~-2j)
    └─ [Segmentation temporelle]
       ├─ Préparation : 16 Jun - 18 Jul 2025
       ├─ Confinement Phase 1 : 19 Jul - 25 Jul (décalage incubation)
       └─ Confinement Phase 2 : 26 Jul - 18 Sep (post-décalage)

    OUTPUT : y_sj(t) = série chronologique par (sexe, âge)

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 1 : SPÉCIFICATION MODÈLE NON-CONTRÔLÉ (Modèle 1)                 │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Compartiments : 10k + 5 = 35 (k=3)
    │  ├─ Humains : S_mj, E_mj, I_mj, A_mj, R_mj (×2 sexes, ×3 âges)
    │  └─ Moustiques : S_a, I_a, S_v, E_v, I_v
    │
    ├─ Paramètres fixes (littérature) :
    │  ├─ ω = 1/4.5, ω' = 1/4.5, γ = 1/7, γ' = 1/7
    │  ├─ λ = 0.0902, d = 1/7.4, a = 0.145, ϖ = 1/5.5
    │  ├─ n = 0.0181, q = 0.155
    │  ├─ τ = 30, T = 365
    │  └─ N_p = constant (pop Foshan 2025 par groupe)
    │
    ├─ Paramètres à estimer (PMCMC) :
    │  ├─ β_vp (transmission mosquito→humain)
    │  ├─ β_pv (transmission humain→mosquito)
    │  ├─ x (ratio mosquito/humain)
    │  └─ IRR_sj (multiplicateurs risque par groupe)
    │
    └─ Système ODE : 35 équations différentielles ordinaires

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 2 : ESTIMATION PARAMÈTRES PMCMC                                   │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Phase 1 : Préparation (16 Jun - 18 Jul)
    │  ├─ [Initialization] θ⁽⁰⁾ = prior means
    │  ├─ [Particle Filter] Évaluer likelihood p(y|θ)
    │  │  - N = 500 particles
    │  │  - Resample si ESS < N/2
    │  │  - Output : p̂(y₁:ₜ|θ)
    │  │
    │  ├─ [MCMC Chain] Metropolis-Hastings K=5000 iterations
    │  │  ├─ Burnin = 1000
    │  │  ├─ Proposal : Gaussian Random Walk σ_proposal calibré
    │  │  └─ Output : {θ⁽ᵏ⁾}_{k>1000}
    │  │
    │  └─ [Posterior Summary]
    │     ├─ Point estimates : E[θ|y] ou mode
    │     └─ Credible intervals : 2.5%, 97.5% quantiles
    │
    └─ Phase 2 : Confinement (19 Jul - 18 Sep) - Utilisé Phases 1 paramètres

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 3 : DÉCOMPOSITION NOMBRE REPRODUCTION BASE                        │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Next-Generation Matrix F·V⁻¹(E₀) au DFE
    ├─ Calcul ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))
    │
    ├─ Décomposition par groupe démographique :
    │  ├─ ℛ₀(vp) = Σ ℛ₀(vpI_mj) + ℛ₀(vpA_mj) + ℛ₀(vpI_fj) + ℛ₀(vpA_fj)
    │  └─ Poids relatif chaque composante → Identification groupes clés
    │
    └─ Output : ℛ₀ par phase, par groupe, contribution asympto vs sympto

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 4 : SPÉCIFICATION MODÈLE CONTRÔLÉ (Modèle 2)                     │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Ajouter contrôles u₁(t), u₂(t), u₃(t) à Modèle 1
    ├─ Modifier paramètres de transmission :
    │  ├─ β_vp ← (1-u₁)·β_vp
    │  ├─ β_pv ← (1-u₂)·β_pv
    │  └─ N_v ← (1-u₃)·x·N_p
    │
    └─ Contraintes contrôles : 0.2 ≤ u_i(t) ≤ 0.8

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 5 : FORMULATION PROBLÈME CONTRÔLE OPTIMAL                         │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Fonction objectif :
    │  └─ G(u) = ∫₀ᵀ [ Σ_sj p_sj·I_sj(t) + 0.5·u₁² + 0.5·u₂² + 0.5·u₃² ] dt
    │
    ├─ Minimiser G(u*) s.c. Modèle 2 ODEs + contraintes contrôles
    │
    ├─ Construct Hamiltonien :
    │  └─ ℋ = L + Σ ηᵢ·fᵢ
    │
    └─ Conditions optimalité (Pontryagin)

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 6 : RÉSOLUTION SYSTÈME CONTRÔLE OPTIMAL                           │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Forward-Backward Sweep Method
    │  ├─ [Iteration k]
    │  │  ├─ Forward RK4 : x⁽ᵏ⁾ = integrate ODE état avec u⁽ᵏ⁻¹⁾
    │  │  ├─ Backward RK4 : η⁽ᵏ⁾ = integrate adjoint avec x⁽ᵏ⁾
    │  │  ├─ Update u⁽ᵏ⁾ = argmin_Θ ℋ(x⁽ᵏ⁾, η⁽ᵏ⁾, u, t)
    │  │  ├─ Relax : u_new = (1-ω)·u_old + ω·u_calculated (ω=0.5)
    │  │  └─ Check converge : ||u⁽ᵏ⁾ - u⁽ᵏ⁻¹⁾||₂ < ε (ε=10⁻⁴)
    │  │
    │  └─ Output : u* = (u₁*, u₂*, u₃*) trajectoires optimales
    │
    └─ Adjoint 35 ODEs backward (ηᵢ(T) = 0)

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 7 : VALIDATION ET ANALYSE SENSITIVITÉ                             │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Goodness-of-fit :
    │  ├─ RSS = Σₜ Σ_sj (y_sj(t) - ŷ_sj(t|θ))²
    │  ├─ RMSE, MAE, MAPE par groupe
    │  └─ AIC/BIC comparaison vs k=2 âges ou k=4 âges
    │
    ├─ Scan paramètres 3D dans espace (u₁,u₂,u₃) ∈ [0,1]³
    │  ├─ Grille 11×11×11 = 1331 points
    │  ├─ Évaluer ℛ_eff(u₁,u₂,u₃) pour chaque point
    │  └─ Identifier seuils R_eff < 1 (contrôle possible)
    │
    └─ Output : Heatmaps, surface plots, Pareto frontiers

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 8 : ÉVALUATION STRATÉGIES ALTERNATIVES                            │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Scénarios 1-8 : Combos u₁, u₂, u₃ (voir Partie 2, section 17)
    ├─ Métriques :
    │  ├─ Cumulative infections par groupe
    │  ├─ Pic incidence (jour + amplitude)
    │  ├─ Durée épidémie (jusqu'à R_eff < 1)
    │  └─ Cost-effectiveness ratio (infections évitées / $ dépensés)
    │
    └─ Comparaison : Scores globaux vs groupe-spécifiques

┌──────────────────────────────────────────────────────────────────────────┐
│ ÉTAPE 9 : RAPPORTAGE RÉSULTATS                                          │
└──────────────────────────────────────────────────────────────────────────┘
    ├─ Figures
    │  ├─ Fig 1 : Dynamiques temporelles + phases épidémio
    │  ├─ Fig 2 : Décomposition ℛ₀ par groupe
    │  ├─ Fig 3 : Comparaison stratégies infectés simulés vs observés
    │  ├─ Fig 4 : Heatmaps R_eff vs (u₁,u₂,u₃)
    │  ├─ Fig 5 : Schéma compartiments
    │  ├─ Fig 6 : Distribution géographique globale
    │  └─ Fig 7 : Framework d'analyse
    │
    ├─ Tableaux
    │  ├─ Table 1 : ℛ₀ contributes par phase
    │  ├─ Table 2 : Paramètres interventions
    │  ├─ Table 3 : Stratégies (8 scénarios)
    │  ├─ Table 4 : Valeurs paramètres
    │  └─ Table S1,S2,S3 : Données détaillées (annexes)
    │
    └─ Discussion + Limitations + Future Work

```

---

## PARTIE 24 : PSEUDO-CODE DÉTAILLÉ

### 24.1 Pseudo-code Modèle Non-Contrôlé (Phase Estimation)

```
╔════════════════════════════════════════════════════════════════════════════╗
║           ALGORITHM 1: MODEL FITTING WITH PMCMC (Model 1)                 ║
╚════════════════════════════════════════════════════════════════════════════╝

INPUT:
  y_sj(t) for t=0..T_prep, sj ∈ {6 groups}    // Observed daily cases
  x₀                                           // Initial compartments
  θ_prior                                      // Prior distributions
  
OUTPUT:
  θ_posterior ~ p(θ|y)                        // Posterior samples
  θ_map, credible_intervals                   // Point estimates

MAIN ALGORITHM:
  
  // Step 1: Initialize
  for k = 1 to K_iter
    if k == 1
      θ^(k) ← sample from θ_prior
    else
      θ^(k) ← θ^(k-1)  // Start from last accepted
    
    // Step 2: Propose new candidate
    θ_star ← θ^(k-1) + ε·randn()   // Gaussian random walk, ε tuned
    
    // Step 3: Evaluate likelihood via Particle Filter
    p_hat_star ← PARTICLE_FILTER(y, θ_star, Model_1)
    p_hat_prev ← PARTICLE_FILTER(y, θ^(k-1), Model_1)
    
    // Step 4: Metropolis-Hastings acceptance ratio
    log_α ← log(p_hat_star) - log(p_hat_prev) 
           + log(π(θ_star)) - log(π(θ^(k-1)))  // Add log-priors
    
    if log(uniform(0,1)) < log_α
      θ^(k) ← θ_star         // Accept
      n_accepted ← n_accepted + 1
    // else: θ^(k) ← θ^(k-1)  // Reject
  
  // Step 5: Post-processing
  θ_burn ← θ^(k)_{k > K_burnin}
  θ_map ← mode(θ_burn)
  θ_mean ← mean(θ_burn)
  CI_95% ← [quantile(θ_burn, 0.025), quantile(θ_burn, 0.975)]
  
  return θ_map, θ_mean, CI_95%, acceptance_rate

SUBROUTINE PARTICLE_FILTER(y, θ, ODE_model):
  
  x_particles[1..N] ← initialize from x₀
  weights[1..N] ← 1/N
  
  for t = 1 to T
    // Step A: Propagate particles
    for i = 1 to N
      x_particles[i] ← RK4_integrate(ODE_model, x_particles[i], θ, Δt)
    
    // Step B: Evaluate likelihood at observation y(t)
    for i = 1 to N
      ŷ[i] ← extract_observable(x_particles[i])   // Extract I_sj from state
      weights[i] ← weights[i] · L(y(t) | ŷ[i])   // Poisson or Negative Binomial
    
    // Step C: Resample if needed (ESS criterion)
    ESS ← 1 / sum(weights_normalized²)
    if ESS < N/2
      indices ← multinomial_resample(weights, N)
      x_particles ← x_particles[indices]
      weights ← 1/N
    
    // Step D: Update marginal likelihood estimate
    L_hat(t) ← sum(weights) / N
  
  p_hat(y|θ) ← product(L_hat(t) for t=1..T)
  return p_hat(y|θ)

SUBROUTINE RK4_INTEGRATE(f, x, θ, Δt):
  k1 ← f(t, x, θ)
  k2 ← f(t+Δt/2, x+k1·Δt/2, θ)
  k3 ← f(t+Δt/2, x+k2·Δt/2, θ)
  k4 ← f(t+Δt, x+k3·Δt, θ)
  x_new ← x + (k1 + 2·k2 + 2·k3 + k4)·Δt/6
  return x_new
```

### 24.2 Pseudo-code Modèle Contrôlé Optimal

```
╔════════════════════════════════════════════════════════════════════════════╗
║         ALGORITHM 2: OPTIMAL CONTROL VIA FORWARD-BACKWARD SWEEP           ║
╚════════════════════════════════════════════════════════════════════════════╝

INPUT:
  x₀                                          // Initial state
  θ (estimated from Algorithm 1)               // Fixed parameters
  T_final = 95 days                           // Time horizon
  u_min=0.2, u_max=0.8                        // Control bounds
  
OUTPUT:
  u_opt = (u₁*, u₂*, u₃*)(t)                  // Optimal control trajectories

MAIN ALGORITHM:

  // Initialization
  u⁽⁰⁾ ← initialize controls (e.g., constant 0.5)
  iter ← 0
  converged ← False
  
  WHILE NOT converged AND iter < 100
    
    // ═══════════════════════════════════════════════════════════════════
    // FORWARD SWEEP: Integrate State Equations
    // ═══════════════════════════════════════════════════════════════════
    
    t ← 0
    x ← x₀
    
    WHILE t < T_final
      // Compute state derivatives with current control u^(iter)
      ẋ ← MODEL_1_RHS(x, u^(iter)(t), θ)     // 35 ODEs
      
      // RK4 integration
      x(t+Δt) ← RK4_INTEGRATE(ẋ, x, θ, u^(iter), Δt)
      
      // Store trajectory for backward pass
      trajectory_x[t] ← x
      
      t ← t + Δt
    
    // ═══════════════════════════════════════════════════════════════════
    // BACKWARD SWEEP: Integrate Adjoint Equations
    // ═══════════════════════════════════════════════════════════════════
    
    t ← T_final
    η ← 0                    // Terminal condition η(T) = 0 for all 35 vars
    
    WHILE t > 0
      // Compute adjoint derivatives (using chain rule on ℋ)
      // η̇ᵢ = -∂ℋ/∂xᵢ = -p_sj·δ(i in I_sj) - Σⱼ ηⱼ·∂fⱼ/∂xᵢ
      
      x_t ← trajectory_x[t]  // Retrieve state at this time
      η̇ ← ADJOINT_RHS(η, x_t, u^(iter)(t), θ)  // 35 co-state equations
      
      // RK4 backward integration
      η(t-Δt) ← RK4_INTEGRATE_BACKWARD(η̇, η, Δt)
      
      // Store adjoint for control update
      trajectory_η[t] ← η
      
      t ← t - Δt
    
    // ═══════════════════════════════════════════════════════════════════
    // CONTROL UPDATE: Optimal u using ∂ℋ/∂u = 0
    // ═══════════════════════════════════════════════════════════════════
    
    FOR t = 0 TO T_final STEP Δt
      
      x_t ← trajectory_x[t]
      η_t ← trajectory_η[t]
      
      // Compute optimal u* = argmin_u ℋ(x_t, η_t, u, t)
      
      // u₁* : mosquito→human transmission control
      num_u1 ← 0
      FOR j=1 TO 3
        num_u1 += (η_E_mj - η_S_mj) · β_vp·IRR_mj·S_mj·I_v/N_p
        num_u1 += (η_E_fj - η_S_fj) · β_vp·IRR_fj·S_fj·I_v/N_p
      ENDFOR
      u_1_computed ← num_u1 / (p_{k+1})  // p_{k+1} = cost weight
      
      // u₂* : human→mosquito transmission control
      u_2_computed ← (η_E_v - η_S_v) · β_pv·S_v·Σ_I/N_p / (p_{k+2})
      
      // u₃* : mosquito population suppression
      u_3_computed ← η_S_a · a·c(t)·x·N_p / (p_{k+3})
      
      // Project onto feasible set [u_min, u_max]
      u₁_update ← clamp(u_1_computed, u_min, u_max)
      u₂_update ← clamp(u_2_computed, u_min, u_max)
      u₃_update ← clamp(u_3_computed, u_min, u_max)
      
      // Relaxation / Damping for stability
      ω ← 0.5  // Relaxation factor
      u₁^(iter+1)(t) ← (1-ω)·u₁^(iter)(t) + ω·u₁_update
      u₂^(iter+1)(t) ← (1-ω)·u₂^(iter)(t) + ω·u₂_update
      u₃^(iter+1)(t) ← (1-ω)·u₃^(iter)(t) + ω·u₃_update
    
    ENDFOR
    
    // ═══════════════════════════════════════════════════════════════════
    // CONVERGENCE CHECK
    // ═══════════════════════════════════════════════════════════════════
    
    error ← ||u^(iter+1) - u^(iter)||₂  // L2 norm difference
    
    IF error < 1e-4
      converged ← True
    ENDIF
    
    u^(iter) ← u^(iter+1)
    iter ← iter + 1
  
  ENDWHILE
  
  u_opt ← u^(iter)
  return u_opt

SUBROUTINE MODEL_1_RHS(x, u, θ):
  // Compute ẋ = f(t,x,u,θ) for all 35 variables
  
  // Extract compartments from state vector x
  S_m1, E_m1, I_m1, A_m1, R_m1 ← x[1:5]
  ... (all 35 indices)
  
  N_p ← sum of all human compartments
  N_v ← S_a + I_a + S_v + E_v + I_v
  c_t ← cos((t - 30)/365 · 2π)
  
  // Compute derivatives (ODE system from Part 1)
  dS_m1/dt ← -(1-u₁)·β_vp·IRR_m1·S_m1·I_v / N_p
  dE_m1/dt ← (1-u₁)·β_vp·IRR_m1·S_m1·I_v / N_p - q·ω'·E_m1 - (1-q)·ω·E_m1
  ... (all 35 derivatives)
  
  return [dS_m1/dt, dE_m1/dt, ..., dI_v/dt]^T

SUBROUTINE ADJOINT_RHS(η, x, u, θ):
  // Compute η̇ = -∂ℋ/∂x from Theorem 1 (Part 2)
  
  // This is complex algebra; example for one component:
  // dη_S_m1/dt = -∂ℋ/∂S_m1
  //            = η_S_m1·[(1-u₁)·β_vp·IRR_m1·I_v/N_p]
  //            - η_E_m1·[(1-u₁)·β_vp·IRR_m1·I_v/N_p]
  
  // Full system : 35 adjoint equations (See Theorem 1)
  
  return [dη_S_m1/dt, dη_E_m1/dt, ..., dη_I_v/dt]^T

FUNCTION clamp(x, min, max):
  if x < min return min
  if x > max return max
  return x
```

### 24.3 Pseudo-code Analyse Sensitivité ℛ_eff

```
╔════════════════════════════════════════════════════════════════════════════╗
║        ALGORITHM 3: 3D PARAMETER SWEEP & R_EFF ANALYSIS                   ║
╚════════════════════════════════════════════════════════════════════════════╝

INPUT:
  θ (from Algorithm 1)
  Model 2 (controlled)
  
OUTPUT:
  R_eff[u₁, u₂, u₃] for u_i ∈ [0, 1]
  Heatmaps, Contours
  Thresholds where R_eff < 1

MAIN ALGORITHM:

  n_grid ← 11  // 11 values per dimension
  u_values ← linspace(0, 1, n_grid)  // [0, 0.1, 0.2, ..., 1]
  
  FOR i = 0 TO n_grid-1
    FOR j = 0 TO n_grid-1
      FOR k = 0 TO n_grid-1
        
        u₁ ← u_values[i]
        u₂ ← u_values[j]
        u₃ ← u_values[k]
        
        // Evaluate system equilibrium or steady-state R_eff
        R_eff[i,j,k] ← COMPUTE_EFFECTIVE_R(u₁, u₂, u₃, θ)
        
      ENDFOR
    ENDFOR
  ENDFOR
  
  RETURN R_eff (3D array)

SUBROUTINE COMPUTE_EFFECTIVE_R(u₁, u₂, u₃, θ):
  
  // Method: Evaluate at disease-free equilibrium of controlled system
  // and compute ℛ_eff = √(ℛ_eff_vp × ℛ_eff_pv)
  
  // Adjust parameters
  β_vp_eff ← (1-u₁) · β_vp
  β_pv_eff ← (1-u₂) · β_pv
  N_v_eff ← (1-u₃) · x · N_p
  
  // Components (from decomposition)
  ℛ_vp_eff ← compute_vp_reproduction(β_vp_eff, θ)
  ℛ_pv_eff ← compute_pv_reproduction(β_pv_eff, N_v_eff, θ)
  
  ℛ_eff ← sqrt(ℛ_vp_eff × ℛ_pv_eff)
  
  return ℛ_eff

SUBROUTINE compute_vp_reproduction(β_vp_eff, θ):
  
  // ℛ_vp = Σ_j,s [ β_vp·IRR_sj·S_sj0 · (pathway_I or pathway_A) ] / N_p
  // pathway_I ← (1-q)·ω / γ
  // pathway_A ← q·ω' / γ'
  
  ℛ_vp ← 0
  
  FOR j=1 TO 3   // 3 age groups
    FOR s IN {m, f}
      S_s_j_0 ← equilibrium susceptibles
      
      pathway_I ← (1-q)·ω / (q·ω'+(1-q)·ω) / γ
      pathway_A ← q·ω' / (q·ω'+(1-q)·ω) / γ'
      
      ℛ_vp += β_vp_eff · IRR_sj · S_sj0 / N_p · (pathway_I + pathway_A)
  
  return ℛ_vp

SUBROUTINE compute_pv_reproduction(β_pv_eff, N_v_eff, θ):
  
  // ℛ_pv = β_pv·S_v0 / N_p · ϖ / (d+ϖ) · 1/d
  
  S_v_0 ← N_v_eff  // At equilibrium all susceptible initially
  
  ℛ_pv ← β_pv_eff · S_v_0 / N_p · (ϖ/(d+ϖ)) · (1/d)
  
  return ℛ_pv
```

---

## PARTIE 25 : IMPLÉMENTATION PYTHON REPRODUISANT ÉTAPES CLÉS

```python
# ╔════════════════════════════════════════════════════════════════════════════╗
# ║         IMPLEMENTATION PYTHON CHIKUNGUNYA MODEL - CHIKV_MODEL.PY           ║
# ╚════════════════════════════════════════════════════════════════════════════╝

import numpy as np
import pandas as pd
from scipy.integrate import odeint, solve_ivp
from scipy.optimize import minimize
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Tuple, Dict, List

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 0: DATA STRUCTURES & PARAMETERS
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class CHIKParameters:
    """Fixed biological parameters"""
    # Incubation & recovery (humans)
    q: float = 0.155       # Prob asymptomatic
    omega: float = 1/4.5   # Rate E → I_symp (day⁻¹)
    omega_p: float = 1/4.5 # Rate E → A_asymp (day⁻¹)
    gamma: float = 1/7     # Recovery I_symp (day⁻¹)
    gamma_p: float = 1/7   # Recovery A_asymp (day⁻¹)
    
    # Mosquito dynamics
    lambda_: float = 0.0902  # Larval emergence (day⁻¹)
    d: float = 1/7.4         # Natural mortality adult (day⁻¹)
    a: float = 0.145         # Birth rate (day⁻¹)
    varpi: float = 1/5.5     # EIP rate (day⁻¹)
    n: float = 0.0181        # Vertical transmission
    
    # Seasonality
    tau: float = 30      # Phase offset (days)
    T: float = 365       # Period (days)
    
    # Transmissions (TO ESTIMATE)
    beta_vp: float = None  # Mosquito→Human
    beta_pv: float = None  # Human→Mosquito
    x: float = None        # Mosquito/human ratio
    
    # IRR (Incidence Rate Ratios - TO ESTIMATE)
    IRR: Dict[str, Dict[str, float]] = None  # IRR_sj indexed by sex, age

    def seasonal_factor(self, t: float) -> float:
        """c(t) = cos((t-τ)/T · 2π)"""
        angle = 2 * np.pi * (t - self.tau) / self.T
        return np.cos(angle)

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 1: MODEL CLASS & ODE SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class CHIKVModel:
    """
    Age-sex structured Chikungunya transmission model
    States: S_sj, E_sj, I_sj, A_sj, R_sj for humans (s ∈ {m,f}, j ∈ {0,1,2})
            S_a, I_a, S_v, E_v, I_v for mosquitoes
    Total: 10k + 5 = 35 state variables (k=3)
    """
    
    def __init__(self, params: CHIKParameters, N_p: float):
        self.params = params
        self.N_p = N_p  # Total human population (constant)
        self.age_groups = 3
        self.sexes = ['m', 'f']
        self.state_dim = 10 * self.age_groups + 5  # 35
        
        # Indices mapping (for readability)
        self.idx = {}
        idx_counter = 0
        for sex in self.sexes:
            for age in range(self.age_groups):
                prefix = f"{sex}{age}"
                self.idx[f"S_{prefix}"] = idx_counter
                self.idx[f"E_{prefix}"] = idx_counter + 1
                self.idx[f"I_{prefix}"] = idx_counter + 2
                self.idx[f"A_{prefix}"] = idx_counter + 3
                self.idx[f"R_{prefix}"] = idx_counter + 4
                idx_counter += 5
        
        self.idx['S_a'] = 30
        self.idx['I_a'] = 31
        self.idx['S_v'] = 32
        self.idx['E_v'] = 33
        self.idx['I_v'] = 34
    
    def get_state_names(self) -> List[str]:
        """Return list of state variable names"""
        names = []
        for sex in self.sexes:
            for age in range(self.age_groups):
                prefix = f"{sex}{age}"
                for comp in ['S', 'E', 'I', 'A', 'R']:
                    names.append(f"{comp}_{prefix}")
        names.extend(['S_a', 'I_a', 'S_v', 'E_v', 'I_v'])
        return names
    
    def rhs_uncontrolled(self, x: np.ndarray, t: float) -> np.ndarray:
        """
        Right-hand side of uncontrolled ODEs (Model 1)
        dx/dt = f(t, x, θ)
        """
        p = self.params
        dx = np.zeros(self.state_dim)
        
        # Population sums
        N_v = x[self.idx['S_a']] + x[self.idx['I_a']] \
              + x[self.idx['S_v']] + x[self.idx['E_v']] + x[self.idx['I_v']]
        
        # Total infectious (for human→mosquito term)
        I_total = 0
        for sex in self.sexes:
            for age in range(self.age_groups):
                I_total += x[self.idx[f"I_{sex}{age}"]] \
                         + x[self.idx[f"A_{sex}{age}"]]
        
        # Seasonal factor
        c_t = p.seasonal_factor(t)
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # HUMAN EQUATIONS (by sex & age)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        for sex in self.sexes:
            for age in range(self.age_groups):
                idx_S = self.idx[f"S_{sex}{age}"]
                idx_E = self.idx[f"E_{sex}{age}"]
                idx_I = self.idx[f"I_{sex}{age}"]
                idx_A = self.idx[f"A_{sex}{age}"]
                idx_R = self.idx[f"R_{sex}{age}"]
                
                # Force of infection (mosquito→human)
                irr = p.IRR[sex][age]  # Incidence Rate Ratio
                foi = irr * p.beta_vp * x[idx_S] * x[self.idx['I_v']] / self.N_p
                
                # dS/dt
                dx[idx_S] = -foi
                
                # dE/dt
                dx[idx_E] = foi - p.q * p.omega_p * x[idx_E] \
                                 - (1 - p.q) * p.omega * x[idx_E]
                
                # dI/dt (symptomatic)
                dx[idx_I] = (1 - p.q) * p.omega * x[idx_E] - p.gamma * x[idx_I]
                
                # dA/dt (asymptomatic)
                dx[idx_A] = p.q * p.omega_p * x[idx_E] - p.gamma_p * x[idx_A]
                
                # dR/dt
                dx[idx_R] = p.gamma * x[idx_I] + p.gamma_p * x[idx_A]
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # MOSQUITO EQUATIONS (larval)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        idx_Sa = self.idx['S_a']
        idx_Ia = self.idx['I_a']
        
        # dS_a/dt = a·c(t)·(N_v - n·I_a) - λ·S_a
        dx[idx_Sa] = p.a * c_t * (p.x * self.N_p - p.n * x[idx_Ia]) \
                    - p.lambda_ * x[idx_Sa]
        
        # dI_a/dt = a·c(t)·n·I_a - λ·I_a
        dx[idx_Ia] = p.a * c_t * p.n * x[idx_Ia] - p.lambda_ * x[idx_Ia]
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # MOSQUITO EQUATIONS (adult)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        idx_Sv = self.idx['S_v']
        idx_Ev = self.idx['E_v']
        idx_Iv = self.idx['I_v']
        
        # dS_v/dt = λ·S_a - β_pv·S_v·I_total/N_p - d·S_v
        dx[idx_Sv] = p.lambda_ * x[idx_Sa] \
                    - p.beta_pv * x[idx_Sv] * I_total / self.N_p \
                    - p.d * x[idx_Sv]
        
        # dE_v/dt = β_pv·S_v·I_total/N_p - (d+ϖ)·E_v
        dx[idx_Ev] = p.beta_pv * x[idx_Sv] * I_total / self.N_p \
                    - (p.d + p.varpi) * x[idx_Ev]
        
        # dI_v/dt = λ·I_a + ϖ·E_v - d·I_v
        dx[idx_Iv] = p.lambda_ * x[idx_Ia] + p.varpi * x[idx_Ev] \
                    - p.d * x[idx_Iv]
        
        return dx
    
    def rhs_controlled(self, x: np.ndarray, t: float, u: Tuple[float, float, float]) -> np.ndarray:
        """
        Right-hand side with control interventions (Model 2)
        u = (u_1, u_2, u_3)
        """
        u1, u2, u3 = u
        
        p = self.params
        dx = np.zeros(self.state_dim)
        
        # Modified parameters
        beta_vp_eff = (1 - u1) * p.beta_vp
        beta_pv_eff = (1 - u2) * p.beta_pv
        N_v_eff = (1 - u3) * p.x * self.N_p
        
        # ... (similar structure to rhs_uncontrolled but with eff params)
        # [Code identical except β_vp → β_vp_eff, β_pv → β_pv_eff, N_v → N_v_eff]
        
        return dx

    def integrate_uncontrolled(self, x0: np.ndarray, t_span: Tuple[float, float], 
                               t_eval: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Integrate uncontrolled system
        Returns: (t, x) solution arrays
        """
        sol = solve_ivp(self.rhs_uncontrolled, t_span, x0, t_eval=t_eval, 
                       method='RK45', dense_output=False)
        return sol.t, sol.y.T
    
    def integrate_controlled(self, x0: np.ndarray, t_span: Tuple[float, float],
                            t_eval: np.ndarray, u_func):
        """
        Integrate controlled system where u = u_func(t)
        u_func : callable returning (u1, u2, u3) at time t
        """
        def rhs_wrapper(t, x):
            u = u_func(t)
            return self.rhs_controlled(x, t, u)
        
        sol = solve_ivp(rhs_wrapper, t_span, x0, t_eval=t_eval,
                       method='RK45', dense_output=False)
        return sol.t, sol.y.T

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 2: REPRODUCTION NUMBER COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════

class ReproductionNumber:
    """Compute and decompose R₀"""
    
    @staticmethod
    def compute_R0_vp(params: CHIKParameters, N_p: float) -> float:
        """
        ℛ₀(vp) = Σ_j,s [ β_vp·IRR_sj·S_sj0 · f(I+A) ] / N_p
        """
        R0_vp = 0
        for sex in ['m', 'f']:
            for age in range(3):
                irr = params.IRR[sex][age]
                
                # Pathways
                pathway_I = (1 - params.q) * params.omega / \
                           (params.q * params.omega_p + (1 - params.q) * params.omega) / params.gamma
                pathway_A = params.q * params.omega_p / \
                           (params.q * params.omega_p + (1 - params.q) * params.omega) / params.gamma_p
                
                # Assume S_sj0 ≈ N_p * pop_fraction_sj
                S_sj0 = N_p * 0.5 / 3  # Rough estimate: equal split
                
                R0_vp += params.beta_vp * irr * S_sj0 / N_p * (pathway_I + pathway_A)
        
        return R0_vp
    
    @staticmethod
    def compute_R0_pv(params: CHIKParameters, N_p: float) -> float:
        """
        ℛ₀(pv) = β_pv·S_v0 / N_p · ϖ/(d+ϖ) · 1/d
        """
        S_v0 = params.x * N_p  # Initial susceptible mosquitoes
        R0_pv = params.beta_pv * S_v0 / N_p * (params.varpi / (params.d + params.varpi)) * (1 / params.d)
        return R0_pv
    
    @staticmethod
    def compute_R0(params: CHIKParameters, N_p: float) -> float:
        """ℛ₀ = √(ℛ₀(vp) × ℛ₀(pv))"""
        R0_vp = ReproductionNumber.compute_R0_vp(params, N_p)
        R0_pv = ReproductionNumber.compute_R0_pv(params, N_p)
        R0 = np.sqrt(R0_vp * R0_pv)
        return R0, R0_vp, R0_pv

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 3: PARAMETER ESTIMATION (SIMPLIFIED PMCMC)
# ═══════════════════════════════════════════════════════════════════════════

class PMCMCEstimator:
    """Simplified Particle MCMC for parameter estimation"""
    
    def __init__(self, model: CHIKVModel, data: pd.DataFrame):
        self.model = model
        self.data = data  # Observed cases y_sj(t)
    
    def likelihood(self, x_simulated: np.ndarray, y_observed: np.ndarray) -> float:
        """
        Poisson likelihood: p(y|x) = ∏ Poisson(y | λ=extracted(x))
        """
        # Extract I_sj from simulated state
        I_simulated = []
        for sex in ['m', 'f']:
            for age in range(3):
                idx = self.model.idx[f"I_{sex}{age}"]
                I_simulated.append(x_simulated[:, idx])
        I_simulated = np.array(I_simulated).T  # Shape: (T, 6)
        
        # Poisson log-likelihood
        log_lik = 0
        eps = 1e-10
        for t in range(len(y_observed)):
            for sj in range(6):
                lambda_t = max(I_simulated[t, sj], eps)
                log_lik += y_observed[t, sj] * np.log(lambda_t) - lambda_t
        
        return log_lik
    
    def estimate(self, theta_init: Dict, n_iter: int = 100) -> Dict:
        """
        Simple MH-MCMC (not full Particle Filter for brevity)
        Returns posterior samples
        """
        samples = {key: [] for key in theta_init.keys()}
        
        theta_current = theta_init.copy()
        accepted = 0
        
        for it in range(n_iter):
            # Propose (Gaussian RW)
            theta_star = {k: v + 0.1 * np.random.randn() for k, v in theta_current.items()}
            
            # Ensure positive
            theta_star = {k: max(v, 0.01) for k, v in theta_star.items()}
            
            # Evaluate likelihood
            self.model.params.beta_vp = theta_star.get('beta_vp', theta_current['beta_vp'])
            self.model.params.beta_pv = theta_star.get('beta_pv', theta_current['beta_pv'])
            
            t, x_star = self.model.integrate_uncontrolled(...)  # Needs x0
            lik_star = self.likelihood(x_star, self.data.values)
            
            self.model.params.beta_vp = theta_current['beta_vp']
            self.model.params.beta_pv = theta_current['beta_pv']
            t, x_curr = self.model.integrate_uncontrolled(...)
            lik_curr = self.likelihood(x_curr, self.data.values)
            
            # MH step
            log_alpha = lik_star - lik_curr
            if np.log(np.random.rand()) < log_alpha:
                theta_current = theta_star
                accepted += 1
            
            # Store sample
            for key in samples.keys():
                samples[key].append(theta_current[key])
        
        print(f"Acceptance rate: {100*accepted/n_iter:.1f}%")
        return {k: np.array(v) for k, v in samples.items()}

# ═══════════════════════════════════════════════════════════════════════════
# SECTION 4: DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    # Initialize parameters
    N_p = 7.3e6  # Foshan population
    
    params = CHIKParameters(
        beta_vp=0.3,  # Would be estimated
        beta_pv=0.3,  # Would be estimated
        x=10,         # Would be estimated
        IRR={'m': {0: 1.0, 1: 2.5, 2: 0.8},
             'f': {0: 1.0, 1: 2.3, 2: 0.9}}
    )
    
    # Create model
    model = CHIKVModel(params, N_p)
    
    # Initial conditions (disease-free + few infected)
    x0 = np.zeros(35)
    # Set initial susceptibles
    for sex in ['m', 'f']:
        for age in range(3):
            idx_S = model.idx[f"S_{sex}{age}"]
            x0[idx_S] = N_p * 0.5 / 3  # Half population, equally distributed
    
    # Initial infected (small)
    x0[model.idx['I_m1']] = 1
    x0[model.idx['S_v']] = params.x * N_p * 0.8
    x0[model.idx['S_a']] = params.x * N_p * 0.2
    
    # Integrate
    t_prep = np.linspace(0, 33, 100)  # Preparedness: 16 Jun - 18 Jul (33 days)
    
    t, x = model.integrate_uncontrolled(x0, (0, 33), t_prep)
    
    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(t, x[:, model.idx['I_m1']], 'r-', label='I_males_15-59')
    plt.plot(t, x[:, model.idx['I_f1']], 'o-', label='I_females_15-59')
    plt.xlabel('Days')
    plt.ylabel('Infected (I)')
    plt.title('CHIKV Epidemic Curve - Preparedness Phase')
    plt.legend()
    plt.grid(True)
    plt.savefig('/home/claude/CHIKV_example_output.png', dpi=150, bbox_inches='tight')
    print("Plot saved to CHIKV_example_output.png")
    
    # Compute R0
    R0, R0_vp, R0_pv = ReproductionNumber.compute_R0(params, N_p)
    print(f"\nℛ₀ = {R0:.4f}")
    print(f"ℛ₀(vp) = {R0_vp:.4f}")
    print(f"ℛ₀(pv) = {R0_pv:.4f}")

# ═══════════════════════════════════════════════════════════════════════════
# END OF FILE
# ═══════════════════════════════════════════════════════════════════════════
```

---

## PARTIE 26 : AMBIGUÏTÉS ET PARAMÈTRES MANQUANTS

### 26.1 Paramètres Non Spécifiés Numériquement

| Paramètre | Relevance | Status |
|-----------|-----------|---------|
| p_sj (weights in objective L) | Critique pour allocation resources | **MANQUANT** |
| p_{k+1}, p_{k+2}, p_{k+3} (cost weights) | Pivot balance u₁ vs u₂ vs u₃ | **MANQUANT** |
| Dates précises transitions contrôles | Réconstruction exacte | **IMPLICITE** |
| Population âge-sexe (détail) | Calcul IRR | Tableau S1 (annexe) |
| Cas asymptomatiques observés | Validation modèle | **PAS RAPPORTÉS** |

### 26.2 Ambiguïtés Méthodologiques

1. **Détermination du groupe de référence IRR** : Pourquoi males 0-14?
2. **Calcul IRR temporel** : Constant vs variant par phase?
3. **Offset diagnostic** : Symptôme→Diagnostic = 1-2 jours assumé
4. **Retards implémentation contrôles** : Assumé 0 jours
5. **Compliance taux réels vs modélisés** : u_proclamé ≠ u_effectif?

### 26.3 Limitations Documentées

```
§ LIMITACIONES EXPLICITAS
1. Pas de vaccination (Ixchiq)
2. Pas de variables climatiques (T, RH, précipitation)
3. Pas de structure spatiale (homogeneous mixing)
4. Pas de mobility données (importation)
5. Pas de lag reporting exact
```

---

Fin PARTIE 3 - PIPELINE COMPLET + IMPLÉMENTATION

**À FAIRE ENSUITE :**
1. Tests unitaires Python (validation ODE)
2. Fit réel données Foshan (PMCMC complète)
3. Optimisation contrôle (forward-backward sweep)
4. Validation croisée sensitivité
5. Génération figures publication-quality
