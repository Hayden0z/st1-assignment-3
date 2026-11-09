# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: [Friday Group 3]
Members and UG/PG applicability: [Tobyn Dwyer * tobynjames, Hanyia Iftikhar * ArduinoO121, Hayden Ozimek * Hayden0z, UG]


## A Release scope and starting SHA

Release label/version and requirements baseline: [Final SmartCare Project, Stage 9 is finished]
Common starting SHA / branch / applicable members: [bfaddd53f0805a0815ffe7cb6781c16377b32741, Main, Tobyn Dwyer * tobynjames, Hanyia Iftikhar * ArduinoO121, Hayden Ozimek * Hayden0z]
PG starting SHA / branch / applicable members or not applicable: []
Working-state review and approved integration: [Approved by Hayden]
Protected common candidate and PG differences: []
Feature freeze / owner / verifier: [Hayden has finsihed Stage 9, no additional functionalities]


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [response]

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | [Two tests prove this test_cancel_retains_history & test_failed_cancel_retains_history] | [st1-assignment-3\project\tests\test_services.py , 00597fa61e588c1165b80974b5c01a971ee52c23] | [Tobyn] | [Yes] | [None] |

| Architecture responsibilities are appropriate | [Even distrobution of work accross all 3 team members] | [Spans accross all files & commits] | [All team memberrs] | [Yes] | [None] |

| Rescheduling is safe — PG only | [] | [] | [] | [] | [] |

| AI use is responsible — common recheck / PG assurance | [Prompts done but no implementations made] | [Spans across all files & commits] | [All team members] | [Yes] | [None] |
| System is maintainable | [System passes code checks required from each stage] | [Spans across all files & commits] | [All team members] | [Yes] | [None] |
| FR-01–03 register/find and validation | [three tests prove this test_required_fields] | [st1-assignment-3\project\tests\test_starter.py, 882a9beeafd0df9238a823e7e91d73325e66018f] | [Tobyn] | [Yes] | [None] |
| FR-04–05 booking/conflict rules | [Two tests prove this test_registration_and_booking & test_conflict_rule_and_different_practitioner] | [st1-assignment-3\project\tests\test_starter.py, 882a9beeafd0df9238a823e7e91d73325e66018f] | [All team members] | [Yes] | [None] |
| FR-06–08 cancellation/history/find | [Three tests prove this test_failed_cancel_retains_history, test_cancel_retains_history, test_find_items_by_ID] | [st1-assignment-3\project\tests\test_services.py, 00597fa61e588c1165b80974b5c01a971ee52c23] | [Tobyn] | [Yes] | [None] |
| FR-09 and QRY/FP listing/filter/order/purity | [response] | [response] | [response] | [response] | [response] |
| UI full console sequence and error recovery | [response] | [response] | [response] | [response] | [response] |
| Session-only scope / FR-10 retired | [response] | [response] | [response] | [response] | [response] |
| PG RES and assurance integration | [response] | [response] | [response] | [response] | [response] |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [Version 12] | [\SmartCare_Starter\st1-assignment-3> - python main.py --interactive  ] | [bfaddd53f0805a0815ffe7cb6781c16377b32741] | [Works] | [menu appears and works when command is run] |

| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |

| Affected focused checks after correction | [NA] | [NA] | [NA] | [NA] | [NA] |

| Full integrated recheck | [Within Github] | [Github reposotroy] |

Prior assertions preserved / reviewed test diff: [No changes required, we all all happy with the current product]

Remaining failure / limitation: [You can book a appointment that overlaps with a patients current appointment - this could be fixed]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [Run --interactive, register 3 persons and find them] | [they get found] | [Items were found] | [console outputs P ID:2
practitioner found] |

| Valid booking | [make a bookings in the menu] | [booking is made] | [Booked sucsessfully] | [Appointment ID:10
Patient ID:1
Practitioner ID:2
Date/time (YYYY-MM-DD HH:MM):2004-04-04 12:00
Appointment booked successfully.] |

| Same practitioner exact-time conflict rejected | [book two of the same appointment in a row] | [new appointmnet is rejected] | [appoinmnet was rejected] | [Appointment ID:12
Patient ID:1
Practitioner ID:2
Date/time (YYYY-MM-DD HH:MM):2004-04-04 12:00
Issue dected Practitioner already has a SCHEDULED appointment at this time] |

| Different practitioner same time allowed | [diffrent practioner allows for bookings at the same time as other bookings] | [new booking works] | [booked sucsessfuly] | [Enter appioment details 
Appointment ID:12
Patient ID:1
Practitioner ID:3
Date/time (YYYY-MM-DD HH:MM):2004-04-04 12:00
Appointment booked successfully.] |

| Cancel SCHEDULED and retain/find CANCELLED object | cancel appointment - then find appointment | appoint is still findable after canceling | works | enter 
Enter appioment ID 
Appointment ID:10
Appointment successfully Canclled .

appioment ID 
Appointment ID:10
appioment found |

| Invalid/repeated cancellation rejected | cancel appoinment, then try to cancel it again | system won't let you canclel an appoinment twice | issue detected comment raised | Enter appioment ID 
Appointment ID:10
Issue dected Only SCHEDULED appointments may be cancelled |

| Default all-status listing | display all appoinments by defualt when searching for a practioners appointments | default = all | default does = all but appoinments come up as id's not as a readable entry | Enter Practitioner ID
Practitioner ID: 3
Status filter (scheduled/cancelled/completed, blank = all): 
<smartcare.domain.Appointment object at 0x000001D840C6B910>|

| Explicit filtering / empty vs unknown / deterministic order | seach for appoinments and select a filter | only items matching the filter apear | cancled appoint apears when searching for cancled appointment | Enter Practitioner ID
Practitioner ID: 2
Status filter (scheduled/cancelled/completed, blank = all): cancelled
<smartcare.domain.Appointment object at 0x000001D840C3F750> |

| Invalid date/status/menu/lookup recovery and continued operation| type invalid format for one of the required feilds | menu stays active but lets user know they've made a mistake | exception message visiable | Appointment ID:1
Patient ID:1
Practitioner ID:2
Date/time (YYYY-MM-DD HH:MM):2026 10 1 9   
Issue dected Use date/time format YYYY-MM-DD HH:MM |


| Session-only limitation and normal exit | data is only stored per session | serching for an appointment after closing the session means it will no longer exist | could not cancel appointment after restarting console as it no longer exists| Enter appioment ID 
Appointment ID:10
Issue dected Appointment not found|

| One meaningful requirement-linked pytest test explained | test_find_items_by_ID | you can find exisitng items using their id | tests pass | running 
python -m pytest tests/test_services.py::test_find_items_by_ID
collected 1 item                                                                                                                                               

tests\test_services.py .                                                                                                                                 [100%]

====================================================================== 1 passed in 0.01s
 
| Architecture and one actual AI decision / known limitation | AI not used in project|

Stable demo owner / fresh process / command: [from reposotroy folde run
python main.py --interactive 
]



## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [smart care folder] | [OOP in use with moduels and classes] | [no change] |
| PascalCase and snake_case naming | [tests and functions use snake case - datastore foundation items using Pascal] | [see previos] | [no change] |
| Useful type hints and meaningful docstrings | [domain.py] | [values are of required type - string or datetime, and there is inputvalidation for date's] | [no change] |
| Four-space indentation and imports/layout | [whole project] | [basic indentaion used with python] | [no change] |
| Focused methods / duplication / dead or commented code | [NA] | [no commented out code remiains that's not in use] | [no change] |
| Globals / leakage / unnecessary inheritance or frameworks | [whole project] | [no found inherritance issues] | [no change] |
| No SQLite/persistence/repository ABCs/speculative features | [built in datastore with no sql database] | [response] | [no change] |
| Synthetic data / secrets / dependencies / provenance | [Datetime depenancy] | [dependancy is not deprecated] | [no change] |
| Significant common Copilot contributions and human verification | [copilot not used outside of md. docuemnts] | [response] | [response] |


copilot not used outside of md. docuemnts
| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [whole project] | [Tobyn] | [scope finalized and all functionality implemented] |
| Out-of-scope capabilities and known limitations | [Tobyn] | [booking confilts with patients not throwing an error is a known limitation] | [not in scope] |
| Confirmed teaching Python version and dependency installation | [teaching version  - 3.11.1 datetime depenancy ] | [tobyn] | [checked] |
| Working directory / demo / interactive / test commands | [to run interactive python main.py --interactive 
tests can be run with python -m pytest 
] | [tobyn] | [checked] |
| Repository structure and architecture responsibilities | [owner is Hayden, we push without PR] | [tobyn] | [checked] |
| Responsible AI summary / synthetic-data rule |Ai not used outside of md docuemnts
| Release label/version and SHA links | [github] | [tobyn] | [checked] |
Root README index and project/README verified: [verified]
Fresh clone or extracted ZIP / candidate identity: [no cloned zip, can be done in git]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


## M Formative questions

1. What is a release candidate? [response]

2. What is feature freeze and why is it used? [response]

3. What is regression testing in a release context? [response]

4. What is a known limitation? [response]

5. What is technical debt? [response]

6. What are release notes? [response]

7. What is software maintenance? [response]

8. What is the purpose of the individual demonstration/viva? [response]

9. What should the final responsible-AI check establish before release? [response]

10. What is the main course conclusion about AI and the role of the software engineer? [response]


## N Reflection viva and handover

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
