# Ava Kimani: SRE Documentation Voice Persona

## Background & Personality

Ava Kimani is a 38-year-old Senior Site Reliability Engineer from Nairobi, Kenya. With 15 years of experience in the field, she started her career at a local telecom company before moving to a global cloud provider where she specialized in reliability engineering for distributed systems.

### Personal Traits:
- **Direct and no-nonsense**: Ava has no patience for vanity metrics or unrealistic promises. She values honesty and transparency above all.
- **Warm but firm**: While approachable and genuinely interested in helping others learn, she's not afraid to challenge faulty assumptions.
- **Pragmatic problem-solver**: Believes in practical solutions over theoretical perfection.
- **Storyteller**: Uses relatable analogies from everyday Kenyan life to explain complex technical concepts.
- **Advocate for measurement**: Her catchphrase "Reliability you can measure" stems from her belief that unmeasured reliability is merely wishful thinking.

### Professional Philosophy:
Ava believes that reliability engineering isn't about perfection, but about setting realistic expectations and meeting them consistently. She advocates for SRE practices that acknowledge the reality of distributed systems—they will fail, but we can manage and learn from those failures.

## Speaking Style & Mannerisms

- Uses clear, concise language free of unnecessary jargon
- Often integrates Swahili phrases and Kenyan references when explaining concepts
- Has a characteristic habit of playfully "slapping wrists" (figuratively) when she catches someone focusing on vanity metrics
- Frequently uses the phrase "Let me stop you right there" when she notices a misconception
- Balances technical rigor with accessibility—never dumbing down concepts but making them understandable

## Teaching Approach for SRE Topics

### On SLOs & Error Budgets:
"Think of an SLO like a promise to your users. Not a vague 'we'll try our best' but a specific commitment: 'your requests will get responses in under 300ms 99.9% of the time.' And that 0.1%? That's your error budget—your permission to take risks, to innovate. Use it wisely."

### On Latency SLIs:
"When measuring API latency, remember the journey your data takes. Your users don't care if your API is lightning fast if your database is crawling! Always measure end-to-end experiences. In my village, we say 'a chain is only as strong as its weakest link.' Your system reliability works the same way."

### On Vanity Metrics:
*Playfully slaps wrist* "Ah! I see you bragging about that 99.999% uptime again! But what does that mean for your users? Nothing if you're not measuring what they actually care about. Drop the vanity metrics and focus on user experience. Are your customers happy? That's the real metric."

## Visual Appearance & Environment
Ava is often visualized in documentation with:
- Professional but comfortable attire, often including vibrant Kenyan-inspired patterns
- Working from a modern co-working space in Nairobi with the city skyline visible
- Surrounded by multiple monitors displaying dashboards and metrics
- A coffee mug with "Reliability you can measure" printed on it
- A small whiteboard where she sketches concepts as she explains them

## Sample Documentation Voice

"Hello, I'm Ava, and today we're going to talk about something I'm passionate about: meaningful SLIs for your API and database layers.

*Notices a "100% uptime" goal on a slide*

*Playfully slaps wrist* Let's not start with impossible promises! Instead, let's talk about what your users actually experience and how to measure it reliably.

Your API might respond quickly, but if your database query takes 5 seconds, your users are still waiting 5 seconds. That's why we need to measure latency at both layers and understand their relationship.

Let me show you how to set up proper latency SLIs that capture the full user experience, not just what makes your team look good in meetings. Remember: reliability you can measure is the only reliability that matters!"

This character combines technical expertise with an authentic personality, creating a memorable "voice" for your SRE documentation that will engage readers while effectively teaching important reliability engineering concepts.