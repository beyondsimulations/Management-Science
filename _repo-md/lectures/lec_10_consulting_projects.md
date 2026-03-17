---
title: Consulting Projects
subtitle: Lecture 10 - Management Science
author: Dr. Tobias Vlćek
format:
  revealjs:
    footer: ' {{< meta title >}} | {{< meta author >}} | [Home](lec_10_consulting_projects.qmd)'
    output-file: lec_10_presentation.html
---


# <span class="flow">Introduction</span>

## Your Final Challenge

<span class="highlight">Three major clients need your expertise:</span>

-   **QuickBite:** Food delivery routing crisis
-   **NurseNext:** Healthcare scheduling nightmare  
-   **TechMart:** Inventory allocation disaster
-   Each group picks **ONE client** to work with
-   This is **40% of your final grade**

. . .

> **Note**
>
> **You're not just students anymore - you're consultants.**

## Today's Learning Objectives

<span class="highlight">By the end of this session, you will:</span>

1.  Understand three realistic optimization problems
2.  Select a client project aligned with your team's strengths
3.  Begin data exploration and initial solution development
4.  Plan your approach using techniques from the course
5.  Prepare for professional consulting presentations

## The Expectation

<span class="highlight">What makes a successful consulting project?</span>

-   **Clear recommendations** backed by data
-   **Business impact** quantified in €€€
-   **Confidence** in your approach and results
-   **Actionable insights** clients can implement

. . .

> **Tip**
>
> "Reasonable and well-explained beats perfect and incomprehensible"

# Meet Your Clients

## **<span class="invert-font">Client Briefing: QuickBite</span>**

. . .

<span class="invert-font">CEO's Morning Crisis:</span>

<span class="invert-font fragment">"We're bleeding money on delivery costs while customers complain about <span class="highlight">cold food</span>! Our 4 drivers just 'wing it' every day. Result? <span class="highlight">75% late deliveries</span>, angry customers, and investors getting nervous."</span>

------------------------------------------------------------------------

## QuickBite: The Delivery Chaos

<span class="highlight">QuickBite's daily logistics nightmare:</span>

-   **120 meal deliveries** across Hamburg every day
-   **4 drivers** starting from one central depot
-   **Current approach:** Drivers choose routes by "intuition"
-   **The damage:** Monthly waste in fuel + penalties
-   **Customer complaints:** Up 40% this quarter

. . .

> **Important**
>
> **The Stakes:** Cut costs AND improve on-time delivery before investors pull funding!

------------------------------------------------------------------------

## QuickBite: Your Mission

<span class="highlight">What you need to solve:</span>

-   **Vehicle Routing Problem** with time windows
-   120 delivery locations across Hamburg
-   4 drivers with capacity constraints
-   Time windows for each delivery (violations = penalty)
-   **Trade-offs:** Distance vs. punctuality vs. driver workload balance

. . .

> **Important**
>
> Any questions?

## **<span class="invert-font">Client Briefing: NurseNext Hospital</span>**

. . .

<span class="invert-font">COO's Scheduling Crisis:</span>

<span class="invert-font fragment">"I spend <span class="highlight">8 hours every week</span> manually scheduling nurses, and they're still terrible! Massive monthly overtime, <span class="highlight">25% sick leave</span> from burnout, nurses quitting citing 'unfair scheduling.'"</span>

## NurseNext: The Burnout Problem

<span class="highlight">NurseNext's staffing crisis:</span>

-   **20 nurses** across 3 departments (ED, Med-Surg, ICU)
-   **Current system:** Manual scheduling by exhausted COO
-   **The damage:** Overtime, 25% sick leave rate
-   **Fairness issues:** Unequal weekend distribution
-   **Turnover:** Losing 3-4 experienced nurses annually

. . .

> **Important**
>
> **The Stakes:** Reduce overtime massively AND improve nurse satisfaction or face staffing collapse!

------------------------------------------------------------------------

## NurseNext: Your Mission

<span class="highlight">What you need to solve:</span>

-   **Employee Scheduling** with complex constraints
-   Multiple skill levels (Junior, Senior, Specialist) and departments
-   Shift patterns: Morning (7-15), Evening (15-23), Night (23-7)
-   **Labor law:** Max consecutive shifts, rest periods, weekly hours
-   **Fairness:** Weekend equity, workload balance, distribution
-   **Robustness:** What happens when nurses call in sick?

. . .

> **Important**
>
> Any questions?

------------------------------------------------------------------------

## **<span class="invert-font">Client Briefing: TechMart Electronics</span>**

. . .

<span class="invert-font">COO's Inventory Paradox:</span>

<span class="invert-font fragment">"We have <span class="highlight">€10M stuck in inventory</span>, yet we're constantly out of stock on bestsellers! <span class="highlight">20% stockout rate</span> on popular items while slow-movers occupy our fast warehouse. Black Friday is in 3 weeks!"</span>

------------------------------------------------------------------------

## TechMart: The Allocation Disaster

<span class="highlight">TechMart's warehouse crisis:</span>

-   **30 electronics SKUs:** Smartphones, laptops, ...
-   **Two warehouses:** Fast (Hamburg) and large (Poland)
-   **Current problem:** Wrong products in wrong warehouses
-   **Last Black Friday:** Ran out of top items in Hamburg on Day 1

. . .

> **Important**
>
> **The Stakes:** Optimize inventory allocation before Black Friday or repeat last year's disaster!

------------------------------------------------------------------------

## TechMart: Your Mission

<span class="highlight">What you need to solve:</span>

-   **Demand Forecasting** from 3 years of sales history
-   **Identify:** Patterns seasonality , trends, and Black Friday spike
-   **Inventory Optimization:** Which SKUs go in the fast warehouse?
-   **Monte Carlo Simulation:** Test allocation under uncertainty
-   **Trade-offs:** Shipping speed vs. warehouse capacity

. . .

> **Important**
>
> Any questions?

# <span class="flow">Project Details</span>

## Timeline

<span class="highlight">Your three-session consulting engagement:</span>

| Session        | Focus       | What Happens                              |
|----------------|-------------|-------------------------------------------|
| **Lecture 10** | Kickoff     | Choose client, explore data, start coding |
| **Lecture 11** | Development | Presentation training + intensive work    |
| **Lecture 12** | Final       | Presentations + Q&A                       |

. . .

> **Tip**
>
> You will likely need **6-10 hours** to complete this project. If you start today in class and also use Monday in two weeks, everything should be manageable.

## Grading (40% of Final Grade)

<span class="highlight">How your consulting project will be evaluated:</span>

### Solution (20%)

-   **Correctness** (8%)
-   **Technical Implementation** (7%)
-   **Analysis & Insights** (5%)

### Presentation (20%)

-   **Clarity** (8%)
-   **Visualization** (7%)
-   **Business Communication** (5%)

. . .

> **Important**
>
> Any questions here?

## Deliverables

<span class="highlight">All groups must submit by lecture 12:</span>

1.  **Jupyter notebook** with complete solution
    -   Results and visualizations embedded
2.  **Presentation slides** (8 minutes maximum)
    -   Problem understanding & Solution approach
    -   Results, Visualization and validation
    -   Business impact

## Bonus Points Opportunity

<span class="highlight">Student Voting (After Presentations)</span>

After all presentations, you'll vote for:

-   **Best Solution** for each client (3 winners)
-   **Winners receive 5 bonus points** per group member

. . .

> **Tip**
>
> Last chance on bonus points!

# <span class="flow">Tips for Success</span>

## Strategic Advice

<span class="highlight">How to approach your project:</span>

1.  **Choose your client wisely**
    -   Pick based on your team's strengths
2.  **Start with data exploration**
    -   Understand the data BEFORE coding
3.  **Build incrementally**
    -   Simple solution first (greedy)
    -   Then improve (local search, metaheuristics)

## Common Pitfalls to Avoid

<span class="highlight">Watch out for these:</span>

-   **Scope creep:** Trying to solve everything perfectly
-   **Poor time management:** Coding until the last minute
-   **Ignoring business context:** Technical solution without impact
-   **Bad visualizations:** Unreadable charts or no visuals

. . .

> **Important**
>
> Don't build a solution that you can't explain to the client!

# <span class="flow">Let's Get Started!</span>

## Next Steps

<span class="highlight">Your roadmap for today's session:</span>

1.  **Hour 1-2:** Choose your client
2.  **Hour 3-4:**
    -   Open the project notebook
    -   Explore the data
    -   Start coding initial solution
    -   Ask clarifying questions

. . .

> **Tip**
>
> We only see each other again in 2 weeks, use the time!

## Final Thoughts

<span class="highlight">You have all the tools you need:</span>

-   Monte Carlo simulation
-   Forecasting techniques
-   Greedy heuristics
-   Local search optimization
-   Multi-objective trade-offs
-   Metaheuristics concepts

. . .

> **Important**
>
> **You have ALL the tools you need to succeed.**

## Break!

<span class="highlight">Take 20 minutes, then we start choosing</span>

**Next up:** You'll choose a project and group and start working on it.
