# Source notes and corrected traps

This study tool uses the supplied BUAD 310 practice exam and all six slide decks. The 30 supplied questions retain their original question and option order. Their answers are independently worked solutions, **not an official answer key**. Additional questions are original practice, not predictions of the actual exam.

## What the practice PDF establishes

- The real exam described in the PDF has 20 multiple-choice questions and a 70-minute limit. The supplied practice exam has 30 questions and describes itself as slightly easier.
- It tests both concepts and calculation, including recognizing Excel functions and arguments without using Excel during the exam.
- Printed references include z* values at 90%, 95%, and 99%, selected chi-square critical values, and any needed t-critical value within a question.
- The slides additionally cover two independent means, equal-variance pooling, Welch's method, and two-proportion inference. These are included even though the practice PDF does not directly exercise all of them.
- Mock-exam topic counts are a balanced study choice; the actual exam's topic distribution is unknown.

## Corrections and interpretation notes

1. **Hypothesis Testing, slide 32:** with p ≈ 0.0285 and α = 0.01, the correct comparison is p > 0.01, not p > 0.05. The slide's nonrejection decision at 1% is correct.
2. **Hypothesis Testing, slide 22:** at fixed α, increasing n generally reduces Type II error and increases power; the nominal Type I rate remains α. A larger sample does not automatically reduce both error rates at the same fixed threshold.
3. **Student_HT with Two Sample Means, slides 10–16:** some subscripts, SD/variance labels, and numerical substitutions are inconsistent. Use sₚ² = [(n₁−1)s₁² + (n₂−1)s₂²]/(n₁+n₂−2), with clear separation of SD s from variance s². Fresh worked examples in this tool use consistent inputs. The pooled estimator is not inherently biased just because sample sizes differ when the equal-population-variance model holds.
4. **Student_HT with Two Sample Means, slide 18:** “0.006 × 2 = 0.0012” is a decimal error. For the displayed t = 3.42 and df = 61, the two-sided p-value is about 0.00112. A rounded unshown statistic can give a slightly different value. It is still strongly significant at 5%.
5. **Confidence Intervals for Proportions, slide 5:** α = 1 − confidence **level**, not 1 − a confidence interval. A frequentist 95% procedure captures the fixed parameter in about 95% of repeated samples; it does not say 95% of individual observations lie in the interval.
6. **Sampling Distribution, slide 13:** n ≥ 30 is the course rule of thumb for CLT questions, not a universal guarantee of a nearly normal sampling distribution under every possible population shape.
7. **Proportion conditions:** the handwritten course slides use at least 5 successes and 5 failures per group. Many other courses use 10. This tool names the course convention where it matters; follow your instructor's stated rule on the exam. Chi-square also uses the course rule of expected count ≥ 5 in every cell.
8. **CI/test connection:** a matched two-sided test and CI can agree about whether a null value is plausible. With approximate proportions methods, a Wald CI and a null-based z test use different SEs and need not agree exactly at the boundary. Overlap of two separate group CIs does not establish that their difference is nonsignificant; analyze the CI/test for the difference directly.

The handwritten material in Chi Square Test of Independence slides 22–28 and CI Sigma Known and Unknown slides 8–10 was reviewed as images, not inferred from empty text extraction.
