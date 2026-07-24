# Algorithm 1: Adaptive Context-Aware Risk Assessment (ACARA)

**Input:**

- Network traffic statistics

**Output:**

- Traffic context
- Adaptive risk score
- Risk level
- Mitigation recommendation

---

1. Collect network traffic statistics.

2. Extract traffic features:
   - Entropy
   - Flow Count
   - Packet Count
   - Unique Source IPs
   - Average Packet Size

3. Normalize all extracted features to the range [0,1].

4. Determine the current traffic context using the normalized feature values.

5. Select context-dependent feature weights according to the detected traffic context.

6. Compute the adaptive risk score using the normalized features and the selected weights.

7. Classify the adaptive risk score into one of the predefined risk levels:
   - LOW
   - MEDIUM
   - HIGH
   - CRITICAL

8. Generate the corresponding mitigation recommendation:
   - LOW → Monitor Traffic
   - MEDIUM → Increase Monitoring
   - HIGH → Apply Rate Limiting
   - CRITICAL → Recommend OpenFlow Drop Rule

9. Return the traffic context, adaptive risk score, risk level, and mitigation recommendation.