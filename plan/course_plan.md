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
- Assignment 1: Risk & Forecasting (Due Lecture 8)
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
- Note, I want the students to rise the ranks of the coffee shop Bean Counter from notebook to notebook until they are the CEO at the end of notebook #11.

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
- Note, I want the students to rise the ranks of the coffee shop Bean Counter from notebook to notebook until they are the CEO at the end of notebook #11.

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

**Hour 4: Interactive Notebook #7 - Small Recap + GitHub Copilot Setup**
- Recap on previous topics with a few training tasks
- **Integration of core skills: functions + dictionaries + sorting**

- **GitHub Copilot Introduction** (15 min)
  - What is GitHub Copilot? Your AI pair programmer
  - Live demo: "Watch Copilot help me write code"
    - Example: Ask Copilot to write a function to calculate shipping costs
    - Show how to accept/reject/modify suggestions
  - Setup instructions walkthrough:
    - GitHub Student Developer Pack (free Copilot access)
    - Installing Copilot in VS Code / Jupyter
    - Quick troubleshooting tips
  - **When to use Copilot:**
    - Understanding syntax
    - Writing boilerplate code
    - Getting unstuck on simple problems
    - ❌ Replacing learning fundamentals

---

### Lecture 3: Data Science Foundation - NumPy & Pandas

**Objectives:**
- Master NumPy basics for numerical computing
- Learn essential Pandas operations for data manipulation
- Create basic visualizations for business insights
- Final readiness check before algorithms
- Note, I want the students to rise the ranks of the coffee shop Bean Counter from notebook to notebook until they are the CEO at the end of notebook #11.

**Hour 1: Interactive Notebook #8 - NumPy Essentials**
- Why NumPy? Speed vs. Python lists for numerical work
- Creating arrays (from lists, `zeros()`, `ones()`, `arange()`)
- Vectorized operations (fast element-wise math without loops)
  - Example: `prices * 1.2` (add 20% tax to all prices at once)
  - Example: `revenues - costs` (calculate profit for all products)
- Statistical functions: `mean()`, `std()`, `min()`, `max()`
- **Random number generation** (preview for Lecture 4):
  - `np.random.uniform()` - random numbers in a range
  - `np.random.normal()` - bell curve distributions
  - `np.random.randint()` - random integers
  - Simple example: Simulate 100 dice rolls, calculate average
- **Practice exercises integrated throughout** (5-10 min coding each)

**Hour 2: Interactive Notebook #9 - Pandas Basics**
- What is a DataFrame? (Spreadsheet in Python with superpowers)
- Creating DataFrames from dictionaries and lists
- Exploring data:
  - `head()`, `tail()` - preview data
  - `info()` - column types and missing values
  - `describe()` - statistical summary
  - `shape` - rows and columns count
- Selecting data:
  - Single columns: `df['column_name']`
  - Multiple columns: `df[['col1', 'col2']]`
- Creating new calculated columns: `df['profit'] = df['revenue'] - df['cost']`
- **Filtering data** with boolean conditions: `df[df['sales'] > 1000]`
  - Keep it simple: one condition at a time
  - Example: Find all products with price > 100
  - Example: Find all sales in January
- Sorting with `sort_values()`: ascending and descending
- **Reading CSV files** with `pd.read_csv()`
- Reading excel files into Pandas
- **Practice exercises integrated throughout** (5-10 min coding each)

**Hour 3: Interactive Notebook #10 - Visualization & Integration with Copilot**

- **Visualization Basics** (20 min)
  - Why visualize? "A picture is worth a thousand rows"
  - Basic plotting with matplotlib/pandas:
    - Bar charts: `df.plot(kind='bar')` - for comparisons (MOST USEFUL)
    - Line plots: `df.plot()` - for time series
    - Histograms: `df['column'].hist()` - for distributions
    - Scatter plots: `df.plot.scatter(x='x', y='y')` - for relationships
  - Customizing plots:
    - Titles: `plt.title('Sales Over Time')`
    - Labels: `plt.xlabel()`, `plt.ylabel()`

- **Integrated exercises WITH Copilot** (30 min):
  - **Exercise 1:** Load sales CSV, filter for one category, create bar chart of top 10 products
    - Students write comments, let Copilot suggest code
    - Focus: Understanding the data pipeline (filter → sort → plot)
  - **Exercise 2:** Simulate 1000 dice rolls (NumPy), plot distribution histogram
    - Practice: Ask Copilot to help with histogram styling
    - See the distribution pattern appear!
  - **Exercise 3:** Create profit column, find top 10 most profitable products, create sorted bar chart
    - Combine: calculated columns + filtering/sorting + visualization

**Hour 4: Small Lecture: Recap, Questions and Outlook**

- **Copilot Tips for Visualizations** (5 min)
  - "Copilot is GREAT at matplotlib boilerplate"
  - Show: Comment → Copilot generates full plotting code
  - Tip: Always review and understand what Copilot suggests
  - Common pitfall: Copilot might use outdated syntax, verify it works!

- **Final 10 minutes:**
  - Quick recap: "What did we learn and why does it matter?"
    - NumPy: Fast numerical operations
    - Pandas: Data exploration, filtering, groupby
    - Visualization: Communicate insights
  - Preview of Lecture 4: "Next week, Monte Carlo simulations - we'll use everything we learned today to model business uncertainty"
  - **Copilot strategy going forward:**
    - "Use it for syntax, not thinking"
    - "Your job: understand the logic, Copilot's job: remember the syntax"

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

**Scenario:**
TechVenture Innovation Fund has €2M to invest. You must select **exactly 2 startups** out of 4 candidates to invest €1M each. Which combination gives the best expected total return?

**Data Provided for Each Startup:**
Each startup's annual return follows a known probability distribution:

1. **CloudAI Solutions** - AI SaaS Platform
   - Return distribution: Normal(mean=25%, std=15%)
   - Market: Enterprise AI tools

2. **GreenGrid Energy** - Renewable Energy Tech
   - Return distribution: Normal(mean=18%, std=8%)
   - Market: Solar storage systems

3. **HealthTrack Pro** - Medical Devices
   - Return distribution: Normal(mean=30%, std=25%)
   - Market: Wearable diagnostics (high risk, high reward)

4. **FinFlow** - Fintech Payment Platform
   - Return distribution: Uniform(min=10%, max=35%)
   - Market: B2B payment processing

**Task:**
Use Monte Carlo simulation to:
1. Simulate 10,000 scenarios for each startup's annual return
2. For each possible combination of 2 startups, calculate:
   - Expected total return (sum of 2 startups × €1M each)
   - Risk (standard deviation of total return)
   - Probability of losing money (return < 0%)
   - Probability of achieving 50% total return
3. Recommend the best combination of 2 startups

**Deliverables:**
- One-slide recommendation
- Which 2 startups to invest in
- Expected total return
- Risk assessment (probability of loss)
- Brief justification (1-2 sentences)
- Optional (but nice histogram or box plot comparing return distributions)

**Competition Format:**
- **60-70 minutes development in class**
- **Students can continue development till next session**
- **Present:** 2-3 slide PDF (at the start of next session)
- **20 at start of next lecture:** Each teams present their recommendation (2 min each + Q&A)

**Starter Code Provided:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulation parameters
n_simulations = 10000
investment_per_startup = 1_000_000  # €1M

# Startup return distributions
# YOUR CODE

```

**Tips for Students:**
- Focus on getting one startup simulation working first
- Then scale to all 4 startups
- Use loops or lists to avoid repetitive code
- Copilot can help with visualization code

### Lecture 5: Forecasting the Future

**Domain Focus:** Retail & Marketing
**Key Questions:** How can we predict future demand from historical patterns?

**Hour 1: Student Presentations - Competition Lecture 4**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - Patterns in Data**
- Show sales data: Can you spot the pattern?
- Trend, seasonality, and residuals explained
- The forecasting toolkit: MA, exponential smoothing, seasonal models
- Cost of forecast errors
- Simple methods often win

**Hour 3: Notebook Session - Time Series & Forecasting Methods**

```python
# Part 1: Working with Time Series Data (20 min)
# Students will learn:
# - Converting strings to dates: pd.to_datetime()
# - Extracting date components: .dt.month, .dt.day_of_week, .dt.year
# - Sorting by date

# Part 2: Moving Averages (15 min)
# - Simple moving average: df['sales'].rolling(window=7).mean()
# - Why we use rolling averages (smoothing noise)
# - Visualizing original vs. smoothed data

# Part 3: Forecasting Methods (25 min)
# Students will implement:
# 1. Simple moving average forecast
# 2. Weighted moving average (recent data matters more)
# 3. Exponential smoothing (introduction)
# 4. Forecast accuracy metrics (MAE, RMSE)

def forecast_demand(historical_data, method='exponential'):
    """Students build multiple forecasting methods"""
    # Guided implementation with starter code
```
**Discussion (last 5 minutes):** What do the results tell us? Share insights, debugging tips, interpretation challenges.

**Hours 4: Competition - "The Predictor"**
- **Scenario:** Major retailer needs inventory planning for four christmas weeks
- **Data Provided:**
  - 2 years of weekly sales for 3 products
- **Task:**  December demand forecast per product
- **Competition Format:**
  - 60 minutes development (in class), rest at home
  - Visualization of results
  - Comparison to real values (known by lecturer) in next session
- **Bonus Points:** Lowest total forecast error

**Assignment 1 Introduction (Last 10 min):**
- "The Risk & Forecast Analyzer" - Due Lecture 8
- Part A: Portfolio optimization
- Part B: Demand forecasting implementation

### Lecture 6: Smart Quick Decisions in Scheduling

**Domain Focus:** Manufacturing Operations
**Key Question:** Can simple rules solve complex scheduling problems quickly?
**Core Concept:** Greedy/Constructive Heuristics

**Hour 1: Student Presentations - Competition Lecture 5**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Power of Simple Rules**
- The job shop scheduling problem: Why it's NP-hard (brief!!)
- Live demonstration: "The Pizza Kitchen Crisis"
  - 5 pizzas, 3 ovens, different cooking times
  - Students suggest rules → test them live
- Classic greedy rules explained:
  - SPT (Shortest Processing Time): Get quick wins
  - EDD (Earliest Due Date): Keep customers happy
  - FIFO: When in doubt, be fair
- Real-world impact: How Toyota uses these rules
- When greedy works (and when it fails spectacularly)

**Hour 3: Notebook Session - Building Schedulers**
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

**Hours 4: Competition - "The Bike Factory Friday Crisis"**
- **Scenario:** Custom bicycle factory, Friday afternoon chaos
  - "We just got 8 rush orders for Monday delivery!"
  - 16 total jobs for weekend production
  - 2 different workstations (paint, assembly)
  - Each job needs to be painterd first and then assembled
  - Overtime costs €100/hour after 8pm

- **Data Provided:**
  - Job details: processing times on both workstations
  - Machine capabilities and setup times
  - Current time: Friday 2pm

- **Task:** Minimize total cost (overtime)

- **Competition Format:**
  - 60 minutes development in class, continue at home
  - Can use any greedy rule or combination
  - Submit schedule + cost calculation
  - Comparisons of total cost

- **Bonus Points:** Lowest total cost

**Assignment 2 Introduction (Last 10 min):**
- "The Optimizer's Toolkit" - Due Lecture 10
- Will require scheduling + routing + improvement

### Lecture 7: Better Routing - Local Search & Improvements

**Domain Focus:** Logistics & Delivery
**Key Question:** How do we systematically improve solutions?
**Core Concept:** Local Search and 2-Opt

**Hour 1: Student Presentations - Competition Lecture 6**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Traveling Salesman Problem**
- What is TSP? Real-world examples (delivery, drilling, genome sequencing)
- Why is it hard? (Factorial growth: 10! = 3.6M routes)
- Construction heuristics: Nearest neighbor (greedy)
- Improvement: 2-opt swap explained visually
- When to stop improving? (no improvement found)
- The local optima trap: Why we get stuck
- Mention other neighborhood structures without too much detail:
  - 2-opt: swap edges
  - Swap: exchange customers between routes
  - Relocate: move one customer to different position

**Hour 3: Notebook Session - Building a TSP solver**
```python
# Provided to students:
- Distance calculation function
- Route visualization function
- Starting template

# Students implement:
def nearest_neighbor_route(start, cities, distances):
    """Build route by always going to nearest unvisited city"""
    # Students fill in

def calculate_route_distance(route, distances):
    """Calculate total distance of route"""
    # Students fill in

def two_opt_swap(route, i, j):
    """Reverse segment of route between i and j"""
    return route[:i] + route[i:j+1][::-1] + route[j+1:]

def improve_route(route, distances):
    """Keep trying 2-opt swaps until no improvement"""
    # Students fill in
    improved = True
    while improved:
        improved = False
        for i in range(len(route)-1):
            for j in range(i+2, len(route)):
                # Try swap, keep if better
                pass
```

- **Class Discussion (5 min):**
  - How much improvement did 2-opt give?
  - Why does it eventually stop improving?
  - Ideas for escaping local optima?

**Hours 4: Competition - "The Bakery Delivery Route"**
- **Scenario:** Artisan bakery delivers to 12 cafes each morning
  - "We promise fresh bread every morning!"
  - Must visit all cafes exactly once
  - Return to bakery at the end
  - Some cafes have time windows

- **Data Provided:**
  - 12 cafe locations (x, y coordinates)
  - Bakery location (x, y coordinates)
  - Time windows for 3 bakeries
  - Vehicle specs (capacity, speed, cost per km)

- **Task:** Minimize total distance

- **Competition Format:**
  - Initial route (construction method)
  - Final route (after improvement)
  - Total distance for each
  - Route visualization
  - Winner explains construction + improvement strategy

- **Bonus Points:** Best score (distance)

### **Lecture 8: Tough Trade-offs - Multi-Objective Optimization**
**Assignment 1 Due**

**Domain Focus:** Sustainability & Strategic Planning
**Key Question:** What do you do when you can't have it all?
**Core Concept:** Multi-Objective Optimization & Pareto Frontiers

**Hour 1: Student Presentations - Competition Lecture 7**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Balance Challenge**
- **Opening Hook:** "The Tesla Dilemma"
  - Making electric cars (performance vs. range vs. cost)
  - "You can't maximize everything - every design is a trade-off"

- **Real-world conflicts** (keep it simple):
  - Fast delivery vs. Low cost vs. Low emissions
  - Product quality vs. Manufacturing speed
  - Profit vs. Environmental impact

- **Simple Transportation Problem Example:**
  - Assigning deliveries to warehouses
  - Warehouse A: Close (low cost) but small (limited capacity)
  - Warehouse B: Far (high cost) but large (high capacity)
  - Different assignments = different trade-offs

- **Pareto Frontier Explained Visually:**
  - Dominated vs. non-dominated solutions
  - "You can only improve one thing by making something else worse"
  - **Focus on 2D visualization only** (cost vs. emissions)
  - Interactive demo: plot 5-6 solution points, identify dominated ones

- **The Weighted Sum Approach** (primary method):
  - Combine multiple objectives into single score
  - `total_score = w1 × cost + w2 × emissions`
  - Adjusting weights = shifting priorities
  - Live demo: change weights, watch optimal solution shift
  - Simple and practical for business decisions

- **Brief mention** (5 min): Other approaches exist (ε-constraint, goal programming) but weighted sum is most practical for consultants

- **Real examples:**
  - Amazon: "Fast shipping costs more, so we offer Prime vs. Standard"
  - Airlines: "We balance on-time vs. fuel cost with buffer time"

**Hour 3: Notebook Session - Weighted Sum in Action**
*Students implement a simple delivery assignment problem with two objectives*

```python
# Simplified notebook with pre-built functions for students

# Part 1: Understanding the Problem (10 min)
# - Given: 10 deliveries, 2 warehouses (A: close/small, B: far/large)
# - Objective 1: Minimize cost (distance-based)
# - Objective 2: Minimize carbon emissions (truck type matters)
# - Students calculate cost and emissions for a given assignment

# Part 2: Weighted Sum Function (15 min)
def calculate_weighted_score(assignment, w_cost=0.5, w_emissions=0.5):
    """Calculate combined score using weights"""
    cost = calculate_cost(assignment)
    emissions = calculate_emissions(assignment)
    return w_cost * cost + w_emissions * emissions

# Students implement this function
# Test with different assignments

# Part 3: Exploring Trade-offs (15 min)
# Students try different weight combinations:
# - w_cost=1.0, w_emissions=0.0 (only care about cost)
# - w_cost=0.0, w_emissions=1.0 (only care about emissions)
# - w_cost=0.5, w_emissions=0.5 (balanced)
# - w_cost=0.7, w_emissions=0.3 (cost-focused)

# Part 4: Visualizing the Pareto Frontier (15 min)
# Pre-built plotting function provided
# Students generate 5-10 different solutions (using greedy heuristics from Lecture 6)
# Plot them on cost vs. emissions chart
# Identify which solutions are dominated
```

- **Class Discussion (5 min):**
  - Which weight combination would you recommend? Why?
  - How would you present these trade-offs to a CEO?
  - What if the CEO says "I want low cost AND low emissions"?

**Hours 4: Competition - "The Green Logistics Challenge"**

- **Scenario:** Logistics company facing new EU regulations
  - "We must cut carbon 40% by 2030 while staying profitable and maintaining service"
  - Design transportation problem assignment

- **Two Objectives:**
  1. **Minimize Delivery Cost:** Distance × delivery frequency × cost per km
  2. **Minimize Carbon Emissions:** Distance × delivery frequency × emissions per km

- **Data Provided:**
  - 12 customers (x, y) coordinates
  - 3 distribution center locations (fixed positions)
  - 1 distribution center has electric cars with low emissions but is more expensive
  - Emission rates: standard trucks emit 0.2 kg CO₂/km

- **Task:** Assign each of the 12 customers to one of the 3 distribution centers

- **Constraints:**
  - Each customer assigned to exactly one center
  - All customers must be served

- **Deliverables:**
  1. Your zone-to-center assignment
  2. Total cost and total emissions
  3. Optional: Scatter plot showing zones colored by assigned center
  4. Brief justification (1-2 sentences): Why these weights?

- **Competition Format:**
  - **60 minutes development in classe, continue at home**
  - Students can use greedy assignment (from Lecture 6) with weighted sum
  - Present: metrics + 2-3 visualization slides
  - **Evaluation**: Each team picks their own weights (must justify)
  - **Winner**: Best solution quality given their stated weights + best justification

### Lecture 9: The Metaheuristics Toolkit - Beyond Greedy

**Domain Focus:** Complex Optimization
**Key Question:** What advanced techniques exist when greedy and local search aren't enough?
**Core Concept:** Survey of Metaheuristics (awareness, not implementation)

**Hour 1: Student Presentations - Competition Lecture 8**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Optimization Landscape**

- **Opening: The Local Optima Trap** (10 min)
  - "Remember Lecture 7? Our 2-opt improvement got stuck."
  - Visualization: Lost in the mountains at night with a flashlight
  - You can see nearby solutions, but the best solution might be far away
  - Real example: Your delivery route is good, but there's a MUCH better one across town

- **The Three Levels of Optimization** (5 min)
  ```
  Level 1: Construction (Greedy) → Get A solution fast
  Level 2: Improvement (Local Search) → Make it better
  Level 3: Metaheuristics → Escape traps, explore widely
  ```

- **Metaheuristic #1: Simulated Annealing** (10 min)
  - **Metaphor:** Cooling molten metal to form perfect crystals
  - **Key idea:** Sometimes accept WORSE solutions to escape traps
  - **The temperature trick:**
    - Hot (early): "Let's try something crazy!" (accept bad moves often)
    - Warm (middle): "Getting pickier..." (accept bad moves sometimes)
    - Cold (late): "Only improvements now" (like hill climbing)
  - **Live demo video/animation:** Watch SA escape a trap where hill climbing fails
  - **When to use:** Scheduling, assignment problems, discrete optimization
  - **GenAI tip:** "ChatGPT/Copilot can write SA code if you describe your problem clearly"

- **Metaheuristic #2: Genetic Algorithms** (10 min)
  - **Metaphor:** Evolution and natural selection
  - **Key idea:** Maintain a POPULATION of solutions, combine the best ones
  - **The process:**
    1. Start with 50 random solutions (population)
    2. Pick the best 10 (selection - "survival of the fittest")
    3. Combine pairs to create new solutions (crossover - "breeding")
    4. Randomly change some parts (mutation - "genetic variation")
    5. Repeat for many generations
  - **Visual:** Show how solutions "evolve" over 100 generations
  - **When to use:** Complex problems with many variables, when you have time
  - **Real examples:** NASA uses GAs for antenna design, engineers for structural optimization
  - **GenAI tip:** "Copilot knows GA templates - just describe your fitness function"

- **Metaheuristic #3: Tabu Search** (5 min)
  - **Metaphor:** Exploration with a memory/no-return policy
  - **Key idea:** Keep a "tabu list" of recent moves - don't repeat them
  - **Why it works:** Forces exploration of new areas instead of cycling
  - **When to use:** When your algorithm keeps revisiting the same solutions
  - **Simple example:** "I just swapped customers A and B, so don't swap them back for 10 iterations"

- **Metaheuristic #4: Ant Colony Optimization** (5 min)
  - **Metaphor:** How ants find shortest paths to food
  - **Key idea:** Good solutions leave "pheromone trails" that attract future solutions
  - **The process:** Early ants explore randomly, later ants follow successful trails
  - **When to use:** Routing problems (TSP, VRP), network design
  - **Cool fact:** Amazon warehouse robots use ACO-inspired algorithms

- **Quick mentions** (3 min):
  - **Particle Swarm:** Birds flocking, good for continuous optimization
  - **Variable Neighborhood Search:** Try different neighborhoods when stuck
  - **Many more exist!** Research is ongoing

- **Comparison Table - Your Decision Guide:**
  ```
  Method              | Speed    | Code Complexity | Best For                    | GenAI Help?
  --------------------|----------|-----------------|-----------------------------|--------------
  Greedy              | Fastest  | Simple          | Quick decisions             | Easy
  Local Search (2-opt)| Fast     | Medium          | Improving solutions         | Easy
  Simulated Annealing | Medium   | Medium          | Escaping local optima       | Easy
  Genetic Algorithm   | Slow     | Complex         | Complex multi-variable      | Medium
  Tabu Search         | Medium   | Medium          | Preventing cycling          | Medium
  Ant Colony          | Slow     | Complex         | Routing/path problems       | Hard
  ```

- **Closing message:** (2 min)
  - "You don't need to memorize implementations"
  - "Key skill: Knowing WHICH tool to use for WHICH problem"
  - "With GenAI, you can use these techniques even without deep expertise"
  - "In today's notebook, you'll see examples and learn how to work WITH AI to apply them"

**Hour 3: Interactive Notebook - Metaheuristics in Action (Demos + GenAI Integration)**

**NEW APPROACH:** Students don't implement from scratch - they run provided implementations and learn to use GenAI to adapt them

**Part 1: Understanding Through Demos** (20 min)
- **Pre-built visualization notebooks provided**
- Students run and observe:
  ```python
  # Demo 1: Hill Climbing vs. Simulated Annealing (10 min)
  # - Same TSP problem, watch both algorithms
  # - See SA escape local optima
  # - Adjust temperature schedule, observe impact
  # Students just RUN code, observe, answer questions:
  #   Q: "At what iteration did SA escape the trap?"
  #   Q: "What happens if you cool too fast?"

  # Demo 2: Genetic Algorithm Evolution (10 min)
  # - Watch 100 generations evolve
  # - See best solution improve over time
  # - Adjust mutation rate, observe impact
  # Students answer:
  #   Q: "Which generation found the best solution?"
  #   Q: "What happened when mutation rate = 0?"
  ```

**Part 2: Working WITH GenAI** (20 min)
- **Guided exercise: Adapting code with Copilot/ChatGPT**
  ```python
  # Provided: Basic SA template for TSP
  # Task: Adapt it for a simple assignment problem

  # Step 1: Students describe the problem to Copilot in comments
  # "I have 10 tasks and 3 workers. Each task takes different time on different workers."
  # "I want to minimize total completion time."

  # Step 2: Let Copilot suggest neighborhood moves
  # Students learn: How to prompt AI, how to verify suggestions

  # Step 3: Run adapted code, compare to greedy solution
  ```

- **Key learning outcome:** "I can DESCRIBE a problem and USE metaheuristics, even if I don't code them from scratch"

**Part 3: Decision Framework Practice** (10 min)
- Students get 3 scenario cards:
  1. "Schedule 50 nurses across 7 days with complex constraints"
  2. "Route 100 deliveries across 5 vehicles"
  3. "Assign 20 projects to 8 teams with skill requirements"

- **Task:** For each scenario, recommend:
  - Which metaheuristic to try?
  - Why that one?
  - How would you describe it to GenAI to get code?

- **Class discussion:** Share recommendations, instructor validates

**Class Discussion (5 min):**
- "What surprised you about metaheuristics?"
- "Which one would you try first for your consulting project?"
- "How confident do you feel using GenAI to implement these?"

**Hours 4: Competition - "The Weekend Restaurant Staffing Challenge"**

- **Scenario:** A three Michelin star restaurant weekend scheduling crisis
  - "I need to schedule my 18 servers across 6 shifts this weekend"
  - "Problem: My experienced servers are expensive, but customers expect quality service"
  - "Last weekend I had all junior staff on Saturday dinner - disaster! But using experienced staff everywhere kills my profit margins"

- **The Challenge:**
  - We have skill requirements for quality service (experienced servers needed)
  - But we don't have enough experienced servers to meet all requirements
  - Must balance: Labor costs vs. Service quality penalties
  - Students can use greedy heuristics OR Simulated Annealing

- **Data Provided:**

  **18 Servers Available:**
  - 6 Experienced Servers (€75/hour, can handle any shift)
  - 12 Junior Servers (€25/hour, still learning)

  **6 Shifts This Weekend (Friday-Sunday):**
  - Friday Dinner - 4 hours
  - Friday Late - 4 hours
  - Saturday Lunch - 4 hours
  - Saturday Dinner - 4 hours
  - Sunday Lunch - 4 hours
  - Sunday Dinner - 4 hours

  **Each shift needs exactly 3 servers**
  - Total: 6 shifts × 3 servers = 18 positions
  - Everyone works exactly once

- **Shift Quality Requirements:**
  - **Dinner shifts** (busy, high-value customers): Need at least 2 Experienced servers
  - **Lunch shifts** (moderate traffic): Need at least 1 Experienced server
  - **Late shift** (cleanup): No requirement (can be all Junior)

- **The Problem:**
  - Minimum Experienced needed: 2+0+1+2+1+2 = **8 Experienced servers**
  - Available: **Only 6 Experienced servers** ❌
  - **We MUST violate some requirements!** Which shifts take the hit?

- **Cost Structure:**
  - **Labor cost:** Experienced = €25/hour, Junior = €15/hour
  - **Understaffing penalty:** €200 per shift that doesn't meet skill requirements
    - Dinner with <2 Experienced: €200 penalty (poor service, complaints)
    - Lunch with <1 Experienced: €200 penalty (slower service)
    - Late shift: No penalty (it's just cleanup)

- **Task:** Assign 18 servers to 6 shifts (3 per shift) to minimize total cost (labor + penalties)

- **Constraints:**
  - Each shift gets exactly 3 servers
  - Each server works exactly 1 shift
  - All 18 positions must be filled

- **Approaches Allowed:**
  - **Greedy heuristic** - Design your own rule-based assignment (perfectly acceptable!)
  - **Local search improvement** - Start with greedy, then try swaps to improve
  - **Metaheuristics with GenAI** - Use ChatGPT/Copilot to implement SA, GA, or other methods (optional!)
  - **Random search** - Generate many random solutions, pick best
  - **Your creative approach** - Surprise us!

- **GenAI Usage Encouraged:**
  - "I have 18 servers (6 experienced at €75/hr, 12 junior at €25/hr) to assign to 6 shifts..."
  - Ask ChatGPT/Copilot to suggest an approach
  - You can use metaheuristics WITHOUT coding them from scratch!
  - Focus on understanding the solution, not implementing the algorithm

- **Deliverables:**
  1. Complete schedule (which servers on which shifts)
  2. Total labor cost breakdown
  3. Penalties incurred (which shifts violated, why)
  4. Total cost (labor + penalties)
  5. Brief explanation (2-3 sentences): What was your approach?

- **Competition Format:**
  - 60 minutes development in class, rest at home
  - **Any approach accepted** - From simple greedy to advanced metaheuristics
  - **GenAI is your partner** - Use it strategically!
  - Submit: one-slide summary with schedule + costs + approach description
  - **Evaluation:** Lowest total cost wins

- **Bonus Points:**
  - **Best total cost** (lowest): Standard competition bonus (10/6/3 points)

- **Tips for Students:**
  - **If going greedy/simple:**
    - Assign experienced servers to dinner shifts first (prioritize high penalties)
    - Minimize penalties first, then optimize labor cost
    - Try multiple greedy rules, pick best result
    - Can still win with a smart greedy approach!

  - **If using GenAI for metaheuristics:**
    - Clearly describe the problem in your prompt
    - Specify constraints explicitly (each shift needs 3, each server works once)
    - Ask for SA or GA implementation
    - Verify the code works and makes sense
    - Understand what the algorithm is doing (you'll need to explain it!)

  - **Hybrid approach (recommended):**
    - Start with greedy solution (fast, understandable)
    - Use GenAI to improve it with local search or SA
    - Compare results - document the improvement

## PART III: Consulting Competition (Lectures 10-12)
*No mini-competitions - focus on final project*
**Assignment 2 Due**

### Lecture 9: Client Briefings

**Hour 1: Student Presentations - Competition Lecture 9**
- Students present their solutions to the last competition in short 2-3 minute pitches
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: The Projects**

**The Setup:**
"Welcome to Management Consulting! Three major clients need your expertise and each group picks one client. Each has critical business problems requiring advanced analytics. You have 3 sessions to develop and present your solution."

#### Client 1: QuickBite - The Food Delivery Revolution**
**Industry:** Food Delivery / Logistics
**CEO Persona:** "We're bleeding money on delivery costs while customers complain about cold food"

**The Problem:**
"We deliver 32 meals daily in Berlin. Current system: drivers choose their own routes. Result: €50 average cost per delivery hour, 35% late deliveries, cold food complaints. We need smart routing that keeps food hot."

**Technical Requirements:**
- Time windows for all deliveries (but simple ones)
- Violations mean cold food and a penalty
- 3 drivers from one depot

**Deliverables Required:**
1. Routing algorithm for 32 orders
2. Visualization of the routes
3. Performance metrics
4. Cost savings projection

#### Client 2: NurseNext - Healthcare Scheduling Crisis
**Industry:** Healthcare
**COO Message:** "Our nurses are burning out, and overtime is killing our budget"

**The Problem:**
- 20 nurses, 2 departments, complex requirements
- Current: €300K monthly overtime, 25% sick leave, high turnover
- Need: automated fair scheduling

**Technical Requirements:**
- Multiple skill levels
- Shift patterns
- Labor law compliance (consecutive days)
- Fairness metrics

**Deliverables:**
1. Weekly schedule
2. Fairness metrics
3. Overtime reduction metrics
4. What-if analysis (1 or 2 random staff members sick)

#### Client 3: TechMart - Inventory Balancing
**Industry:** E-commerce / Retail
**COO Persona:** "We have €10M stuck in inventory, yet we're out of stock on bestsellers"

**The Problem:**
"We sell 50 electronics SKUs online with two warehouses. One fast warehouse for shipping with a low capacity and one large warehouse to store slow-movers. Problem: 20% stockout rate on popular items while slow-movers occupy most of the fast warehouses space. Black Friday is coming - we need smart inventory positioning NOW."

**The Data:**
- 2 years sales history
- Warehouse capacities
- Cost estimation associated with each shipping delay due to wrong warehouse allocation
- SKUs must be fully allocated to either warehouse

**Core Techniques Needed:**
- Demand forecasting
- Inventory optimization (which SKU in which warehouse)
- Monte Carlo for simulation of costs

**Deliverables:**
1. Demand forecasting model for Black Friday month
2. Inventory allocation across the two warehouses
3. Small simulation to show the forecasted deliveries
4. Cost saving estimation due to better allocation

**Data Release & Exploration**

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
