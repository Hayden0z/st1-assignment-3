# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Fri 8:30 - 10:30 Group 3
- Members, GitHub usernames and cohorts: Tobyn(TobynJames) ,Hayden(HaydenOz) ,Hanyia(ArduinoO121)
- Repository URL: https://github.com/Hayden0z/st1-assignment-3
- Starting SHA: [response]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Patient search 
- Context: the Patient search function finds a specific instince or object of the patient class 
- Requirement: able to search up a requried patient with thier assicotied information 
- Acceptance criteria: Patient search is able to find the correct patient with the assicotied information given 
- Scope: Big as patients are a cruciel part of the smartcare busssiness,messing up the search function can have cruciel consquences for example having the wrong patient in a appioment.or using wrong information for a specific patient.  
- Definition of Done: paitent search can correctly pull up the patient with the correct information 
- Owner: data_store.py
- Actual issue link: class search patient is not being imported 

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Appoiment cancellation
- Context: Updating the appioment status to cancelled while retaining the appioment 
- Requirement: appioments must have statues that are able to be upcoming,completed or cancelled
- Acceptance criteria: appioments can be cancelled but still retain information 
- Scope: involes prcationers and patients 
- Definition of Done: appioments stautes can be changes to cancelled 
- Owner: AppointmentStatus is in domain.py while cancel_appointment is in services.py  
- Actual issue link: datastore not connecting proprly 

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|---|---|
| changes | [Weak] | [Single word without description of said changes] |
| final version | [Weak] | [indicates the version but doesn't discribe what has been added] |
| Add patient search by ID | [Strong] | [directly names the new addition] |
| fix stuff | [Weak] | [fix what? dosn't discribe new fixes] |
| Prevent cancellation of completed appointments | [Strong] | [directly states a new feature] |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns: Affects other code and add another dependancy 
- Responsibility and architecture concerns: Increases complexity of software, and add's dependancy deprecation risk if external 
- Testing and review concerns: Can't be tested in an isolated enviroment if it edits unrelated code
- Changes to remove or separate, with reasons: Recomendation to change the new code to run indipendently 

## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence: No information on such tests and how many, no conformation of what looks good
- Follow-up review question 1: clarify What looks good
- Follow-up review question 2: Please list out all tests past
- Follow-up review question 3: Please list if it failed any hidden tests
- Follow-up review question 4: Please increase scope of testing
- Follow-up review question 5: Please reveiw it in the context of the rest of the aplication
- Additional questions if useful: [NA]

## E Team workflow agreement

| Practice | Team agreement |
|---|---|
| Branch naming | Single main branch |
| Commit message convention | Rough Time and day + Stage worked on (Any new feature must be named) |
| PR size | Work on one stage at a time limmiting Pull Size |
| Another-member review requirement | No review requirement |
| Merge rule | NA |
| Significant Copilot disclosure rule | NA |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement | Owner | Acceptance criteria or precise link | Status |
|---|---|---|---|---|
| [issue 1] | [response] | [response] | [response] | [response] |
| [issue 2] | [response] | [response] | [response] | [response] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [Tobyn]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

- Member: [Hanyia]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

- Member: [Hayden]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

You can commit many small changes that don't add up to anything significant 

## L Stage 6 formative questions

1. What is version control?

GIT's version control is it having multible branches people can work on at the same time

2. Why is a feature branch useful?

It creates an inviroment where things might not be fully functional but new features can be tested and worked on

3. What makes a commit a good engineering commit?

Add's functionality to the project and has good message attached

4. What is a pull request?

A dev requesting to merge changes from one branch to another

5. What is the purpose of code review?

Making sure the code works but is also approved by others

6. What does a Git diff show?

The diffrence between commits

7. What is a Definition of Done?

The state a pull request / branch must reach before it can be approved into the main branch

8. What is the appropriate role of GitHub Copilot in pull-request review?

code testing

9. Why should individual contribution not be judged only by commit count?

You can commit many small changes that don't add up to anything significant 

10. What is the Stage 6 engineering rule?

[response]

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
