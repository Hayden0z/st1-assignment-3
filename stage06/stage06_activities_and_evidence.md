# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: Fri 8:30 - 10:30 Group 3
- Members, GitHub usernames and cohorts: Tobyn(TobynJames) ,Hayden(HaydenOz) ,Hanyia(ArduinoO121)
- Repository URL: https://github.com/Hayden0z/st1-assignment-3
- Starting SHA: [c950052]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: Patient search 
- Context: the Patient search function finds a specific instince or object of the patient class 
- Requirement: able to search up a requried patient with thier assicotied information 
- Acceptance criteria: Patient search is able to find the correct patient with the assicotied information given 
- Scope: Big as patients are a cruciel part of the smartcare busssiness,messing up the search function can have cruciel consquences for example having the wrong patient in a appioment.or using wrong information for a specific patient.  
- Definition of Done: paitent search can correctly pull up the patient with the correct information 
- Owner: Tobyn
- Actual issue link: class search patient is not being imported 

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: Appoiment cancellation
- Context: Updating the appioment status to cancelled while retaining the appioment 
- Requirement: appioments must have statues that are able to be upcoming,completed or cancelled
- Acceptance criteria: appioments can be cancelled but still retain information 
- Scope: involes prcationers and patients 
- Definition of Done: appioments stautes can be changes to cancelled 
- Owner: Tobyn
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
| [Patient Search was not implemented] | [To look up a patient with ID] | [Tobyn] | [Patient search looks up patient with ID, returns lookup error if no ID is matched] | [Implemented] |
| [Appointment Cancellation was not implemented] | [To be able to find an appointment by ID and update its status to "Canceled"] | [Tobyn] | [Appointment cancellation looks up an appointment by ID and returns a lookup error if not found; if found, it updates the appointment's status to cancelled] | [Implemented] |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [No standard pull requests, instead we as a group notify eachother of when we're working on main]
- Linked issue and requirement: [Lastest push was Markdown work updated, requirement was to finish stage 6 markdown file]
- Feature branch: [main is the only branch]
- Changed behaviour: [code untouched]
- Meaningful commits: [1f3c623 - This was the only code change commit]
- Test command, directory and observed result: [No test ran in stage 6]
- Another-member reviewer: [Not required]
- Human observations recorded before Copilot: [copilot not used]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [Tests to be ran in stage 7]
- Key feedback: [No feedback]
- Author response/change and verification: [No pull requests, but we are running a group chat for change and verifitcation statments]
- Reviewer recheck and approval: [Self approval before pushing changes, but notofiying groupchat before editing main]
- Merge outcome and SHA: [NA]
- Significant Copilot assistance: [None]
- Linked issue closure: [#1 & #2]
- Each member updated main: [Tobyn, Hanyia & Hayden]
- Integrated verification after merge: [Na There was no merge]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- NOT USED IN STAGE 6
- Member and task: [NOT USED IN STAGE 6]
- Prompt/purpose and relevant issue/diff: [NOT USED IN STAGE 6]
- Summary of output: [NOT USED IN STAGE 6]
- Human check against actual code, requirements and tests: [NOT USED IN STAGE 6]
- Decision — Accept / Modify / Reject: [NOT USED IN STAGE 6]
- Reason: [NOT USED IN STAGE 6]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [NOT USED IN STAGE 6]
- Copilot noticed: [NOT USED IN STAGE 6]
- Overlap: [NOT USED IN STAGE 6]
- What did the human reviewer notice that Copilot did not: [NOT USED IN STAGE 6]
- What did Copilot identify that the human reviewer initially missed: [NOT USED IN STAGE 6]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [NOT USED IN STAGE 6]
- Which evidence justified merge approval: [NOT USED IN STAGE 6]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [Tobyn]
- Implementation: [Markdown work and Code implementation 1f3c623]
- Testing: [no testing ran in stage 6]
- Review: [Happy with the stage 6 state]
- Issue refinement: [Identified missing code in 3 classes and used existing classes to fill in missing code]
- Design and responsibility discussion: [Organiziing group and group workflow]
- Debugging or integration: [no testing or debugging in stage 6 ]
- Documentation or team support: [Documentation written here with all 3 team memeber]

- Member: [Hanyia]
- Implementation: [Was not done for this section.]
- Testing: [Was not done for this section.]
- Review: [Helped in reviewing work after finished.]
- Issue refinement: [Was not done for this section.]
- Design and responsibility discussion: [Was not done for this section.]
- Debugging or integration: [Was not done for this section.]
- Documentation or team support: [Supported development of documentation.]

- Member: [Hayden]
- Implementation: [not for this section]
- Testing: [open and ran some files to see what the issue is for the requriments ]
- Review: [work and evidence]
- Issue refinement: [not for this section]
- Design and responsibility discussion: [what are the issues for the functional requriments ]
- Debugging or integration: [not for this section]
- Documentation or team support: [wrote up the begging bit of stage 6 being a requriments to issue section]

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

[Identify issues > documented issues > implement code > test > push to main branch > uppdated documentation]

## M Completion and handover

- Starting SHA: [c950052]
- Final Stage 6 code SHA: [1f3c623]
- Test command: [Tests to be run in stage 6]
- Working directory: [st1-assessment-3]
- Observed result: [Stage 6 complete!]
- PR and another-member reviewer: [No Push Requests]
- Unresolved issue or none: [None]
- Stage 7 handover status: [ready for tutor checkpoint]
- Final submitted SHA if later than tested SHA: [1f3c623]

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
