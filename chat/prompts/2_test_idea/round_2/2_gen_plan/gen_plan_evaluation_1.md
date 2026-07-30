# gen_plan_evaluation_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_jv2O_AqFqWEi` — Algorithmically Weighted Ensemble Forecasting for Adaptive Time Series Dynamics
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_evaluation_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 22:20:29 UTC

````
<hypothesis>
kind: hypothesis
title: Algorithmically Weighted Ensemble Forecasting
hypothesis: >-
  Time series predictions improve when base forecasting models are dynamically weighted based on their algorithmic complexity
  (measure of simplicity) relative to recent prediction accuracy, rather than accuracy alone. Simple models get priority when
  data is abundant and patterns are stable, while complex models are preferred when data reveals rich dynamics that simpler
  models miss.
motivation: >-
  Forecasting research has dominated on two incomplete objectives: (1) maximize prediction accuracy, leading to complex overfit
  models that fail under distribution shift, or (2) minimize complexity alone, producing oversimplified predictions that ignore
  genuine structure. Neither approach optimizes the fundamental trade-off between what a model can capture and how much evidence
  we have to warrant capturing it. By making complexity an ONLINE variable that shifts with data abundance and volatility,
  we create a principled adaptive mechanism that would optimize long-run prediction ROI. This could fundamentally change how
  we approach short-horizon forecasting where computational constraints and overfitting risks are highest.
assumptions:
- >-
  Time series exhibits gradually decaying complexity (over time, patterns stabilize from noise to signal, then from simple
  to complex structure)
- >-
  Simple and complex models have complementary strengths (simple models generalize, complex models exploit fine-grained patterns)
- >-
  Data quality does not fundamentally degrade over training horizon (no systematic bias accumulation)
- >-
  Algorithmic complexity can be reliably estimated or approximated for forecasting models
investigation_approach: >-
  Build a multi-model ensemble containing both simple models (last-value, 3-point moving average, linear regression) and complex
  models (LSTM, ARIMA). Implement an online complexity-weighted mechanism where each model receives: (1) a performance score
  (negative error on recent windows), and (2) a complexity penalty (inverse of estimated model complexity). Models' dynamic
  weights are the product of their recent performance and their current complexity penalty signal. Test on diverse synthetic
  time series (random noise, sinusoidal with drift, chaotic Lorenz, non-stationary AR processes) and compare against (a) equal-weighted
  ensemble, (b) performance-only weighting (Bayesian model averaging), (c) naive Last-Value forecast, and (d) 3-point moving
  average.
success_criteria: >-
  The complexity-weighted ensemble will significantly outperform the simple baselines (p<0.01 for MSE and RMSE metrics) across
  at least 70% of test environments. Crucially, it will show superior performance on series with moderate complexity where
  neither oversimplification nor overfitting are obvious choices: non-stationary AR(2) processes with slowly varying coefficients,
  and Lorenz-like chaotic systems with noise. Additionally, complexity-weighted weights should exhibit clear dynamics tracking
  data characteristics (diverging weights when series transitions from noisy to structure-rich phases).
related_works:
- >-
  Abélès et al. (2024, arXiv:2402.14684): Uses online learning expert aggregation to track Markovian variance switches in
  time series. DIFFERENCE: Focuses on detecting regime changes, not managing accuracy-complexity trade-off.
- >-
  Gunasekaran et al. (2025, Nature Communications): Applies predictive coding with future-guided reconstruction. DIFFERENCE:
  Uses two-teacher-student architecture, not complexity-weighted ensemble.
- >-
  Raftery (1995): Bayes model averaging weights models by posterior predictive accuracy. DIFFERENCE: Static Bayesian weights
  based on held-out likelihood, not dynamic complexity-adjusted weighting.
- >-
  Small (2002, Physical Review E): Uses Minimum Description Length (MDL) to select neural network architectures for time series.
  DIFFERENCE: Static architecture selection on static data, not online complexity-aware weighting of diverse models in tournaments.
- >-
  Wood et al. (2023, JMLR): Studies diversity in ensemble learning. DIFFERENCE: Optimizes for prediction agreement variance,
  not complexity-relative accuracy.
inspiration: >-
  Cross-field transfer from OPTIMIZATION THEORY (online learning with expert advice) and STATISTICAL LEARNING THEORY (PAC
  bounds, Occam's Razor principles). Core mechanism: Bayesian portfolio optimization where each "expert" (forecasting model)
  gets both a performance PREDICTION BETTER and a INVERSE COMPLEXITY PREDICTION COST, with all updates happening ONLINE without
  storing full training history.
terms:
- term: Algorithmic complexity
  definition: >-
    The length of the shortest computer program (in a fixed language) that can generate the model's predictions or the underlying
    pattern being modeled. Lower complexity indicates simpler, more parsimonious models.
- term: Online weighting
  definition: >-
    Dynamic adjustment of model weights after each new data point without retraining models, using only a sliding window of
    recent errors and updates.
- term: Prediction ROI
  definition: >-
    The ratio of prediction accuracy improvement to computational/cognitive cost - a measure of how much precision we gain
    per unit of complexity incurred.
- term: Complexity penalty signal
  definition: >-
    A dynamically updating weight inversely proportional to model complexity, designed to favor simpler models when data is
    abundant or noisy, without completely discarding them when they might capture genuine structure.
summary: >-
  Forecasting improves when we dynamically balance model complexity against prediction accuracy rather than optimizing either
  dimension alone. By using online learning principles to maintain complexity-aware weights across Simple vs. Complex models,
  we can adaptively choose which modeling approach fits each regime of the time series.
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: evaluation_iter2_dir3
type: evaluation
objective: >-
  Perform rigorous statistical analysis, significance testing, and weight dynamics analysis on forecasting results
approach: >-
  Compute MSE and RMSE across all models and environments, conduct Wilcoxon signed-rank tests for significance, analyze weight
  trajectories relative to series complexity changes, and perform ablation studies separating complexity penalties.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle
</artifact_executor_scope>

<artifact_planning_rules>
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for evaluation artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_plan/gen_plan_evaluation_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EVALUATION artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "metrics_descriptions": {
      "description": "What metrics will be computed and how they're defined",
      "title": "Metrics Descriptions",
      "type": "string"
    },
    "metrics_justification": {
      "description": "Why these metrics are the right ones - what do they tell us about the hypothesis",
      "title": "Metrics Justification",
      "type": "string"
    }
  },
  "required": [
    "title",
    "metrics_descriptions",
    "metrics_justification"
  ],
  "title": "EvaluationPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_plan/gen_plan_evaluation_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-30 22:20:29 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```
