# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Friday Group 3 
Members and UG/PG cohorts: Tobyn, Hanyia & Hayden
Record owner / contribution links for each member: 
Tobyn - Testing, debugging & MD document writing for Fr-01
Hanyia - Testing, debugging & MD document writing for Fr-02
Hayden - Md document work for formitive questions


Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

- Appointment disappears after cancellation. - Symptom as it's the discribed issue
- The data-store removal path is probably being called. - Hpyothesis as it's a theroy as to what is causing the issue
- The failing test shows store.find_appointment('A1') returns None. Evidence, isolates the issue to a scource
- The service layer is badly designed. Hypothesis but a bad one that dosn't explain much
- Traceback points to smartcare/services.py line 42 in the example. Evidence, isolates the issue to a scource


### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: [complete]

Function: Same-practitioner/time booking
expected behaviour: Error when an appoint is made with the same practitoner at the same time
observed behaviour: Test fails as an error is not raised when an appointment is booked at the same time as other
Minimal reproduction: Test ran 3 times
Initial Hypothesis: Logic is backwards within the test swapping the assert test for the raise error test
Second Hypothesis: Test is functional, definition of has_practitioner_conflict within book_appointment function is inncorect

Evidence: Within data store has_practitioner_conflict checks 3 things in each appointment to check for conflicts
1: Same practitoner as new bookings
2: same time as new bookings
3: current bookings is schedulaed
if all 3 things are true the error appears

Logic is incorect - for #1 
"appointment.practitioner.practitioner_id != practitioner_id"

It's checking if the new appointment dosn't have the same practioner - where it should check if it does

requirement: New bookings must not overlap with exisiting ones that occour at the same time with the same practioner

Soulution: Update line 110 in data_store.py from
appointment.practitioner.practitioner_id != practitioner_id
to 
appointment.practitioner.practitioner_id == practitioner_id

Conclution - test runs correctly after doing this

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

A test expecting cancelled appointments to be deleted should be removed as this is not a functional requirement
The test itself could be replaced with a test making sure that cancelled appointment still do exist as FR-07 states appoinment history must be retained

A test expecing diffrenet practitioners booked in appointments at the same time to cause conflict is correct as
AC-04.2 only permits a different practitioner on appoinments at the same time and rejects a same-practitioner SCHEDULED conflict; 

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.

Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Issue Title: 70 Line long AppointmentService method 
Items to resolve and their smells 
Issue: Duplicate status strings - Smell: repeated lines of code
Issue: direct collection manipulation - Smell: Data Store is accecet directly and without using a public get
Issue: printing validation - Smell: Terminal Logs have extra data that isn't always required
Issue: four nested conditioals - Smell: undesired Primid shape visible when looking at code




### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.


Issue: Rejection of Same-practitioner/time booking not functional 
exception: Raise error when a new appointment is booked with the same time and practioner as a previosuly booked one (That's still schedualed)
assertion: Assert booking a new appointment a new appointment is booked with the same time as a previosuly booked one (But a diffrent practitoner)
Expected value: same time appointments fail when reusing practioners but pass when using diffrent ones
Test: test_conflict_rule_and_different_practitioner 
Call path:
Practioner D2 Registerd
Apppointment # 1 booked at Time with D1 Practioner
Exception expeceted when another appointment (#2) is raised same time with D1 practioner
EXECPTION NOT RAISED
Requirement:AC-04.2 - appoinemtns with same practitioners at the same time raise conflict 

Evidence: Test test_conflict_rule_and_different_practitioner fails
Possible causes (In order of probibility): 
1 - Function checking for conflict has logic error
2 - Test itself has logic error
3 - datastore dosn't retain information to check if appointment already is schedualed



### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Issue isn't documented the quick fix may ignore a larger issue

Test error:

    def test_conflict_rule_and_different_practitioner() -> None:
        """Verify conflict rule and different practitioner."""
        data_store, _, _, appointment_service = foundation()
        PractitionerService(
            data_store,
        ).register_practitioner('D2', 'Morgan Example', 'General')
        when = datetime(2026, 10, 1, 9)
        appointment_service.book_appointment('A1', 'P1', 'D1', when)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

tests\test_starter.py:127: Failed

Classification responses (1–5, each with reason): [complete]

Tutorial debugging record — Logic looked at, issue traced to data_store.py /has_practitioner_conflict bool

expected; Bool to return true when same practioner is checked against all other active bookings with the same time
observed; line 110 checks if the practioner is not the same to reutrn true
reproduction; runing test again draws same error
hypothesis; changing line 110 from 'not equals' to 'equals' will fix the erorr
evidence to inspect: updating line 110 then rerunning test fixes issue

Traceback — 
exception: Raise error when a new appointment is booked with the same time and practioner as a previosuly booked one (That's still schedualed)
assertion: Assert booking a new appointment a new appointment is booked with the same time as a previosuly booked one (But a diffrent practitoner)
Expected value: same time appointments fail when reusing practioners but pass when using diffrent ones
Test: test_conflict_rule_and_different_practitioner 
Call path:
Practioner D2 Registerd
Apppointment # 1 booked at Time with D1 Practioner
Exception expeceted when another appointment (#2) is raised same time with D1 practioner
EXECPTION NOT RAISED
Requirement:AC-04.2 - appoinemtns with same practitioners at the same time raise conflict 

ranked causes and discriminating checks:
Root cause was line 110 and not the test's own logic

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: f3347a870e003aead0d2a043994808ccdd782b84
- Baseline test command: python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner
 working directory: Project
  / observed result: Test Failed / 
  evidence: Line 127 Exception test failed 

- Clean preparation SHA if a record-only commit followed Stage 7: NA
- Branch and preparer :debug/08stage branch created to debug 
/ how teammates obtained this branch: Created during stage 8 and switched to for all debugging

- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]

- Bounded diff inspected and recovery location (not committed): Main branch as recovery
- Prepared faulty-state commit SHA: f3347a870e003aead0d2a043994808ccdd782b84
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: test_conflict_rule_and_different_practitioner fails during test running, stops at first expected exception (which is not raised)
- Expected behaviour and requirement: Test is expected to get an exception when attempting to book two appoinemnts at the same time with the same practioner
- Minimal synthetic reproduction steps: re-running the test
- Meaningful failing test path/name and exact relevant failure: project/tests/test_stater.py :: test_conflict_rule_and_different_practitioner
- Human hypothesis and intended checks: Logic with test is inncorrect - after reviewing test logic this was not the case - to check book_appointment function iteself
- Supported root cause and inspected code/runtime evidence: Book appoinment function using has_practitioner_conflict method to check if the practioner is free has_practitioner_conflict is defined in data_store.py and has invalid logic
- Smallest justified fix / diff / why other behaviour is preserved: edit logic of has_practitioner_conflict 
- Repair SHA / focused verification result: ea165bd508ef080896737c4c16f4849f150d9216

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: Cancelled appointments are not listed in the appointment history.
- Expected behaviour and requirement: Cancelled appointments should be listed in appointment history.
- Minimal synthetic reproduction steps: 
· Book appointment
· Cancel appointment
· Check for cancelled appointment
· Creates error
- Meaningful failing test path/name and exact relevant failure: 
Test function: test_cancel_retains_history()
File path: st1-assignment-3/project/tests/test_services.py
- Human hypothesis and intended checks: see E, F8-02.
Two hypothesis
1. Find appointment query does not search for cancelled appointments.
2. Program deletes cancelled appointments.
- Supported root cause and inspected code/runtime evidence: 
Root cause is the following:

Within Data_store.py at line 93 the find_appoinemnt function excludes canclled appointmsnets with the line
and appointment.status.value != "cancelled"::\

Inspected code/runtime evidence is that the statement, when commented out, reveals no errors and all debugging checks have passed.

- Smallest justified fix / diff / why other behaviour is preserved: The root cause statement is deleted to ensure smooth running of the program.

- Repair SHA / focused verification result: [d562aae443c95e904f916e68a9d37917d1b6d1ac]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

observed: Cancled appointments don't apear in search query 
expected: All appoinments are retianed regardless of status
reproduction: Book appointment, cancle, then search for it's ID

### F8-01 human entry
Likely cause and why plausible: has_practitioner_conflict dosen't check correct values to flag itself as true
Evidence intended to inspect / competing explanation / discriminating check: Logic of the initial test is clean, and so is the book_appointment function - so the issue must lie within the conflict check function
Member and saved sequence/time or commit showing this preceded consultation: [ea165bd508ef080896737c4c16f4849f150d9216]


### F8-02 human entry
Likely cause and why plausible: Find appointment query does not search for cancelled appointment - the reason why the search won't bring them up is because it's not looking for it
Evidence intended to inspect / competing explanation / discriminating check: Other methods of finding the appointment work such as, booking, cancleing, then checiking if the item itself has been updated to cancled - this can be done proving the item still exists
Member and saved sequence/time or commit showing this preceded consultation: [d562aae443c95e904f916e68a9d37917d1b6d1ac]

Likely cause and why plausible: Program deletes cancelled appointments.
Evidence intended to inspect / competing explanation / discriminating check: Inpsect the cancel function to see if it removes the entry from the datastore
Member and saved sequence/time or commit showing this preceded consultation: Not continued after first hypothosis was correct

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Here is a code issue in our program, it's likey cause and evidence
has_practitioner_conflict dosen't check correct values to flag itself as true
Evidence intended to inspect / competing explanation / discriminating check: Logic of the initial test is clean, and so is the book_appointment function - so the issue must lie within the conflict check function
Suggest 3 soultion's

1. Correct the comparison logic in has_practitioner_conflict / The function may be comparing the wrong fields (e.g., practitioner ID, date, or time), / Correct items are being compaired / wrong / reject suggestion is incorrect 
2. Review the data being passed into has_practitioner_conflict /  The conflict detection logic may be correct, but it could be receiving incorrect or incomplete appointment values / has_practitioner_conflict is passing the correct data / wrong / reject - all correct data is being passed: 
3. Ensure the function checks all existing appointments / The function may only examine part of the appointment / Only practioner and time is checkd, but this is all that is required / wrong / reject - function is checking all appointments and their required information : 
Final human conclusion and comparison with initial hypothesis: All 3 options are slighty off, the logic was using all the correct values, it was the logic operater checking if the appointments had the same practioner was set to 'not equals' instead of 'equals'

### F8-02 Copilot review

Actual prompt / output reference and member: By Tobyn -

Here is a code issue in our program, it's likey cause and evidence 
Likely cause and why plausible: Find appointment query does not search for cancelled appointment - the reason why the search won't bring them up is because it's not looking for it
Evidence intended to inspect / competing explanation / discriminating check: Other methods of finding the appointment work such as, booking, cancleing, then checiking if the item itself has been updated to cancled - this can be done proving the item still exists
Suggest 3 soultion's

1. Update the find appointment query to include cancelled appointments / The search function is likely filtering out appointments with a status of "cancelled". / checking the search function this is true / correct / accept

2. Add a search option/filter for cancelled appointments / If the current design intentionally hides cancelled appointments, providing a dedicated filter / F8-02 requires cancled appointments to be retained, no filter required / wrong / reject - out of scope:

3. Review and correct appointment status handling after cancellation / The appointment may still exist, but its status could be stored incorrectly / All appointments are stored in the same datastore, the status should not affect how it's stored / wrong / reject - not miss assumes how the system works: 

Final human conclusion and comparison with initial hypothesis: Copilot option #1 is the same as the soultuion found by us humans

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [f3347a870e003aead0d2a043994808ccdd782b84] | [python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner] | [test fail] |
| F8-01 after repair | [ea165bd508ef080896737c4c16f4849f150d9216] | [python -m pytest tests/test_starter.py::test_conflict_rule_and_different_practitioner] | [test pass] |
| F8-02 before repair | [c5df411155d77dbf0b81c8e552aa5aeb0e2059fa] | [python -m pytest tests/test_services.py::test_cancel_retains_history  ] | [test pass & had to be changed to check data store to see the error] |
| F8-02 after repair | [d562aae443c95e904f916e68a9d37917d1b6d1ac] | [python -m pytest tests/test_services.py::test_cancel_retains_history  ] | [test pass] |
| Full suite after both repairs, before refactor | [TO REPLACE] | [python -m pytest -vv -s] | [All 17 tests pass] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour:
f8-01 test_conflict_rule_and_different_practitioner assertion books appointment with time and practioner that dosn't have a conflict, since this raised and error we knew something was wrong
f8-02 test_cancel_retains_history first assertion checks and appointment exists, then checks it can be cancled - both work - failed assertion was the third one that checks if you can still find the cancled appointment
Unrelated failures investigated / resolution: [Other fails came up when trying to fix F8-02, but after appliing the correct fix all tests pass]

## H. Refactoring decision and before/after verification

Smell and exact location: The test's led us to find what was wrong there was no easy to spot smell 
Small proposed structural change / why justified: issue tracing is harder when each function calls methods that exist in other files, having each function operate in one file makes it easier to spot the issues
External behaviour to preserve / relevant tests: preserve the functions being seprate, just house them in the same py file
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: this change will not be made
Focused and full after-refactor commands / working directory / results / evidence: changes not made
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: changes not made

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: 
f8-01 added to git as issue #4 - closed by Tobyn
f8-02 added to git as issue #5 - closed by Tobyn
Branch / prepared, repair and refactor checkpoints: debug/08stage branch created to debug
PR link and another member's reviewer identity: [365a338 Merge pull request #6 from Hayden0z/debug/08stage Reviewer = Hanyia]
Key human feedback, difference from Copilot findings and response/outcome: copilot suggested 6 total items with 1 being correct - out of the two issues it could only solve 1
Actual review approval / merge evidence: [Authored by Tobyn and merged 365a3389207764f82db9836aa7ea479d10893634]
Integrated code SHA and team pull/retest command / working directory / result: [365a3389207764f82db9836aa7ea479d10893634]
Evidence-only later SHA / explanation if different: [not applicable]
Each member's substantive contribution and artefact: 

Tobyn - Testing, debugging & MD document writing for Fr-01 & merge request 
Hanyia - Testing, debugging & MD document writing for Fr-02
Hayden - Md document work for formitive questions

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [the first one was promsing and it hit the problem on the head, the other suggestions didn't have the context of the full system and assumed there was other items at play which didn't exist]
2. What evidence changed your group's view? [Hanyia found that the issue relating to F8-02 was in data store which led to us fixing the issue]
3. How did regression tests protect the refactoring? [we could test one item on it's own and find fixes, but also after appliying a fix we could run all tests to make sure our fix didn't affect other tests]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Before an engineer changes some code in a system their first must find out what the root issue is and isolate,and look into the issue and understand the root issue of the problem.so engineers will isolate specific chunks of code to find out the issue and slowly work on and fix the error with.Because if a engineer rushes trying to fix code more issues will pop up 

2. Where should expected behaviour come from during debugging?

When a system is being debugged the expected behaviour comes from authoritative sources that are true and not from assumed assumptions.for example this can be documentation or prior working versions of the software            

3. What is a debugging hypothesis?

A debugging hypothesis is a detailed and explained version of how a person's code produces an error or unexpected behaviour      

4. What is a regression test and why is it retained?

A regression test is a software assurance test that checks and re-runs previous tests that exist in the software to ensure that previous bug fixes,new features and refactoring don't break; this is why regression tests are retained so that previous add functionality and fixes don't break. 

5. What is meant by root cause?

Root cause means the main problem and the fundamental event and underlying issue that is the origin with a problem,and if it is fixed it will stop causing issues       

6. What is refactoring?

Refactoring is the practice of improving the internal structure of existing code without changing the external functionality of the code

7. What is a swallowed exception?

A swallowed expectation is when an error happens with using a try catch block and then the program just ignores it or discards it       

8. What is a code smell?

A code smell is a surface level sign in a computer designed code that hints to deeper design or sturctal design problem   

9. How should GitHub Copilot-generated debugging diagnoses be treated?

So GitHub Copilot-generated debugging diagnoses must be treated as unverified hypothesis or drafts or drafts that require a person to validate, review code and do testing before application.This is because the GitHub Copilot is prone to logic gaps and edge cases

10. What is the Stage 8 engineering rule?

Response: Breaking down and debugging using different branches

## L. Completion and handover

- [ x] Existing project, earlier tests and stage records preserved.
- [ x] Passing Stage 7 SHA and safe preparation details recorded.
- [ x] Both defects reproduced with meaningful failing tests.
- [x ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ x] One genuine refactor verified under passing before/after tests.
- [ x] Human PR review, feedback resolution and integrated retest recorded.
- [x ] Tutorial, three reflections and ten formative responses complete.
- [x ] Local recovery metadata excluded from submitted source.
- [ x] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I. 365a3389207764f82db9836aa7ea479d10893634
Submitted SHA and evidence-only difference if any: [365a3389207764f82db9836aa7ea479d10893634]
Unresolved issues or incomplete checks / owner / next action: [NA]
Handover note: Well done everyone 
