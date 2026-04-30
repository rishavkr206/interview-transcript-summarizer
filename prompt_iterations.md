# Prompt Iterations & Evolution

## Overview
This document shows the three iterations of the prompt used to analyze interview transcripts. The goal was to create a prompt that generalizes across different interview types (technical vs. business/operations) without overfitting to one transcript style. Both sample transcripts were tested — Transcript 1 is a technical mobile/full-stack developer interview; Transcript 2 is a business operations/program management interview.

---

## ITERATION 1: BASELINE (Simple & Direct)

### Prompt Used:
```
Analyze this interview transcript and provide:

1. TOPICS COVERED: List main themes discussed (e.g., technical skills, problem-solving, leadership)
2. PROFILE: What role/profile fits this candidate? (e.g., "Backend Engineer - Senior", "Product Manager - Mid-level")
3. CANDIDATE SUMMARY: 3-6 sentences covering background, strengths, concerns, and overall impression.

Keep it concise and specific to the transcript.
```

### Input (Excerpt — Transcript 1: Technical Interview):
```
[13:06] Candidate: Hi sir. My name is Prasanna Kumar. I have around nine plus years of experience in software development. My core technical expertise is on Angular, React and Ionic framework. I'm working with the backend by using Node.js, Express and .NET Core.
[13:33] Candidate: I've worked mostly on service-based applications, risk assessment management tools, and communication-based applications. Mainly I focus on Ionic Angular and Ionic Capacitor and Cordova for native functionalities and I deployed applications to iOS and Android. AI assist — Cursor, GitHub Copilot and Claude for the last two years.
[24:57] Candidate: Service layer: "create an Angular service with the CRUD operations using HTTP client and retry and error handling". If I wanted to add anything manually, like interceptors or centralized error handling and strong typing, I will be adding manually.
[55:05] Candidate: Zustand, I cannot use this. I worked on React Query.
[55:14] Interviewer: Can you write an example of Zustand for creating a useStore?
[55:24] Candidate: Yeah. Like a constant. Use store. This is the base structure.
```

### Output (Transcript 1):
```
1. TOPICS COVERED
   - Mobile app development
   - Angular and React frameworks
   - Backend development
   - AI-assisted coding tools
   - State management
   - CSS and responsive design

2. PROFILE
   Backend Engineer — Senior Level

3. CANDIDATE SUMMARY
   Prasanna Kumar is a software developer with nine years of experience specializing in Angular, React, and Ionic frameworks with backend exposure in Node.js and .NET Core. He has worked on service-based applications and risk assessment tools. His strengths include cross-platform mobile development and familiarity with AI coding tools like Cursor and GitHub Copilot. A concern is that he struggled when asked about Zustand, indicating gaps in newer state management tools. Overall a capable developer with solid foundational skills.
```

### What Worked:
✅ Correctly extracted main topics at a surface level  
✅ Identified years of experience (nine years)  
✅ Captured some technical skills and AI tool usage  

### What Didn't Work:
❌ **Profile classification was WRONG** — labelled him "Backend Engineer" when his core is clearly Full-Stack Mobile (Ionic, Angular, React with Node only as secondary)  
❌ Too generic — topics like "Mobile app development" and "Backend development" are too broad; missed specifics like Capacitor, Cordova, Tailwind  
❌ No distinction between seniority signals — nine years ≠ senior automatically; communication style and depth of answers matter  
❌ Would completely fail on Transcript 2 (business/ops) — this prompt has no guidance for non-technical interviews  

### Changes for Next Iteration:
- Add branching logic for technical vs. business/operations interviews
- Be explicit about what "profile" means: role + seniority level with justification
- Add examples to guide role classification format
- Explicitly separate strengths from concerns in the summary

---

## ITERATION 2: STRUCTURED & CONTEXT-AWARE

### Prompt Used:
```
Analyze this interview transcript. The candidate is being interviewed for a specific role/domain.

Provide a structured summary with:

1. TOPICS COVERED
   - Identify the main technical, business, or management themes discussed
   - For technical interviews: list frameworks, tools, architectures
   - For business/ops interviews: list processes, KPIs, stakeholder dynamics
   - List 5-8 key topics

2. PROFILE & ROLE FIT
   - Determine the appropriate role/profile (e.g., "Senior Backend Engineer", "Operations Manager - Mid-level")
   - Consider: years of experience, depth/breadth of skills, seniority signals, domain expertise
   - Provide 1-2 sentences justifying why this profile fits

3. CANDIDATE SUMMARY
   - Background: Career progression, education if mentioned, key transitions
   - Strengths: 2-3 key strengths demonstrated in the interview
   - Concerns or Gaps: Any hesitations, areas needing improvement
   - Overall Impression: 1 sentence on how well they fit the role
   - Keep to 4-6 sentences total

Avoid: Generic praise. Be specific to what was actually discussed in the transcript.
```

### Input (Excerpt — Transcript 2: Business/Ops Interview):
```
[3:31] Candidate: Myself Krishna. From Telangana, Hyderabad. B.Tech in mechanical engineering, 2018.
[4:05] Candidate: In 2019 I joined an ed-tech company as associate in operations. Soon moved to digital finance — managed end-to-end finance operations: sales, orders, revenue, marketing spends.
[5:01] Candidate: Then promoted into a new department — FDPU, fraud detection and prevention unit. Got exposure to interact with CBOs, CEOs, CXOs.
[5:28] Candidate: From scratch to ISO certification. Building a CRM, drafting KRAs and KPIs, building dashboard for fraud detection.
[16:05] Candidate: I built my own score by giving weightages. Identified PIN codes from past data where customers pay one EMI and leave. Gave weightage to gender, PIN code, educational qualifications. Today 100 sales punched, run through the score — instead of 100 audits, we do only 10 required ones.
[61:59] Interviewer: You use lot of jargons in Hindi when you try to explain. In starting round fine, but as rounds increase it will be about communication and confidence.
```

### Output (Transcript 2):
```
1. TOPICS COVERED
   - Fraud detection and risk scoring
   - Vendor management and onboarding
   - CRM implementation and BRD drafting
   - KPI and KRA definition for sales operations
   - Stakeholder and leadership communication
   - BPO process optimization and dialer systems
   - Data analytics and dashboard reporting

2. PROFILE & ROLE FIT
   Operations Manager — Mid-level

   Justification: Krishna has approximately 5–6 years of progressive operations experience, moving from associate to leading cross-functional initiatives including fraud detection systems, CRM implementation, and vendor management. His scope of work — engaging C-suite, enrolling 22 vendors, building risk scoring from scratch — signals mid-level ownership, but he lacks the formal program management structure expected at senior level.

3. CANDIDATE SUMMARY
   Krishna holds a B.Tech in mechanical engineering and transitioned into operations at an ed-tech company in 2019, progressing from finance operations to building a fraud detection unit from the ground up. His key strengths include hands-on fraud risk system design (building a proprietary risk score that reduced audits from 100 to 10 per batch), vendor lifecycle management (onboarding and eventually terminating underperforming vendors), and cross-functional leadership across tech, product, and sales teams. A notable concern raised by the interviewer is his heavy use of Hindi jargon when explaining complex situations, which could be a liability in leadership and international stakeholder meetings. Overall, Krishna is a high-potential operations professional with strong execution skills but needs deliberate work on structured English communication before senior leadership roles.
```

### What Worked:
✅ **Correctly identified Operations Manager role** — did not confuse it with a technical profile  
✅ Captured domain-specific topics (KPI tracking, BPO optimization, fraud detection) rather than generic labels  
✅ Picked up the communication concern flagged by the interviewer  
✅ Branching logic worked — produced relevant output for a business interview  

### What Didn't Work:
❌ Profile justification still somewhat vague — "mid-level ownership" needs more grounding in specific evidence  
❌ On Transcript 1, the role was still slightly off — described candidate as "Full-Stack Developer" but didn't capture that Mobile (Ionic) is his primary specialization  
❌ Format of output was inconsistent — sometimes bullet points, sometimes prose, depending on the run  
❌ No explicit instruction to note hesitations during live coding or technical gaps  

### Changes for Next Iteration:
- Add concrete format examples to lock in output structure
- Add an IMPORTANT block to handle edge cases (hesitation = concern, not a strength)
- Explicitly instruct the model not to assume the role — derive it purely from transcript content
- Distinguish between technical confidence and communication quality as separate axes

---

## ITERATION 3: REFINED & EXEMPLIFIED (FINAL — CHOSEN)

### Prompt Used:
```
Analyze this interview transcript and provide a structured candidate assessment:

1. TOPICS COVERED
   - Extract 6-8 main topics/themes discussed in the interview
   - For technical interviews: frameworks, tools, architecture patterns, coding approaches
   - For business/operations interviews: processes, KPIs, stakeholder management, strategic decisions
   - Format as a simple bulleted list
   - Example: ["AI-assisted coding", "Ionic framework", "Mobile responsiveness", "State management"]

2. PROFILE & ROLE FIT
   - Determine the best-fit role and seniority level
   - Consider: years of experience, depth of expertise, breadth of skills, communication style, confidence level
   - Format: "[Role] — [Seniority Level]" (e.g., "Full-Stack Mobile Engineer — Mid-level" or "Operations Manager — Mid-level")
   - Justification: 1-2 specific sentences explaining why this profile fits based on demonstrated skills/experience

3. CANDIDATE SUMMARY
   - Write 4-6 sentences covering:
     a) Background: Career progression, education, key roles/transitions
     b) Strengths: 2-3 key strengths demonstrated (with specific examples from the interview)
     c) Concerns: Areas that need improvement or hesitations observed
     d) Overall Impression: One concluding sentence on how well-suited they are
   - Be specific. Avoid generic praise. Reference actual content from the transcript.

IMPORTANT:
- Do not assume the role. Let the interview content guide the classification.
- Distinguish between technical confidence and soft skills (communication, clarity).
- If candidate shows hesitation or gaps, note them as concerns, not strengths.
- If the candidate's background doesn't align with typical profiles, still classify based on demonstrated capability.
```

### Input (Excerpt — Transcript 1: Technical Interview):
```
[13:06] Candidate: Hi sir. My name is Prasanna Kumar. I have around nine plus years of experience in software development. My core technical expertise is on Angular, React and Ionic framework. I'm working with the backend by using Node.js, Express and .NET Core.
[27:13] Interviewer: You are building a mobile first dashboard using Ionic v7 plus that must work seamlessly across devices. How would you structure the UI, handle responsiveness and ensure performance for large datasets?
[27:41] Candidate: Feature based reusable components. Feature modules like dashboard, reports, settings. Reusable components like cards, data table list, filters and loaders for lazy loading.
[55:05] Candidate: Zustand, I cannot use this. I worked on React Query.
[55:14] Interviewer: Can you write an example of Zustand for creating a useStore?
[55:24] Candidate: Yeah. Like a constant. Use store. This is the base structure.
```

### Output (Transcript 1):
```
1. TOPICS COVERED
   - AI-assisted coding (Cursor, GitHub Copilot, Claude)
   - Ionic framework and mobile-first dashboard design
   - Capacitor plugin ecosystem (camera, filesystem, network)
   - Tailwind CSS and utility-first styling approach
   - Angular modular architecture and state management (RxJS, NgRx)
   - React state management strategy (Context API, React Query)
   - Live coding: Zustand store and Redux slice

2. PROFILE & ROLE FIT
   Full-Stack Mobile Engineer — Mid-level

   Justification: Prasanna has nine years of experience with a clear specialization in Ionic/Angular mobile development and secondary full-stack exposure via Node.js. He demonstrates solid architectural thinking (lazy loading, feature modules, RxJS/NgRx) but showed hesitation on newer React tools (Zustand) and struggled to write complete code snippets under interview pressure, which are signals of mid-level rather than senior capability.

3. CANDIDATE SUMMARY
   Prasanna Kumar is a nine-year software developer with core expertise in Angular, React, and Ionic framework, having built cross-platform mobile apps deployed to iOS and Android, and integrated AI coding tools like Cursor and GitHub Copilot into his workflow for the past two years. His strengths include strong Ionic mobile architecture knowledge (feature modules, lazy loading, virtual scroll for large datasets), practical Capacitor plugin usage (camera, filesystem, network sync), and a structured approach to CSS design systems using Tailwind. A notable concern is his unfamiliarity with Zustand — when asked to write a useStore example he produced only a rough base structure — and a tendency to answer conceptually rather than with precise code during live coding segments. Overall, Prasanna is a dependable mid-level mobile engineer well-suited for Ionic-heavy product teams, though he would benefit from deepening his React ecosystem knowledge before moving into senior or lead roles.
```

### Output (Transcript 2 — confirming generalization):
```
1. TOPICS COVERED
   - Fraud detection system design and risk scoring
   - Vendor onboarding, management, and termination
   - CRM implementation and BRD/PRD drafting
   - KPI and KRA definition for sales and operations teams
   - BPO process optimization (predictive dialing, auto-dialers)
   - Stakeholder communication and data-driven leadership presentations
   - Prioritization frameworks for competing P1 requests

2. PROFILE & ROLE FIT
   Program/Operations Manager — Mid-level

   Justification: Krishna brings 5–6 years of progressive operations experience spanning fraud detection, vendor management, CRM implementation, and analytics — consistently operating at a cross-functional scope. His demonstrated ability to build systems from scratch and engage C-suite stakeholders is strong, but his communication style (flagged by the interviewer for Hindi jargon) and lack of formal program management methodology place him at mid-level rather than senior.

3. CANDIDATE SUMMARY
   Krishna is a mechanical engineering graduate who pivoted into ed-tech operations in 2019, rapidly progressing from finance operations associate to leading a fraud detection and prevention unit (FDPU) where he built a proprietary risk scoring system that reduced required audits from 100 to just 10 per batch. His standout strengths include end-to-end system ownership (ISO certification, CRM implementation, fraud score design), data-driven vendor management (enrolling and eventually terminating underperforming vendors through a structured, legally-aware process), and strong analytical reporting for senior leadership (weekly/monthly executive dashboards covering revenue, ROAS, CAC, and batch operations). The key concern raised directly in the interview is his tendency to use Hindi jargon when explaining complex ideas, which the interviewer specifically warned would become a barrier in leadership and international stakeholder rounds. Overall, Krishna is a high-execution operations professional with impressive breadth for his experience level, and is a strong mid-level candidate who needs structured communication coaching before being considered for senior program management roles.
```

### Why This Is the Final Version:
1. **Format examples locked in structure** — adding `"[Role] — [Seniority Level]"` with concrete examples eliminated inconsistent formatting across runs
2. **IMPORTANT block handled edge cases** — explicitly flagging hesitation as a concern (not a strength) caught the Zustand gap in Transcript 1 and the Hindi jargon issue in Transcript 2
3. **Branching logic generalized well** — the technical vs. business/ops split produced appropriate topic categories for both transcripts without manual tuning
4. **Role classification grounded in evidence** — "do not assume the role" instruction prevented the Iteration 1 error of defaulting to "Backend Engineer"
5. **Tested on both transcripts** — final prompt handles a mobile dev interview and a program management interview with equal quality

---

## Summary of Evolution

| Aspect | Iteration 1 | Iteration 2 | Iteration 3 |
|--------|------------|------------|------------|
| Handles both interview types? | ❌ No | ⚠️ Somewhat | ✅ Yes |
| Clear role classification? | ❌ Wrong role | ✅ Correct | ✅ Correct + justified |
| Specific output format? | ❌ No | ⚠️ Inconsistent | ✅ Locked in with examples |
| Catches hesitation as concern? | ❌ No | ⚠️ Sometimes | ✅ Explicit instruction |
| Tested on both transcripts? | ❌ No | ⚠️ Partially | ✅ Yes |
| Ready for submission? | ❌ No | ❌ No | ✅ Yes |
