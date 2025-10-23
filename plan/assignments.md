# Management Science Assignments for Business Students

---

## Assignment 1: Risk Analysis & Forecasting
**Due:** Start of Lecture 6
**Weight:** 20% of final grade
**Expected Time:** 3-5 hours
**Format:** Jupyter notebook with code and explanations
**Work:** Groups

### Overview
You're a junior analyst at a consulting firm. A client needs help with two common business problems:
1. Understanding investment risk using simulation
2. Forecasting product demand

**Goal:** Show you can apply Monte Carlo simulation and basic forecasting to real business problems.

---

### Part A: Investment Risk Simulation (50%)

#### The Scenario
Your client wants to invest €100,000 in a new product launch. They need to understand the risk.

#### Given Information
- Best case: €300,000 return (20% probability)
- Most likely: €150,000 return (60% probability)
- Worst case: €50,000 return (20% probability)
- These probabilities change based on market conditions (you'll simulate this uncertainty)

#### Your Tasks

**Task 1: Build a Simple Monte Carlo Simulation (15%)**
```python
# Create a function that:
# 1. Runs 10,000 simulations
# 2. For each simulation, randomly picks an outcome
# 3. Returns all simulation results

def simulate_investment(n_simulations=10000):
    # Your code here
    # Hint: use np.random.choice() with probabilities
    pass
```

**Task 2: Add Uncertainty (15%)**
```python
# Now make it more realistic:
# The probabilities themselves are uncertain!
# - Best case probability: 10% to 30% (uniform distribution)
# - Worst case probability: 10% to 30% (uniform distribution)
# - Most likely probability: whatever remains to sum to 100%

def simulate_with_uncertainty(n_simulations=10000):
    # Your code here
    # For each simulation, first randomly generate probabilities
    # Then use those probabilities to pick outcome
    pass
```

**Task 3: Analysis & Visualization (20%)**
- Create a histogram of returns
- Calculate the probability of losing money (return < €100,000)
- Calculate the 95% Value at Risk (VaR) - "We're 95% confident we won't lose more than X"
- Create a simple chart showing how the probability of profit changes with different investment amounts
- **Business Question:** Should the client make this investment? Write 3-4 sentences explaining your recommendation

---

### Part B: Demand Forecasting (50%)

#### The Scenario
A retail client provides 2 years of monthly sales data. They need forecasts for the next 3 months to plan inventory.

#### Your Tasks

**Task 1: Implement Moving Average (15%)**
```python
# Create a function for moving average forecast
def moving_average_forecast(data, window_size=3):
    # Your code here
    # Return forecast for next period
    pass

# Test with window sizes of 2, 3, and 6 months
# Which works best and why?
```

**Task 2: Implement Exponential Smoothing (15%)**
```python
# Create exponential smoothing forecast
def exponential_smoothing(data, alpha=0.3):
    # Your code here
    # Remember: new forecast = alpha * actual + (1-alpha) * old forecast
    pass

# Try alpha values: 0.1, 0.3, 0.5, 0.9
# What does alpha control?
```

**Task 3: Evaluate and Compare (20%)**
- Split data: first 20 months for training, last 4 months for testing
- Calculate forecast error (MAE) for each method
- Create a line chart showing: actual sales, moving average forecast, exponential smoothing forecast
- **Business Question:** Which method would you recommend and why? How much safety stock should they hold (just as an estimation)? (Write 3-4 sentences)

#### Data Provided
```python
# sales_data.csv contains:
# month, sales_units, season (spring/summer/fall/winter)
# Just 24 rows of data - simple and manageable
```

---

## Assignment 2: Optimization in Practice
**Due:** Start of Lecture 10
**Weight:** 20% of final grade
**Expected Time:** 4-5 hours
**Format:** Jupyter notebook with code and explanations
**Work:** Groups

### Overview
Your consulting firm has been hired by "CityExpress," a local delivery company. They have two main operational challenges that need optimization solutions.

---

### Part A: Smart Delivery Routes (50%)

#### The Scenario
CityExpress has 12 customer orders to deliver tomorrow.
They have 1 delivery van and need an efficient route starting and ending at their depot.

#### Your Tasks

**Task 1: Build a Basic Route (20%)**
```python
def calculate_distance(location1, location2):
    """Calculates distance between two locations"""
    # YOUR CODE HERE:

def calculate_total_distance(route, locations):
    """Calculates total distance for a route"""
    # YOUR CODE HERE

def nearest_neighbor_route(depot, customer_locations):
    """
    Build a route using nearest neighbor heuristic:
    1. Start at depot
    2. Go to nearest unvisited customer
    3. Repeat until all customers visited
    4. Return to depot
    """
    route = [depot]
    unvisited = customer_locations.copy()
    current = depot

    # YOUR CODE HERE: Build the route
    # Hint: For each position, find nearest unvisited customer

    route.append(depot)  # Return to depot
    return route

# Test your function and calculate total distance
```

**Task 2: Improve Your Route (20%)**
```python
def try_swap_improvement(route, locations):
    """
    Tries to improve route by swapping two customers
    Returns: improved_route, improvement_amount
    """
    # YOUR CODE HERE:

def improve_route(initial_route, locations, max_iterations=50):
    """
    Repeatedly try to improve the route
    Stop when no improvement found or max_iterations reached
    """
    current_route = initial_route.copy()
    total_improvement = 0

    for i in range(max_iterations):
        # YOUR CODE: Use try_swap_improvement function
        # If improvement found, update current_route
        # Track total improvement
        # Stop if no improvement found
        pass

    return current_route, total_improvement

# How much did you improve the original route?
```

**Task 3: Business Analysis (10%)**
- Visualize both routes (before and after improvement) on a map or as graph
- Calculate:
  - Original route distance
  - Improved route distance
  - Percentage improvement
  - Estimated cost savings (€2 per km)
- **Business Question:** If CityExpress has 50 deliveries per day, how much could they save per month with route optimization? (3-4 sentences)

#### Data Provided
```python
# location_data.csv contains:
# x,y coordinates of 12 customers and the depot x,y coordinates
# Just 13 rows of data - simple and manageable
```

---

### Part B: Staff Scheduling Challenge (50%)

#### The Scenario
CityExpress warehouse needs to schedule 6 workers across a week (Monday-Friday). Each day needs 2-3 workers, and each worker should work exactly 3 days.

#### Your Tasks

**Task 1: Create a Valid Schedule (20%)**
```python
def check_schedule_valid(schedule):
    """Checks if schedule meets all constraints"""
    # YOUR CODE HERE:

def visualize_schedule(schedule):
    """Creates a nice visualization of the schedule"""
    # YOUR CODE HERE:

# You implement:
def create_basic_schedule():
    """
    Create a schedule that meets basic requirements:
    - 6 workers, 5 days
    - Each worker works exactly 3 days
    - Each day has 2-3 workers

    Return: 5x6 array where schedule[day][worker] = 1 if working, 0 if not
    """
    schedule = np.zeros((5, 6), dtype=int)

    # YOUR CODE: Create a valid schedule
    # Strategy suggestion:
    # 1. First ensure each worker gets 3 days
    # 2. Then check each day has 2-3 workers

    return schedule

# Verify your schedule is valid!
```

**Task 2: Optimize for Preferences (20%)**
```python
# Given data:
worker_preferences = {
    0: [0, 1, 2],  # Worker 0 prefers Mon, Tue, Wed
    1: [2, 3, 4],  # Worker 1 prefers Wed, Thu, Fri
    2: [0, 2, 4],  # Worker 2 prefers Mon, Wed, Fri
    3: [1, 3],     # Worker 3 prefers Tue, Thu
    4: [0, 1],     # Worker 4 prefers Mon, Tue
    5: [3, 4]      # Worker 5 prefers Thu, Fri
}

def calculate_satisfaction_score(schedule, preferences):
    """Calculates how many preferred days each worker got"""
    # YOUR CODE HERE:

def improve_schedule_for_satisfaction(schedule, preferences, iterations=30):
    """
    Try to improve satisfaction by swapping assignments
    Keep changes only if they maintain validity and improve satisfaction
    """
    current_schedule = schedule.copy()

    for _ in range(iterations):
        # YOUR CODE:
        # 1. Pick two random workers
        # 2. Try swapping one of their days
        # 3. Check if new schedule is still valid
        # 4. Check if satisfaction improved
        # 5. Keep change if both conditions met
        pass

    return current_schedule

# Compare satisfaction before and after
```

**Task 3: Analysis and Recommendations (10%)**
- Calculate and compare:
  - Total satisfaction score (initial vs improved)
  - Distribution of workload across days
  - Fairness metric (how equal is satisfaction across workers?)
- Create visualizations for both schedules
- **Business Question:** What's the trade-off between operational needs and worker satisfaction? How would you handle a worker who can't work their preferred days? (3-4 sentences)

---

### What I'm Looking For

#### Excellent (90-100%)
- All functions work correctly
- Clear improvements achieved
- Insightful business analysis
- Clean, well-commented code
- Goes beyond requirements (e.g., tests multiple strategies)

#### Good (70-89%)
- Most functions work
- Some improvement achieved
- Reasonable business insights
- Code mostly clear
- Meets all basic requirements

#### Satisfactory (50-69%)
- Basic functions work
- Valid solutions produced
- Attempted business analysis
- Code runs without errors
- Most requirements attempted

---

### Tips for Success

**Start Simple**
- Get a working solution first, then optimize
- Print intermediate results to check your logic

**Use the Helpers**
- Don't reinvent the wheel
- Focus your effort on the algorithm logic

**Think Like a Consultant**
- Every optimization has a real business impact
- Consider implementation feasibility

**Common Pitfalls to Avoid**
- Don't forget to validate schedules after changes
- Don't optimize forever - "good enough" is often perfect
- Don't forget the business questions

---

### Submission Requirements

Submit a Jupyter notebook containing:
1. Your code implementations
2. Visualizations of results
3. Business analysis answers

**File naming:** `Assignment2_[GroupNames].ipynb`

---

### Support Resources

**Course Hours**
- Focus on understanding concepts
- Help with debugging
- Clarifying requirements

**What You Can Use**
- All course notebooks
- NumPy/Pandas documentation
- Basic Python tutorials
- Discussion with classmates
- Help from generative AI if understood

**What You Can't Do**
- Copy code from others
- Submit AI-generated code without understanding it

---

### Late Policy
- -10% per day late
- Maximum 3 days late
- Exceptions only for documented emergencies

---

### Final Thoughts

This assignment is about learning to apply optimization thinking to real problems.
We've simplified the implementation complexity so you can focus on:
- Understanding the problems
- Applying algorithmic thinking
- Interpreting results
- Making business recommendations

Remember: You're training to be business problem-solvers who can work with data and algorithms, not computer scientists. Focus on insights over implementation perfection! Good luck!
