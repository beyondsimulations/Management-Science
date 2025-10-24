# Management Science for Business

## Course Philosophy & Structure

### Core Concept
Students build a comprehensive "consultant's toolkit" by solving real problems across diverse business domains. Each algorithm is a tool, each case is a client, and each presentation is a boardroom pitch. We are not teaching programming or algorithms in a vacuum - we're developing problem-solvers who can tackle complex business challenges with analytical rigor and practical wisdom.

### Objective
Transform business students into analytically-capable consultants who can prototype optimization solutions and communicate insights effectively.

### Class Size
40 students, working in groups of 3-4 (10-13 groups)

### Lecture Format
Actual format depends on course section and academic hours are each 45 minutes long
- **Lectures 1-3:** Python Foundation
  1. **Hour 1-4:** Learning Programming with interactive Notebooks
- **Lectures 4-9:** Algorithmic Foundations
  1. **Hour 1:** Interactive lecture explaining core concepts
  2. **Hour 2:** Interactive notebook work (45 min) + class discussion (15 min)
  3. **Hours 3-4:** Competition challenge with real data (no notebook) + solution presentations
  4. **Bonus Points:** Best solution team gets bonus points toward final grade
- **Lectures 10-12:** Consulting Project
  1. **Hour 1:** Introduction of new concept/ presentation training
  2. **Hour 3-4:** Students work in groups on their project and lecturer checks progress/helps

### Expectations
- Students spend 4-6 hours/week outside class
- Assignments take 3-5 hours each
- Code quality: functional and clear, not perfect
- Focus on insights over implementation elegance

### Assignment Strategy
- Assignment 1: Risk & Forecasting (Due Lecture 7)
- Assignment 2: Full Optimization Toolkit (Due Lecture 10)
- Final Competition: Client projects (Lectures 10-12)

### Grading
Students earn points in the course and the total number of points achieved lead to the final mark of the course. In total, up to 100 points (without bonus) can be earned.

#### Grade Composition
- Assignment 1: 30% (Risk & Forecasting)
- Assignment 2: 30% (Optimization Toolkit)
- Competition Project: 40%
  - Solution quality: 20%
  - Presentation: 20%
- Bonus points if competition won in class and if project was choose by others (see Bonus Points)

#### Assignment Rubrics
**Technical Implementation (50%)**
- Correctness of algorithms
- Code quality and documentation
- Efficiency and scalability
- Additional features

**Analysis & Insights (30%)**
- Problem understanding
- Results interpretation
- Business recommendations
- Going beyond requirements

**Communication (20%)**
- Clarity of documentation
- Visualization quality
- Executive summary

#### Bonus Points
During lectures 4-9 students can earn bonus points if they have the best, second-best or third best solution in the competition challenge. The best solution receives 10 bonus points, the second group receives 6 bonus points and the third best group receives 3 bonus points for all group members.
In the final presentations, each best group of the three topics with the best solution gets 10 bonus points on top (based on voting) of best solution per client and best presentation.

### Contingency Plans

**If students struggle with Python:**
- Pair programming buddy system
- Additional office hours
- Cheat Sheets are provided with all the information
- Students can/ will use generative AI in the course

**If assignments too challenging:**
- Provide additional scaffolding code
- Create intermediate checkpoints
- Peer programming sessions
- Partial credit for approach even if not fully working

**If competition too ambitious:**
- Simplify data complexity
- Provide more starter code
- Reduce scope of deliverables
- Focus on one core algorithm per client

### Key Success Factors

#### Students
1. **Master Python basics** in first 3 lectures - foundation is critical
2. **Start assignments early** - they require iteration
3. **Collaborate actively** - peer learning is encouraged
4. **Think like consultants** - always consider business impact
5. **Document everything** - your code is your product

#### Instructor
1. **Ensure Python readiness** after Lecture 3 - no one left behind
2. **Interactive Notebooks** students learn solving problems step by step
3. **Real-world context** in every example to maintain relevance
4. **Encourage experimentation** - failures teach as much as successes
5. **Celebrate victories** - recognize good work publicly

## Course Plan

### PART I: PYTHON FOUNDATION (Lectures 1-3)
*No Mini-competitions yet! Focus on building solid Python foundations.*

#### Lecture 1: Welcome to Management Science

**Objectives:**
- Inspire students about Management Science applications
- Set up Python development environment with uv
- Master Python fundamentals: variables, lists, loops, conditionals

**Hour 1: Course Introduction + Setup (45 min)**
- Welcome and course overview (15 min)
- "From Amazon to Hospitals: Where algorithms make millions"
- The consultant mindset: "You're junior consultants, not just students"
- Course structure, assignments, and competition preview
- Why Python? The language of modern analytics
- Installing Python with uv (modern Python package manager)
- Setting up Jupyter notebooks
- Troubleshooting session - ensure everyone is ready
- First code: `print()` and basic commands

**Hour 2: Interactive Notebook #1 - Variables & Basic Data Types**
- Variables as named storage
- Data types: int, float, string
- Basic arithmetic operations
- f-strings for output formatting

**Hour 3: Interactive Notebook #2 - Lists & Basic Loops**
- Creating and accessing lists (indexing, slicing)
- List operations: `append()`, `len()`
- For loops for iteration
- Loops with `range()` for indexed access
- Calculating aggregations (sum, average, count)

**Hour 4: Interactive Notebook #3 - Conditionals & While Loops**
- If/elif/else statements
- Comparison operators (==, !=, >, <, >=, <=)
- Boolean logic (and, or)
- Conditionals within loops
- While loops for iterative processes
- Building filtered lists
- 10 minute recap and preview of next session

---

#### Lecture 2: Python Programming Advances

**Objectives:**
- Master functions for code organization
- Understand dictionaries and tuples for structured data
- Learn sorting of structured data
- Build integrated mini-project

**Hour 1: Interactive Notebook #4 - Functions**
- Why functions? (code reusability)
- Function structure: def, parameters, return
- Functions with business logic
- Functions calling other functions
- Returning multiple values with tuples
- Tuple basics: immutable sequences for function returns
- Unpacking tuple returns

**Hour 2: Interactive Notebook #5 - Dictionaries**
- Dictionaries for structured data (key-value pairs)
- Creating, accessing, and updating dictionaries
- Lists of dictionaries
- Looping through structured data
- Filtering and processing dictionary data
- Using dictionaries with functions

**Hour 3: Interactive Notebook #6 - Sorting & Finding Best Options**
- Sorting simple lists (`sorted()`, `reverse=True`)
- Finding min/max with built-in functions
- Sorting by multiple fields
- Finding min/max in dictionaries
- Applying to scheduling problems (SPT, EDD rules preview)

**Hour 4: Interactive Notebook #7 - Integration Mini-Project**
- **Complete order management system**
- Order processing and validation
- Inventory management (check stock, update inventory)
- Order prioritization by multiple criteria
- Delivery scheduling with time calculations
- Business reporting
- **Integration of all skills learned in Lectures 1-2**
- 10 minute recap and preview of data analysis

---

### Lecture 3: Data Science Foundation - NumPy & Pandas

**Objectives:**
- Master NumPy for numerical computing and Monte Carlo
- Learn Pandas for data manipulation and forecasting prep
- Create visualizations for business insights
- Final readiness check before algorithms

**Hour 1: Interactive Notebook #8 - NumPy Essentials**
- Why NumPy? Speed vs. Python lists
- Creating arrays (from lists, zeros, ones, arange, linspace)
- Vectorized operations (fast element-wise math)
- Statistical functions: mean, std, min, max, percentiles
- **Random number generation** (uniform, normal, integers)
- Simple Monte Carlo simulation example
- Boolean indexing and filtering

**Hour 2: Interactive Notebook #9 - Pandas Basics**
- DataFrames vs arrays (labeled columns)
- Creating DataFrames from dictionaries
- Exploring data: `head()`, `info()`, `describe()`, `shape`
- Selecting columns and rows (`iloc`, column names)
- Creating new calculated columns
- **Filtering data** with boolean conditions
- Sorting with `sort_values()`
- **Reading CSV files** with `pd.read_csv()`

**Hour 3: Interactive Notebook #10 - Pandas for Analysis**
- **GroupBy aggregations** (sum, mean, count, multiple agg)
- **Datetime operations** (extract month, week, day_of_week)
- **Rolling averages** (critical for forecasting)
- Cumulative calculations (`cumsum`)
- Pivot tables for cross-tabulation
- Merging datasets with `merge()`
- Seasonal analysis patterns

**Hour 4: Interactive Notebook #11 - Visualization & Final Integration**
- Basic plotting with matplotlib (line, bar, histogram, scatter)
- Creating multi-plot dashboards with subplots
- Time series visualizations
- Distribution plots for Monte Carlo results
- Customizing plots (titles, labels, legends, colors)
- **Complete analytics project:** delivery startup analysis
  - Data exploration and cleaning
  - Time-based analysis (hourly, daily patterns)
  - Driver performance metrics
  - Business insights visualization
- **Final readiness check before algorithms**
- **15 min:** GitHub Education + Copilot setup guide
- **AI pair programming best practices**

## PART II: MANAGEMENT SCIENCE TOOLS (Lectures 4-9)
*Mini-competitions begin here*
*Remember to upload notebook solutions for students!*

### Lecture 4: Dealing with Uncertainty - Monte Carlo

**Domain Focus:** Finance & Investment Decisions
**Key Questions:** How do we make decisions when we can't predict the future?

**Hour 1: Interactive Lecture - Welcome to Uncertainty**
- Interactive demonstration: "The Casino Game"
- Real-world examples: Netflix series decisions, pharmaceutical R&D
- Probability distributions and their business meaning
- The mathematics of risk: expected value, variance, percentiles
- When and why Monte Carlo beats analytical methods

**Hour 2: Building Crystal Ball Simulations (Notebook)**
```python
# Students will implement:
# 1. Simple investment return simulation
# 2. Adding uncertainty to multiple variables
# 3. Correlation between risks
# 4. Confidence interval calculation
# 5. Visualization of results

def simulate_coffee_shop(n_simulations=10000):
    """Should we open a new coffee shop?"""
    # Students code along
    daily_customers = np.random.normal(100, 20, n_simulations)
    avg_purchase = np.random.uniform(8, 12, n_simulations)
    # Build up complexity gradually...
```
**Discussion (last 5 minutes):** What do the results tell us? Share insights, debugging tips, interpretation challenges.

**Hours 3-4: Competition - "The Startup Investment Challenge"**
- **Scenario:** TechVenture Innovation Fund needs investment analysis
- **Data Provided:**
  - 5 potential startups with historical metrics
  - Market research data
  - Competitor performance data
- **Task:** Build simulation to find optimal portfolio allocation
- **Deliverables:**
  - Deliverable: One-slide recommendation with risk profile
  - Risk/return analysis for each startup
  - Recommended portfolio mix
  - Probability of 3x return
- **Competition Format:**
  - 60 minutes development
  - 20 minutes for top 3 teams to present one-slider
  - 10 minutes for winning solution walkthrough
- **Bonus Points:** Best risk-adjusted returns

**Assignment 1 Introduction (Last 10 min):**
- "The Risk & Forecast Analyzer" - Due Lecture 7
- Part A: Portfolio optimization
- Part B: Demand forecasting implementation

### Lecture 5: Forecasting the Future

**Domain Focus:** Retail & Marketing
**Key Questions:** How can we predict future demand from historical patterns?

**Hour 1: Interactive Lecture - Patterns in Data**
- Show sales data: Can you spot the pattern?
- Trend, seasonality, and residuals explained
- The forecasting toolkit: MA, exponential smoothing, seasonal models
- Cost of forecast errors
- Simple methods often win

**Hour 2: Notebook Session - From Simple to Smart**
```python
# Students will implement:
# 1. Moving averages (simple, weighted)
# 2. Exponential smoothing
# 3. Seasonal decomposition
# 4. Forecast accuracy metrics
# 5. Prediction intervals

def forecast_demand(historical_data, method='exponential'):
    """Students build multiple forecasting methods"""
    # Guided implementation
```
**Discussion (last 5 minutes):** What do the results tell us? Share insights, debugging tips, interpretation challenges.

**Hours 3-4: Competition - "The Black Friday Predictor"**
- **Scenario:** Major retailer needs Black Friday inventory planning
- **Data Provided:**
  - 3 years of daily sales for 10 products
  - Previous Black Friday patterns
  - Product categories (as they might influence each other)
- **Task:** November demand forecast per product
- **Competition Format:**
  - 60 minutes development
  - 10 minutes teams receive held-out data to test their algorithm
  - Accuracy comparison (using held-out data)
- **Bonus Points:** Lowest total forecast error

### Lecture 6: Smart Quick Decisions in Scheduling

**Domain Focus:** Manufacturing Operations
**Key Question:** Can simple rules solve complex scheduling problems quickly?
**Core Concept:** Greedy/Constructive Heuristics

**Hour 1: Interactive Lecture - The Power of Simple Rules**
- The job shop scheduling problem: Why it's NP-hard (brief!!)
- Live demonstration: "The Pizza Kitchen Crisis"
  - 5 pizzas, 3 ovens, different cooking times
  - Students suggest rules → test them live
- Classic greedy rules explained:
  - SPT (Shortest Processing Time): Get quick wins
  - EDD (Earliest Due Date): Keep customers happy
  - Critical Ratio: Balance urgency and time
  - FIFO: When in doubt, be fair
- Real-world impact: How Toyota uses these rules
- When greedy works (and when it fails spectacularly)

**Hour 2: Notebook Session - Building Schedulers**
*Interactive Notebook: job_shop_greedy.ipynb*
```python
# Students will implement:
def schedule_SPT(self):
    """Shortest Processing Time First"""
    # Sort by processing time, assign to machines
    # Calculate completion times and tardiness

def schedule_EDD(self):
    """Earliest Due Date First"""
    # Sort by due date, assign to machines

def schedule_critical_ratio(self):
    """Critical Ratio: (due_date - current_time) / processing_time"""
    # Dynamic rule that adapts as time progresses

def visualize_gantt(self, schedule):
    """Create Gantt chart visualization"""
    # Beautiful timeline chart (code given!)

def calculate_metrics(self, schedule):
    """Calculate tardiness, makespan, utilization"""
    return {
        'total_tardiness': ...,
        'max_tardiness': ...,
        'makespan': ...,
        'machine_utilization': ...
    }

# Compare all three rules on same dataset
# Which rule wins? Why?
```
**Discussion (last 5 minutes):**
- What do the results tell us?
  - Which rule worked best?
  - Can you think of scenarios where each would win?
  - What if we combined rules?

**Hours 3-4: Competition - "The Bike Factory Friday Crisis"**
- **Scenario:** Custom bicycle factory, Friday afternoon chaos
  - "We just got 8 rush orders for Monday delivery!"
  - 40 total jobs for weekend production
  - 5 different workstations (frame, paint, assembly, quality, packaging)
  - Each job needs specific sequence through stations
  - Overtime costs €100/hour after 8pm

- **Data Provided:**
  - Job details: processing times, due dates, priority levels
  - Machine capabilities and setup times
  - Current time: Friday 2pm
  - Rush order premium: €500 if on time, €0 if late

- **Task:** Minimize total cost (tardiness penalties + overtime)

- **Competition Format:**
  - 60 minutes development
  - Can use any greedy rule or combination
  - Submit schedule + cost calculation
  - Comparisons of total cost
  - Winner presents their rule and explains why it worked

- **Bonus Points:** Lowest total cost

**Assignment 2 Introduction (Last 10 min):**
- "The Optimizer's Toolkit" - Due Lecture 10
- Will require scheduling + routing + improvement

### Lecture 7: Better Routing - Local Search & Improvements
**Assignment 1 Due**

**Domain Focus:** Logistics & Delivery
**Key Question:** How do we systematically improve solutions?
**Core Concept:** Local Search and 2-Opt

**Hour 1: Interactive Lecture - The Art of Improvement**
- Shortest Path in a Graph
- The Traveling Salesman Problem: Simple to state, hard to solve
- Live demonstration: "The Coffee Delivery Challenge"
- From TSP to VRP: Adding vehicles and capacity
- Neighborhood structures:
  - 2-opt: swap edges
  - Swap: exchange customers between routes
  - Relocate: move one customer to different position
- Hill climbing: Always go uphill until you can't
- The local optima trap: Why we get stuck

**Hour 2: Notebook Session - Building Route Optimizers**
*Interactive Notebook: routing_and_local_search.ipynb*
```python
# Students will implement:
# A shortest path algorithm on a graph
# A simple TSP solver with 2-opt local Search

```
- **Class Discussion (5 min):**
  - How much improvement did 2-opt give?
  - Why does it eventually stop improving?
  - Ideas for escaping local optima?

**Hours 3-4: Competition - "The Urban Delivery Challenge"**
- **Scenario:** Startup delivery company's first big contract
  - "We promised same-day delivery across Berlin!"
  - 20 delivery locations across the city
  - 1 delivery van from one location
  - All deliveries must be completed today
  - Some customers have time windows

- **Data Provided:**
  - Customer locations (real Berlin coordinates)
  - Time windows for 30% of customers
  - Distance/time matrix
  - Vehicle specs (capacity, speed, cost per km)

- **Task:** Minimize total distance + time window violations

- **Competition Format:**
  - 60 minutes development
  - Must implement construction + improvement
  - Submit routes visualization + total cost
  - Winner explains construction + improvement strategy

- **Bonus Points:** Best score (distance)

### **Lecture 8: Tough Trade-offs - Multi-Objective Optimization**

**Domain Focus:** Sustainability & Strategic Planning
**Key Question:** What do you do when you can't have it all?
**Core Concept:** Multi-Objective Optimization & Pareto Frontiers

**Hour 1: Interactive Lecture - The Balance Challenge**
- **Opening Hook:** "The Tesla Dilemma"
  - Making electric cars (performance vs. range vs. cost vs. sustainability)
  - "You can't maximize everything"

- Real-world conflicts:
  - Fast delivery - Low cost - Low emissions
  - Product quality - Manufacturing speed - Worker satisfaction
  - Profit - Customer satisfaction - Environmental impact

- The Transportation Problem
  - Assigning depots to customers
  - Different assignments with different objectives possible

- Pareto Frontier explained:
  - Dominated vs. non-dominated solutions
  - "You can only improve one thing by making something else worse"
  - Visual: 2D and 3D Pareto fronts

- Approaches to multi-objective problems:
  1. **Weighted Sum:** Assign importance to each objective
  2. **ε-Constraint:** Optimize one, constrain others
  3. **Goal Programming:** Set targets, minimize deviation
  4. **Pareto Search:** Find all non-dominated solutions

- Real examples:
  - Amazon: Speed vs. Cost vs. Carbon footprint
  - Airlines: On-time vs. Fuel cost vs. Passenger satisfaction
  - Supply chains: Reliability vs. Inventory vs. Lead time

**Hour 2: Notebook Session - Finding the Balance**
```python
# Students will implement:
# Multi Objective Optimizier (if this is possible based on greedy algorithms and local search!)

# Interactive exploration:
# 1. Students adjust weights and see how solution changes
# 2. Visualize Pareto frontier
# 3. Identify "knee points" (best balanced solutions)
# 4. Analyze trade-off rates
```

- **Class Discussion (5 min):**
  - Which objective matters most to you? Why?
  - How would you present trade-offs to a CEO?
  - What happens when stakeholders disagree on weights?

**Hours 3-4: Competition - "The Green Logistics Challenge"**
- **Scenario:** Logistics company facing new EU regulations
  - "We must cut carbon 40% by 2030 while staying profitable and maintaining service"
  - Design next-generation transportation problem assignment

- **Three Conflicting Objectives:**
  1. **Minimize Cost:** Fleet + fuel + warehouse + labor
  2. **Minimize Carbon Emissions:** New EU regulations with penalties

- **Data Provided:**
  - 20 customer zones across Europe
  - 5 potential warehouse locations
  - Fleet options:
    - Diesel trucks: cheap, fast, high emissions
    - Electric vans: expensive, slower (charging), zero emissions
    - Hybrid: medium on all
  - Delivery volume forecasts
  - Carbon pricing scenarios (€50, €100, €200 per ton)

- **Task:** Design transportation network + fleet composition

- **Deliverables:**
  1. Your proposed solution (network + fleet)
  2. Performance on both objectives
  3. Pareto frontier showing alternatives
  4. Recommendation with justification

- **Competition Format:**
  - 60 minutes development
  - Pareto frontier between both alternatives
  - Best solution based on your heuristic approach
  - Team closest to optimal allocation wins
  - Top 3 teams present their Pareto frontier and defend recommendations

### Lecture 9: Escaping the Trap - Simulated Annealing & Metaheuristics

**Domain Focus:** Complex Optimization
**Key Question:** How do we escape local optima and find great solutions?
**Core Concept:** Simulated Annealing + Metaheuristics Overview

**Hour 1: Interactive Lecture - The Temperature of Optimization**
- **Opening Hook:** "Why Your Phone Gets Hot When Thinking"
  - Connection between physical annealing and optimization

- The local optima problem revisited:
  - "Remember Lecture 7? We got stuck."
  - Visualization: Lost in the mountains at night

- **Physical Annealing Process:**
  - Blacksmith demonstration (video): heating metal makes it flexible
  - Slow cooling creates perfect crystal structure
  - Fast cooling creates brittle material

- **Simulated Annealing Algorithm:**
  - Start "hot": accept bad moves frequently
  - Cool down slowly: become more selective
  - End "cold": only accept improvements
  - The magic: `accept_probability = exp(-delta/temperature)`

- Live demonstration: SA vs. Hill Climbing
  - Same problem, watch them run side-by-side
  - Hill climbing gets stuck quickly
  - SA explores, finds better solutions

- **Cooling Schedules:**
  - Linear: T = T - α
  - Geometric: T = T × α (most common)
  - Adaptive: adjust based on acceptance rate

- When to use SA:
  - Discrete optimization with local search neighborhoods
  - When you need good solutions, not perfect ones
  - When problem has many local optima

- **Quick Tour of Other Metaheuristics:**

  **Genetic Algorithms (5 min):**
  - Population-based, inspired by evolution
  - Good for: Large search spaces, multiple local optima
  - When to use: Have time to run, need diverse solutions

  **Tabu Search (3 min):**
  - Local search with memory: "don't go back"
  - Good for: Intensification and diversification
  - When to use: Cycling is a problem

  **Ant Colony Optimization (3 min):**
  - Inspired by ant foraging behavior
  - Good for: Routing problems, combinatorial optimization
  - When to use: Problem has natural path representation

  **Particle Swarm Optimization (2 min):**
  - Swarm intelligence
  - Good for: Continuous optimization

- **Comparison Table:**
```
Method          | Complexity | Speed | Solution Quality | Best For
----------------|-----------|-------|------------------|------------------
Greedy          | Low       | Fast  | Good             | Quick decisions
Local Search    | Low       | Fast  | Better           | Improvement
SA              | Medium    | Medium| Great            | Escaping traps
GA              | High      | Slow  | Great            | Complex landscapes
Tabu            | Medium    | Medium| Great            | Cycling problems
```

**Hour 2: Notebook Session - Mastering Simulated Annealing**
```python
# Students will implement a complete but simple SA framework for an easy scheduling problem without any additional constraints

# Students compare SA vs Hill Climbing on one problem
# See how SA consistently finds better solutions
```

- **Class Discussion (5 min):**
  - How did SA escape local optima?
  - What happened when you cooled too fast? Too slow?
  - Which cooling schedule worked best?

**Hours 3-4: Competition - "The Hospital Scheduling Crisis"**
- **Scenario:** City hospital emergency department scheduling nightmare
  - "We have a scheduling crisis! Staff are quitting due to unfair schedules and we're violating labor laws!"
  - Must create 2-week schedule for emergency department
  - Balance coverage and costs

- **Data Provided:**
  - **30 staff members** with:
    - Skills: Junior nurse, Senior nurse (Costs)
    - Availability: Some can't work certain days
    - Maximum hours per week

  - **Shift requirements** (per day):
    - Morning (6am-2pm): Need 5 staff (3 senior, 2 junior)
    - Afternoon (2pm-10pm): Need 6 staff (3 senior, 3 junior)
    - Night (10pm-6am): Need 4 staff (2 senior, 2 junior)

  - **Constraints:**
    - No staff works >5 days per week
    - No staff works >10 hours per day
    - Minimum 11 hours rest between shifts

  - **Costs:**
    - Understaffed shift: €1,000 penalty per missing staff
    - Overtime (>40 hrs/week): €50/hour

- **Task:** Create optimal 14-day schedule using Simulated Annealing

- **Deliverables:**
  1. Complete schedule (staff × shifts × days)
  2. Total cost breakdown (including constraints)

- **Competition Format:**
  - 60 minutes development
  - Must implement Simulated Annealing
  - Submit metrics for cost, workload and constraint violation

- **Additional 10 Bonus Points:**
  - "Best SA Visualizer" - best visualization of SA progress
  - Must show temperature, acceptance rate, solution quality evolution

- **Bonus Points:**
  - Lowest total cost
  - Zero constraint violations
  - Best fairness score (most balanced workload)

## PART III: Consulting Competition (Lectures 10-12)
*No mini-competitions - focus on final project*
**Assignment 2 Due**

### Lecture 9: Client Briefings

**Hour 1: The Projects**

**The Setup:**
"Welcome to Management Consulting! Three major clients need your expertise and each group picks one client. Each has critical business problems requiring advanced analytics. You have 3 sessions to develop and present your solution."

#### Client 1: QuickBite - The Food Delivery Revolution**
**Industry:** Food Delivery / Logistics
**CEO Persona:** "We're bleeding money on delivery costs while customers complain about cold food"

**The Problem:**
"We deliver 100 meals daily in Berlin. Current system: drivers choose their own routes. Result: €50 average cost per delivery hour, 35% late deliveries, cold food complaints. We need smart routing that considers traffic, meal prep times, and keeps food hot."

**Technical Requirements:**
- Time windows for all deliveries
- Traffic variation by time of day (approximated)
- Driver shift constraints
- 3 drivers from one depot

**Deliverables Required:**
1. Routing algorithm for 100 orders
2. Visualization of the routes
3. Performance metrics
4. Cost savings projection

#### Client 2: NurseNext - Healthcare Scheduling Crisis
**Industry:** Healthcare
**COO Message:** "Our nurses are burning out, and overtime is killing our budget"

**The Problem:**
- 50 nurses, 3 departments, complex requirements
- Current: €300K monthly overtime, 25% sick leave, high turnover
- Need: automated fair scheduling

**Technical Requirements:**
- Multiple skill levels
- Shift patterns and preferences
- Labor law compliance
- Fairness metrics

**Deliverables:**
1. Monthly schedule
2. Fairness and satisfaction metrics
3. Overtime reduction metrics
4. What-if analysis (1 or 2 random staff members sick)

#### Client 3: TechMart - Inventory Balancing
**Industry:** E-commerce / Retail
**COO Persona:** "We have €10M stuck in inventory, yet we're out of stock on bestsellers"

**The Problem:**
"We sell 100 electronics SKUs online with two warehouses. One fast warehouse for shipping with a low capacity and one large warehouse to store slow-movers. Problem: 20% stockout rate on popular items while slow-movers occupy most of the fast warehouses space. Black Friday is coming - we need smart inventory positioning NOW."

**The Data:**
- 2 years sales history
- Warehouse capacities
- Cost estimation associated with each shipping delay due to wrong warehouse allocation
- SKUs must be fully allocated to either warehouse

**Core Techniques Needed:**
- Demand forecasting with seasonality
- Inventory optimization (which SKU in which warehouse)
- Monte Carlo for simulation of costs

**Deliverables:**
1. Demand forecasting model for Black Friday month
2. Inventory allocation across the two warehouses
3. Small simulation to show the forecasted deliveries
4. Cost saving estimation due to better allocation

**Hour 2: Data Release & Exploration**

- Each package contains:
  - Comprehensive data files
  - Evaluation metrics
- Teams begin exploratory data analysis

**Hour 3-4: Development Time**

- Intensive coding session
- Instructor does rounds (5 min per team)
- Peer consultation encouraged
- At the end: each team briefly reports progress
- Share one key insight discovered

**Remind students:** Solutions don't need to be perfect - focus on reasonable approach and clear communication

### Lecture 11: Development Sprint

**Objectives:** Presentation Training and Intensive development time

**Hour-by-Hour Breakdown:**

**Hour 1: Masterclass - Selling Technical Solutions (30-60 min)**
- The McKinsey Pyramid Principle
- "So What?" test for every slide
- Dealing with skeptical executives
- Pitch structure template provided:
  1. Problem understanding (1 min)
  2. Solution approach (2 min)
  3. Results and validation (2 min)
  4. Business impact (1 min)
  5. Q&A prep (5 min)

**Hours 2-4: Team Work Time (120 min)**
- Focus on both solution AND presentation
- Peer exchanges encouraged
- Instructor does rounds (10 min per team)
- Suggested milestone: working prototype by hour 4
- End goal: Basic solution running

### Lecture 12: The Consulting Finals

**Format: Shark Tank Meets Consulting**
- Professional presentation competition

**Setting:**
- Professional atmosphere (encourage business casual)

**Hour-by-Hour Breakdown:**

**Hour 1: QuickBite Delivery Solutions**
- 3-4 teams present (12 minutes each)
  - 8 min presentation
  - 4 min Q&A from "CEO" and class
- CEO announces winning approach

**Hour 2: NurseNext Scheduling Systems**
- 3-4 teams present
- Focus on fairness metrics
- Nurses' union representative asks questions
- COO selects winning solution

**Hour 3: TechMart**
- 3-4 teams present
- Emphasis on success in business
- Director chooses best approach

**Hour 4: Awards & Reflection**

- **Awards (20 min)**
  - Based on student online voting
    - Best Solution per client
    - Best Presentation
  - Each group for each of the three topics with the best solution gets 5 bonus points on top (based on voting)

- **Course Reflection (15 min)**
  - Key learnings synthesis
  - From Python basics to complex optimization
  - Real-world applications
  - Future learning paths

## Course Evolution Notes

### After Each Cohort
- Survey: What was too hard/easy?
- Adjust competition difficulty
- Refine notebook exercises
- Update business examples

### Continuous Improvement
- Keep it practical
- Maintain business focus
- Reduce complexity if needed
- Celebrate student achievements
