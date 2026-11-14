# Brief generation: all counties

Run 2026-11-14T13:21:19+00:00 · {'validated': 22}

| County | Status | Attempts | Remaining problems | Flags (high / medium / low) |
|---|---|---|---|---|
| Etelä-Karjala | validated | 2 | 0 | 1 / 2 / 0 |
| Helsinki | validated | 1 | 0 | 0 / 2 / 2 |
| Itä-Uusimaa | validated | 2 | 0 | 0 / 1 / 3 |
| Keski-Uusimaa | validated | 1 | 0 | 0 / 3 / 1 |
| Kymenlaakso | validated | 1 | 0 | 0 / 1 / 1 |
| Länsi-Uusimaa | validated | 1 | 0 | 0 / 0 / 0 |
| Päijät-Häme | validated | 1 | 0 | 0 / 2 / 0 |
| Vantaa ja Kerava | validated | 2 | 0 | 0 / 0 / 1 |
| Etelä-Savo | validated | 1 | 0 | 0 / 2 / 1 |
| Keski-Suomi | validated | 1 | 0 | 0 / 0 / 1 |
| Pohjois-Karjala | validated | 1 | 0 | 0 / 3 / 0 |
| Pohjois-Savo | validated | 2 | 0 | 0 / 1 / 1 |
| Pohjanmaa | validated | 1 | 0 | 0 / 0 / 0 |
| Satakunta | validated | 1 | 0 | 0 / 3 / 0 |
| Varsinais-Suomi | validated | 2 | 0 | 0 / 1 / 0 |
| Kainuu | validated | 1 | 0 | 0 / 0 / 0 |
| Keski-Pohjanmaa | validated | 1 | 0 | 0 / 3 / 2 |
| Lappi | validated | 2 | 0 | 0 / 0 / 2 |
| Pohjois-Pohjanmaa | validated | 1 | 0 | 0 / 1 / 0 |
| Etelä-Pohjanmaa | validated | 1 | 0 | 0 / 1 / 0 |
| Kanta-Häme | validated | 1 | 0 | 0 / 0 / 1 |
| Pirkanmaa | validated | 1 | 0 | 0 / 2 / 0 |

## Review flags (for human review only)

**Etelä-Karjala**

- [medium] `how_sure_are_we.details[3]`: Overreach: the cited Yle MOT claims state that the figures are national averages and not county-specific, which does not support the universal claim that no county-specific wait times exist.
- [medium] `what_to_do_first.details[2]`: Unsupported statement: the cited claim [q:1b9eaf2217] only translates the phrase 'in the organisation of treatment responsibility' ('hoitovastuun järjestämisessä') and does not state that treatment responsibility organisation varies regionally.
- [high] `what_to_do_first.details[3]`: Misstated milestones and missing scope caveats: under measure 3.2.1 ([q:f07a34a300], [q:4a856bd695]), only the registry decree is scheduled to be updated by 2026–2028 (not the quality registry itself) and the 2029–2031 milestone is annual reports for at least five cancers (no timeframe is given for 90% coverage); additionally, measures 3.1.2 and 2.5.2 in 2026–2028 apply only to five cancers (unnamed or most common), not all cancers.

**Helsinki**

- [medium] `how_sure_are_we.headline`: None of the cited claims state that county treatment shares are crude or not age-adjusted (only a national age-adjusted reference line for men's curative treatment and missing-stage claims are cited), and the cited diagnosis claim states specifically that curative shares cannot be stage-adjusted rather than all county treatment shares.
- [medium] `how_sure_are_we.details[1]`: The cited claims only provide the national age-adjusted reference lines from Kuva 16 for curative treatment by sex; they do not establish that age-adjusted values exist nowhere else in the report, nor do they mention Helsinki, its crude curative difference, or the absence of a county Kuva 16 figure.
- [low] `what_to_do_first.details[0]`: In the cited notes for STM roadmap measure 3.2.1, the 2029–2031 deadline applies to annual reports for at least five cancers, not specifically to the 90% coverage indicator.
- [low] `what_to_do_first.details[3]`: Conflates the timelines of STM roadmap measures 2.5.2 and 1.2.3: county adoption by 2029–2031 applies to measure 1.2.3 (care-coordinator guidance), whereas measure 2.5.2 plans standardised referral criteria in national pathways for at least the five most common cancers by 2026–2028 and all significant cancers by 2029–2031.

**Itä-Uusimaa**

- [low] `what_to_do_first.headline`: Claim rec:3 recommends publishing/reporting per-county recording completeness for stage, drug treatment, and MDT coding—not 'auditing', and specifically 'drug treatment' rather than 'treatment' in general.
- [low] `what_to_do_first.details[0]`: Under STM roadmap measure 3.2.1, the 2029–2031 milestone is annual reports for at least five cancers, whereas the 90% data coverage indicator applies to the quality registry's data base rather than the annual reports.
- [medium] `what_to_do_first.details[1]`: STM roadmap measure 3.1.2 plans cancer-specific access times only for five (unnamed) cancers by 2026–2028 (with all significant cancers following by 2029–2031); omitting this scope restriction overstates what is planned by 2026–2028.
- [low] `what_to_do_first.details[2]`: STM roadmap measure 2.5.2 plans standardised referral criteria for at least the five most common cancers by 2026–2028 (and all significant cancers by 2029–2031), rather than for all cancers by 2026–2028.

**Keski-Uusimaa**

- [medium] `where_we_lag.headline`: The claim that Keski-Uusimaa lags the national benchmark only in recorded MDT meetings is not supported by the two cited claims, which cover only MDT recording and provide no information about other treatment categories or indicators.
- [medium] `how_sure_are_we.headline`: None of the cited claims mention age adjustment or that county treatment shares are crude, and bs:coverage:Diagnosis states only that curative shares cannot be stage-adjusted rather than all treatment shares.
- [low] `what_to_do_first.details[1]`: Omits that the 2026–2028 milestone in STM roadmap measure 3.1.2 covers only five unnamed cancers, which makes the 2026–2028 target appear broader than the cited claims support.
- [medium] `what_to_do_first.details[2]`: Stating that regional pathway documents show only KYS provides these features omits the scope caveat in reg:only_kys_xray that only 5 regional pathways were reviewed, not all 22 areas.

**Kymenlaakso**

- [medium] `what_to_do_first.details[0]`: The cited claims for STM roadmap measure 3.1.2 state that national pathway descriptions and cancer-specific access-to-care times by 2026–2028 are planned only for five (unnamed) cancers (with all significant cancers by 2029–2031), so omitting that scope overreaches by implying general or lung-cancer target access times by 2026–2028.
- [low] `what_to_do_first.details[2]`: The cited claims state that under measure 3.2.1 annual reports for at least five cancers are planned by 2029–2031 and that the planned registry has an indicator of 90% coverage including stage, but do not state that 90% coverage will be achieved by 2029–2031.

**Päijät-Häme**

- [medium] `where_we_lag.details[1]`: Unsupported causal claim (overreach): the sentence states that Päijät-Häme's crude shares are above national levels 'Because treatment categories overlap', whereas the cited claims only note that categories overlap for both county and national figures and do not support overlapping categories as the cause of the county exceeding national shares.
- [medium] `what_to_do_first.details[1]`: Overreach / missing scope qualifier: the cited STM roadmap claims (q:def306014c, q:b326e35410) state that measure 3.1.2 plans national pathway descriptions and cancer-specific access times for five (unnamed) cancers by 2026–2028 (and all significant cancers by 2029–2031), not for lung cancer or all cancers generally by 2026–2028.

**Vantaa ja Kerava**

- [low] `how_sure_are_we.headline`: None of the claims cited in this sentence mention that county treatment shares are crude or lack age adjustment (which come from the county treatment and Kuva 16 claims not cited here); additionally, bs:coverage:Diagnosis states that curative shares cannot be stage-adjusted, rather than county treatment shares in general.

**Etelä-Savo**

- [medium] `what_to_do_first.details[0]`: The cited claims for STM roadmap measure 3.2.1 state that the 90% target is for the quality registry's overall data coverage (including stage information), not specifically '90% stage coverage', and they assign the 2029–2031 timeframe to annual reports for at least five cancers rather than to achieving 90% coverage.
- [low] `what_to_do_first.details[1]`: The cited claims specify that STM roadmap measure 3.1.2 plans national pathway descriptions and access times by 2026–2028 only for five (unnamed) cancers before covering all significant cancers by 2029–2031, which is omitted in the 2026–2028 clause.
- [medium] `what_to_do_first.details[3]`: The cited claims specify that STM roadmap measure 2.5.2 includes standardised referral criteria and symptom-based models by 2026–2028 only in the national pathways of at least the five most common cancers (with all significant cancers by 2029–2031), so stating this without the cancer-scope limitation overstates what is planned for 2026–2028.

**Keski-Suomi**

- [low] `how_sure_are_we.headline`: None of the claims cited for this sentence mention that county treatment shares are crude or unadjusted for age (only stage adjustment is supported by bs:coverage:Diagnosis); the crude and age-adjustment claims are cited in details[0] rather than here.

**Pohjois-Karjala**

- [medium] `what_to_do_first.details[0]`: Overreaches the STM roadmap claims (q:def306014c, q:b326e35410): measure 3.1.2 plans national pathway descriptions and access times by 2026–2028 only for five (unnamed) cancers, and for all significant cancers by 2029–2031.
- [medium] `what_to_do_first.details[1]`: Missing scope qualifier on STM roadmap measure 2.5.2 (q:c61439b30f, q:37bb4c3b38): the 2026–2028 target covers at least the five most common cancers (all significant cancers by 2029–2031), and for measure 1.2.3 (q:abcbb06ae3, q:050ee09ebe) county adoption is planned for 2029–2031 with the care phase left unspecified.
- [medium] `what_to_do_first.details[2]`: Overreaches STM roadmap scope and blurs national vs county scope: measure 3.1.2 (q:990a0d39a0) by 2026–2028 applies only to five unnamed cancers (all significant cancers by 2029–2031) and measure 3.2.1 (q:f07a34a300) annual reports by 2029–2031 cover at least five cancers; additionally, the ~48% missing stage figure (bs:coverage:Diagnosis, q:7885b0974f) is a national report-wide figure rather than established for Pohjois-Karjala specifically.

**Pohjois-Savo**

- [medium] `how_sure_are_we.headline`: Overreach: the cited claim (cty:no_treatment_record:Pohjois_Savon_hyvinvointialue) only shows that Pohjois-Savo's crude share with no treatment record within 12 months (19.3%, 95% CI 16.5–22.6) is lower than the national share (27.5%). Because 'no treatment record' mixes untreated patients and unrecorded treatment, a lower share relative to the national benchmark does not directly establish 'relatively complete treatment recording' as a supported finding rather than a cautious inference.
- [low] `what_to_do_first.details[0]`: Minor imprecision: the cited STM roadmap claims attach the 2029–2031 timeline to annual reports for at least five cancers rather than specifying 2029–2031 as the deadline for the 90% coverage indicator, and the 90% target refers to the registry's overall data coverage (including stage) rather than stage coverage alone.

**Satakunta**

- [medium] `where_we_lag.details[0]`: Missing caveat: the cited claim [cty:curative:Satakunnan_hyvinvointialue] notes that treatment categories overlap, which is not stated in this sentence.
- [medium] `what_to_do_first.details[0]`: Overreach: [rec:1] recommends reporting lung cancer access times using THL Ohjaus 21/2016 definitions, whereas [thl:21_2016] states that THL Ohjaus 21/2016 defines how access times are recorded for 16 cancers; the team did not recommend reporting all 16 cancers.
- [medium] `what_to_do_first.details[2]`: Misleading timeline and missing caveat: [q:f07a34a300] notes that STM roadmap measure 3.2.1 updates the registry decree by 2026–2028 and schedules annual reports for at least five cancers by 2029–2031, rather than completing the national quality registry itself by 2026–2028; also [cty:mdt_recorded:Satakunnan_hyvinvointialue] notes that categories overlap, which is omitted.

**Varsinais-Suomi**

- [medium] `what_to_do_first.details[1]`: Overreaches the cited STM roadmap claims (q:ed87906241, q:0c7bf2dacb) by stating measure 3.1.2 plans national pathways by 2026–2028 without noting that the 2026–2028 target applies only to five unnamed cancers, while pathways for all significant cancers are planned for 2029–2031.

**Keski-Pohjanmaa**

- [low] `how_sure_are_we.details[0]`: The cited claims state that Kuva 16 covers age-adjusted curative treatment by sex, not that age-adjusted values exist only in Kuva 16.
- [low] `how_sure_are_we.details[2]`: The cited claims state that diagnosis is based on clinical examination or findings alone, such as imaging, in about 20% of patients, rather than imaging specifically being the basis in all 20%.
- [medium] `what_to_do_first.details[0]`: The cited claims state that measure 3.2.1 plans annual reports for at least five cancers by 2029–2031 and mentions 90% data coverage, but do not state that 90% coverage is scheduled specifically by 2029–2031; also states 48% missing stage without the qualifier 'about' or 'nearly half'.
- [medium] `what_to_do_first.details[1]`: Omits the scope caveat that measure 3.1.2's 2026–2028 milestone covers only five unnamed cancers, not national pathways and access times in general.
- [medium] `what_to_do_first.details[3]`: Omits the scope caveat that measure 2.5.2's 2026–2028 milestone applies to the national pathways of at least the five most common cancers (with all significant cancers by 2029–2031).

**Lappi**

- [low] `what_to_do_first.headline`: Team recommendation 3 ([rec:3]) recommends reporting and publishing county-level recording completeness for stage, drug treatment, and MDT coding, not auditing recording completeness for crude treatment shares.
- [low] `what_to_do_first.details[0]`: The cited claims ([bs:coverage:Diagnosis] and [q:7885b0974f]) state that stage at diagnosis is missing for 'nearly half' (~48%) of new patients, whereas '48% missing stage' omits the approximation.

**Pohjois-Pohjanmaa**

- [medium] `how_sure_are_we.headline`: The claim that public report data lack age adjustments is not supported by any of the cited claims (which cover diagnosis concordance, stage missingness, referral, and treatment start only), and overreaches since Kuva 16 of the public report does include age-adjusted curative treatment figures by sex (though not county values for Pohjois-Pohjanmaa).

**Etelä-Pohjanmaa**

- [medium] `what_to_do_first.details[2]`: The cited claims state that the 2029–2031 timeframe in STM roadmap measure 3.2.1 applies to publishing annual reports for at least five cancers, whereas the 90% data coverage target in q:4a856bd695 is stated without a 2029–2031 deadline.

**Kanta-Häme**

- [low] `how_sure_are_we.headline`: The cited claims ([lit:hilmo_90], [bs:coverage:Diagnosis], [bs:coverage:Treatment_start]) support diagnosis concordance, missing stage (~48%, preventing stage adjustment of curative shares), and missing treatment start dates, but none of the cited claims state that table treatment shares lack age adjustment or that pathway timestamps beyond treatment start are omitted.

**Pirkanmaa**

- [medium] `where_we_lag.headline`: Overreach: claim reg:not_monitored states that no region says in its pathway document whether it meets its stated times, which shows a lack of public reporting rather than proving that the county does not monitor target times internally.
- [medium] `where_we_lag.details[2]`: Overreach: calling the stated times 'unmonitored targets' goes beyond claim reg:not_monitored, which only supports that no region says in its pathway document whether it meets its stated times.

