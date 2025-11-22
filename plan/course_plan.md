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
  1. **Hour 1:** Competition presentations from previous week (student solutions)
  2. **Hour 2:** Interactive lecture explaining core concepts using **competition scenario**
  3. **Hour 3:** Interactive notebook with **Bean Counter narrative** for practice
  4. **Hour 4:** Competition challenge (same scenario as lecture) + development time
  5. **Bonus Points:** Best solution team gets bonus points toward final grade
- **Lectures 10-12:** Consulting Project
  1. **Hour 1:** Introduction of new concept/ presentation training
  2. **Hour 3-4:** Students work in groups on their project and lecturer checks progress/helps

### Content Structure for Lectures 4-9
**Important Pedagogical Approach:**
- **Lecture (Hour 2):** Focus on the **competition client/scenario** to preview the challenge
- **Notebook (Hour 3):** Use **Bean Counter narrative** consistently for practice
- **Competition (Hour 4):** Apply skills to the **same scenario from the lecture**

This structure ensures:
1. Students see the competition context during the lecture
2. Practice safely with familiar Bean Counter scenarios
3. Apply their skills to the previewed challenge
4. No direct copying possible (different contexts for practice vs. competition)

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

**Hour 1: Student Presentations** - Competition results from Lecture 3

**Hour 2: Interactive Lecture - Welcome to Uncertainty**
- **Focus on TechVenture Innovation Fund scenario** (the competition)
- Interactive demonstration: Investment portfolio risk
- Probability distributions in investment returns
- The mathematics of risk: expected value, variance, percentiles
- When and why Monte Carlo beats analytical methods
- Show example with 2 of 4 startups selection

**Hour 3: Building Simulations (Notebook with Bean Counter)**
```python
# Bean Counter CEO scenario:
# Should we open a new Bean Counter location?
# Students will implement:
# 1. Simple revenue simulation for new store
# 2. Adding uncertainty to costs and demand
# 3. Correlation between variables
# 4. Confidence interval calculation
# 5. ROI visualization

def simulate_bean_counter_expansion(n_simulations=10000):
    """Should Bean Counter expand to a new location?"""
    # Students code along with Bean Counter context
    daily_customers = np.random.normal(100, 20, n_simulations)
    avg_purchase = np.random.uniform(8, 12, n_simulations)
    # Build up complexity gradually...
```
**Discussion (last 5 minutes):** What do the results tell us? Share insights, debugging tips, interpretation challenges.

**Hour 4: Competition - "The Startup Investment Challenge"**

**Scenario (same as lecture):**
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
- Students present their solutions to the startup investment competition
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - Patterns in Data**
- **Focus on MegaMart Christmas Challenge scenario** (the competition)
- Show MegaMart's historical sales: Can you spot the pattern?
- Trend, seasonality, and residuals in retail data
- The forecasting toolkit: MA, exponential smoothing, Holt-Winters
- Cost of forecast errors for MegaMart inventory
- Simple methods often win

**Hour 3: Notebook Session - Bean Counter's Seasonal Forecasting**

```python
# Bean Counter CEO scenario:
# Predicting demand for seasonal drinks
# - Iced Coffee (summer)
# - Pumpkin Spice Latte (fall)
# - Peppermint Hot Chocolate (winter)

# Part 1: Working with Bean Counter's Time Series (20 min)
# - Converting order timestamps to dates
# - Extracting patterns from 2 years of data
# - Identifying seasonal peaks

# Part 2: Moving Averages for Coffee Sales (15 min)
# - Simple moving average: df['sales'].rolling(window=7).mean()
# - Smoothing daily fluctuations
# - Visualizing Bean Counter trends

# Part 3: Forecasting Methods for Bean Counter (25 min)
# Students will implement:
# 1. Simple MA for steady products
# 2. Weighted MA for trending items
# 3. Exponential smoothing
# 4. Accuracy metrics for Bean Counter

def forecast_bean_counter_demand(historical_data, method='exponential'):
    """Predict next month's coffee demand"""
    # Implementation with Bean Counter context
```
**Discussion (last 5 minutes):** How to handle seasonal products at Bean Counter?

**Hour 4: Competition - "MegaMart's Christmas Challenge"**
- **Scenario (same as lecture):** MegaMart needs December inventory planning
- **Data Provided:**
  - 2 years of weekly sales for 3 products
- **Task:** Forecast 4 weeks of December demand per product
- **Competition Format:**
  - 60 minutes development (in class), rest at home
  - Visualization of forecasts
  - Comparison to actual values in next session
- **Bonus Points:** Lowest total forecast error (MAE)

**Assignment 1 Introduction (Last 10 min):**
- "The Risk & Forecast Analyzer" - Due Lecture 8
- Part A: Portfolio optimization
- Part B: Demand forecasting implementation

### Lecture 6: Smart Quick Decisions in Scheduling

**Domain Focus:** Manufacturing Operations
**Key Question:** Can simple rules solve complex scheduling problems quickly?
**Core Concept:** Greedy/Constructive Heuristics

**Hour 1: Student Presentations - Competition Lecture 5**
- Students present their MegaMart forecasting solutions
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Power of Simple Rules**
- **Focus on Custom Cycles bike factory scenario** (the competition)
- The two-stage scheduling problem: Assembly → Painting
- Live demonstration: "The Bike Factory Friday Crisis"
  - 16 bikes, 2 workstations, overtime costs
  - Students suggest rules → test them live
- Classic greedy rules for bike production:
  - SPT: Complete quick bikes first
  - EDD: Meet Rush order deadlines
  - FIFO: Fair processing order
- Cost analysis: Overtime (€100/hr) vs. penalties (€50-150)
- When greedy works (and when hybrids win)

**Hour 3: Notebook Session - Bean Counter's Scheduling Mastery**
*Bean Counter CEO manages Friday rush*
```python
# Bean Counter CEO scenario:
# 47 coffee orders on Friday morning
# 3 espresso machines
# Various customer deadlines

# Students will implement:
def schedule_bean_counter_spt(orders):
    """Quick orders first at Bean Counter"""
    # Sort by processing time
    # Calculate wait times

def schedule_bean_counter_edd(orders):
    """Meeting coffee deadlines"""
    # Sort by customer pickup time
    # Minimize late orders

def visualize_coffee_gantt(schedule):
    """Bean Counter's schedule visualization"""
    # Timeline of coffee production

def calculate_bean_counter_metrics(schedule):
    """Bean Counter performance metrics"""
    return {
        'avg_wait_time': ...,
        'late_orders': ...,
        'customer_satisfaction': ...
    }

# Test on 47 real Friday orders
# CEO decision: which rule for Bean Counter?
```
**Discussion (last 5 minutes):** Which rule maximizes Bean Counter customer satisfaction?

**Hour 4: Competition - "The Bike Factory Friday Crisis"**
- **Scenario (same as lecture):** Custom Cycles Manufacturing
  - 16 bicycle orders (Standard, Rush, Custom)
  - 2 workstations: Assembly → Painting
  - Overtime costs €100/hour after Saturday 8pm
  - Rush penalties €150, Standard €50

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
- Students present their bike factory scheduling solutions
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Bakery Delivery Challenge**
- **Focus on Artisan Bakery scenario** (the competition)
- The morning bread delivery problem: 12 cafes, fresh bread promise
- TSP complexity: 12! = 479 million possible routes
- Construction: Nearest neighbor for bakery routes
- Improvement: 2-opt swaps to reduce driving distance
- Live demo with bakery's actual cafe locations
- When local search gets stuck: The bakery's dilemma
- Time windows add complexity (some cafes open early)

**Hour 3: Notebook Session - Bean Counter's Delivery Optimization**
*Bean Counter CEO optimizes coffee bean deliveries*
```python
# Bean Counter CEO scenario:
# Delivering coffee beans to 10 franchise locations
# Single delivery truck, minimize fuel costs

# Provided to students:
- Bean Counter location coordinates
- Franchise distances
- Visualization functions

# Students implement for Bean Counter:
def bean_counter_nearest_neighbor(start, franchises, distances):
    """Build delivery route for Bean Counter franchises"""
    # Students implement

def calculate_bean_route_distance(route, distances):
    """Total distance for coffee delivery route"""
    # Students implement

def improve_bean_route(route, distances):
    """2-opt improvement for Bean Counter deliveries"""
    # Use 2-opt swaps to optimize
    # Track improvement metrics

# Test on real Bean Counter franchise data
# How much fuel cost saved?
```

- **Discussion (5 min):** How much did 2-opt save Bean Counter on delivery costs?

**Hour 4: Competition - "The Artisan Bakery Delivery Route"**
- **Scenario (same as lecture):** Morning bread delivery optimization
  - 12 cafes requiring fresh bread
  - Must visit all cafes exactly once
  - Return to bakery at the end
  - 3 cafes have early time windows

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
- Students present their bakery delivery route solutions
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - The Green Logistics Challenge**
- **Focus on logistics company's EU regulation challenge** (the competition)
- The trade-off: Cut carbon 40% while staying profitable
- 12 customers, 3 distribution centers, conflicting objectives
- One center has electric vehicles (low emissions, high cost)
- Visualizing the Pareto frontier: Cost vs. Emissions
- Weighted sum approach: `score = w1 × cost + w2 × emissions`
- Live demo: Adjusting weights shifts optimal assignments
- Real logistics decisions: Amazon's Prime vs. Standard trade-off

**Hour 3: Notebook Session - Bean Counter's Sustainability Decisions**
*Bean Counter CEO balances profit and environment*
```python
# Bean Counter CEO scenario:
# Opening new locations: Downtown (profitable, high emissions)
# vs. Suburban (less profit, green building)
# Supplier choice: Local (expensive, low carbon)
# vs. International (cheap, high carbon)

# Part 1: Bean Counter's Dilemma (10 min)
# - 8 potential new locations for Bean Counter
# - 2 objectives: Maximize profit, Minimize carbon footprint
# - Calculate both metrics for each location

# Part 2: Weighted Decision Making (15 min)
def bean_counter_score(location, w_profit=0.5, w_carbon=0.5):
    """Score potential Bean Counter locations"""
    profit = calculate_location_profit(location)
    carbon = calculate_carbon_impact(location)
    return w_profit * profit - w_carbon * carbon

# Part 3: Bean Counter Trade-offs (15 min)
# Test different corporate strategies:
# - Profit-first (w_profit=0.9)
# - Green-first (w_carbon=0.9)
# - Balanced (w_profit=0.5)
# What's best for Bean Counter's brand?

# Part 4: Presenting to Bean Counter Board (15 min)
# Create Pareto frontier visualization
# Identify dominated location options
# Prepare CEO recommendation
```

- **Discussion (5 min):** What weights align with Bean Counter's values?

**Hour 4: Competition - "The Green Logistics Challenge"**

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
- Students present their green logistics solutions
- Best student group receives 10 BP, second receives 6 BP and third receives 3 BP.

**Hour 2: Interactive Lecture - Restaurant Staffing Optimization**
- **Focus on three-star restaurant staffing challenge** (the competition)
- The weekend crisis: 18 servers, 6 shifts, skill requirements
- Problem: Only 6 experienced servers but need 8 (impossible!)
- Trade-offs: Labor costs vs. service quality penalties

- **Why Simple Methods Fail:**
  - Greedy gets stuck (can't escape bad assignments)
  - 2-opt doesn't help (different problem structure)
  - Need smarter exploration of solution space

- **The Three Levels Applied to Restaurant:**
  ```
  Level 1: Greedy assignment → Quick but suboptimal
  Level 2: Local swaps → Minor improvements
  Level 3: Metaheuristics → Smart exploration
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

**Hour 3: Notebook - Bean Counter's Advanced Optimization**
*Bean Counter CEO tackles complex scheduling with metaheuristics*

**Part 1: Bean Counter's Staffing Challenge** (20 min)
- **Pre-built demos for Bean Counter scenarios:**
  ```python
  # Demo 1: Bean Counter barista scheduling
  # - 20 baristas, different skill levels
  # - Watch greedy vs. simulated annealing
  # - SA escapes local optima in staff assignments
  # Students observe and answer:
  #   Q: "When did SA find better schedule?"
  #   Q: "How much cost saved vs greedy?"

  # Demo 2: Bean Counter expansion planning
  # - Genetic algorithm for location selection
  # - 50 potential sites, choose best 10
  # - Watch solutions evolve
  # Students analyze:
  #   Q: "Which generation found best locations?"
  #   Q: "How diverse were final solutions?"
  ```

**Part 2: Adapting for Bean Counter with GenAI** (20 min)
- **Bean Counter-specific problems:**
  ```python
  # Provided: SA template for scheduling
  # Task: Adapt for Bean Counter's holiday staffing

  # Step 1: Describe Bean Counter's problem to Copilot
  # "Bean Counter needs to schedule 30 baristas across
  # Christmas week with varying demand and skills"

  # Step 2: Let Copilot suggest Bean Counter-specific moves
  # - Swap shifts between baristas
  # - Move experienced staff to rush hours

  # Step 3: Compare to Bean Counter's current manual approach
  ```

**Part 3: Bean Counter Decision Framework** (10 min)
- Bean Counter scenarios for metaheuristic selection:
  1. "Holiday week scheduling with 50 staff"
  2. "Delivery routing for 20 franchises"
  3. "Menu optimization across 15 locations"

- **CEO Decision:** Which technique for each Bean Counter challenge?

- **Class discussion:** Share recommendations, instructor validates

**Class Discussion (5 min):**
- "What surprised you about metaheuristics?"
- "Which would Bean Counter benefit from most?"
- "How confident do you feel using GenAI to implement these?"

**Hour 4: Competition - "The Three-Star Restaurant Staffing Challenge"**

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

### Lecture 10: Client Briefings

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
"We deliver 100 meals daily in Berlin. Current system: drivers choose their own routes. Result: way too high average cost per delivery hour, 75% late deliveries, cold food complaints. We need smart routing that keeps food hot."

**Technical Requirements:**
- Time windows for all deliveries, which can be violated
- Violations mean cold food and a penalty
- 4 drivers from one depot

**Deliverables Required:**
1. Routing algorithm for 100 orders
2. Visualization of the routes
3. Performance metrics
4. Cost savings projection

#### Client 2: NurseNext - Healthcare Scheduling Crisis
**Industry:** Healthcare
**COO Message:** "Our nurses are burning out, and overtime is killing our budget"

**The Problem:**
- 20 nurses, 3 different departments, complex requirements
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
- 3 years sales history
- Warehouse capacities
- Cost estimation associated with each shipping delay due to wrong warehouse allocation
- SKUs must be fully allocated to either warehouse
- Uncertainty regarding some things to make monte carlo useful

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
