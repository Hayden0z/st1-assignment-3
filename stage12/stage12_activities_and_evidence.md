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

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: [README setup completed, tests passed, Release]

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
| FR-09 and QRY/FP listing/filter/order/purity | [] | [] | [] | [] | [] |
| UI full console sequence and error recovery | [] | [] | [] | [] | [] |
| Session-only scope / FR-10 retired | [] | [] | [] | [] | [] |
| PG RES and assurance integration | [] | [] | [] | [] | [] |


## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | [Version 12] | [\SmartCare_Starter\st1-assignment-3> - python main.py --interactive  ] | [bfaddd53f0805a0815ffe7cb6781c16377b32741] | [Works] | [menu appears and works when command is run] |

| Complete PG if applicable | [] | [] | [] | [] | [] |

| Affected focused checks after correction | [NA] | [NA] | [NA] | [NA] | [NA] |

| Full integrated recheck | [Within Github] | [Github reposotroy] |

Prior assertions preserved / reviewed test diff: [No changes required, we all all happy with the current product]

Remaining failure / limitation: [You can book a appointment that overlaps with a patients current appointment - this could be fixed]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [] | [] | [] | [] |
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
| No SQLite/persistence/repository ABCs/speculative features | [built in datastore with no sql database] | [] | [no change] |
| Synthetic data / secrets / dependencies / provenance | [Datetime depenancy] | [dependancy is not deprecated] | [no change] |
| Significant common Copilot contributions and human verification | [copilot not used outside of md. docuemnts] | [] | [] |


copilot not used outside of md. docuemnts
| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [Explaining documentation terminology] | [Does not affect code/requirements] | [Done by group members] | [Accepted for documentation] | [No change to code, changes to documentation] |
Access route or approved equivalent / limitations: [Accessed through copilot/md files, no limitations]
Available AI evidence and missing evidence honestly disclosed: [Copilot log]


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
Verifier and clean environment / actual version: [Verified by Hanyia, On clean software/laptop]
Setup/run/test commands and observed results: [Tests can not be ran after cloneing zip due to missing pytest depenancy the menu does work]
Missing local file or setup gap / remedy and recheck: [run in project folder
python -m pip install -r requirements-dev.txt - then tests work (when ran from project folder)]


## G Known limitations debt and release notes

Delivered features: [all functional requires deliverd]
Important fixes: [stage 8 debugging fixes for f8-01 & f8-02]
Architecture/quality improvements: [None]
Known limitations: [patinet can have overlapping booking]
AI-assisted development note: [NONE]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [Patient conflict] | [meduim] | [not in scope] | [ignore ] | [not accepted] |
Session-only synthetic data and minute-precision local time: [This would need to be fixed as the data should be stored somewhere not relying on a session to remain open]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [None of these additional features are added]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [must be aest]
Difference between accepted scope limit and unresolved required behaviour: [No unresolved required behaviour]



## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [Stage 8 Appointment History Debugging] | [Return all bookings regardless of cancellation] | [Affects patient understanding and clinical transparency] | [Tobyn/Hanyia] | [Commented out line 94 for data_store.py] | [Yes, all tests pass and no errors present] | [None] |
Justified no-change conclusion if no defect found: [Appointment history Behaviour matches specifications, no changes required]
Release blockers still open / status: [No additional features required, Status: Operational]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [No files/issues were reviewed after commit]
Independent reviewer / feedback / response: [Project code reviewer was Pranav Gupta, Reviewed Stage 6, 7 & 8, Recieved feedback on testing/debugging methods]
Integration commit / full recheck: [No new commits were made]
Tracked and untracked file inspection / cleanliness: [Only intended files are included in the release]
Secrets/staff material/caches/tool-metadata exclusion check: [No credentials or sensitive data detected]
Candidate recovery plan / known-good SHA: [Latest version, b114da143ed21438febd8059d129ba04e4b508e0]
Named substantive contributions: [No major contributions were made]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [READY FOR COURSE RELEASE]
Approver / date / rationale and evidence: [Hanyia/All team members, 9/11/2026, All Functional requirements have been met, SmartCare_Starter/st1-assignment-3/project/tests]
What risks remain / conditions / owners: [No risks remain, Group 3]
Can the team explain the system: [Architecture can be concisely explained]
Can a change be recovered: [Recoverable changes must be saved in a backup system and lastest SHA]
Common decision / PG decision where different: [READY FOR COURSE RELEASE]


## K Final tested release SHA

Exact common tested SHA: [bfaddd53f0805a0815ffe7cb6781c16377b32741]
Exact PG tested SHA or not applicable: [None]
Final submitted SHA / repository URL: [b114da143ed21438febd8059d129ba04e4b508e0]
Evidence-only later commit and difference explanation: [Added release documentation only, no executable code changed]
Executable changes after testing and re-verification: [No executable code changed]
Source ZIP name / SHA correspondence / extracted comparison: [File on Github as repository and not ZIP]


## L Submission package verification

- [ x] Feature freeze and scoped requirements traced.
- [x ] Applicable full regressions, integrated demo and invalid paths verified.
- [x ] Architecture/code quality and final AI/dependency checks complete.
- [ x] Root README and project/README reproduced by another verifier.
- [ x] Release notes, technical debt and limitations visible.
- [x ] Independent human review, integration and release decision recorded.
- [x ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ x] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [x ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [x ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [x ] Mixed-group common protection and candidate upload routing checked.
- [x ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [(https://github.com/Hayden0z/st1-assignment-3)]
Deadline/timezone: [9/11/2026 12:59PM AEST]
Repository access arrangement: [All team members have access]
Mixed-candidate upload arrangement: [Hanyias laptop will upload link]
Oral/video recording/accessibility arrangements: [do to seprately]
Remaining administration or release dependency: [No]


## M Formative questions

1. What is a release candidate? [a release candidate is a software that is near completion   version of a software has passed being bugged tested and can be considered for a public release.  ]

2. What is feature freeze and why is it used? [feature freezes is a period of time in a project development when all work of adding new features and capabilities stopped.This is used so teams can focus and work on bug fixes and critical updates on the project ]

3. What is regression testing in a release context? [the practice of re doing previously executed code in a program this is all before a release of a program.this is all done so that recent code changes for example new features or bug fixes are correct and doesn't break current functionality ,]

4. What is a known limitation? [if there is two appointments that have the same data for example date time or same patient.If the two practitioners have different practitioners it will will work and not cause an issue.It's only when it’s the same practitioner it will raise a flag as the system focus on the practitioner]

5. What is technical debt? [technical debt is a concept when development teams take shortcuts or small solutions to meet deadlines   ]

6. What are release notes? [are user summaries published alongside a new software, hardware or update to explain what was changed,affects and why it matters  ]


7. What is software maintenance?  [software maintenance is the process of updating,modifying and checking a software after it has been deployed to the public  ]

8. What is the purpose of the individual demonstration/viva?  [ the main purpose of individual demonstration/viva is to show and check that a student have a true understanding of their work ]

9. What should the final responsible-AI check establish before release?  [the Final responsible-AI should check that a system meets full requirements,safety accountability and performance]

10. What is the main course conclusion about AI and the role of the software engineer? [the main conclusion about AI is that it acts like an assistant to the software developer giving tips and ideas to fix an issue but a developer does not have to take its advice    ]

## N Reflection viva and handover

Strongest evidence SmartCare is ready: [Yes]
Weakest area: [UI dosn't display full appointment details]
How AI use changed from Stage 1 to Stage 12: [Ai not used outside of MD docuemnts]
Start doing — engineering and AI use: []
Stop doing — engineering and AI use: []
Continue doing — engineering and AI use: []
What worked / caused rework / future delivery improvement: [Bookings recoring meetings  twice weekly to do work together as a group]
One paragraph — If AI can write code why do we still need software engineers: [

    Software engeingering is not just about writing code, you also need to understand or come up with the system as a whole adhering to the scope that you or the steakholdes have outlined for you. To simply just write code you could add out of scope features or not add features as intennted. therefore there is alot more to the job of software engniners as to where if AI could perfectly write all the code we need we'd still have people in charge of making sure the output is as intendeted
]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [Smartcare link requires a new system so they don't have to rely on multible spreadsheets and physical documents] |
| Two requirements and acceptance criteria | [Can be ran on one central computer, is small and easy to use] |
| Domain model and architecture | [python code with a built in data store] |
| Design trade-off | [can only be ran in a terminal running python] |
| Meaningful test and its limits / 100 percent coverage | [17 tests all valid] |
| Diagnosed defect and verification | [no defects in the tests]
| Shared store and session-state/query responsibilities | [Major data stored on data_store.py and retrieved on testing files/service/domain.py] |
| What would break if session-state lookup/query responsibilities changed? | [Appointment history may not be recorded correctly] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [cancellation focuses on a single entity/object, conflict coordination focuses on multiple domain objects] |
| FR-07 retained history test | [Cancelled appointments remain visible in history] |
| Actual AI change rejected/modified or honestly accepted with verification | [AI changes were not implemented] |
| Unresolved limitation / future production work | [No work gaps] |
| Personal implementation contribution | [Hanyia coded finding & retaining practitioner/appointment values, test_services.py] |
| Personal test/review/design/integration contribution | [Hanyia helped revise documentation, Recorded documentation in Stage 12] |
| PG agentic change and rescheduling verification | [Not PG] |
| PG responsible-AI risk/remediation or supported no finding | [Not PG] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [Not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [Personal reflection/Hanyia in Stage 12 & Canvas]
No further coding stage. Later corrections use the published assessment process.
