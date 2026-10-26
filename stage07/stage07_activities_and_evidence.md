# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|---|---|---|
| FR-01 Register patient | the patient information is correctly inputted with correct data and format that can be registered | patient name has integers/numbers all patient information have incorrect input data,which will not let the information of the patient pass into the system  | The patient is successfully added when the patient’s information is valid  |

| FR-05 Prevent practitioner conflict | Booking a free appointment for the practitioner at any time slot   
 | Booking two appointments for the practitioner at the same time | System prevents they to be double booking for any practitioner so no overlap is caused |

| FR-06 Cancel appointment | being able to cancel the appointment based on its ID and also changing your condition | attempting to cancel an appointment that does not exist | Only valid appointments are able to be canceled by changing their status to canceled |

| FR-07 Retain cancelled history | Cancel a appointment an check that is able to be viewed in records | Delete or search for a canceled appointment that does not exist | canceled appointments remain stored as an appointments status changes so all appointments remain stored and can be viewed in a record |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [ Weak/unclear]  Why: Because assert True always passes and nothing is tested for the behaviour of the program.it provides no evidence that that assert true works

`assert appointment is not None`
Judgement: [ Weak/unclear]  Why: Only checks if an appointment object exists.This does not check if an appointment object has correct information example time is 11:30pm 

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour ]  Why: assert appointment.status == AppointmentStatus.CANCELLED directly checks if an appointment object status has changed to Canceled,This is the expected function of the appointment cancellation feature.However a limit would be that it can not verify that an appointment is stored in history 

`assert len(results) > 0`
Judgement: [ Weak/unclear]  Why: Only confirms that some results have been returned,this does not check if it has found the correct patient or appointment.

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour]  Why: This verifies the searching of the appointment A1,returns the correct and expected appointment record.This puts the finding functionality to the test.A limit would be that it doesn't check the appointments status

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: done this might import images as it is a table

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1)assert object is not none |Only checks that the object exists does not check if the data is correct |Checks that the objects data is correct when searched for example a patient when searched by their ID  |

| 2)assert object is not none | another example can be it checks a appointment exists however does not check the status or details | [same thing as the first and the same example but change patient with appointment  |

| 3)assert True  | Always passes True checks nothing | test that canceling an appointment changes the status to canceled  canceled |
| 4)assume SMS notifications | Just Thinks that SMS notifications exists however are nowhere in the project just assumes |Should test an actual function in the project like a canceled appointment can be seen |
| 5)assume SMS notifications | Same thing justs tests functionalities that don’t exist | test what happens when you cancel a non existent appointment  |


### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
A program that has 100% code coverage can coexist with poor software verification.This is because when every line is executed and run the results can not be correct and the software will not check.Because code coverage is all about measuring how much code is executed.while software verification measures whether the software behaves correctly based on requirements on the software. So having 100 percent code coverage can coexist with poor software verification because a system can run and execute all the lines code well but the results outputted may not be correct 

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| Book appointment | Appointment can be booked with name, patient and practitioners & time | A1 | test_starter.py file | test_unregistered_participants_rejected function in the Test_starter.py file | stores appointment without error | Sucsess | Supplied |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| A1 | Book appointment | Appointment can be booked with name, patient and practitioners & time | Positive | See outcome if correct values in an appointment | Correct values are booked | Matches scope and system design |


## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
[Verification answers are we making the software correctly for example Question1 as it does  the correct and negative testing for the functional requirements]

2. What question does validation answer?
[Validation answers the question of are we making the correct software]

3. What is a unit test?
[A unit test is a software test that runs and checks a single component of a software.Unit testing can be a great component because it unit testing can check isolated components and sees that there work and cause no issues.unit testing can detect early bugs and fix them,and unit testing can be used as great documentation as the units that are being tested are being looked  documented on what works and what causes issues]

4. What is a pytest fixture?
[Pytest fixture is a reusable function that is designed to be reliable and sets a reliable consistent context for tests before a test runs.]

5. What is parametrisation in pytest?
[Allows a function to be run multiple times with different input testing what the output would be.Instead of writing different test functions for every data variation]

6. What is regression testing?
[Is adding new code but executing and checking that the new code fixes the required issues but doesn't cause new issues to occur.]

7. What does code coverage tell us, and what does it not prove?
[Code coverage tells us that lines of code can be executed/can do inputs and more for example running calculations.what code coverage doesn't tell us is the output of the results as code coverage does not check the information and data of the code it just runs it.]

8. What makes an assertion weak?
[An assertion is weak when it passes everything even if the codes output is incorrect or broken]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[The role of the GitHub Copilot as a test assistant appropriate roles for GitHub Copilot as a test assistant would be maintenance,fixing repetitive features.GitHub Copilot should not take the intent people do just help give small suggestions and help with doing very repetitive features]

10. What is the Stage 7 engineering rule?
[Gathering evidence with testing,what their prove,gain results,as well with using Unit testing]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
