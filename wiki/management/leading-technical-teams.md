---
type: playbook
title: "Leading Technical Teams in the AI Era"
tags: [technical-leadership, ai-management, agentic-ai, model-governance, vendor-risk, cyber-risk, technical-teams]
created: 2026-05-17
updated: 2026-05-17
sources: [hbr-year-in-tech-2026, hbr-decision-making, hbr-stop-holding-yourself-back-2025]
related: [management/managing-senior-people, management/cross-functional-teaming, principles/decision-making, organization/adaptive-organization, organization/operating-rhythm, principles/curiosity]
---

# Leading Technical Teams in the AI Era

## Use Case

You lead engineers, data scientists, ML practitioners, security professionals, or a mixed technical organization. You are confronting one or more of:

- Deploying agentic AI alongside human teams and unsure how to design the partition.
- Building or operating AI/ML systems whose decisions affect customers, employees, or regulators — and unsure how to govern model development.
- Discovering that a vendor or platform on which you depend has become a single point of failure (CrowdStrike-style).
- Managing senior technical individual contributors whose skills now overlap with or are augmented by AI.
- Trying to time strategic investment in slow-developing technology — autonomous systems, biotech, quantum, advanced materials — when the underlying capabilities mature at different rates.
- Setting the team posture on the future-of-work questions your engineers are reading about and worrying about.

This playbook focuses on the *leadership* moves, not the technical decisions. The technical literature is plentiful; the management literature is thinner.

## Diagnosis

You are in a "leading technical teams in the AI era" situation when:

- A capable engineer asks *"why am I doing this work? An agent can do it faster."* and you do not have a good answer.
- Your AI deployment plan is more detailed than your governance plan. (If you cannot answer *"how would we know if this model went off?"*, your governance is behind your capability.)
- You have not mapped which vendors and platforms your team's work hard-depends on.
- A new agentic-AI capability has arrived and someone is already deploying it — and you do not have a partition rule for human-vs-agent decisions.
- Your senior technical ICs are starting to spend more time prompting agents than writing code, and you have not updated your operating model accordingly.
- You are being asked for a "five-year AI strategy" and you sense any specific bet you make is likely to be wrong.

## First Principles

**1. Innovation is collective, even when it looks heroic (Anthony).**
Even disruptive technology stories with a clear protagonist involve a wide cast: backers, partners, infrastructure-builders, supply-chain enablers. The leadership posture: protect and design for the cast, not the lone genius. Apply this to AI deployments too — the most successful ones involve product, ops, legal, security, and end-users working together, not a small "AI team" working alone.

**2. The hardest part of AI deployment is organizational, not technical (Zoldi & Levine).**
*"Getting this system up and running wasn't a technology problem, first and foremost. It was an organization and people problem."* The standards, governance, user-experience, and adoption work outweigh the modeling work by a large margin. Leaders who treat AI as a technology problem leave the organizational work undone — and pay for it later in trust failures, regulatory pushback, and silent non-adoption.

**3. Agentic AI changes management problems; it does not remove them (Purdy).**
Goal-setting, team selection, and decision-space scaffolding remain firmly human work. Agentic AI is *more* sensitive to goal-setting quality than human teams, because the agent lacks tacit context. SMART goals matter more, not less.

**4. AI trust depends on architecture, not on the AI itself.**
Three properties make an AI system trustworthy: interpretability (the system can be understood), auditability (decisions can be reviewed), enforceability (rules cannot be bypassed). Without all three, trust is performative.

**5. Cyber and vendor risk are interdependence risks (Yahalom).**
The CrowdStrike outage was not caused by a hostile actor — it was caused by a routine content update from a trusted vendor. A single point of failure in your dependency graph creates a single point of failure in your operations. Leaders must map the graph and run tabletop exercises on the most concentrated dependencies.

**6. Patient perseverance beats premature commitment to a specific tech bet.**
ChatGPT was year 66 for AI. Autonomous vehicles trace to 1925. Treat hot new technologies as the *tail end* of a long curve, and time your bets accordingly. The Technology Feasibility Matrix (Marion/Deeds/Friar) is the structured way to do this.

**7. The future of work depends on who you ask.**
Tech entrepreneurs predict imminent post-scarcity; economists predict gradual productivity gains; journalists predict imminent dystopia. *Each group believes their predictions are obvious and the others' are preposterous.* The leader's job is to hold all three views and *make* the future the team will actually inhabit, not to passively forecast it.

## Step-by-Step Approach

### Step 1: Map the human-AI partition for your team's work, function by function.

For each major function your team performs (e.g., code review, customer support, model evaluation, incident response, design, documentation):

- **What does an agent decide alone?** (Low-stakes, reversible, well-bounded — for example, formatting, routine queries, scheduled monitoring.)
- **What does an agent recommend for human approval?** (Higher-stakes, common patterns — code suggestions, customer-response drafts, alert triage.)
- **What does an agent never touch?** (High-stakes, irreversible, ethically charged — production deployments, personnel decisions, security exceptions.)

Write the partition down. Publish it. Revisit quarterly. *If you do not write it, the partition is being decided by whoever moves first.*

### Step 2: Set SMART goals for AI deployments with explicit contextual *why*.

Use the same discipline you would for a new human team member, with one addition: explain *why* these goals matter to the business in the prompt or system context. Agents lack the tacit understanding that human team members absorb over years. Include:

- Specific outcome metrics (not just throughput).
- The customer or end-user the work serves.
- The constraint set (what the agent should *not* optimize at the expense of).
- The feedback loop — how performance will be evaluated and how the agent will be adjusted.

### Step 3: Build a model-development governance system before you scale.

Adapt the FICO blockchain-ATD approach to your scale. The components:

- **Standards first, tech second.** Decide which algorithms, fairness tests, and approval gates are required *before* building the infrastructure to enforce them.
- **An immutable record per model.** Variables used, design decisions, training and test data, latent features, fairness/ethics tests, sign-offs, post-deployment incidents. At small scale, this is a structured wiki page or git-tracked artifact; at larger scale, the FICO blockchain approach.
- **User-friendly UX is non-negotiable.** If using the governance system creates friction, mavericks will route around it.
- **Iterate on quick wins.** Pick the highest-risk model class first; build the governance for that; then extend.
- **Persistent storage.** Models evolve over years. The artifact trail must survive personnel changes and tech stack migrations.
- **Maintenance discipline.** This is software; it needs security updates, vulnerability management, and upgrades over its lifetime.

### Step 4: Map your vendor and platform dependency surface.

For each vendor, model provider, and platform on which the team hard-depends, document:

- **Concentration risk** — how much of our work fails if this vendor fails?
- **SLA and resilience options** — what is the contractual commitment, and what is our fallback?
- **Update policy** — do we apply vendor updates immediately, after delay, with phased rollout? (CrowdStrike: the answer matters.)
- **Accountability path** — if this vendor's failure causes our outage, who absorbs the loss? Is that path tested?

Run a tabletop exercise quarterly on the most concentrated dependency. Treat it as a real incident: who would notice, what would we do, how long would recovery take?

### Step 5: Re-architect senior technical IC work for AI-augmentation.

Senior ICs whose former job was high-volume code production are increasingly performing higher-leverage work: architecture, code review, prompt engineering, agent supervision, governance, mentorship. Manage the transition explicitly:

- Name the change. *"Your job is shifting from producing X to supervising Y producing X."*
- Update success metrics. Throughput-of-output gives way to quality-of-supervision, agent-team performance, and judgment-on-edge-cases.
- Provide new skill development. The supervision of AI agents is a new skill; treat it as such.
- Watch for the atrophy problem. Skills that move to agents will atrophy in humans. Decide which to preserve via deliberate practice and which to let go.
- Address the identity question directly. Many senior engineers find their craft identity threatened by AI. Acknowledge it; do not paper it over with productivity narratives.

### Step 6: For strategic technology bets, use the Technology Feasibility Matrix.

For each emerging technology relevant to your industry, plot it on two axes: technical feasibility (low / high) × cost (high / low):

- **Mass market** (high feasibility, low cost) — ready for full deployment.
- **Mission critical** (high feasibility, high cost) — feasible but investment-intensive; partner or pilot.
- **Magic bullet** (low feasibility, low cost) — research-stage but cheap to track.
- **Moon shot** (low feasibility, high cost) — far horizon; monitor through external signals.

For multi-technology innovations (autonomous vehicles, advanced manufacturing, biotech), each underlying technology may be in a different quadrant. The *convergence window* — when costs of all needed technologies fall together — is the strategic moment.

Strategies for the window:
- **Proactive** — early signal, shape the trajectory of developing technologies.
- **Reactive** — late signal, partner with established competitors or startups.
- **Intermediate-product** — Netflix's DVD business while broadband matured.
- **High-cost-entry** — luxury or niche markets that absorb early pricing.

### Step 7: Hold all three future-of-work scenarios.

Tech-optimist (AI brings post-scarcity), economist-skeptic (gradual productivity gains, new jobs replace old), journalist-pessimist (labor disruption, inequality, surveillance). In strategic planning:

- Run scenarios under each.
- Identify the moves that are robust across all three. (Investing in employee data literacy, for instance, looks good in all three scenarios.)
- Watch which scenario your *team* is implicitly assuming — usually the one matching their training.
- Name the assumption. Discuss it.

### Step 8: Decide your organization's data-governance posture before it becomes political.

The data-cooperatives question (Parra-Moyano & Joshi) is coming. Employees' data — performance metrics, communications, code, sensor data — is being used to train models that may eventually replace them. Decide *now*:

- Are employees informed when their data is used for training?
- Is there meaningful consent?
- Is there a collective-input mechanism (data literacy program, employee council, contractual clause)?
- What is your fairness posture on the productivity gains from employee-data-trained AI?

Leaders who answer these *before* the question becomes politically forced will navigate the transition with more credibility.

## Suggested Language

- **Naming the AI partition:** *"For this function, the agent decides A and B. It recommends C, which a human approves. It never touches D. Let me explain why."*
- **Setting agentic AI goals:** *"The success metric for this agent is X. The customer or end-user it serves is Y. The constraint is Z — we will not optimize for X at the expense of Z. We will evaluate weekly and adjust."*
- **Communicating the role-shift to a senior IC:** *"The job is changing. The work that used to be your craft is moving to agents. The work that's left — and the work I need you on — is judgment, architecture, supervision, and edge cases. Let's talk about what that looks like, what new skills you need, and what success looks like in the new shape."*
- **Naming a governance gap:** *"We have a deployment plan and we do not have a governance plan. Until we have both, this is not ready to ship."*
- **Naming a vendor risk:** *"We have a single point of failure here. We have not run a scenario where this vendor fails. I want that scenario run before we add another dependency on them."*
- **Holding scenario diversity:** *"I notice we are planning as if scenario A is the only plausible future. Let's spend half an hour on each of B and C, and identify the moves that work across all three."*
- **Addressing the identity question:** *"You're not wrong that the work is changing. The craft you built matters and isn't disappearing — but it is shifting. I want to be honest about that. Let's talk about what the next chapter looks like for you."*

## What To Avoid

- **AI deployment without governance.** Building model-deployment pipelines before model-governance ones is the canonical mistake. Reverse the order.
- **Treating agentic AI as software to install.** It is more like onboarding a new team member: it needs goals, context, supervision, and feedback.
- **Letting the partition decide itself.** Whoever pushes hardest in the moment will get more authority for agents than they should have.
- **Single-vendor concentration without acknowledgment.** Every dependency that is not mapped is a risk you cannot manage.
- **Throughput metrics for senior ICs in AI-augmented work.** Throughput will be high regardless; what matters is the *quality* of supervision and the *judgment* on edge cases. Measure those.
- **Picking one future-of-work scenario.** Even when your team strongly believes one, the planning posture is to hold all three.
- **Premature commitment to a specific technology bet.** The technology will likely change shape before it matures. Bet on categories and pilots; defer specific commitments.
- **Treating senior ICs' identity concerns as resistance.** They are real. The concern often points at the *actual* gap in your transition plan.

## Escalation Path

If the team is struggling with the AI transition:

1. **Re-run the partition.** Likely it is too permissive (agents doing things humans should) or too restrictive (humans doing things agents could).
2. **Audit the governance.** A model is in production whose behavior you cannot explain or recall the design decisions for. Stop deployments until the gap is closed.
3. **Engage HR / Legal / Ethics.** Once the data-governance or labor-relations question is forced by an incident, the cost is high. Get ahead of it.
4. **External review.** When the internal team is too close, an external technical and governance audit is worth its cost. Use it before, not after, an incident.

## Follow-Up Actions

- Quarterly: review the partition. Is it being honored? Has the right boundary moved?
- Quarterly: tabletop the highest-risk vendor failure scenario.
- Annually: audit the model-governance system. Are the artifacts being kept current? Are the standards being met?
- Annually: re-run the future-of-work scenario discussion with the team. What has changed in the last year?
- Per-deployment: post-mortem on what the partition got right and wrong. Adjust the standards.

## Related Frameworks

- [[management/managing-senior-people]] — senior technical ICs in an AI-augmented environment
- [[management/cross-functional-teaming]] — Edmondson's four-function model applies cleanly to mixed human-agent teams
- [[principles/decision-making]] — the human-AI partition is a decision-space scaffolding problem
- [[organization/adaptive-organization]] — agentic AI as a new layer of the adaptive organization
- [[organization/operating-rhythm]] — cadence-matching to learning rhythm in AI deployments
- [[principles/curiosity]] — the disposition behind questioning what to delegate to agents
- [[coaching/career-development]] — for senior ICs whose career trajectory is being reshaped by AI

## Sources

- **[[sources/hbr-year-in-tech-2026]]** — Primary source. Anthony's four patterns of disruption, Purdy on agentic AI imperatives, Zoldi & Levine on FICO blockchain-ATD governance, Yahalom on CrowdStrike and explainable cyber risk, Parra-Moyano & Joshi on data cooperatives, Marion/Deeds/Friar on the Technology Feasibility Matrix and convergence windows, Dries/Luyckx/Rogiers on future-of-work scenarios.

- **[[sources/hbr-decision-making]]** — Reeves/Moldoveanu/Job on the eight non-data dimensions of decision-making; the principle that AI changes the *substrate* of decision-making, not its principles. Charan's culture-of-indecision frame applies cleanly to AI governance.

- **[[sources/hbr-stop-holding-yourself-back-2025]]** — Wilkins on self-limiting beliefs; the senior IC who fears AI atrophy is often dealing with a hidden-blocker pattern that limits exploration of the new role.
