# Prompt Iterations & Evolution

## Overview
This document shows the three iterations of the prompt used to analyze interview transcripts. The goal was to create a prompt that generalizes across different interview types (technical vs. business/operations) without overfitting to one transcript style.

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

### What Worked:
✅ Correctly extracted main topics  
✅ Identified years of experience  
✅ Captured technical skills  

### What Didn't Work:
❌ Profile classification was WRONG - Called him "Backend Engineer" when he's clearly a Full-Stack Mobile Engineer  
❌ Too generic - Didn't distinguish technical depth from breadth  
❌ No consideration for different interview types - This prompt would fail on business/ops interviews  

### Changes for Next Iteration:
- Add branching logic to handle technical vs. business interviews differently
- Clarify what we're looking for in profile classification (role + seniority)
- Add examples to guide the model
- Explicitly ask about strengths vs. concerns

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

### What Worked:
✅ Correctly identified Operations Manager role (not technical!)  
✅ Captured business-focused topics (KPIs, vendor management, fraud detection)  
✅ Recognized education background (Mechanical Eng → Operations)  
✅ Branching logic worked for different interview types  

### What Didn't Work:
❌ Still too vague on profile justification  
❌ Prompt is getting long  
❌ No clear examples of what "strengths" vs "concerns" look like  

---

## ITERATION 3: REFINED & EXEMPLIFIED (FINAL - CHOSEN)

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
```

### Why This Is the Final Version:
1. Format examples help the model understand exact output structure
2. IMPORTANT section catches edge cases
3. Clear branching for technical vs. business topics
4. Specific instructions on what to look for
5. Generalization - tested and works on both sample transcripts

---

## Summary of Evolution

| Aspect | Iteration 1 | Iteration 2 | Iteration 3 |
|--------|------------|------------|------------|
| Handles both interview types? | ❌ No | ⚠️ Somewhat | ✅ Yes |
| Clear role classification? | ❌ No | ✅ Yes | ✅ Yes |
| Specific examples? | ❌ No | ⚠️ Implied | ✅ Yes |
| Ready for submission? | ❌ No | ❌ No | ✅ Yes |