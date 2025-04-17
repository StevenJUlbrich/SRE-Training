## Dev Playbook: SLOs, Dashboards, and Not Getting Paged at 3AM

Welcome, busy devs. This is your stripped-down, straight-talking guide to not breaking production, or if you do, at least breaking it *gracefully*.

This playbook is focused on:

- Why you need SLOs
- How to set good ones
- Using dashboards like a grown-up
- Avoiding incident drama with basic observability hygiene

---

### 🔑 What You Actually Need to Know

**SLIs** = Metrics that tell you what your users feel (e.g., latency, error rate).

**SLOs** = Targets for those metrics (e.g., "99.9% of logins under 300ms").

**Error Budget** = How much you’re allowed to fail without it being a crisis.

**SLA** = Legal panic button. Don't worry—someone else writes these.

---

### 🛠️ Setting Up SLOs (Without Wasting Everyone’s Time)

1. **Pick your SLIs wisely:**

   - Latency, errors, throughput, saturation.
   - If a user would complain, it’s probably a good SLI.

2. **Define the SLO:**

   - Don’t go for 99.999% unless you’re allergic to sleep.
   - Start with 99.5% or 99.9% depending on the service.

3. **Error Budget Rule of Thumb:**

   ```python
   total_requests = 1_000_000
   slo = 0.999
   allowed_failures = total_requests * (1 - slo)
   print(allowed_failures)  # That’s your wiggle room
   ```

---

### 📊 Dashboards That Work (and Don’t Lie to You)

**Golden Signals to Always Track:**

- **Latency** – How slow is it?
- **Errors** – What’s failing?
- **Traffic** – How much stuff?
- **Saturation** – Are we running out of resources?

**Dashboard Do’s:**

- Make it about *user experience*, not CPU usage.
- Burn-down chart for your error budget? Good.
- Traffic light status for SLOs? Better.

**Dashboard Don’ts:**

- If it takes more than 10 seconds to interpret, no one will look at it until it’s too late.

---

### 🚨 How to Not Get Blamed (or Blame Someone Else)

- **Use burn rate alerts**: Only page when we’re actually draining the error budget fast.
- **Have 1–2 SLOs per service**: More than that and nobody knows what’s on fire.
- **Monitor critical user journeys**: If checkout breaks, it’s worse than if search autocomplete does.

```python
def projected_burn_rate(error_rate, budget, hours):
    return (error_rate / budget) * hours
```

---

### 👥 Talking to SREs Like They’re People

- Ask: "What SLO would you recommend for this endpoint?"
- Share metrics early—before launch.
- Don’t ship a feature if your observability is basically a shrug emoji.

---

### 🧼 Observability Hygiene Checklist (aka The Stuff Future You Will Thank You For)

✅ 1. Do your SLOs reflect actual user pain? “API uptime” is cute. “Checkout success rate” is useful. Choose wisely.

✅ 2. Can your dashboard tell you if you're in trouble—fast? If it takes longer than a microwave popcorn cycle to interpret, it’s too complex.

✅ 3. Is your alerting strategy based on burn rate, not server drama? Alerts should whisper, "Fix this before users notice," not scream, "Disk is 85% full again, lol."

✅ 4. Do your metrics have context? Logging errors is great. Knowing if they blow the error budget? Chef’s kiss.

✅ 5. Does someone on your team actually know what the error budget is right now? If they say “maybe,” they mean no. Fix it.

---

### 🧘 Final Thought

SLOs aren’t red tape. They’re guardrails so you can build fast without wrecking the car. Respect them, and you get to ship more. Ignore them, and you get to write incident reports.

Happy deploying.

