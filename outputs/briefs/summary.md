# Brief generation: all counties

Run 2026-11-14T12:27:00+00:00 · {'validated': 22}

| County | Status | Attempts | Remaining problems | Flags (high / medium / low) |
|---|---|---|---|---|
| Etelä-Karjala | validated | 1 | 0 | 0 / 2 / 1 |
| Helsinki | validated | 1 | 0 | 0 / 2 / 0 |
| Itä-Uusimaa | validated | 1 | 0 | 0 / 2 / 1 |
| Keski-Uusimaa | validated | 1 | 0 | 0 / 2 / 2 |
| Kymenlaakso | validated | 1 | 0 | 0 / 1 / 1 |
| Länsi-Uusimaa | validated | 1 | 0 | 0 / 0 / 2 |
| Päijät-Häme | validated | 1 | 0 | 0 / 2 / 0 |
| Vantaa ja Kerava | validated | 1 | 0 | 0 / 0 / 2 |
| Etelä-Savo | validated | 1 | 0 | 0 / 0 / 0 |
| Keski-Suomi | validated | 1 | 0 | 0 / 0 / 1 |
| Pohjois-Karjala | validated | 1 | 0 | 0 / 0 / 0 |
| Pohjois-Savo | validated | 1 | 0 | 0 / 1 / 0 |
| Pohjanmaa | validated | 1 | 0 | 0 / 0 / 0 |
| Satakunta | validated | 1 | 0 | 0 / 2 / 0 |
| Varsinais-Suomi | validated | 1 | 0 | 0 / 4 / 2 |
| Kainuu | validated | 1 | 0 | 0 / 0 / 0 |
| Keski-Pohjanmaa | validated | 1 | 0 | 0 / 2 / 2 |
| Lappi | validated | 1 | 0 | 0 / 0 / 0 |
| Pohjois-Pohjanmaa | validated | 1 | 0 | 0 / 0 / 0 |
| Etelä-Pohjanmaa | validated | 1 | 0 | 0 / 2 / 2 |
| Kanta-Häme | validated | 2 | 0 | 0 / 2 / 0 |
| Pirkanmaa | validated | 1 | 0 | 0 / 1 / 0 |

## Review flags (for human review only)

**Etelä-Karjala**

- [medium] `how_sure_are_we.details[1]`: None of the cited claims state that the county shares are crude or not age-adjusted, and missing stage data (~48% nationally) only explains why shares cannot be stage-adjusted, not why they are unadjusted for age.
- [medium] `what_to_do_first.headline`: The cited recommendation claims (rec:3, rec:1, rec:2) do not state that recording-completeness reporting should be prioritised over the other two recommendations; rec:3 only advises reading county gaps in those fields as data-quality signals first.
- [low] `what_to_do_first.details[2]`: According to the cited claims, only the care-coordinator guidance leaves the care phase open (q:050ee09ebe), whereas the standardised referral criteria plans (q:9a1cd194f5, q:c61439b30f) specifically concern transfer to specialist care and diagnostic tests; grouping both under 'leave the care phase open' is imprecise.

**Helsinki**

- [medium] `how_sure_are_we.headline`: Overreaches and partly contradicts the cited claims: bs:coverage:Diagnosis explicitly states that the registry records the diagnosis date ('Registry diagnosis date'), so saying public registry data do not capture 'pathway dates' is inaccurate; additionally, bs:coverage:Primary_care_occupational_health states that primary care visits are not included in the report's data and occupational health is not mentioned in the report (rather than claiming that no public registry data capture pre-specialist care).
- [medium] `how_sure_are_we.details[1]`: None of the cited claims support the statement that 'no age-adjusted county value is provided'; k16:curative:men:national and k16:curative:women:national only report the digitised national reference lines from Kuva 16 and say nothing about whether age-adjusted county values are provided.

**Itä-Uusimaa**

- [low] `how_sure_are_we.headline`: Claim [bs:coverage:Primary_care_occupational_health] specifies that primary care visits are 'not included in the report's data' (and explicitly warns never to say 'excluded'), rather than being omitted from public data generally.
- [medium] `how_sure_are_we.details[0]`: Claim [cty:no_treatment_record:Itä_Uudenmaan_hyvinvointialue] states that Itä-Uusimaa's 31.6% (95% CI 26.4–37.4) no-treatment-record share is 'not distinguishable vs national 27.5%'. Calling it 'above-national' without noting that its confidence interval includes the national benchmark overstates the comparison.
- [medium] `what_to_do_first.details[1]`: Claims [q:def306014c] and [q:b326e35410] specify that the 2026–2028 roadmap target covers national care pathway descriptions and access-to-care times for five unnamed cancers, not cancer pathways in general or lung cancer specifically.

**Keski-Uusimaa**

- [medium] `how_sure_are_we.headline`: Overreach: the cited claim [cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue] states that 26.4% (95% CI 22.7–30.5) is not distinguishable from the national 27.5%, and [bs:coverage:Treatment_start] notes that the 27.5% share mixes untreated patients with unrecorded treatment; neither claim supports the conclusion that 26.4% versus 27.5% suggests relatively complete treatment recording.
- [medium] `how_sure_are_we.details[0]`: Overreach: even framed as an inference, the cited claims do not support treating the county figure as a signal below 27.5% or consistent with relatively complete treatment recording, since [cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue] states it is not distinguishable from 27.5% and [bs:coverage:Treatment_start] notes that the 27.5% rate mixes untreated patients and unrecorded treatment.
- [low] `how_sure_are_we.details[3]`: Minor imprecision in measure: [bs:coverage:Imaging] and [q:5eb155decc] state that approximately 20% is the share based on clinical examination alone, such as imaging, rather than imaging alone.
- [low] `what_to_do_first.details[1]`: Plan presented with certainty: stating that the Filha programme's diagnostics guideline "is due" before the 2030 interim evaluation frames a future programme plan from [q:8f358a9de6] and [q:614febebf2] as a fixed deadline rather than something the programme plans or intends.

**Kymenlaakso**

- [low] `how_sure_are_we.headline`: Claim [bs:coverage:Diagnosis] states that stage at diagnosis is missing for nearly half (~48%) of new patients, preventing stage adjustment, rather than being completely unmeasured.
- [medium] `what_to_do_first.details[2]`: The sentence attributes uniform recording instructions to what the Cancer strategy implementation roadmap plans, whereas [q:82d365cd2c] is from the Filha National Lung Cancer Programme 2026–2035 and states that uniform recording instructions must be ensured.

**Länsi-Uusimaa**

- [low] `how_sure_are_we.details[0]`: The cited claims state that missing stage at diagnosis (~48%) prevents stage adjustment of curative shares, not that it is the reason county treatment shares are not age-adjusted.
- [low] `how_sure_are_we.details[2]`: According to the cited quote q:5eb155decc, approximately 20% refers to clinical examination alone (such as imaging), rather than imaging specifically.

**Päijät-Häme**

- [medium] `where_we_lag.details[1]`: Missing required caveat from the cited county claims: the three treatment categories overlap (they sum to 124.9%), and the sentence does not note that categories overlap (or that the shares are not age- or stage-adjusted).
- [medium] `how_sure_are_we.details[1]`: Missing required caveat from the cited county claims: the listed categories overlap (life-prolonging, symptomatic, no-treatment-record, and MDT-recorded are not mutually exclusive), which is omitted from the sentence.

**Vantaa ja Kerava**

- [low] `how_sure_are_we.details[0]`: Missing stage (~48%) explains why shares cannot be stage-adjusted, not why they are unadjusted for age; also, Kuva 16 is a figure from which the national reference lines were digitised rather than Kuva 16 providing only national reference lines.
- [low] `what_to_do_first.details[2]`: The cited roadmap claims specify 2029–2031 county adoption only for the coordinator guidance (q:abcbb06ae3), not for the national pathways (q:def306014c) or referral criteria (q:c61439b30f), which also specifically apply to five or at least the five most common cancers.

**Keski-Suomi**

- [low] `how_sure_are_we.details[2]`: The cited quote (q:5eb155decc) attributes the approximately 20% share to clinical examination alone, giving imaging as an example ('clinical examination alone, such as imaging, in approximately 20%'), rather than to imaging specifically.

**Pohjois-Savo**

- [medium] `how_sure_are_we.headline`: The cited claims only give the county and national no-treatment-record shares and stage missingness; they do not establish that a lower no-treatment-record share indicates relatively complete treatment recording. Because the indicator mixes untreated patients and unrecorded treatment, presenting this inference as what the data suggest without that caveat is an overreach.

**Satakunta**

- [medium] `how_sure_are_we.details[3]`: Attaches 'approximately 20% of diagnoses' to imaging in general, whereas bs:coverage:Imaging and q:5eb155decc state that approximately 20% of diagnoses are based on clinical examination alone, such as imaging.
- [medium] `what_to_do_first.details[1]`: Uses the wrong verb ('completed') for the Filha programme's recommendation: q:614febebf2 states that the sub-area recommendations will be implemented ('toteutetaan') before the 2030 interim evaluation, and q:432c0e51d6 only says the upcoming recommendation is due before the 2030 mid-term evaluation.

**Varsinais-Suomi**

- [medium] `where_we_lag.headline`: Missing required caveat from the cited claims: the listed treatment and recording categories overlap (patients can fall into more than one category), and the county shares are not age- or stage-adjusted.
- [medium] `where_we_lag.details[2]`: Missing required caveat from the cited claims that the treatment categories overlap.
- [medium] `where_we_lag.details[3]`: Missing required caveat from the cited claims that these categories overlap.
- [low] `how_sure_are_we.details[1]`: Imprecise causal wording: missing stage data (~48%) explains why the treatment shares cannot be stage-adjusted, not why Taulukko 11 shares are not age-adjusted (Kuva 16 provides age-adjusted curative shares).
- [low] `how_sure_are_we.details[2]`: Minor imprecision: the cited quote states diagnosis is based on clinical examination alone (such as imaging) in approximately 20% of cases rather than imaging specifically, and the 93.6% specialist visit share is a national figure (no county breakdown) without being labelled as national.
- [medium] `what_to_do_first.details[0]`: Missing required caveat from the cited county claims that the listed categories overlap.

**Keski-Pohjanmaa**

- [medium] `how_sure_are_we.headline`: Overreach and missing caveat: the cited claim cty:no_treatment_record:Keski_Pohjanmaan_hyvinvointialue only states that 25.0% of patients had no treatment record within 12 months (not distinguishable from the uncited 27.5% national share). It does not support inferring relatively complete recording, and the sentence omits that a no-treatment-record share mixes untreated patients and unrecorded treatment.
- [medium] `how_sure_are_we.details[0]`: Overreach: even when framed as an inference, having a 25.0% no-treatment-record share indistinguishable from the 27.5% national figure (both mixing untreated patients and unrecorded treatment per bs:coverage:Treatment_start) does not support that treatment recording is relatively complete or that the 22.3% versus 27.0% curative share is less likely to be a recording artefact.
- [low] `how_sure_are_we.details[2]`: Minor imprecision: bs:coverage:Treatment_start specifies that public data show which treatment type is recorded within 12 months (with 27.5% having no treatment record, mixing untreated patients and unrecorded treatment), rather than whether treatment actually occurred; additionally, q:5eb155decc attributes the approximately 20% figure to clinical examination alone (such as imaging) rather than imaging alone.
- [low] `what_to_do_first.headline`: Minor imprecision: 1.4% in cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue is the crude share of patients with an MDT meeting recorded (n=2/148), not the completeness rate of MDT recording, and rec:3 recommends publishing recording completeness rather than auditing it.

**Etelä-Pohjanmaa**

- [medium] `where_we_lag.headline`: Overreach and missing caveat: the cited claim only shows the county's symptomatic treatment share is below the national average, not that it 'lags' (a lower share of symptomatic-only care does not indicate worse performance), and the sentence omits the required caveat that treatment categories overlap.
- [medium] `how_sure_are_we.details[0]`: Overreach: having a no-treatment-record share indistinguishable from the national 27.5% (which mixes untreated patients and unrecorded treatment) does not support inferring that treatment recording is relatively complete or that the symptomatic-treatment difference is unlikely to be a recording artefact.
- [low] `how_sure_are_we.details[2]`: Minor imprecision: the cited quote states that approximately 20% of diagnoses are based on clinical examination alone, such as imaging, rather than imaging alone.
- [low] `what_to_do_first.headline`: Minor imprecision: recommendation 2 proposes naming a contact person for the diagnostic phase (and adding a persistent-symptoms referral rule), rather than 'standardising ... diagnostic contacts'.

**Kanta-Häme**

- [medium] `where_we_lag.details[1]`: Missing required caveat from the cited claims: treatment categories overlap (a patient can receive multiple treatment types, so shares across categories do not sum to 100%).
- [medium] `what_to_do_first.details[1]`: Overreach and minor imprecision: the cited roadmap claim (q:b326e35410) specifies national pathways and target access times in 2026–2028 are planned for five unnamed cancers (so it is not known whether lung cancer is included), and THL guidance 21/2016 defines how cancer access times are recorded for 16 cancers rather than 'defining 16 cancers'.

**Pirkanmaa**

- [medium] `where_we_lag.headline`: Overreach: exceeding national crude (unadjusted, overlapping) treatment-share benchmarks does not establish that Pirkanmaa's main pathway gaps are limited to unmonitored local target times and unmeasured referral-to-treatment access times, nor do the cited claims rank or exhaust Pirkanmaa's pathway gaps.

