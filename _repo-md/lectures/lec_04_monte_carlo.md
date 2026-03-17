---
title: Dealing with Uncertainty
subtitle: Lecture 4 - Management Science
author: Dr. Tobias Vlćek
format:
  revealjs:
    footer: ' {{< meta title >}} | {{< meta author >}} | [Home](lec_04_monte_carlo.qmd)'
    output-file: lec_04_presentation.html
---


# <span class="flow">Introduction</span>

## **<span class="invert-font">Client Briefing: TechVenture Innovation Fund</span>**

. . .

<span class="invert-font">CEO's Dilemma:</span>

<span class="invert-font fragment">"We have €2M to invest in <span class="highlight">2 of 4 startups</span>. Each promises great returns, but the future is uncertain. How do we make the best choice without just gambling?"</span>

## Business: Valuing Uncertainty

<span class="question">Question</span>: <span class="highlight">Why can't we just pick the two startups with the highest average returns?</span>

. . .

-   **Hidden Risk:** A startup with 30% average return but 50% chance of failure might be worse than 20% return with 5% failure chance
-   **Portfolio Effects:** Two risky startups together might amplify risk beyond acceptable levels
-   **Tail Events:** The worst-case scenario can matter as much as the average case

. . .

> **Warning**
>
> **Common Pitfall:** Optimizing on averages ignores the distribution of outcomes.

## Real-World Examples

<span class="highlight">Where uncertainty modeling is critical:</span>

**Netflix Series Decisions**

-   Will a show hit 10M viewers?
-   Range: 500K to 50M
-   Investment: €20M per season

**Pharmaceutical R&D**

-   Will the drug pass trials?
-   Success rate: 10-20%
-   Investment: €1B over 10 years

. . .

> **Important**
>
> When decisions are expensive and outcomes are uncertain, **Monte Carlo simulation** can be helpful to **reduce risk** and **maximize value**!

# <span class="flow">Core Concepts</span>

## Rolling the Dice 10,000 Times I

<span class="question">Question</span>: If you roll two dice, what's the probability of getting exactly 7 as result?

. . .

**Method 1: Math**

-   Count combinations: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
-   Total combinations: 36
-   Probability: 6/36 = 16.67%

## Rolling the Dice 10,000 Times II

<span class="question">Question</span>: If you roll two dice, what's the probability of getting exactly 7 as result?

. . .

**Method 2: Simulation**

``` python
import numpy as np
np.random.seed(42)

# Roll two dice 10,000 times
dice1 = np.random.randint(1, 7, size=10_000)
dice2 = np.random.randint(1, 7, size=10_000)
total = dice1 + dice2

# What fraction equals 7?
probability = (total == 7).mean()
print(f"Simulated probability of rolling 7: {probability:.1%}")
```

    Simulated probability of rolling 7: 16.2%

## How Probability Converges

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-3-output-1.png" width="1330" height="464" />

. . .

> **Tip**
>
> As we roll more dice, the estimated probability converges to the true value (16.7%)

## The Law of Large Numbers

<span class="highlight">Fundamental Principle:</span> **As sample size increases, sample average converges to the true expected value**

. . .

If $X_1, X_2, \ldots, X_n$ are independent random samples from the same distribution with mean $\mu$:

$$\text{As } n \to \infty, \quad \bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \to \mu$$

. . .

> **Note**
>
> This is WHY simulations works. More simulations = better estimates!

## The Central Limit Theorem

<span class="highlight">Another Fundamental Principle:</span> **The sum of many random variables tends toward a normal distribution**

. . .

**What it means:**

-   Even if individual returns are <span class="highlight">NOT</span> normally distributed...
-   The portfolio of many assets <span class="highlight">WILL</span> be approximately normal
-   The average of many simulations <span class="highlight">WILL</span> be approximately normal

. . .

> **Tip**
>
> **For Business:** This is why we can use normal distributions to model portfolio returns, even when individual assets have skewed or unusual distributions!

## Why This Matters for Business

<span class="question">Question</span>: How many simulations do we need for reliable results?

. . .

``` python
# Test convergence with different sample sizes
sample_sizes = [10, 100, 1000, 10000, 100000]
estimates = []

for n in sample_sizes:
    dice1 = np.random.randint(1, 7, size=n)
    dice2 = np.random.randint(1, 7, size=n)
    total = dice1 + dice2
    prob = (total == 7).mean()
    estimates.append(prob)
    print(f"n={n:6d}: Estimated probability = {prob:.4f}")
```

    n=    10: Estimated probability = 0.2000
    n=   100: Estimated probability = 0.1900
    n=  1000: Estimated probability = 0.1480
    n= 10000: Estimated probability = 0.1652
    n=100000: Estimated probability = 0.1670

## Practical Guidelines

<span class="highlight">How many simulations should you run?</span>

-   **Quick exploration:** 10,000 simulations
    -   Good for initial insights, prototyping
-   **Critical decisions:** 100,000+ simulations
    -   Financial risk models, regulatory compliance
-   **When to stop:** When more simulations <span class="highlight">don't change</span> conclusion

. . .

> **Important**
>
> If your decision changes with 10x more simulations, you didn't run enough!

# <span class="flow">Monte Carlo Method</span>

## The Monte Carlo Method

<span class="highlight">Three Simple Steps:</span>

1.  **Model the Uncertainty:**
    -   Define probability distributions for unknown variables
2.  **Simulate Many Scenarios:**
    -   Generate thousands of possible outcomes
3.  **Analyze the Results:**
    -   Calculate statistics from the simulation

. . .

> **Note**
>
> Monte Carlo Casino in Monaco inspired the method's development in the 1940s.

## Step 1: Model the Uncertainty

<span class="highlight">Key Function:</span> `np.random.normal(loc, scale, size)`

-   **loc**: The center (mean/average)
-   **scale**: The spread (standard deviation)
-   **size**: How many samples to generate

. . .

``` python
# AI-Growth: average 38% return, ±25% volatility
returns = np.random.normal(loc=0.38, scale=0.25, size=10_000)
print(f"Mean return: {returns.mean():.1%}")
print(f"Std deviation: {returns.std():.1%}")
print(f"Minimum: {returns.min():.1%}")
print(f"Maximum: {returns.max():.1%}")
```

    Mean return: 38.8%
    Std deviation: 24.8%
    Minimum: -67.0%
    Maximum: 125.7%

## Expected Returns

Let's calculate percentiles with `np.percentile()`.

. . .

<span class="question">Question:</span> Do you still know what a percentile is?

. . .

``` python
print(f"\nPercentiles:")
print(f"  5th: {np.percentile(returns, 5):.1%} (worst 5% of scenarios)")
print(f" 25th: {np.percentile(returns, 25):.1%} (worst 25% of scenarios)")
print(f" 50th: {np.percentile(returns, 50):.1%} (median)")
print(f" 75th: {np.percentile(returns, 75):.1%} (best 25% of scenarios)")
print(f" 95th: {np.percentile(returns, 95):.1%} (best 5% of scenarios)")
```


    Percentiles:
      5th: -2.7% (worst 5% of scenarios)
     25th: 22.1% (worst 25% of scenarios)
     50th: 38.9% (median)
     75th: 55.7% (best 25% of scenarios)
     95th: 78.6% (best 5% of scenarios)

## Understanding the Distribution

<span class="question">Question</span>: Before we plot, what shape do you expect for `np.random.normal()`?

. . .

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-7-output-1.png" width="821" height="433" />

## Risk Analysis

<span class="question">Question</span>: What's the probability that AI-Growth loses money?

. . .

``` python
# Calculate risk metrics
prob_loss = (returns < 0).mean() # proportion of returns that are less than zero
prob_double = (returns > 1.0).mean()  # proportion greater than 100%

print(f"Probability of loss: {prob_loss:.1%}")
print(f"Probability of doubling money: {prob_double:.1%}")
```

    Probability of loss: 6.0%
    Probability of doubling money: 0.8%

. . .

> **Important**
>
> With 6 % chance of loss, AI-Growth is relatively safe. Easy for one startup, right?

## Different Distributions

<span class="highlight">Attention: Not everything follows a normal distribution!</span>

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-9-output-1.png" width="783" height="465" />

## Overview

## Normal

``` python
# Most common in nature/business
# Bell-shaped, symmetric
returns = np.random.normal(mean, std, size)

# Example: CloudAI startup returns
cloudai = np.random.normal(0.25, 0.15, 10000)  # 25% ± 15%
```

**Main Characteristics:**

-   Symmetric bell curve
-   Most values cluster around mean
-   Common in nature and business

## Uniform

``` python
# Equal probability across range
# Example: FinFlow returns between 10-35%
returns = np.random.uniform(0.10, 0.35, size)

# Example: FinFlow startup returns
finflow = np.random.uniform(0.10, 0.35, 10000)  # 10-35% equally likely
```

**Main Characteristics:**

-   All values equally likely
-   Hard boundaries (min/max)
-   Good for modeling complete uncertainty within range

## Exponential

``` python
# Time between events
# Example: Customer arrivals, equipment failure
times = np.random.exponential(scale, size)

# Example: Time between customer arrivals (minutes)
arrivals = np.random.exponential(5, 10000)  # Average 5 minutes
```

**Main Characteristics:**

-   Many small values, few large ones
-   Always positive
-   Common for waiting times and rare events

# <span class="flow">Portfolios</span>

## Combining Investments

**Suppose we have the following startups:**

<span class="highlight">CloudAI, GreenGrid, HealthTrack, FinFlow</span>

. . .

<span class="question">Question</span>: If we must pick 2 of 4, how many unique pairs exist?

. . .

**The Math:**

$$\binom{4}{2} = \frac{4!}{2! \times 2!} = \frac{4 \times 3 \times 2 \times 1}{(2 \times 1) \times (2 \times 1)} = \frac{24}{4} = 6$$

. . .

> **Tip**
>
> Each combination has different risk-return characteristics!

## Four Startup Profiles

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-14-output-1.png" width="754" height="466" />

. . .

<span class="question">Question</span>: Which startup is the best choice?

## Key Metrics for Decision Making

<span class="question">Question</span>: Which metrics matter most for investment decisions?

-   **Expected Return:** Average outcome across all scenarios
-   **Volatility (Risk):** Standard deviation of returns
-   **Probability of Loss:** How often do we lose money?
-   **Upside Potential:** Chance of exceptional returns (\>50%)
-   **Tail Risk:** What happens in the worst 10% of cases?

. . .

> **Important**
>
> No metric tells the whole story. Investors consider multiple dimensions of risk and return.

## Understanding Tail Risk

<span class="highlight">Tail Risk:</span> The danger lurking in worst-case scenarios

**Expected Shortfall (ES)**

-   Average loss in worst X% of cases
-   Goes beyond simple probability
-   Measures depth of potential losses
-   Critical for risk management

. . .

> **Warning**
>
> A portfolio with higher average returns might have catastrophic tail risk. Always look at the extremes!

# <span class="flow">Correlation & Dependence</span>

## The Independence Assumption

<span class="highlight">So far, we've assumed startups succeed or fail independently.</span>

. . .

**Independent Events:**

-   CloudAI's success doesn't affect GreenGrid's success
-   Each startup faces separate, unrelated risks
-   Portfolio risk = Average of individual risks

. . .

<span class="question">Question</span>: Is this realistic in the real world?

. . .

> **Warning**
>
> **Reality Check:** Many business risks are correlated! Economic downturns, market trends, and technology shifts affect multiple companies simultaneously.

## What is Correlation?

<span class="highlight">Correlation measures how two variables move together.</span>

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} \quad \text{where } -1 \leq \rho \leq 1$$

. . .

**Interpreting Correlation:**

-   **ρ = +1:** Perfect positive correlation (move together)
-   **ρ = 0:** No correlation (independent)
-   **ρ = -1:** Perfect negative correlation (move opposite)

## Correlation in Practice

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-16-output-1.png" width="761" height="466" />

. . .

> **Tip**
>
> In Python: `np.corrcoef(returns1, returns2)` calculates correlation

## Why Correlation Matters

<span class="highlight">Two AI startups in your portfolio:</span>

**Scenario 1: Independent (ρ = 0)**

-   One fails due to technical issues, other succeeds
-   Risk is averaged out

**Scenario 2: Positively Correlated (ρ = 0.8)**

-   Both rely on same AI infrastructure provider - risk is amplified!

. . .

> **Warning**
>
> Diversification only reduces risk when investments are not highly correlated!

## Impact on Portfolio Risk

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-17-output-1.png" width="948" height="467" />

. . .

> **Important**
>
> Higher correlation = Wider distribution = More risk!

## Real-World Correlation Examples

<span class="highlight">Common sources of correlation in business:</span>

-   **Industry-specific:** All tech startups affected by downturn
-   **Geographic:** All European companies affected by EU regulations
-   **Supply chain:** Multiple companies relying on same supplier
-   **Macroeconomic:** Interest rates, inflation affect most businesses

. . .

> **Tip**
>
> **Diversification:** Choose investments with LOW correlation to reduce portfolio risk!

## When Diversification Fails

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-18-output-1.png" width="948" height="467" />

. . .

> **Warning**
>
> **2008 Financial Crisis:** Many "diversified" portfolios collapsed due to correlations!

# <span class="flow">When Monte Carlo?</span>

## When to Use Monte Carlo

<span class="question">Question</span>: For our simple startup examples so far, do we really NEED Monte Carlo?

. . .

**Short answer: No!** For basic mean/variance calculations, we can use analytical formulas.

. . .

<span class="highlight">So when is Monte Carlo truly necessary?</span>

## Necessary vs. Convenient

<span class="highlight">You can use math (analytical solutions):</span>

-   **Simple distributions:** Mean and variance of normal distributions
-   **Linear combinations:** Portfolio of independent assets

. . .

<span class="highlight">You NEED Monte Carlo when:</span>

-   **Complex dependencies:** Nonlinear relationships
-   **Path-dependent problems:** Outcome depends on a sequence
-   **No closed-form solution:** The math is intractable

## Real Monte Carlo Applications

<span class="highlight">Where Monte Carlo is ESSENTIAL, not just convenient:</span>

**1. Option Pricing with Path Dependencies**

``` python
# Payoff depends on AVERAGE price over time
n_simulations = 10000; strike_price = 105; payoffs = []
for sim in range(n_simulations):
    prices = [100]  # Starting price
    for day in range(365):
        prices.append(prices[-1] * (1 + np.random.normal(0.001, 0.02)))
    payoff = max(0, np.mean(prices) - strike_price)
    payoffs.append(payoff)
payoffs = np.array(payoffs)
print(f"Average option value: ${payoffs.mean():.2f}")
print(f"Probability of profit: {(payoffs > 0).mean():.1%}")
```

    Average option value: $19.58
    Probability of profit: 68.9%

## Real Monte Carlo Applications II

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-20-output-1.png" width="756" height="467" />

## Real Monte Carlo Applications III

**2. Supply Chain with Cascading Effects**

``` python
# Each stage affects the next (nonlinear dependencies)
n_simulations = 10000; factory_capacity = 150; demand = 120; price = 5
penalty = 10; revenues = []

for sim in range(n_simulations):
    parts_delivered = np.random.poisson(100)
    production = min(parts_delivered, factory_capacity)
    if production >= demand:
        revenue = demand * price
    else:
        revenue = production * price - penalty
    revenues.append(revenue)

revenues = np.array(revenues)
print(f"Average revenue: ${revenues.mean():.2f}")
print(f"Worst-case revenue: ${revenues.min():.2f}")
```

    Average revenue: $489.22
    Worst-case revenue: $325.00

## Real Monte Carlo Applications IV

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-22-output-1.png" width="756" height="467" />

## Real Monte Carlo Applications V

**3. Project Management with Sequential Risks**

``` python
# Project phases must happen in order, later phases only if earlier succeed
n_simulations = 10000; shape = 2; scale = 10; project_times = []

for sim in range(n_simulations):
    total_time = 0
    for phase in ['design', 'build', 'test', 'deploy']:
        # Each phase has uncertain duration
        phase_time = np.random.gamma(shape, scale)
        total_time += phase_time
        if np.random.random() < 0.1:
            total_time += phase_time * 0.5  # Rework time
    project_times.append(total_time)

project_times = np.array(project_times)
print(f"Average project duration: {project_times.mean():.1f} days")
print(f"90th percentile: {np.percentile(project_times, 90):.1f} days")
```

    Average project duration: 84.3 days
    90th percentile: 125.2 days

## Real Monte Carlo Applications VI

<img src="lec_04_monte_carlo_files/figure-markdown_strict/cell-24-output-1.png" width="756" height="467" />

## Example: Why Still Useful?

<span class="question">Question</span>: If we can calculate variance analytically, why simulate?

. . .

-   **Visualization:** Seeing the full distribution is intuitive
-   **Flexibility:** When problems become complex, simulation adapts
-   **Extensions:** Practice for complex problem

. . .

> **Tip**
>
> Think of our examples as learning the tool on simple problems so you can solve complex ones where Monte Carlo is required!

## When NOT to Use Monte Carlo

<span class="highlight">Even when you CAN use Monte Carlo, sometimes you shouldn't:</span>

. . .

-   **Simple analytical solution exists and suffices**
    -   Use math directly: faster, more precise, easier to understand
-   **Can't reasonably estimate input distributions**
    -   Garbage in = garbage out; need solid basis for assumptions
-   **Problem is deterministic (no uncertainty)**
    -   Simulation adds complexity without value

. . .

> **Warning**
>
> Simulation is a tool for managing uncertainty, not creating false precision!

# <span class="flow">Making Smart Decisions</span>

## Decision Framework

1.  <span class="highlight">Define Your Risk Tolerance</span>
    -   Can you afford to lose money and what's your time horizon?
    -   Are you risk-averse or risk-seeking?
2.  <span class="highlight">Evaluate Multiple Metrics</span>
    -   Don't just maximize returns, consider volatility and risk
    -   Look at probability of achieving goals
3.  <span class="highlight">Scenario Test</span>
    -   What if distributions change or a company fails?

## The Plan for the Day

**Hour 1:**

**Lecture**

-   Concepts
-   Examples
-   Visualization

**Hour 2:**

**Practice Notebook**

-   Simulation
-   Hands-on coding
-   Build your skills

**Hours 3-4:**

**Competition**

-   TechVenture
-   Team collaboration
-   €2M investment

. . .

<span class="highlight">Remember:</span> The lecture gives you concepts. The notebook gives you practice. The competition tests your skills!

## Hour 2: Simulation

**Your Practice Case: Bean Counter Expansion**

-   Model uncertain variables (customers, spending)
-   Combine multiple uncertainties
-   Calculate business metrics (VaR, profit probability)
-   Make data-driven recommendations

## Hours 3-4: The Challenge

<span class="highlight">TechVenture Investment Competition</span>

-   **Your Budget:** €2 million
-   **Your Choice:** Pick 2 of 4 startups
-   **Your Goal:** Maximize risk-adjusted returns
-   **Your Deliverable:** One-slide recommendation + 3-minute pitch

. . .

Consider multiple risk metrics and prepare a clear justification!

. . .

<span class="highlight">Prizes:</span> **10 / 6 / 3 bonus points** for top three teams!

# <span class="flow">Key Takeaways</span>

## What You've Learned Today

**Concepts**

-   Monte Carlo simulation
-   Probability distributions
-   Risk has multiple dimensions
-   Expected Value vs. Variance
-   Correlation and dependence

**Skills**

-   Using `np.random` for simulation
-   Calculating risk metrics
-   Visualizing uncertainty
-   Comparing portfolios
-   Understanding correlation

. . .

> **Warning**
>
> Monte Carlo doesn't predict <span class="highlight">THE</span> future - it shows possible futures! And correlation can amplify or reduce risk!

## Next Week

<span class="highlight">Forecasting the Future</span>

-   Moving from simulation to prediction
-   Time series analysis
-   Trend and seasonality detection
-   Measuring forecast accuracy

. . .

<span class="highlight">Now, short break and then we start coding!</span>
