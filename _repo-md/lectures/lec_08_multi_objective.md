---
title: Multi-Objective Optimization
subtitle: Lecture 8 - Management Science
author: Dr. Tobias Vlćek
format:
  revealjs:
    footer: ' {{< meta title >}} | {{< meta author >}} | [Home](lec_08_multi_objective.qmd)'
    output-file: lec_08_presentation.html
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


# <span class="flow">Introduction</span>

## **<span class="invert-font">Client Briefing: EcoExpress Logistics</span>**

. . .

<span class="invert-font">Operations Director's Dilemma:</span>

<span class="invert-font fragment">"EU regulations demand 40% emission cuts, but we can't sacrifice <span class="highlight">profitability</span>, <span class="highlight">service quality</span>, or <span class="highlight">reliability</span>!"</span>

## The Fleet Challenge

<span class="highlight">EcoExpress operates regional last-mile delivery across 3 cities</span>

-   EU Green Deal: 40% emission reduction by 2025
-   Rising fuel costs (€2.1/L diesel)
-   Amazon entering our market (speed pressure)
-   Driver shortage (need automation-friendly vehicles)

. . .

<span class="question">Question:</span> How do we transform our fleet while staying competitive?

## Today's Learning Objectives

<span class="highlight">By the end of this lecture, you will be able to:</span>

1.  Explain why most decisions involve competing objectives
2.  Identify and visualize Pareto optimal solutions
3.  Apply normalization techniques to make objectives comparable
4.  Implement apporaches to find trade-off solutions
5.  Make decisions from a Pareto frontier

## Quick Recap: Local Search

<span class="highlight">Last week we optimized routes for delivery:</span>

-   Started with greedy construction (e.g. Nearest Neighbor)
-   Improved with local search (e.g. 2-opt)
-   Considered time windows
-   **But: We only optimized distance**

. . .

<span class="question">Question:</span> What if we also care about emissions, cost, AND customer satisfaction?

# <span class="flow">The Problem</span>

## Single vs Multi-Objective

**Single Objective**

-   <span class="highlight">"Minimize total distance"</span>
-   Clear winner. Easy, right!

. . .

**Multiple Objectives**

-   <span class="highlight">"Minimize cost AND emissions AND maximize speed"</span>
-   No clear answer...

. . .

<span class="question">Question:</span> Any idea how to approach this?

## EcoExpress Vehicle Options

| Type | Purchase Cost (€) | Operating (€/km) | CO2 (g/km) | Speed (km/h) | Capacity (parcels) | Reliability |
|----|----|----|----|----|----|----|
| E-Truck | 75000 | 0.18 | 0 | 55 | 300 | 0.93 |
| Hybrid | 45000 | 0.25 | 95 | 65 | 200 | 0.95 |
| Diesel | 35000 | 0.38 | 185 | 70 | 250 | 0.88 |
| E-Bike | 12000 | 0.05 | 0 | 30 | 50 | 0.98 |
| Auto | 95000 | 0.12 | 0 | 40 | 150 | 0.94 |

. . .

<span class="question">Question:</span> Which vehicle is "best" for EcoExpress?

## Trade-offs Everywhere

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-3-output-1.png" width="760" height="465" />

. . .

> **Important**
>
> Every vehicle excels at something different!

## Real Business Constraints

<span class="highlight">Beyond the numbers, consider:</span>

-   **EU regulations:** Carbon tax of €100/ton CO₂ starting 2025
-   **Competition:** Amazon promises 2-hour delivery
-   **Labor market:** Autonomous vehicles reduce driver dependency
-   **Urban zones:** Zero-emission zones in city centers
-   **Peak times:** Black Friday = 3x normal volume

. . .

> **Important**
>
> There is no single "optimal" solution - only trade-offs

# <span class="flow">Pareto Optimality</span>

## Dominated Solutions

<span class="highlight">A solution is dominated if another solution is:</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-4-output-1.png" width="754" height="467" />

. . .

> **Important**
>
> Better in at least one objective and not worse in any objective!

## The Pareto Frontier

<span class="highlight">The Pareto frontier is the set of all non-dominated solutions</span>

-   No solution is objectively "better"
-   Each represents a different trade-off
-   Moving along frontier: gain in one objective, loss in another
-   Decision makers choose based on **preferences**

. . .

<span class="question">Question</span> Do you think you get the idea?

## Find the Non-Dominated

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-5-output-1.png" width="756" height="467" />

. . .

<span class="question">Question:</span> Which fleets are non-dominated?

## Three+ Objectives

<span class="highlight">With 3 objectives, the Pareto frontier becomes a surface:</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-6-output-1.png" width="446" height="467" />

. . .

> **Important**
>
> Harder to visualize, but same principle applies!

# <span class="flow">Fleet Composition Problem</span>

## The Fleet Challenge

<span class="highlight">EcoExpress needs to replace their 80 diesel vans</span>

-   Must meet **EU regulation**: Average emissions ≤ 111 g CO₂/km
-   Need capacity for **22,000 parcels/day**
-   Must balance **cost vs. service quality**
-   5 vehicle types available, each with trade-offs

. . .

<span class="question">Question:</span> How do we choose the right mix?

## Vehicle Options Recap

| Type | Purchase Cost (€) | Operating (€/km) | CO2 (g/km) | Speed (km/h) | Capacity (parcels) | Reliability |
|----|----|----|----|----|----|----|
| E-Truck | 75000 | 0.18 | 0 | 55 | 300 | 0.93 |
| Hybrid | 45000 | 0.25 | 95 | 65 | 200 | 0.95 |
| Diesel | 35000 | 0.38 | 185 | 70 | 250 | 0.88 |
| E-Bike | 12000 | 0.05 | 0 | 30 | 50 | 0.98 |
| Auto | 95000 | 0.12 | 0 | 40 | 150 | 0.94 |

. . .

<span class="highlight">Notice: No single vehicle is "best" at everything!</span>

## Fleet Composition Framework

<span class="highlight">This is a discrete selection problem, not continuous allocation</span>

**Decision Variables:**

-   Fleet: How many of each vehicle type? (discrete/integer)
-   $n_i$ = number of vehicles of type $i$ (integers!)
-   Example: $n_{\text{E-Truck}} = 20$, $n_{\text{Hybrid}} = 30$, etc.

## Objective 1: Total Cost

<span class="highlight">Purchase cost + Operating cost over 3 years</span>

$$\text{Total Cost} = \sum_{i} n_i \cdot \left( P_i + O_i \cdot d \cdot y \right)$$

-   $n_i$ = quantity of vehicle type $i$
-   $P_i$ = purchase cost of vehicle type $i$
-   $O_i$ = operating cost per km for type $i$
-   $d$ = daily distance × days per year
-   $y$ = years

## Objective 2: Service Score

<span class="highlight">Composite measure of fleet performance</span>

$$\text{Service Score} = 0.5 \cdot C_{\text{score}} + 0.3 \cdot R_{\text{score}} + 0.2 \cdot S_{\text{score}}$$

-   $C_{\text{score}} = \min\left(1.0, \frac{\text{Total Capacity}}{22000}\right)$ (capacity adequacy)
-   $R_{\text{score}} = \frac{\sum n_i \cdot r_i}{\sum n_i}$ (weighted avg. reliability)
-   $S_{\text{score}} = \frac{\sum n_i \cdot s_i}{70 \cdot \sum n_i}$ (normalized speed)

. . .

> **Note**
>
> Service score captures multiple performance dimensions in one metric!

## Hard Constraint: Emissions

<span class="highlight">EU regulation creates a feasibility boundary</span>

$$\text{Average CO}_2 = \frac{\sum_{i} n_i \cdot e_i}{\sum_{i} n_i} \leq 111 \text{ g/km}$$

Where $e_i$ = CO₂ emissions per km for vehicle type $i$

. . .

**This eliminates some solutions:**

-   All diesel vans: 185 g/km \> 111
-   Mix with too many diesel: Still violates
-   Zero-emission + some diesel: Might work

## Data Source

<span class="highlight">Where Do These Numbers Come From?</span>

. . .

**Vehicle Specifications:**

-   **Purchase costs**: Manufacturer quotes, market research
-   **Operating costs**: Fuel/electricity prices, maintenance records
-   **Capacity**: Vehicle specs (cargo volume, weight limits)
-   **Reliability**: Historical uptime data, manufacturer warranties
-   **EU Standards**: WLTP certification for vehicles
-   **Electric vehicles**: Grid carbon intensity (kWh → g CO₂)

## Example Fleet Comparison

    Three Fleet Strategies:

             name    cost  service        co2  capacity  vehicles
     Cost-Focused 28.9996 0.809705 120.714286     15000        70
         Balanced 19.0478 0.731840  33.928571     13250        70
    Green-Focused 15.3102 0.695373   0.000000     12750        75


    Cost-Focused: ✗ VIOLATES (CO2: 120.7 g/km)
    Balanced: ✓ Compliant (CO2: 33.9 g/km)
    Green-Focused: ✓ Compliant (CO2: 0.0 g/km)

. . .

<span class="question">Question:</span> Which strategy would you choose?

## Visualizing Fleet Trade-offs

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-9-output-1.png" width="728" height="465" />


    Generated 68 feasible fleet compositions

. . .

> **Important**
>
> Each point is a different fleet mix, all meeting emissions constraint!

# <span class="flow">Solution Approaches</span>

## Multi-Objective Optimization

<span class="highlight">You can use optimization solvers or heuristics!</span>

. . .

**With Optimization Solvers**

-   Weighted Sum Method
-   ε-Constraint Method  
-   Goal Programming
-   **Optimal solutions**
-   **Need mathematical model**

**With Heuristics**

-   Weighted Greedy Construction
-   Multi-Objective Local Search
-   Metaheuristics
-   **Good solutions, fast**
-   **No optimality proof**

. . .

> **Important**
>
> In this lecture we use heuristic approaches!

## Foundation: Extreme Points

<span class="highlight">First step for BOTH approaches - find the boundaries:</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-10-output-1.png" width="760" height="467" />

. . .

<span class="question">Question:</span> Why is normalization essential?

## Critical: Normalization

<span class="highlight">Without it, your analysis is meaningless</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-11-output-1.png" width="816" height="466" />

. . .

<span class="question">Question:</span> Any intuition on how to do \[0,1\] normalization?

## How to Normalize

<span class="highlight">The Normalization Formula for \[0,1\]</span>

$$\text{Normalized}_i = \frac{x_i - x_{min}}{x_{max} - x_{min}}$$

. . .

**In Python, this is rather simple!**

. . .

``` python
def normalize_objectives(data):
    return (data - data.min()) / (data.max() - data.min())

# Now weights actually mean something
weighted_score = w1 * normalize(cost) + w2 * normalize(emissions)
```

. . .

> **Tip**
>
> Easy, right?

## Extreme Points

<span class="highlight">There are several reasons why extreme points matter:</span>

1.  **Trade-off Space**: Min/max values bound your Pareto frontier
2.  **Enable Proper Normalization**: Need ranges for scaling to \[0,1\]
3.  **Feasibility**: If single objectives not achievable, problem infeasible
4.  **Stakeholder**: "Best cost is €50k, best emissions is 40kg"

. . .

**Implementation Pattern:**

``` python
def find_extreme_points(problem):
    # Solve for minimum cost (ignore emissions)
    min_cost_solution = minimize(cost_objective, constraints)
    # Solve for minimum emissions (ignore cost)
    min_emissions_solution = minimize(emissions_objective, constraints)
```

## Computational Complexity

<span class="highlight">How hard does it get with more objectives?</span>

. . .

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-12-output-1.png" width="755" height="467" />

. . .

> **Tip**
>
> Why? Because there are just way more potential solutions to check!

## Solver-Based Methods

<span class="highlight">Quick overview - you won't implement these in assignments</span>

1.  **Weighted Sum:** Minimize $w_1 \times \text{cost} + w_2 \times \text{emissions}$
    -   Simple, fast for convex problems
2.  **ε-Constraint:** Minimize cost subject to emissions $\leq \varepsilon$
    -   Systematically vary $\varepsilon$ to find complete frontier
3.  **Goal Programming:** Minimize deviations from targets
    -   Set target for each objective, minimize weighted deviations

. . .

> **Note**
>
> **For your fleet optimization:** You'll use **heuristic approaches** instead!

# <span class="flow">Heuristic Approach</span>

## The Heuristic Strategy

<span class="highlight">For problems without mathematical models</span>

. . .

1.  **Construction:** Build initial solutions with weighted greedy
2.  **Improvement:** Multi-objective local search
3.  **Selection:** Filter dominated solutions to find Pareto frontier

. . .

> **Important**
>
> **Key difference from solvers:**
>
> -   **Solvers:** Need mathematical model, guarantee optimality
> -   **Heuristics:** Work with any evaluation function, find good solutions fast

## Why Heuristics?

<span class="highlight">Depending on the problem:</span>

-   **Combinatorial explosion**
-   Huge solution space even for one problem
-   Evaluating one solution might thus take too long
-   Need diverse Pareto frontier, not just one "optimal" solution
-   Open Source Solvers too slow
-   Commercial solvers too expensive

. . .

<span class="question">Question:</span> How do we build good solutions without a solver?

## The Three-Stage Heuristic Process

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-13-output-1.png" width="756" height="468" />

. . .

<span class="highlight">This is what you'll implement in your assignments!</span>

# <span class="flow">Construction & Improvement</span>

## Construction Methods for MOO

<span class="highlight">How to build initial solutions when you have multiple objectives?</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-14-output-1.png" width="788" height="466" />

. . .

> **Note**
>
> Three choices (for starters). Let's check them out!

## Weighted Greedy Construction

<span class="highlight">Making greedy choices on a weighted objective</span>

1.  **Choose weight vector** w = (w₁, w₂)
2.  **At each step, pick the choice that minimizes:**
    $$w_1 \cdot \text{cost}(x) + w_2 \cdot \text{emissions}(x)$$
3.  **Build complete solution greedily**
4.  **Repeat** with different weights to explore frontier

. . .

> **Tip**
>
> Different weights explore different trade-offs! Easy, right?

## Sequential Greedy (Lexicographic)

<span class="highlight">Optimize one objective at a time, in priority order</span>

1.  **Rank objectives by priority**
    -   E.g. cost (most important) and then emissions (tie-breaker)
2.  **At each step:**
    -   Find choices that minimize **primary** objective
    -   If tie → use **secondary** objective
3.  **Build one working solution**

. . .

> **Tip**
>
> We could also accept primary values within 10% of best so secondary has more influence!

## Diverse Starting Pool

<span class="highlight">Generate many random solutions, keep the non-dominated ones</span>

1.  **Generate N random solutions (e.g., N=100)**
2.  **Evaluate all solutions on both objectives**
3.  **Filter to keep only non-dominated solutions**
4.  **Result:** A diverse set of Pareto-optimal solutions

. . .

> **Tip**
>
> -   Explores **entire** solution space
> -   No bias toward specific weights
> -   Great for **warm-starting** local search

## Local Search for Multi-Objective

<span class="highlight">Special moves that improve multiple objectives:</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-15-output-1.png" width="754" height="465" />

. . .

<span class="question">Question:</span> Which moves are acceptable?

## MOO Local Search Rules

<span class="highlight">Accept a move if:</span>

1.  **Dominance**: New solution dominates current (win-win!)
2.  **Trade-off**: Improves primary, acceptable loss in secondary
3.  **Probabilistic**: Use temperature (like simulated annealing)

. . .

> **Important**
>
> Always keep all your objectives in mind when making decisions.

# <span class="flow">From Pareto Front to Decision</span>

## How to Choose!

1.  <span class="highlight">The Knee Point:</span> Find the "elbow" where improvement slows
2.  <span class="highlight">Satisficing Levels:</span> Set minimum acceptable thresholds
    -   **Cost** must be \< €100k (budget constraint)
    -   **Emissions** must be \< 100 kg (regulatory limit)
    -   **Service level** must be \> 90% (customer requirement)
3.  <span class="highlight">Stakeholder Preferences:</span> Let business priorities guide
    -   **Sustainability:** Minimum emissions that meets constraints
    -   **Operations:** Maximum service level within budget

## Weighting has an Impact

<span class="highlight">The weights thus reflect your values!</span>

<img src="lec_08_multi_objective_files/figure-markdown_strict/cell-16-output-1.png" width="755" height="465" />

. . .

> **Tip**
>
> Depending on your weight, the choice will vary.

# <span class="flow">Advanced</span>

## Speed vs Sustainability Dilemma

<span class="highlight">The Three-Way Trade-off in E-Commerce</span>

1.  **Minimize Delivery Time** (1-day/2-hour promise)
2.  **Minimize Cost** (fuel, labor, fulfillment)
3.  **Minimize Environmental Impact** (carbon footprint)

. . .

<span class="highlight">Faster delivery = More vehicles less full = Higher emissions</span>

. . .

<span class="question">Question:</span> What could retailers do?

## Moving the Frontier

<span class="highlight">Instead of point on the frontier, move the entire frontier:</span>

. . .

<span class="question">Question:</span> Any idea of examples?

. . .

> **Tip**
>
> R&D can fundamentally change what's possible!

# <span class="flow">Briefing</span>

## Today

**Hour 2: This Lecture**

-   Multi-objective
-   Pareto optimality
-   Weighted greedy
-   Local search MOO

**Hour 3: Notebook**

-   Bean Counter CEO
-   Find Pareto frontier
-   Apply weighted greedy
-   Normalize objectives

**Hour 4: Competition**

-   Fleet composition
-   Vehicle selection
-   Cost vs service
-   Justify choice!

## The Competition Challenge

<span class="highlight">EcoExpress Sustainable Fleet Design</span>

. . .

1.  **Select** optimal fleet mix (5 vehicle types)
2.  **Balance** cost vs. service score
3.  **Meet** EU emission constraint (≤ 111 g CO₂/km)
4.  **Ensure** sufficient capacity (22,000 parcels/day)

. . .

> **Important**
>
> Find the best trade-off for your business priorities!

## Choosing Your MOO Approach

<span class="highlight">Different situations call for different methods:</span>

| Situation        | Best                  | Why                 |
|------------------|-----------------------|---------------------|
| Clear priorities | Sequential greedy     | Fast, hierarchy     |
| Exploring        | Weighted greedy       | Different solutions |
| Many solutions   | Diverse pool          | Builds frontier     |
| Quick solution   | Single weighted       | One good compromise |
| Improve existing | Multi-objective local | Refines trade-offs  |

. . .

> **Tip**
>
> **Competition?** Generate diverse pool or weigted, then improve with local search.

## Implementation Pitfalls to Avoid

<span class="highlight">Common bugs that cost you time:</span>

1.  **Forgetting to Normalize**
    -   Always normalize to \[0,1\] first!
2.  **Optimizing Too Many Objectives**
    -   2-3: Manageable, 4+: Exponentially harder
    -   Combine related objectives or use constraints
3.  **Not Checking Solution Feasibility**
    -   Always verify constraints after optimization

## Summary

<span class="highlight">Key Takeaways:</span>

-   Real decisions have multiple conflicting objectives
-   Pareto frontier shows all rational trade-offs
-   Normalization is essential for fair comparison
-   Weights reflect values, make them explicit
-   Visualization crucial for decision-making

## Break!

<span class="highlight">Take 20 minutes, then we start the practice notebook</span>

**Next up:** You'll become Bean Counter's expert

**Then:** The Sustainability competition
