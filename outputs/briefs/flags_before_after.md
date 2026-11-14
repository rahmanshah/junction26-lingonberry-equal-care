# Review flags across pipeline runs

- **Run 1**: 2026-11-14T12:27:00+00:00 · {'validated': 22} · 1 needed the retry
- **Run 2**: 2026-11-14T13:21:19+00:00 · {'validated': 22} · 6 needed the retry
- **Run 3 (final)**: 2026-11-14T14:03:30+00:00 · {'validated': 22} · 15 needed the retry

Causes are assigned by keyword rules on the flag text (`src/compare_flags.py`; first match wins). Flags come from the model review: for human review only, and not fully repeatable between runs.

## By cause

| Cause | Run 1 | Run 2 | Run 3 (final) | Change |
|---|---|---|---|---|
| Overlap caveat missing | 8 | 2 | 0 | -8 |
| ~20% clinical-diagnosis claim read as imaging | 7 | 1 | 2 | -5 |
| No-record share read as recording completeness | 7 | 1 | 0 | -7 |
| Stage vs age-adjustment wording | 5 | 6 | 1 | -4 |
| Plan attribution, dates or verb | 7 | 22 | 4 | -3 |
| Other | 7 | 13 | 17 | +10 |
| **Total** | **41** | **45** | **24** | **-17** |

## By severity

| Severity | Run 1 | Run 2 | Run 3 (final) |
|---|---|---|---|
| high | 0 | 1 | 0 |
| medium | 25 | 28 | 11 |
| low | 16 | 16 | 13 |

## By county (flags)

| County | Run 1 | Run 2 | Run 3 (final) | Status (last) | Attempts (last) |
|---|---|---|---|---|---|
| Etelä-Karjala | 3 | 3 | 2 | validated | 2 |
| Helsinki | 2 | 4 | 0 | validated | 2 |
| Itä-Uusimaa | 3 | 4 | 1 | validated | 1 |
| Keski-Uusimaa | 4 | 4 | 3 | validated | 1 |
| Kymenlaakso | 2 | 2 | 0 | validated | 2 |
| Länsi-Uusimaa | 2 | 0 | 0 | validated | 2 |
| Päijät-Häme | 2 | 2 | 0 | validated | 1 |
| Vantaa ja Kerava | 2 | 1 | 0 | validated | 1 |
| Etelä-Savo | 0 | 3 | 2 | validated | 2 |
| Keski-Suomi | 1 | 1 | 0 | validated | 1 |
| Pohjois-Karjala | 0 | 3 | 1 | validated | 2 |
| Pohjois-Savo | 1 | 2 | 1 | validated | 2 |
| Pohjanmaa | 0 | 0 | 0 | validated | 2 |
| Satakunta | 2 | 3 | 1 | validated | 1 |
| Varsinais-Suomi | 6 | 1 | 3 | validated | 2 |
| Kainuu | 0 | 0 | 3 | validated | 2 |
| Keski-Pohjanmaa | 4 | 5 | 0 | validated | 2 |
| Lappi | 0 | 2 | 1 | validated | 2 |
| Pohjois-Pohjanmaa | 0 | 1 | 1 | validated | 2 |
| Etelä-Pohjanmaa | 4 | 1 | 0 | validated | 2 |
| Kanta-Häme | 2 | 1 | 3 | validated | 1 |
| Pirkanmaa | 1 | 2 | 2 | validated | 2 |

## All flags in the last run (Run 3 (final))

**~20% clinical-diagnosis claim read as imaging** (2)

- [low] Itä-Uusimaa, `how_sure_are_we.details[2]`: The cited claims (bs:coverage:Imaging, q:5eb155decc) state that approximately 20% of patients are diagnosed on clinical examination or findings alone (such as imaging), not that imaging specifically is the diagnosis basis in approximately 20% of patients.
- [low] Varsinais-Suomi, `how_sure_are_we.details[2]`: Minor imprecision: bs:coverage:Imaging and q:5eb155decc state that about 20% of patients are diagnosed on clinical findings/examination alone (such as imaging), not specifically that imaging appears as clinical diagnosis in about 20% of cases.

**Stage vs age-adjustment wording** (1)

- [medium] Pirkanmaa, `where_we_lag.headline`: Overreach: exceeding national crude treatment shares (which are not age- or stage-adjusted, and without citing no-treatment-record data) does not establish that Pirkanmaa's pathway gaps are solely the two documentation omissions in regional pathway documents, as actual waiting times and other pathway stages are not covered by the cited claims.

**Plan attribution, dates or verb** (4)

- [medium] Keski-Uusimaa, `what_to_do_first.details[3]`: Overreaches on STM roadmap measures 3.1.2 and 2.5.2: the cited claims specify that in 2026–2028 they cover only five (unnamed) cancers (3.1.2) or at least the five most common cancers (2.5.2), and that the 2029–2031 milestone for those two measures is extending them to all significant cancers; 'county adoption by 2029–2031' is stated in the cited claims only for measure 1.2.3 (care-coordinator guidance).
- [medium] Kainuu, `how_sure_are_we.details[1]`: Asserts a causal link ('so') between having no cancer quality registry (filha:registry, q:47c7e11303) and lung cancer data reporting, collection and storage being incomplete (q:950a2f797b); the cited claims state both facts separately without establishing causation.
- [medium] Lappi, `what_to_do_first.details[3]`: For STM roadmap measure 2.5.2, the cited claim notes specify that standardised referral criteria and symptom-based models are planned in the national pathways of at least the five most common cancers by 2026–2028 (and for all significant cancers by 2029–2031). Omitting this scope qualifier overstates what is planned by 2026–2028.
- [medium] Kanta-Häme, `what_to_do_first.details[3]`: Missing scope caveat for the 2026–2028 milestone: measures 2.5.2 and 3.1.2 cover only at least the five most common cancers (2.5.2) and five unnamed cancers (3.1.2) by 2026–2028, before expanding to all significant cancers by 2029–2031.

**Other** (17)

- [low] Etelä-Karjala, `what_to_do_first.headline`: Cited claim rec:3 recommends reporting and publishing recording completeness per county for stage, drug treatment, and MDT coding, rather than auditing it.
- [low] Etelä-Karjala, `what_to_do_first.details[0]`: Cited claims bs:coverage:Diagnosis and q:7885b0974f report that stage at diagnosis is missing for nearly half (~48%) of new patients nationally, whereas writing 'plus 48% missing stage' immediately after Etelä-Karjala's county shares omits the approximation ('about'/'~') and does not clarify that the figure is national.
- [low] Keski-Uusimaa, `how_sure_are_we.headline`: Claim fig:age_adjusted_only_kuva16 states that county-level age-adjusted treatment shares do appear in Kuva 16 (by sex, as a PNG figure) and that only the county table (Taulukko 11) gives crude shares only; saying 'county treatment shares are crude' without specifying Taulukko 11 slightly overgeneralizes.
- [low] Keski-Uusimaa, `what_to_do_first.headline`: Claim rec:3 recommends publishing per county how completely stage, drug treatment, and MDT meetings are recorded (recording completeness), whereas 'how stage, drug therapy, and MDT meetings are coded' imprecisely shifts the focus from recording completeness per county to coding methods.
- [medium] Etelä-Savo, `where_we_lag.details[1]`: Causal overreach: saying Etelä-Savo's crude shares are above national benchmarks 'Because treatment categories overlap and a patient can receive several types' asserts a cause not supported by the cited claims, as overlapping categories apply to both county and national figures.
- [low] Etelä-Savo, `what_to_do_first.headline`: Minor overreach in verb choice: rec:3 recommends reporting and publishing recording completeness per county, not 'auditing' it.
- [medium] Pohjois-Karjala, `where_we_lag.details[1]`: The cited claim (cty:symptomatic:Pohjois_Karjalan_hyvinvointialue) requires noting that treatment categories overlap, which is omitted here.
- [medium] Pohjois-Savo, `how_sure_are_we.details[0]`: The cited claims do not mention curative treatment shares or recording artefacts for curative treatment, and in Pohjois-Savo the curative treatment share (24.5%, 95% CI 21.3–28.0) is not distinguishable from the national share (27.0%), making the reference to 'a low curative share' unsupported by the cited claims and potentially misleading.
- [medium] Satakunta, `where_we_lag.headline`: Causal overreach: [reg:satakunta_study] states that the biggest delay from referral to diagnosis occurred in specialist care ('biggest delay in specialist care'), not that specialist care caused the delay.
- [low] Varsinais-Suomi, `how_sure_are_we.headline`: The claim that public data omit pre-diagnostic pathways (plural) goes beyond the cited claims: only bs:coverage:Referral is cited for the pre-diagnostic phase, without citing bs:coverage:Symptoms or bs:coverage:Primary_care_occupational_health.
- [medium] Varsinais-Suomi, `what_to_do_first.details[2]`: Overreach / missing scope caveat: saying the normal X-ray rule is featured 'only in KYS's pathway document' omits that only 5 regional pathways were reviewed (not all 22 areas), as noted in reg:only_kys_xray ('scope: the named region's own document only; not evidence about any other county; 5 regional pathways reviewed, not all 22 areas').
- [low] Kainuu, `how_sure_are_we.headline`: Claim fig:age_adjusted_only_kuva16 states that county-level age-adjusted treatment shares do appear in Kuva 16 (while Taulukko 11 gives crude shares only), so stating unqualifiedly that county treatment shares are not age-adjusted is imprecise.
- [low] Kainuu, `what_to_do_first.headline`: Claim rec:3 recommends publishing per county how completely stage, drug treatment and MDT meetings are recorded ('recording completeness'), not 'coding data'.
- [low] Pohjois-Pohjanmaa, `how_sure_are_we.headline`: The cited claims do not say that public registry data provide 95% confidence intervals for crude 12-month treatment shares; fig:age_adjusted_only_kuva16 states that Taulukko 11 gives crude shares only (while Kuva 16 has 95% CIs for age-adjusted shares). In addition, the cited claims only support missing treatment start dates rather than pathway wait times overall.
- [medium] Kanta-Häme, `where_we_lag.details[2]`: Unsupported causal claim: the sentence states that the 95% confidence intervals include the national values 'Because the treatment categories overlap', whereas the overlap of treatment categories does not cause the confidence intervals to include the national values.
- [low] Kanta-Häme, `how_sure_are_we.headline`: Slight overstatement: according to fig:age_adjusted_only_kuva16, county-level age-adjusted treatment shares do appear in Kuva 16 (as a PNG figure by sex); only the county table (Taulukko 11) lacks age adjustment.
- [low] Pirkanmaa, `what_to_do_first.headline`: Minor imprecision: the cited claims do not support standardising referrals and diagnostic contacts 'from regional pathway documents'—reg:named_contact states that no region names a diagnostic-phase contact person in its pathway document, and rec:2 models the referral template on KYS rather than drawing it from regional pathway documents.

