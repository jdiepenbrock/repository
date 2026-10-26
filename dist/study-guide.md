# Inference Lab — your Exam 2 study guide

Based on all six supplied slide decks and the supplied 30-question practice exam. Worked practice answers are independently derived; no official answer key was supplied.

## How to use this

First try mixed practice without notes. For each miss, name the trap, study that lesson, and redo a similar question. Use flashcards to recall formulas before revealing them. Finish with a 20-question, 70-minute mock exam. A strong practice target is at least 17/20 on fresh mixed questions plus being able to explain each mistake; this is a study goal, not a guaranteed grade.

The mock topic mix is a study choice, not a prediction. The supplied PDF calls the practice exam slightly easier than the real exam. Practice concepts and choices, not just the letters in the supplied key.

## Choose the method before calculating

| Situation | Method | First check |
|---|---|---|
| One numeric population mean, σ known | z mean interval/test | SE = σ/√n |
| One numeric population mean, σ unknown | t interval/test | SE = s/√n; df = n−1 |
| One binary population proportion | z proportion methods | CI SE uses p̂; null test SE uses p₀ |
| Two independent numeric means, σ₁ and σ₂ known | Two-sample z | Add variances of means inside √ |
| Two independent numeric means, unknown equal variances | Pooled two-sample t | Weight sample variances by nᵢ−1; df = n₁+n₂−2 |
| Two independent numeric means, equal variances not assumed | Welch t | Separate variance terms; adjusted df |
| Same people before/after or matched pairs | Paired t on differences | Count pairs; df = number of pairs−1 |
| Two independent binary proportions | Two-proportion z | Equality test uses pooled p̂; CI uses unpooled SE |
| One categorical variable against specified probabilities | χ² goodness of fit | E = n pᵢ; df = k−1 when probabilities fully specified |
| Two categorical variables cross-classified | χ² independence | E = row×column/grand; df = (r−1)(c−1) |

## Printed-reference practice

The supplied exam provides two-sided z*: 90% = 1.645; 95% = 1.960; 99% = 2.576. At α = .05, right-tail χ² cutoffs: df 1: 3.841; 2: 5.991; 3: 7.815; 4: 9.488; 5: 11.070; 6: 12.592; 12: 21.026. Needed t-critical values are supplied within questions.

## A repeatable MCQ routine

1. Identify whether the outcome is numeric, binary, or categorical counts.

2. Identify the parameter (μ, p, a difference, or association), number of groups, and whether observations are independent or paired.

3. For a test, write Hₐ first to determine the tail. For a CI, identify the confidence level and correct multiplier.

4. Write the SE before calculating. Most numerical traps replace √n with n, use SD instead of SE, or pool when they should not.

5. For a test, compute (estimate − null value)/SE and compare p with the stated α. For a CI, use estimate ± critical × SE.

6. Eliminate choices with the wrong units, center, tail, df, or Excel argument. Interpret the conclusion in context.

7. Budget about 3.5 minutes per question on average. Bank time on concept questions, flag slow calculations, and return to them.

## Suggested study blocks

### Diagnose before studying (15 minutes)

Do a mixed diagnostic without notes. For every answer, name the method and the reason; mark guesses even if correct. Use the topic scores to choose what to revisit.

### Learn the decision map (20 minutes)

Read the six short topic lessons. Practice classifying variable type, one versus two samples, mean versus proportion, known versus unknown σ, and alternative direction before touching a calculator.

### Work the algebra by hand (30 minutes)

Calculate one z interval, one t interval, one proportion interval, one pooled two-mean t, one pooled two-proportion z, and one chi-square expected-count calculation. Write SE as a separate step each time.

### Retrieve, then repair (20 minutes)

Answer flashcards before revealing the backs. Drill missed topics and explain why each distractor is wrong. Redo misses later without looking at the explanation.

### Rehearse the real format (70 minutes)

Take a fresh 20-question mixed mock with a 70-minute timer, as described in the practice PDF. Use a calculator and only the reference values supplied with the mock. That averages 3.5 minutes per question; move past a stuck calculation and return.

### Make the last review count (15 minutes)

Review misses and guesses by cause: method, SE, tail, df, algebra, or interpretation. Rewrite the right rule from memory, then solve a different question on that rule. Aim for repeated success on fresh questions, not memorized letters.

## Sampling distributions & standard error

Separate individual observations from averages. Then identify the center, spread, and shape of the statistic you are using.

### Population, sample, statistic, parameter

A parameter describes a population: μ is its mean, σ its standard deviation, and p its proportion. A statistic describes one sample: x̄, s, and p̂. A sampling distribution asks what a statistic would look like over repeated random samples of the SAME size. It is different from the distribution of the individual observations.

**Formula:** E(x̄) = μ; SD(x̄) = SE(x̄) = σ / √n

**Worked example:** If individual commute times average 30 minutes with SD 12, sample means from n=36 are centered at 30 with SE=12/6=2 minutes. Individual people still have SD 12.

**MCQ trap:** The sampling distribution is not the list of observations in one sample, and its center does not move toward zero as n increases.

**Source:** Sampling Distribution, slides 2–5, 14; Practice Exam, Q1, Q7

### Standard deviation versus standard error

SD measures the spread of individual values. SE measures the spread of sample statistics. When σ is unknown, use s to estimate the SE of x̄. A small SE means averages vary little across repeated samples; it does not mean individual people or products are similar.

**Formula:** Known σ: SE = σ / √n
Unknown σ: estimated SE = s / √n
Variance of x̄ = σ² / n

**Worked example:** With σ=20 and n=64, SE=20/8=2.5. The variance of x̄ is 6.25; it is not the SE.

**MCQ trap:** Divide by √n, not n. Do not confuse a variance, a standard deviation, and a standard error.

**Source:** Sampling Distribution, slides 8–12, 14; CI Sigma Known and Unknown, slides 2–3

### What increasing n changes

A larger random sample makes the sampling distribution narrower because SE is proportional to 1/√n. The population SD and population mean do not change merely because we sample more people. The sample mean is still random; a larger n does not guarantee an exact estimate.

**Formula:** SE(new) / SE(old) = √(n_old / n_new)

**Worked example:** To cut SE from 4 to 2, multiply n by 4. Doubling n multiplies SE by 1/√2, about 0.707.

**MCQ trap:** Doubling sample size does not halve SE. More data also does not automatically fix selection bias.

**Source:** Sampling Distribution, slides 9–10, 14; CI Sigma Known and Unknown, slides 3–4

### When can you use the normal curve?

If the population is normal, its sample mean is normal for any n under independent sampling. Otherwise, the Central Limit Theorem gives an approximately normal sampling distribution for sufficiently large n with finite population variance. This course uses n≈30 as the usual rule of thumb. Severe skew, outliers, or heavy tails can require much more data.

**Formula:** For a normal/approximately normal x̄:
z = (x̄ − μ) / (σ / √n)

**Worked example:** A skewed population sampled at n=64 can often be analyzed with a normal approximation for the mean. This does not make the individual observations normally distributed.

**MCQ trap:** The CLT is about the mean’s distribution. It does not say every population becomes normal or that n=30 is a universal guarantee.

**Source:** Sampling Distribution, slides 13–14; CI Sigma Known and Unknown, slide 4; Practice Exam, Q2

### Sampling probabilities & Excel recognition

First decide whether a question concerns one observation X or a sample mean x̄. Use σ for X and σ/√n for x̄. Excel NORM.DIST(x,mean,SD,TRUE) gives a LEFT cumulative area; subtract from 1 for a right-tail probability. TRUE and 1 are equivalent cumulative arguments.

**Formula:** P(x̄ > a) = 1 − NORM.DIST(a, μ, σ/SQRT(n), TRUE)
P(a < x̄ < b) = F(b) − F(a)

**Worked example:** For μ=80, σ=10, n=25, P(x̄>84) uses SE=2, z=2, and is about .0228. The Excel expression is =1-NORM.DIST(84,80,10/SQRT(25),TRUE).

**MCQ trap:** A formula may have the correct tail but the wrong spread. Check BOTH the 1− and the division by SQRT(n).

**Source:** Sampling Distribution, slides 10, 14; Practice Exam, Q6

## Confidence intervals for means

Use estimate ± critical value × standard error. The known-versus-unknown population SD determines z versus t.

### What a confidence interval actually says

The population mean is fixed; intervals change from sample to sample. A 95% method captures the true mean in about 95% of repeated samples when assumptions hold. For one computed interval, say “we are 95% confident that the population mean lies between the endpoints.” This is about a population mean, not the percentage of individual data inside the interval.

**Formula:** CI = point estimate ± margin of error
Margin of error (ME) = critical value × SE
α = 1 − confidence LEVEL

**Worked example:** For a CI of (42,58), x̄=50 and ME=8. The interval estimates μ. It does not claim that 95% of people have values from 42 to 58.

**MCQ trap:** On an MCQ, choose the repeated-sampling interpretation rather than “there is a 95% probability the fixed μ is in this computed interval.”

**Source:** CI Sigma Known and Unknown, slides 5–7; CI Proportions, slides 3–5; Practice Exam, Q8

### Population σ known: use z

When the population standard deviation σ is supplied as known, use the standard normal critical value. Conditions include random, sufficiently independent observations and a normal or sufficiently well-behaved large-sample distribution for x̄.

**Formula:** CI for μ = x̄ ± z* × σ/√n
Two-sided z*: 90%→1.645; 95%→1.960; 99%→2.576

**Worked example:** With x̄=52, σ=7, n=49 and 95% confidence: SE=1, ME=1.96, so CI=(50.04,53.96).

**MCQ trap:** A population MEAN being specified does not make σ known. Read whether the given spread is population σ or sample s.

**Source:** CI Sigma Known and Unknown, slides 6–7; Practice Exam, Q9

### Population σ unknown: use t

Replace unknown σ with sample SD s, and use Student’s t with df=n−1 for one sample. The t curve is symmetric with heavier tails than the standard normal; it approaches normal as df grows. For small samples, a roughly normal population without serious outliers is especially important.

**Formula:** CI for μ = x̄ ± t* × s/√n
df = n − 1

**Worked example:** With n=16, x̄=18, s=4, and supplied t*=2.131: SE=1 and CI=(15.869,20.131).

**MCQ trap:** Use df=n−1, not n. A large n does not make a supplied sample s become a known population σ; t remains the standard choice.

**Source:** CI Sigma Known and Unknown, slides 8–10; Practice Exam, Q12, Q14

### How the interval gets wider or narrower

At a fixed confidence level, larger n narrows the interval and greater variability widens it. At a fixed dataset, higher confidence requires a larger critical value, so the interval widens. Changing confidence changes the margin, not the point estimate. To achieve a desired ME with known σ, solve the ME equation for n and round UP.

**Formula:** Width = 2 × ME
Known-σ planning: n ≥ (z*σ / desired ME)²

**Worked example:** Going from 95% to 99% confidence makes a CI wider. At the same confidence level and σ, cutting ME in half requires four times n.

**MCQ trap:** “More confidence” does not mean “more precise.” Wider intervals have higher coverage but lower precision. The planning formula is algebra from the z interval.

**Source:** CI Sigma Known and Unknown, slides 3, 6–7; Practice Exam, Q11, Q13

### Excel critical values, and linking CI to a test

T.INV.2T(alpha,df) returns the positive two-sided t cutoff: input α, not α/2. T.INV(1−α/2,df) gives the same upper cutoff. NORM.S.INV(1−α/2) gives z*. A two-sided level-α test of a mean using the matching model rejects a candidate μ₀ outside its (1−α) CI.

**Formula:** 90% one-sample t CI with n=20:
=T.INV.2T(0.10,19)
=CONFIDENCE.T(alpha,s,n) returns ME, not endpoints

**Worked example:** For a 95% CI of (10.2,13.8), μ₀=12 is compatible with the interval; μ₀=14 would be rejected by the matching two-sided 5% test.

**MCQ trap:** Do not feed .05 to T.INV.2T for a 90% CI. Do not mistake CONFIDENCE.T’s margin of error for an upper endpoint.

**Source:** CI Sigma Known and Unknown, slide 10; CI Proportions, slide 12; Practice Exam, Q14

## Proportions: intervals & pooled tests

Recognize success/failure data. CI standard errors estimate the population proportions; equality tests use the null’s pooled proportion.

### One proportion: build the interval

A proportion is appropriate when outcomes can be classified as success/failure. Estimate the population proportion p using p̂=x/n, where x is the number of successes. For the usual normal-approximation CI, estimate SE using p̂, then add and subtract z* times that SE.

**Formula:** p̂ = x/n
SE = √[p̂(1−p̂)/n]
CI for p = p̂ ± z*√[p̂(1−p̂)/n]

**Worked example:** If 240 of 400 customers prefer a product, p̂=.60 and SE≈.0245. A 95% CI is .60±1.96(.0245)≈(.552,.648).

**MCQ trap:** Enter percentages as proportions: 60% becomes .60. An interval for p estimates a population proportion, not a sample count.

**Source:** CI Proportions, slides 6–10; Practice Exam, Q10

### Conditions and interpretation

Use random, independent observations and enough successes and failures for a normal approximation. The course’s handwritten two-proportion notes require at least 5 of each outcome in each group; some texts use the more conservative cutoff 10. For this course follow the stated convention. Very sparse data need a different method rather than blindly applying a z formula. For a null-based proportion z test, assess expected successes and failures under p₀ (one sample) or the pooled estimate under equality (two samples) as appropriate.

**Formula:** Successes = n × p̂; failures = n × (1−p̂)
Independent groups: check each group separately

**Worked example:** With n=100 and p̂=.98 there are only 2 failures. The usual course normal-approximation condition fails even though n is 100.

**MCQ trap:** A large total n is not enough when one outcome is rare. “95% confident” concerns population p, not 95% of responses being successes.

**Source:** Chi Square Test of Independence, handwritten slides 23, 27–28; CI Proportions, slides 3, 9–10

### Difference of two proportions: CI uses two estimates

For two independent random groups, estimate p₁−p₂ by p̂₁−p̂₂. A CI does not impose equality, so its SE keeps the two separate sample proportions. The order of subtraction must match the question. A positive interval means group 1 has the higher population proportion.

**Formula:** CI for p₁−p₂ = (p̂₁−p̂₂) ± z*√[p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂]

**Worked example:** Group 1: 60/100=.60. Group 2: 90/200=.45. Difference=.15, SE≈.0603; 95% CI≈(.0318,.2682), or 3.18 to 26.82 percentage points.

**MCQ trap:** A .15 proportion difference is 15 percentage points. Do not call it a 15% relative increase unless you calculate the relative change.

**Source:** CI Proportions, slide 11; Chi Square Test of Independence, handwritten slides 27–28

### Test equal proportions: pool under H₀

For H₀:p₁=p₂, both samples estimate the same population proportion. Combine successes and observations to estimate that shared p. Then standardize the observed difference using this pooled SE. Choose left, right, or two tails from Hₐ.

**Formula:** p̂_pool = (x₁+x₂)/(n₁+n₂)
SE₀ = √[p̂_pool(1−p̂_pool)(1/n₁+1/n₂)]
z = (p̂₁−p̂₂) / SE₀  [null difference 0]

**Worked example:** For 60/100 versus 90/200, p̂_pool=150/300=.50. SE₀≈.06124 and z≈2.449. The .50 is weighted by sample sizes; (.60+.45)/2=.525 would be wrong.

**MCQ trap:** POOL for the usual equality test; do NOT pool for the ordinary difference CI. A pooled test and an unpooled CI need not give exactly identical borderline decisions.

**Source:** Chi Square Test of Independence, handwritten slides 22–25, 27–28

### One-proportion test and interval comparisons

For a one-proportion z test, the null specifies p₀, so its SE uses p₀ rather than p̂. For CI decisions, a difference interval excluding 0 supports a difference at the matching confidence level. Nonoverlap of two separate CIs supports a difference, but overlap alone does not establish equality; analyze the difference directly.

**Formula:** One-proportion z = (p̂−p₀) / √[p₀(1−p₀)/n]
Two-sided p-value = 2[1−Φ(|z|)]

**Worked example:** With p̂=.62, p₀=.50, n=100: SE₀=.05 and z=2.40. A two-sided p-value is about .0164. A CI would instead use √(.62×.38/100).

**MCQ trap:** Do not swap CI SE and null-test SE. A result that fails to reject equality does not prove two populations are identical.

**Source:** Practice Exam, Q22; CI Proportions, slides 12–13; Chi Square Test of Independence, handwritten slides 24–28

## Hypothesis testing: setup, tails & errors

Translate the claim into Hₐ, standardize against H₀, choose the correct tail, and compare p with α.

### Write the hypotheses before calculating

Hypotheses concern a population parameter, such as μ or p, not the observed x̄. The alternative gives the direction: “greater” means >, “less” means <, and “different” means ≠. Equality belongs in H₀. One-sided H₀ may be written as ≤ or ≥; calculations use its boundary value.

**Formula:** Right: H₀:μ≤μ₀; Hₐ:μ>μ₀
Left: H₀:μ≥μ₀; Hₐ:μ<μ₀
Two-sided: H₀:μ=μ₀; Hₐ:μ≠μ₀

**Worked example:** A battery maker claims “at least 50 hours.” To challenge that claim, Hₐ:μ<50 and H₀:μ≥50. This is a left-tailed test.

**MCQ trap:** Do not pick the tail after seeing the statistic. The sign of the statistic can disagree with the prespecified direction of Hₐ.

**Source:** Hypothesis Testing, slides 6–12, 25, 36, 45; Practice Exam, Q19

### Compute the appropriate test statistic

A test statistic asks how many null standard errors the estimate is away from the hypothesized value. Use z for a mean when population σ is known. Use t with df=n−1 when σ is unknown and sample s estimates it. The null value belongs in the numerator.

**Formula:** Known σ: z = (x̄−μ₀)/(σ/√n)
Unknown σ: t = (x̄−μ₀)/(s/√n); df=n−1

**Worked example:** With x̄=52, μ₀=50, σ=8, n=64: SE=1 and z=2. With x̄=18.5, μ₀=18, s=2, n=16: SE=.5 and t=1.

**MCQ trap:** Do not subtract sample SD from the sample mean. Do not divide by a variance. A claim about μ₀ being known is separate from σ being known.

**Source:** Hypothesis Testing, slides 14–15, 27–29, 34–40; Practice Exam, Q20–21

### P-values, tails, and Excel

A p-value is the probability, assuming H₀, of a statistic at least as extreme as observed in the direction(s) of Hₐ. Cumulative distribution functions return left-tail areas. Use 1−CDF for a right tail. For a symmetric two-sided z or t test, double the tail beyond the absolute statistic.

**Formula:** Left z: =NORM.S.DIST(z,TRUE)
Right z: =1-NORM.S.DIST(z,TRUE)
Two-sided z: =2*(1-NORM.S.DIST(ABS(z),TRUE))
Left t: =T.DIST(t,df,TRUE)
Right t: =1-T.DIST(t,df,TRUE)
Two-sided t: =T.DIST.2T(ABS(t),df)

**Worked example:** At z=2, right-tail p≈.0228; two-sided p≈.0455. At z=−1.75, two-sided p is 2[1−Φ(1.75)]≈.0801.

**MCQ trap:** For two tails, use |z| or |t| before taking the upper tail. Doubling the upper-tail area at a negative statistic can produce an impossible p>1.

**Source:** Hypothesis Testing, slides 16–17, 30–31, 41–42; Practice Exam, Q17, Q22

### Make the decision, then state what it means

Reject H₀ when p≤α; otherwise fail to reject H₀. Small p means the observed evidence is unusual under H₀, not that H₀ has that probability of being true. A conclusion should name the population and the alternative direction. Statistical significance does not guarantee a large or practically useful effect.

**Formula:** p ≤ α → reject H₀
p > α → fail to reject H₀
Right-tail critical rule: statistic > positive cutoff
Two-sided: |statistic| > positive cutoff

**Worked example:** If p=.032 and α=.05, reject. If α=.01, fail to reject. In the rail example, p=.0285>.01, so fail to reject at 1%.

**MCQ trap:** “Fail to reject” is not “accept H₀” or “prove no effect.” Slide 32’s printed p>.05 is a typo: that example uses α=.01.

**Source:** Hypothesis Testing, slides 18–19, 32–33, 43–44; Practice Exam, Q18

### Type I error, Type II error, and power

Type I is a false alarm: reject a true H₀. Type II is a missed effect: fail to reject a false H₀. At a fixed sample size, lowering α generally makes rejection harder and increases β. With α fixed, a larger sample generally increases power; the nominal Type I rate remains α.

**Formula:** P(Type I error | H₀ true) = α
P(Type II error | a specified alternative true) = β
Power = 1−β

**Worked example:** If H₀ says a product is not defective, a Type I error declares a good product defective. A Type II error misses a truly defective product.

**MCQ trap:** α is not the probability your particular conclusion is wrong. Slide 22’s claim that larger n reduces both errors needs qualification: with fixed α, the Type I rate stays fixed.

**Source:** Hypothesis Testing, slides 20–22

### A repeatable MCQ routine

Before looking for a formula, identify the variable type and the number of samples. Then identify the parameter, null value, tail, and known versus unknown σ. Compute SE on a separate line; calculate the statistic; compare with p or a critical value; interpret. Excel questions test recognition of the same steps.

**Formula:** Five steps: hypotheses → statistic → decision rule → decision → contextual conclusion

**Worked example:** “25 independent orders, numeric values, σ unknown, Hₐ:μ>80” means one-sample t, df=24, and right-tail p=1−T.DIST(t,24,TRUE).

**MCQ trap:** Most plausible distractors change exactly one ingredient: tail, df, SE, distribution, or null/estimate. Check these five ingredients deliberately.

**Source:** Hypothesis Testing, slides 12–19, 36–44; Practice Exam, Q14, Q17, Q22, Q24

## Comparing two means

For independent numeric samples, select known-variance z, equal-variance pooled t, or unequal-variance Welch t.

### Choose the design and the method

Two means compare a numeric outcome between two populations. The deck focuses on independent random samples. If population variances are known, use z. If unknown but explicitly assumed equal, use pooled t. If unknown and unequal/not assumed equal, use Welch t. Normality or adequate large-sample behavior is needed, especially with small samples.

**Formula:** Estimate = x̄₁−x̄₂
Null value = D₀, usually 0
Statistic = [(x̄₁−x̄₂)−D₀] / appropriate SE

**Worked example:** Comparing purchases from independently sampled Saturday and Sunday shoppers is a two-independent-means setting. Before/after measurements on the same shoppers would be paired; those are not independent groups.

**MCQ trap:** Equal SAMPLE SIZES do not establish equal population variances. A mean problem has numeric outcomes, not counts of success/failure.

**Source:** Two Sample Means, slides 3–6, 8–9, 21–22; paired-design note is a recognition extension

### Known population variances: two-sample z

For independent sample means, variances of their sampling errors add. Use each population variance divided by its sample size. Square root the sum to obtain SE. This is a z method only when the population SDs/variances are known.

**Formula:** SE = √(σ₁²/n₁ + σ₂²/n₂)
z = [(x̄₁−x̄₂)−D₀] / SE

**Worked example:** With σ₁=6, n₁=36, σ₂=8, n₂=64, SE=√(1+1)=√2. A difference of 3 against D₀=0 gives z≈2.121.

**MCQ trap:** Add variances before taking the square root. Do not simply add σ₁/√n₁ and σ₂/√n₂.

**Source:** Two Sample Means, slide 5

### Unknown but equal variances: pool first

The pooled variance is a degrees-of-freedom-weighted average of the two sample variances. Larger samples receive more weight. After finding sₚ², use the same pooled variance for both terms of the SE, then a t distribution with n₁+n₂−2 degrees of freedom.

**Formula:** sₚ² = [(n₁−1)s₁² + (n₂−1)s₂²] / (n₁+n₂−2)
SE = √[sₚ²(1/n₁+1/n₂)]
t = [(x̄₁−x̄₂)−D₀] / SE
df = n₁+n₂−2

**Worked example:** For n₁=10, n₂=12, s₁=2, s₂=3: sₚ²=(9×4+11×9)/20=6.75 and SE≈1.1124. With means 15 and 12, t≈2.697 and df=20.

**MCQ trap:** sₚ² is a VARIANCE. If the problem gives SDs 2 and 3, square them to 4 and 9. Do not average SDs or forget the n−1 weights.

**Source:** Two Sample Means, slides 10–16

### Unknown and unequal variances: Welch

Welch uses each sample’s own variance in the SE rather than a pooled variance. Its adjusted df account for unequal variances and sample sizes; they are generally not n₁+n₂−2 and can be noninteger. Know which formula belongs to which assumption.

**Formula:** SE_W = √(s₁²/n₁+s₂²/n₂)
t_W = [(x̄₁−x̄₂)−D₀]/SE_W
df_W = (s₁²/n₁+s₂²/n₂)² / [(s₁²/n₁)²/(n₁−1)+(s₂²/n₂)²/(n₂−1)]

**Worked example:** For n₁=10, n₂=12, s₁=2, s₂=3, Welch SE≈1.0724 and adjusted df≈19.19. This differs from pooled SE≈1.1124 and df=20.

**MCQ trap:** Using the unpooled SE together with pooled df mixes two methods. Read whether equal variances are actually assumed.

**Source:** Two Sample Means, slides 9, 21–22

### Tails, critical values, and Excel

Hₐ determines the direction of the difference: >0, <0, or ≠0. For a two-sided test, compare |t| with the supplied positive t critical value or use a two-sided p-value. T.TEST works on raw data arrays: tails=1 or 2; type=2 for independent equal-variance t and type=3 for Welch. Type=1 is paired data, not this deck’s independent design.

**Formula:** Pooled two-sided critical value: =T.INV.2T(alpha,n₁+n₂−2)
Two-sided p-value from statistic: =T.DIST.2T(ABS(t),df)
Raw data: =T.TEST(array1,array2,2,2) [pooled]
Raw data: =T.TEST(array1,array2,2,3) [Welch]

**Worked example:** At t≈2.697, df=20, and supplied two-sided 5% cutoff 2.086, reject equality. A matching pooled 95% difference CI is 3±2.086(1.1124)≈(.679,5.321).

**MCQ trap:** The slides contain inconsistent labels/arithmetic in their worked example. Use the clearly stated SD-versus-variance definitions and correct formulas here. T.TEST syntax is an added Excel-recognition aid.

**Source:** Two Sample Means, slides 17–20; formula-recognition extension for T.TEST

## Chi-square: categories & expected counts

Work with category counts, calculate what H₀ predicts, and sum squared discrepancies. Distinguish one categorical variable from two.

### Which chi-square test?

Goodness of fit asks whether ONE categorical variable follows specified category proportions, such as equal brand preference or a fair die. Independence asks whether TWO categorical variables are associated in an r×c contingency table. For independence, H₀ says independent; Hₐ says associated/dependent.

**Formula:** Goodness of fit H₀: category proportions match the specified distribution
Independence H₀: the two categorical variables are independent

**Worked example:** Favorite brand alone across five brands → goodness of fit. Gender and favorite brand in a 2×3 table → independence.

**MCQ trap:** Two categorical variables are not two sample MEANS. A statistically significant association does not by itself establish causation.

**Source:** Chi Square Test of Independence, slides 3–6; Practice Exam, Q23–24, Q30

### Expected counts under H₀

Expected counts describe what the null predicts, not what you observed. For goodness of fit, multiply n by each hypothesized probability. For independence, expected cell count comes from its row and column totals; row and column proportions combine under independence. Use counts, not percentages, in the chi-square statistic.

**Formula:** Goodness of fit: Eᵢ=n×pᵢ₀
Independence: Eᵢⱼ=(row totalᵢ×column totalⱼ)/grand total

**Worked example:** A fair die rolled 180 times has expected count 30 per face. A table cell with row total 120, column total 80, grand total 400 has E=120×80/400=24.

**MCQ trap:** Expected does not mean an equal split unless H₀ actually specifies equal probabilities. Keep expected decimals until the final result.

**Source:** Chi Square Test of Independence, slides 8–9, 12–14, 17; Practice Exam, Q25, Q27

### The chi-square statistic and right-tail logic

Each contribution measures squared observed-minus-expected discrepancy relative to the expected count. Sum across ALL categories/cells. Large discrepancies produce a large χ² and evidence against H₀. Contributions are nonnegative, so the rejection region is always in the right tail.

**Formula:** χ² = Σ[(O−E)²/E]
Reject for χ² > supplied right-tail critical value

**Worked example:** If two categories have observed counts 60 and 40 with expected counts 50 and 50, χ²=(10²/50)+(−10)²/50=4. With df=1 and 5% cutoff 3.841, reject.

**MCQ trap:** Square O−E, then divide by E. Do not divide by O. An association alternative can be “two-sided” in ordinary language, but χ² itself still uses a right-tail probability.

**Source:** Chi Square Test of Independence, slides 8–11; Practice Exam, Q28

### Degrees of freedom and expected-count checks

For an r×c independence table, df=(r−1)(c−1). For a goodness-of-fit test with k categories and fully specified probabilities, df=k−1. The course requires all EXPECTED counts to be at least 5. Observations should be independent and categories mutually exclusive; normality of individual observations is not required.

**Formula:** Independence df=(r−1)(c−1)
Goodness of fit df=k−1 [no parameters estimated]
Course check: every E ≥ 5

**Worked example:** A 3×4 table has df=(3−1)(4−1)=6. Five equally preferred brands have df=4, not 5. Count table rows/columns without the totals row or column.

**MCQ trap:** The requirement is about expected counts, not every observed count. Totals are not extra categories.

**Source:** Chi Square Test of Independence, slides 10, 18; Practice Exam, Q24, Q26, Q29

### Excel and writing the conclusion

CHISQ.DIST.RT gives the p-value from an observed statistic and df. CHISQ.INV.RT gives a right-tail critical value from α and df. CHISQ.TEST uses observed and expected count ranges directly and returns a p-value. Compare that p-value to α and describe the specific category distribution or association.

**Formula:** p-value: =CHISQ.DIST.RT(statistic,df)
Critical value: =CHISQ.INV.RT(alpha,df)
Counts in ranges: =CHISQ.TEST(observed_range,expected_range)

**Worked example:** Five-category goodness of fit at 5% uses =CHISQ.INV.RT(0.05,4). If a 3×4 independence test rejects, say there is evidence the two categorical variables are associated.

**MCQ trap:** INV finds a cutoff from a probability; DIST finds a probability from a statistic. Failure to reject independence does not prove independence.

**Source:** Chi Square Test of Independence, slides 18–20; Practice Exam, Q24; CHISQ syntax is an Excel-recognition aid

## Excel recognition: translate the words into an area

| Task | Recognize this Excel pattern |
|---|---|
| Sample mean probability below a | NORM.DIST(a, μ, σ/SQRT(n), TRUE) |
| Sample mean probability above a | 1 − NORM.DIST(a, μ, σ/SQRT(n), TRUE) |
| Left-tail z p-value | NORM.S.DIST(z, TRUE) |
| Right-tail z p-value | 1 − NORM.S.DIST(z, TRUE) |
| Two-tail z p-value | 2*(1 − NORM.S.DIST(ABS(z), TRUE)) |
| Left-tail t p-value | T.DIST(t, df, TRUE) |
| Right-tail t p-value | 1 − T.DIST(t, df, TRUE) |
| Two-tail t p-value | T.DIST.2T(ABS(t), df) |
| Positive two-sided t critical value | T.INV.2T(α, df), equivalently T.INV(1−α/2, df) |
| Positive two-sided z critical value | NORM.S.INV(1−α/2) |
| χ² p-value | CHISQ.DIST.RT(statistic, df) |
| χ² critical value | CHISQ.INV.RT(α, df) |
| Paired / pooled / Welch two-sided t p-values | T.TEST(A, B, 2, type), type 1 / 2 / 3 respectively |

TRUE (or 1) means cumulative area in NORM.DIST/T.DIST. INV functions turn a probability into a critical statistic; DIST functions turn a statistic into a probability. For directional tests based on T.TEST, check whether the observed difference points toward Hₐ before halving a two-sided p-value.

## The five traps to know cold

- SD describes individuals; SE describes statistics across samples. Divide SD by √n, not n.

- Unknown σ means use t for usual inference about a mean, even when n ≥ 30; t approaches z as df grows.

- More confidence means a wider interval. More data means a narrower interval, all else equal.

- Hₐ determines the tail. A statistic pointing opposite a one-sided Hₐ produces a large p-value.

- Chi-square checks EXPECTED counts. GOF and independence use different df formulas.

## Corrections to the slides

1. **Hypothesis Testing, slide 32:** with p ≈ 0.0285 and α = 0.01, the correct comparison is p > 0.01, not p > 0.05. The slide's nonrejection decision at 1% is correct.
2. **Hypothesis Testing, slide 22:** at fixed α, increasing n generally reduces Type II error and increases power; the nominal Type I rate remains α. A larger sample does not automatically reduce both error rates at the same fixed threshold.
3. **Student_HT with Two Sample Means, slides 10–16:** some subscripts, SD/variance labels, and numerical substitutions are inconsistent. Use sₚ² = [(n₁−1)s₁² + (n₂−1)s₂²]/(n₁+n₂−2), with clear separation of SD s from variance s². Fresh worked examples in this tool use consistent inputs. The pooled estimator is not inherently biased just because sample sizes differ when the equal-population-variance model holds.
4. **Student_HT with Two Sample Means, slide 18:** “0.006 × 2 = 0.0012” is a decimal error. For the displayed t = 3.42 and df = 61, the two-sided p-value is about 0.00112. A rounded unshown statistic can give a slightly different value. It is still strongly significant at 5%.
5. **Confidence Intervals for Proportions, slide 5:** α = 1 − confidence **level**, not 1 − a confidence interval. A frequentist 95% procedure captures the fixed parameter in about 95% of repeated samples; it does not say 95% of individual observations lie in the interval.
6. **Sampling Distribution, slide 13:** n ≥ 30 is the course rule of thumb for CLT questions, not a universal guarantee of a nearly normal sampling distribution under every possible population shape.
7. **Proportion conditions:** the handwritten course slides use at least 5 successes and 5 failures per group. Many other courses use 10. This tool names the course convention where it matters; follow your instructor's stated rule on the exam. Chi-square also uses the course rule of expected count ≥ 5 in every cell.
8. **CI/test connection:** a matched two-sided test and CI can agree about whether a null value is plausible. With approximate proportions methods, a Wald CI and a null-based z test use different SEs and need not agree exactly at the boundary. Overlap of two separate group CIs does not establish that their difference is nonsignificant; analyze the CI/test for the difference directly.

The handwritten material in Chi Square Test of Independence slides 22–28 and CI Sigma Known and Unknown slides 8–10 was reviewed as images, not inferred from empty text extraction.

## Supplied practice exam — worked answer key

Try the supplied questions first. These are independently worked answers, not an official instructor key. Numbers refer to your uploaded practice PDF.

### Question 1: B — The distribution of sample means from all possible samples of a given size

A sampling distribution describes a statistic across repeated samples of the SAME size. Here the statistic is the sample mean, not the individual observations.

### Question 2: B — The sample size is large (typically n ≥ 30)

The course uses n ≥ 30 as a large-sample rule of thumb: sample means become approximately normal even when the population is not. Very severe skew or outliers can require larger n; 30 is not a universal guarantee.

### Question 3: A — σ / √n

SE(x̄) = σ/√n when population σ is known. It measures how much sample means vary across repeated samples. With unknown σ, estimate it using s/√n.

### Question 4: B — Decreases

SE = σ/√n. Increasing n increases the denominator, so SE decreases. Quadrupling n halves SE.

### Question 5: C — 2.5

SE = 20/√64 = 20/8 = 2.5. The population mean 100 is not needed for this calculation.

### Question 6: C — =1-NORM.DIST(33,30,12/SQRT(36),1)

For a sample mean use mean μ = 30 and SE = 12/√36 = 2. P(x̄ > 33) is the RIGHT tail: 1 − NORM.DIST(33,30,2,TRUE). Its z score is 1.5; the probability is about 0.0668. In these formulas 1 means TRUE (cumulative probability).

### Question 7: A — Its mean equals the population mean

The sampling distribution of x̄ is centered at μ: E(x̄) = μ. Its SD is σ/√n, and its shape is exactly normal for a normal population or approximately normal when a suitable CLT applies.

### Question 8: B — 95% of all possible samples would produce intervals containing the true population mean

A 95% confidence PROCEDURE produces intervals containing the fixed population mean in about 95% of repeated samples. For the realized interval, μ is fixed and the interval either covers it or does not. The conventional contextual wording is “we are 95% confident that μ is between 42 and 58.”

### Question 9: A — (14.81, 15.59)

σ is known, so use z*: SE = 1.4/√49 = 0.2. ME = 1.96(0.2) = 0.392. CI = 15.2 ± 0.392 = (14.808,15.592), rounded to (14.81,15.59).

### Question 10: A — (0.360, 0.440)

p̂ = 160/400 = 0.40. SE = √[0.4(0.6)/400] ≈ 0.02449. For 90%, z* = 1.645, so ME ≈ 0.04029. CI ≈ (0.3597,0.4403) → (0.360,0.440).

### Question 11: B — Wider

Higher confidence requires a larger multiplier: z* is 2.576 for 99% versus 1.960 for 95%. With the same data and SE, a larger multiplier gives a wider interval.

### Question 12: C — (3.035, 3.365)

σ is unknown: use t with df = 25 − 1 = 24. SE = 0.4/√25 = 0.08. ME = 2.064(0.08) = 0.16512. CI = 3.2 ± 0.16512 = (3.03488,3.36512) → (3.035,3.365).

### Question 13: D — All of the above

ME = z*σ/√n. Sample size changes the denominator; confidence level changes z*; population SD changes the numerator. All three affect the margin of error.

### Question 14: C — =T.INV.2T(0.10,19)

A 90% two-sided CI has α = 0.10 and df = n − 1 = 19. T.INV.2T takes the TOTAL probability across both tails: =T.INV.2T(0.10,19). Equivalent: =T.INV(0.95,19).

### Question 15: B — No effect or no difference

H₀ usually expresses a baseline of no effect or no difference, including equality at the test boundary. Hₐ expresses the directional or nondirectional effect you seek evidence for.

### Question 16: A — We reject H₀ when it is true

Type I = reject a TRUE H₀ (false alarm). Type II = fail to reject a FALSE H₀ (miss). The significance level α controls the nominal Type I error rate.

### Question 17: B — =1-T.DIST(2.10,24,1)

Hₐ: μ > 80 makes this a right-tailed t test. df = 25 − 1 = 24. The p-value is P(T₂₄ ≥ 2.10) = 1 − T.DIST(2.10,24,TRUE), about 0.0232.

### Question 18: A — Reject H₀

Compare p to α: 0.032 < 0.05, so reject H₀. This is evidence for Hₐ at the 5% level; it does not prove Hₐ or give the probability that H₀ is true.

### Question 19: B — Hₐ: μ < 50

To challenge the manufacturer’s claim “at least 50,” look for evidence of mean lifetime BELOW 50: Hₐ: μ < 50, with H₀: μ ≥ 50. Calculations use the boundary value μ₀ = 50.

### Question 20: D — 3.00

z = (x̄ − μ₀)/(σ/√n) = (28 − 25)/(6/√36) = 3/1 = 3.00. Treat 25 as the hypothesized population mean.

### Question 21: A — 1.00

t = (x̄ − μ₀)/(s/√n) = (18.5 − 18)/(2/√16) = 0.5/0.5 = 1.00, with df = 15.

### Question 22: B — =2*(1-NORM.S.DIST(1.75,1))

For a symmetric z distribution, the two-tailed p-value is 2P(Z ≥ |z|). With z = −1.75, use 2[1 − Φ(1.75)] ≈ 0.0801. Equivalent: 2Φ(−1.75).

### Question 23: B — Test whether a sample distribution matches an expected distribution

Goodness of fit compares observed counts for ONE categorical variable to specified expected proportions. Independence asks whether TWO categorical variables are associated.

### Question 24: B — =CHISQ.INV.RT(0.05,4)

With k = 5 categories and fully specified equal probabilities, goodness-of-fit df = k − 1 = 4. Chi-square rejection is always in the right tail, so the critical value is CHISQ.INV.RT(0.05,4) ≈ 9.488.

### Question 25: D — 30

A fair die assigns probability 1/6 to each of 6 faces. Expected count = n × probability = 180/6 = 30 per face.

### Question 26: B — 6

For independence, df = (r − 1)(c − 1) = (3 − 1)(4 − 1) = 2 × 3 = 6. Do not count row/column totals as categories.

### Question 27: B — 24

Under independence, E = (row total × column total)/grand total = (120 × 80)/400 = 24. Expected counts may be fractional; do not round prematurely.

### Question 28: A — Reject H₀

χ² tests reject in the right tail. Since 9.5 > 9.488, reject H₀ at α = 0.05. The closeness does not change the rule; use the supplied precision.

### Question 29: A — Expected frequencies should be at least 5 in all cells

Use the course condition: expected frequencies at least 5 in every cell, along with random/independent observations and categorical count data. This condition is about EXPECTED counts, not observed counts.

### Question 30: B — Chi-square test of independence

There are TWO categorical variables: gender and brand preference. To test association, use chi-square independence on the 2 × 3 count table. H₀: the variables are independent; Hₐ: they are associated.
