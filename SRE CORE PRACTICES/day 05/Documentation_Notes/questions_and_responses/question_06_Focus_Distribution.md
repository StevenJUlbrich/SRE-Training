# Focus Distribution Analysis for Integration & Triage Training

I've reviewed our outline and the audience analysis document to confirm our proper balance approach for the Integration & Triage training content.

## 1. Maintaining 85% Focus on Core SRE Integration & Triage Concepts

To ensure our 85% focus on core SRE concepts, I recommend:

- Dedicate the majority of each chapter's content to universal SRE principles that would apply across any industry
- Structure each panel to begin with technical concept explanation before applying it to banking
- Ensure implementation guidance focuses primarily on methodology rather than banking-specific procedures
- Include technical depth on signal types, correlation techniques, and investigation methodologies that represent core SRE competencies
- Reserve approximately 5-6 panels per chapter for pure SRE concept teaching without industry context

Key core concepts to emphasize across chapters:
- Signal collection, filtering, and interpretation techniques
- Systematic triage methodologies and frameworks
- Evidence-based troubleshooting approaches
- Hypothesis formulation and testing
- Correlation analysis across distributed systems
- Causal analysis techniques

## 2. Integrating 15% Banking-Specific Applications

For the 15% supporting context, we'll:

- Include 1-2 banking-specific panels per chapter that directly apply concepts to the financial domain
- Use the "Common Example of the Problem" section in each panel to provide banking context
- Include brief regulatory callouts where relevant without making them the primary focus
- Connect each SRE practice to specific banking business impacts in dedicated "Banking Impact" sections
- Use familiar banking terminology to illustrate concepts without letting it dominate
- Incorporate visual elements that depict banking environments (trading desks, payment processing systems)

## 3. Adjustments to Technical Depth vs. Practical Application

Based on our audience analysis from question_04_response_audience.md:

- **Chapter 1-2**: Higher ratio of practical application to technical depth (70:30), leveraging existing monitoring knowledge while introducing new observability concepts
- **Chapter 3-4**: Balanced approach (50:50) as we build on existing troubleshooting skills while introducing new correlation techniques
- **Chapter 5-6**: Maintain balance (50:50) focused on practical implementation of evidence-based investigation
- **Chapter 7-8**: Shift toward more technical depth (40:60) as we introduce advanced concepts in automation and measurement

Throughout all chapters, ensure practical application sections contain concrete, executable steps rather than theoretical benefits.

## 4. Balancing Theoretical Concepts with Concrete Examples

To maintain the proper balance between theory and examples:

- Begin each new concept with a clear theoretical explanation (1 paragraph)
- Follow immediately with a concrete banking example (1-2 paragraphs)
- Include "Before and After" scenarios showing how the concept changes actual practice
- Use a consistent hypothetical banking platform (e.g., "GlobalBank") for continuity across examples
- Include visual representations of both the abstract concept and its concrete application
- Follow the 1:2 ratio - for every theoretical point, provide at least two specific examples
- Ensure examples progress from simple to complex as chapters advance

## 5. Balancing with Audience Analysis and Examples

To align with our audience analysis while maintaining proper examples:

- **Address Knowledge Gaps**: For each identified gap in systems thinking, signal theory, etc., provide explicit bridges from familiar production support concepts to new SRE approaches
- **Leverage Existing Skills**: Reference familiar tools like ITRS Geneos when introducing new concepts, showing how their existing skills transfer
- **Support Mindset Shifts**: Include "mindset moment" callouts in each chapter that explicitly address one of the seven mindset shifts identified in the audience analysis
- **Terminology Alignment**: Begin each chapter with a "terminology bridge" that connects production support terms to SRE concepts
- **Progressive Example Complexity**: Start with simple examples involving familiar systems (payment processing) and gradually introduce more complex scenarios (distributed trading platforms)

Each chapter should include:
- At least one example leveraging their existing alert response experience
- Reference to familiar tools they already use (ITRS Geneos, Splunk)
- Connection to banking processes they understand
- Progressive introduction of new terminology with clear definitions
- Examples that showcase the mindset shift from reactive to proactive operations

By following these guidelines, we'll maintain the proper 85/15 balance between core SRE concepts and banking-specific applications while addressing the specific needs of our audience transitioning from production support to SRE roles.