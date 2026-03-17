---
title: Introduction to Metaheuristics
subtitle: Lecture 9 - Management Science
author: Dr. Tobias Vlćek
format:
  revealjs:
    footer: ' {{< meta title >}} | {{< meta author >}} | [Home](lec_09_metaheuristics.qmd)'
    output-file: lec_09_presentation.html
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


# <span class="flow">Introduction</span>

## **<span class="invert-font">Client Briefing: La Étoile</span>**

. . .

<span class="invert-font">Restaurant Manager's Crisis:</span>

<span class="invert-font fragment">"I need to schedule my <span class="highlight">18 servers across 6 shifts</span> this weekend. Shifts have <span class="highlight">different lengths (4-6 hours)</span>, and if I don't have enough experienced servers on busy shifts, we face <span class="highlight">penalties</span> per missing experienced server from our parent company!"</span>

## The Staffing Challenge

<span class="highlight">A restaurant facing a weekend scheduling crisis:</span>

**La Étoile's Problem:**

-   18 servers available (6 experienced @ €75/hr, 12 junior @ €25/hr)
-   6 shifts with **varying lengths** (4-6 hours each)
-   Each shift needs 3 servers (at least 1 experienced)
-   Server **preferences** matter (1-10 scale, affects quality)

. . .

<span class="question">Question:</span> How to balance labor costs, penalties, AND staff?

## The Cost Impact: Why This Matters

<span class="highlight">The financial stakes are significant with these large penalties:</span>

-   **Minimum Labor Cost**: ~€3,500 (everyone works once)
-   **Experience Penalties**: €0-€1,200 per missing experienced server
-   **Preference Penalties**: €0-€180 per unhappy assignment
-   **Worst Case**: Over €9,000 if poorly scheduled!
-   **Best Case**: ??? with smart optimization

. . .

> **Important**
>
> Potentially up to **large difference** between good and bad scheduling!

## Restaurant Staffing: The Numbers

<span class="highlight">The real-world complexity we're dealing with:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-2-output-1.png" width="838" height="467" />

. . .

> **Warning**
>
> With varying shifts, preferences, and penalties, this is will be a real challenge!

## Today's Objectives

<span class="highlight">What you'll understand after this lecture:</span>

1.  **Why local search fails:** Recap on the local optima trap
2.  **Escape mechanisms:** How to accept worse solutions strategically
3.  **Four powerful metaheuristics:** SA, GA, Tabu Search, ACO
4.  **Selection criteria:** When to use which algorithm

## Hiking in Fog

<span class="highlight">Remember the metaphor with blindfolded eyes from last lecture?</span>

-   **Goal**: Find the highest peak in a mountain range
-   **Challenge**: You're hiking in thick fog (can only see 10 meters)
-   **Position**: Your X,Y coordinates = your decisions
-   **Altitude**: Your current solution quality
-   **Problem**: You might climb a small hill and think it's the summit!

. . .

> **Tip**
>
> This metaphor will guide us through all metaheuristics today!

## Recap: Local Optima

<span class="highlight">Real problems often have thousands of local optima!</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-3-output-1.png" width="756" height="466" />

. . .

<span class="question">Question:</span> Any idea how to escape local optima?

# <span class="flow">Why Simple Methods Fail</span>

## The Silo Problem

<span class="highlight">Why neighborhood optimization fails:</span>

**Technical View: Local Optima**

-   Algorithm climbs nearest hill
-   Gets stuck on "foothill"
-   Can't see the mountain beyond
-   Every move looks worse
-   Believes it found the best

**Analogy: Department Silos**

-   Sales optimizes sales metrics
-   Engineering optimizes quality
-   Finance optimizes costs
-   Each department "wins"
-   **Company performance loses!**

. . .

> **Important**
>
> Sum of local bests ≠ Global best

## Why Greedy Gets Stuck

<span class="highlight">Greedy algorithms can simply trap themselves:</span>

. . .

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-4-output-1.png" width="756" height="463" />

. . .

> **Warning**
>
> Greedy allocates resources early, creating problems later!

## Local Search Also Struggles

<span class="highlight">Because we only ever accept better solutions during search:</span>

. . .

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-5-output-1.png" width="756" height="467" />

. . .

<span class="question">Question:</span> What can we do to cope with this situation?

# <span class="flow">Metaheuristic #1: Simulated Annealing</span>

## Core Concepts

<span class="highlight">The fundamental components:</span>

-   **Solution** = One complete schedule/route/plan
-   **Neighbor** = A slightly modified version
-   **Cost** = How good/bad the solution is

. . .

**The Strategy**

-   Always accept improvements
-   Sometimes accept worse solutions (the change!)

. . .

<span class="highlight">Think of it as strategic risk-taking that decreases over time!</span>

## The Metallurgy Metaphor

<span class="highlight">How annealing steel inspired an optimization algorithm:</span>

**Annealing Metal:**

1.  Heat to high temperature
2.  Atoms move freely
3.  Slowly cool down
4.  Forms crystal structure

**Optimization:**

1.  Start with high "temperature"
2.  Accept bad moves often
3.  Gradually reduce temperature
4.  Converge to good solution

. . .

> **Important**
>
> The willingness to temporarily accept worse solutions is what enables finding the summit!

## Temperature Controls Acceptance

<span class="highlight">Probability of accepting worse solutions lowers with temp:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-6-output-1.png" width="755" height="467" />

. . .

> **Tip**
>
> We essentially compare the cost of the new schedule to the current cost and decide whether to accept the change based on the temperature and the difference in cost.

## Concept

<span class="highlight">How Simulated Annealing Works (Pseudocode)</span>

``` python
def simulated_annealing_concept(current_schedule):
    temperature = 500  # Start "hot" (adventurous)
    best_schedule = current_schedule
    
    while temperature > 1:
        # Step 1: Try a random change (like swapping two shifts)
        new_schedule = make_random_change(current_schedule)
        
        # Step 2: Is it better?
        if cost(new_schedule) < cost(current_schedule):
            current_schedule = new_schedule  # Always accept improvements
        else:
            # NEW: Sometimes accept worse solutions!
            # Hot temperature = more likely to accept
            # Cold temperature = less likely to accept
            if random() < acceptance_probability(temperature):
                current_schedule = new_schedule  # Accept anyway!
        
        # Step 3: Cool down (become less adventurous)
        temperature = temperature * 0.95
        
        # Remember the best we've ever seen
        if cost(current_schedule) < cost(best_schedule):
            best_schedule = current_schedule
    
    return best_schedule
```

## SA in Action: Restaurant Staffing

<span class="highlight">A simplified weekend scheduling problem we'll use throughout:</span>

``` python
# SIMPLIFIED PROBLEM (used across ALL metaheuristics today)
"""
La Étoile's Weekend Challenge:
- 12 servers: 4 experienced (E1-E4), 8 junior (J1-J8)
- 6 shifts: Need 2 servers each
- Everyone works exactly 1 shift
"""
```

. . .

**The initial greedy schedule has the following results:**

. . .

    Greedy Schedule Cost: €5,240
      Labor: €2250, Penalties: €1700, Unhappiness: €1290

. . .

> **Tip**
>
> Let's see how Simulated Annealing can improve the solution!

## Visualizing SA Performance

<span class="highlight">How temperature affects the search behavior:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-9-output-1.png" width="756" height="467" />

. . .

> **Important**
>
> See how SA accepts worse solutions early, enabling escape from local optima!

## Common SA Mistakes

<span class="highlight">Avoid these common implementation errors:</span>

. . .

**Mistake #1: Starting Too Cold**

-   If temperature is too low → Acts like greedy (no exploration)
-   Fix: Start hot enough to accept bad moves

. . .

**Mistake #2: Cooling Too Quickly**

-   If you cool fast → Get stuck early
-   Fix: Cool slowly (multiply by 0.95-0.99, not 0.5)

. . .

> **Warning**
>
> Quick cooling is tempting for speed, but defeats the purpose of SA!

## Temperature Parameter Impact

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-10-output-1.png" width="1106" height="467" />

. . .

> **Tip**
>
> The "Good Balance" explores widely early, then refines carefully. Often you need to balance exploration and exploitation by experimenting with different parameters.

# <span class="flow">Metaheuristic #2: Genetic Algorithms</span>

## Evolution as Optimization

<span class="highlight">How natural selection inspires computational optimization:</span>

**Natural Selection:**

1.  Population of individuals
2.  Fittest survive & reproduce
3.  Offspring inherit traits
4.  Mutations create diversity
5.  Evolution finds adaptation

**Optimization:**

1.  Population of solutions
2.  Best solutions selected
3.  Crossover combines solutions
4.  Mutation adds variation
5.  Evolution finds optimum

. . .

> **Tip**
>
> Just like successful products get more market share, better solutions get more "offspring" in the next generation. It's survival of the fittest, but for schedules, routes, or designs!

## The Genetic Process

<span class="highlight">Four stages repeat each generation:</span>

1.  **Selection:** Choose parents based on fitness
2.  **Crossover:** Combine to create children
3.  **Mutation:** Randomly modify children
4.  **Replacement:** New generation replaces old
5.  **Population Evolution:** Improve population quality

. . .

> **Tip**
>
> Let's see each stage in detail with our restaurant problem!

## Stage 1: Selection (Tournament)

<span class="highlight">How to choose which schedules get to "reproduce":</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-12-output-1.png" width="790" height="467" />

. . .

> **Important**
>
> Each tournament selects one parent, then we pair them up sequentially for crossover.

## Stage 2: Crossover (Recombination)

<span class="highlight">Combine two parent schedules to create offspring:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-13-output-1.png" width="756" height="468" />

. . .

> **Tip**
>
> Crossover randomly combines good building blocks from both parents!

## Stage 3: Mutation

<span class="highlight">Random changes maintain diversity and explore new solutions:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-14-output-1.png" width="756" height="468" />

. . .

> **Tip**
>
> Mutation adds random exploration, like trying something completely new occasionally!

## Stage 4: Replacement I

<span class="highlight">How do offspring join the population?</span>

-   **Generational:** Replace entire population with offspring
-   **Steady-State:** Replace only worst individuals
-   **Elitism:** Always keep the best solutions

. . .

> **Note**
>
> Our approach: **Generational with Elitism**, we create 20 offspring via repeated selection/crossover/mutation, but preserve the 2 best from current generation.

## Stage 4: Replacement II

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-15-output-1.png" width="752" height="468" />

. . .

> **Note**
>
> Elitism ensures we never lose our best solutions while exploring new ones!

## Stage 5. Population Evolution

<span class="highlight">How the population improves over generations:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-16-output-1.png" width="755" height="467" />

. . .

> **Note**
>
> Notice how population average also improves (not just the best)!

## GA vs SA: Head-to-Head

<span class="highlight">Comparing exploration strategies on the restaurant problem:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-17-output-1.png" width="755" height="468" />

. . .

> **Tip**
>
> GA maintains population diversity, SA explores single solution path!

## GA Mistakes: Population Issues

<span class="highlight">Avoid these population-related errors:</span>

. . .

**Mistake #1: Everyone Becomes Identical**

-   If all solutions look the same → Lost diversity
-   Fix: More mutation, bigger population, tournament selection

. . .

**Mistake #2: Too Greedy in Selection**

-   Only keeping the very best → Premature convergence  
-   Fix: Keep some variety, even if not perfect (elitism of 10-20%)

## GA Mistakes: Implementation

<span class="highlight">Technical pitfalls to watch out for:</span>

. . .

**Mistake #3: Breaking the Rules**

-   Crossover might create invalid schedules
-   Fix: Always check and repair after crossover/mutation

. . .

**Mistake #4: Evolution Too Slow**

-   Population too large or too many generations
-   Fix: Start small (50-100), tune based on convergence

# <span class="flow">Metaheuristic #3: Tabu Search</span>

## Core Idea

<span class="highlight">Using memory to avoid cycling through bad solutions:</span>

**Analogy:**

-   Keep a list of recent dates
-   "Not going back there!"
-   Forces you to meet new people
-   After time, memory fades

**In Optimization:**

-   Recent solutions = "tabu"
-   Don't revisit same schedules
-   Forces exploration of new areas
-   Tabu list has limited size

. . .

> **Tip**
>
> Like keeping "lessons learned", you remember not to use them again, but after a while, you might reconsider!

## Concept

<span class="highlight">How Tabu Search Works (Pseudocode)</span>

``` python
def tabu_search_concept():
    tabu_list = []  # Our "never again" list
    current_solution = initial_schedule
    best_solution = current_solution
    
    while not done:
        # Look at all possible moves
        possible_moves = get_all_neighbor_moves(current_solution)
        
        # Filter out the "forbidden" moves
        allowed_moves = []
        for move in possible_moves:
            if move not in tabu_list:  # Not forbidden
                allowed_moves.append(move)
        
        # Pick the best allowed move (even if worse!)
        best_move = select_best(allowed_moves)
        current_solution = apply(best_move)
        
        # Update best if improved
        if cost(current_solution) < cost(best_solution):
            best_solution = current_solution
        
        # Remember this move (add to tabu list)
        tabu_list.append(best_move)
        if len(tabu_list) > 10:  # Keep list size manageable
            tabu_list.pop(0)  # Forget oldest
    
    return best_solution
```

## Tabu Search on Restaurant Problem

<span class="highlight">Real implementation with memory-based exploration:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-18-output-1.png" width="755" height="468" />

. . .

> **Tip**
>
> Tabu Search's memory prevents revisiting bad solutions!

# <span class="flow">Metaheuristic #4: Ant Colony Optimization</span>

## The Core Idea

<span class="highlight">Collective intelligence through chemical signals:</span>

**Reviews:**

-   Popular choices get more 5-star reviews
-   More reviews → more visibility
-   But old reviews fade over time
-   New patterns can emerge

**In Optimization:**

-   Good assignments get "pheromones"
-   Stronger choosen more likely
-   Evaporation against stagnation
-   Colony finds patterns

> **Tip**
>
> Imagine each server-shift pairing has a "rating" that increases when it works well in a schedule. Over time, the best pairings naturally get chosen more often!

## How ACO Works on Scheduling

<span class="highlight">Four key stages in each iteration:</span>

1.  **Construction:** Each ant builds a schedule probabilistically
2.  **Evaluation & Evaporation:** Measure quality, then fade all pheromones
3.  **Reinforcement:** Good schedules deposit pheromones
4.  **Evolution:** Repeat until colony converges

. . .

> **Tip**
>
> Let's see each stage visually!

## ACO: Key Parameters

<span class="highlight">Two critical parameters control the balance:</span>

**Evaporation Rate (ρ)**

-   Higher ρ → More forgetting
-   Lower ρ → Stronger memory
-   Typical: 0.1 - 0.5
-   **Too high**: Colony never learns
-   **Too low**: Gets stuck early

**Number of Ants**

-   More ants → More exploration
-   Fewer ants → Faster iterations
-   Typical: 10 - 50
-   **Too many**: Slow, redundant
-   **Too few**: Miss good patterns

. . .

> **Tip**
>
> Start with ρ=0.3 and n_ants=20, then tune based on problem size.

## Stage 1: Pheromone Construction

<span class="highlight">Ants don't pick randomly, they follow the chemical trails</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-19-output-1.png" width="798" height="463" />

. . .

> **Tip**
>
> To build the initial pheromone matrix, each cell is initialized with a small positive value.

## Stage 2: Evaluation & Evaporation

<span class="highlight">After all ants build schedules:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-20-output-1.png" width="756" height="466" />

. . .

> **Tip**
>
> Evaporation prevents premature convergence as old patterns can fade away!

## Stage 3: Reinforcement

<span class="highlight">Good ants deposit more pheromones:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-21-output-1.png" width="761" height="431" />

<span class="highlight">The best solutions leave the strongest trails for future iterations!</span>

## Stage 4: Evolution Over Iterations

<span class="highlight">Full ACO implementation on restaurant staffing:</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-22-output-1.png" width="835" height="468" />

. . .

> **Tip**
>
> The colony learns collectively step by step.

## ACO vs Other Algorithms

<span class="highlight">How does the ant colony compare?</span>

<img src="lec_09_metaheuristics_files/figure-markdown_strict/cell-23-output-1.png" width="755" height="468" />

. . .

> **Tip**
>
> Any idea why ACO fares worse?

## Why did ACO struggle?

<span class="highlight">The Right Tool for the Wrong Job</span>

ACO is designed for **Sequential Path-Finding** (Graph Traversal).

-   **Best For:** "I am at City A, where should I go next?" (TSP)
-   **Our Problem:** "Who should work Friday Dinner?" (Assignment)

. . .

> **Important**
>
> We forced a "Graph" algorithm onto a "Bin Packing" problem. SA and GA don't care about geometry, so they adapted better!

# <span class="flow">Decision Framework</span>

## When to Use Which Metaheuristic?

<span class="highlight">A decision guide for algorithm selection:</span>

| Method | Time | Quality | Complexity | Best For        |
|--------|------|---------|------------|-----------------|
| Random | xxxx | x       | Trivial    | Baseline        |
| Greedy | xxx  | xx      | Simple     | Quick decisions |
| LS     | xx   | xxx     | Medium     | Improvement     |
| SA     | xx   | xxxx    | Medium     | Single solution |
| GA     | x    | xxxx    | High       | Population      |
| TS     | xx   | xxx     | Medium     | Avoid cycles    |
| ACO    | x    | xxxx    | High       | Changing Paths  |

## The No Free Lunch Theorem

<span class="highlight">Why there's no universal best algorithm:</span>

**"No Free Lunch Theorem":** No single algorithm is best for all problems. Your choice must match your problem structure:

-   **Path/Network Problems** → ACO (pheromones for paths)
-   **Scheduling Problems** → SA or Tabu (neighborhood swaps)
-   **Complex Design** → GA (population diversity)

## Implementation Strategy

<span class="highlight">Guidelines for successful implementation:</span>

1.  **Start Simple**: Always try greedy first as baseline
2.  **Profile Your Problem**: Understand constraints before choosing
3.  **Tune Incrementally**: Don't optimize all parameters at once
4.  **Track Progress**: Monitor convergence to know when to stop
5.  **Hybrid Approaches**: Combine methods (e.g., GA + Local Search)
6.  **Use AI Assistance**: Bridge the "knowledge gap" with GenAI

# <span class="flow">Today's Briefing</span>

## Today

**Hour 2: This Lecture**

-   Metaheuristics
-   Simulated annealing
-   Genetic algorithms
-   Tabu search & ACO

**Hour 3: Notebook**

-   Bean Counter delivery
-   Implement SA
-   Tune parameters
-   Compare performance

**Hour 4: Competition**

-   Restaurant staffing
-   Multi-objective
-   Schedule optimization
-   Justify choice!

## The Competition Challenge

<span class="highlight">La Étoile Restaurant Weekend Staffing</span>

. . .

1.  **Schedule** 18 servers across 6 shifts (different lengths)
2.  **Minimize** labor + experience penalties + preference costs
3.  **Ensure** experienced coverage (strategic placement)
4.  **Respect** 2 servers per shift requirement

. . .

> **Important**
>
> Choose your metaheuristic wisely as this is a tough problem!

## Parameter Tuning Strategies

<span class="highlight">How to find good parameters without wasting time:</span>

1.  **Start with Rules of Thumb**
    -   SA: Initial temp = max cost difference you'd accept
    -   GA: Population = 10-20× number of decision variables
    -   Tabu: Tenure (limit) = √(problem size)
2.  **Grid Search on Small Instance**
    -   Test 3-4 values per parameter
    -   Use 10% of full dataset
    -   Example: `temps = [100, 500]`, `cooling = [0.95, 0.99]`

## Real-World Considerations

<span class="highlight">Technical realities when putting metaheuristics into production:</span>

| Factor               | Questions to Ask               |
|----------------------|--------------------------------|
| **Time Budget**      | How long can optimization run? |
| **Solution Quality** | Need optimal or "good enough"? |
| **Explainability**   | Must justify decisions?        |
| **Problem Changes**  | Static or dynamic data?        |
| **Team Skills**      | Who maintains this code?       |

. . .

> **Important**
>
> Use the **simplest method** that meets your quality target. Complex metaheuristics are great but more costly to maintain!

## Summary

<span class="highlight">Key Takeaways:</span>

-   Metaheuristics escape local optima when exact methods fail
-   SA uses temperature, GA uses evolution, Tabu uses memory
-   Parameter tuning is critical for performance
-   No universal best - problem structure matters
-   Start simple, add complexity only if needed

## Break!

<span class="highlight">Take 20 minutes, then we start the practice notebook</span>

**Next up:** You'll implement metaheuristics for Bean Counter
