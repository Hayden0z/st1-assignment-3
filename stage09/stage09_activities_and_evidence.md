# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- Friday Group 3-->
Members and responsibilities: <!-- Hayden Ozimek * Hayden0z, UG stage nine Tobyn Dwyer * tobynjames, Hanyia Iftikhar * ArduinoO121 both review    -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- week 8 done -->

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity |Domain State |Must be there so patient is corrected connected to the correct appioment  |
| Appointment history |Domain State |dta that must stay avaliable because past appioments will be needed for viewing and to learn from  |
| Temporary menu choice |Trasient State |is needed when a user is using a interface  |
| Practitioner specialty |Domain State |Is a proptey of the practioner is used for finding the right practioner for a appioment  |
| Debug print output |Trasient State |Is temporay delevoper information |
| Appointment status |Domain State |is Requried as it tracks a appiomet's status whether it is Sschculed,completed or Cancclled   |

What is intentionally lost on exit? <!-- it's short form data like temporay vaules or menu examples that are lost when a application is closed   -->

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key |appioment |the date of the appioment |returns datetime and appioment ID does not modify it |uses existing appioment id and datetime |
| select_appointments |appioments, practionersID, status |list appioments |sorts and filters appioments |must not change orignial  |
| Service listing |appioments, practionersID |list appioments |Checks practioner and gets matching appioments |Practioner must exist |
| Console |User input |result or a message |shows menu,reads input |Handles errors |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts: <!-- patient ID/name comes from a regeistered patient and a Patient ID needs to be valid and unqiue practitioner ID/name/specialty comes from a regeistered practioner and the ID must be valid and unique. appointment ID/actual participants/date_time/status refences reqistered patient and practioner,appioment ID must be unique Status is a appioment value and datetime uses a existing datetime contract   -->

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input |Domain class is doing user input |the console should ask for input Appointment.cancel should only change the status  |
| Service prints/reads the menu |Service is doing user interface |the console should dispaly user interface like menus while Services should be handleing bussiness logic instead   |
| Query sorts its source in place |changes the orginal list |the query should be return a new sorted list wothout changing the orginal source  |
| Store prints Appointment saved |store happens when output happens  |The Store should save and return data the console should display messages  |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check: <!-- For appointments.sort(key=appointment_sort_key), the original list is sorted it returns None, and the list identity stays the same. For result = sorted(appointments, key=appointment_sort_key) the original list is unchanged a new sorted list is returned and the result has a different identity. A meaningful mutation check is to save a copy of the original list and compare it after sorting. Checking only the length is not enough because the order may change even when the number of appointments stays the same. -->

Score-example prediction and explanation of passing the named key: <!-- The appointments will be sorted by date time first and then appointment ID if two appointments have the same time. Passing appointment sort key as the key tells the platform example Python which values to use. Python calls the function for each appointment and uses the returned values to determine the order. -->

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion: <!-- The diffrence between cancellation and delete.Cancellation changes the appointment's status to Canclled  instead of deleting it, so the appointment history is kept.for example After cancelling A1, it can still be found using appointment lookup, showing the record is retained. Listing all statuses also shows A1 as Cancelled. A SCHEDULED only list should not show A1 because its status is no longer Scheduled, even though the appointment still exists.   -->

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- make it it's own function  -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 Filter by practitioner | Appointments, practitioner ID | select_appointments() | Only matching appointments returned | QRY-01 |
| QRY-02 Filter by status | Appointments, status | select_appointments() | Only matching status returned | QRY-02 |
| QRY-03 Sort appointments | Appointment list | appointment_sort_key() | Sorted by date/time then appointment ID | QRY-03 |
| QRY-04 List practitioner appointments | Practitioner ID, status | list_practitioner_appointments() | List returned or error raised | QRY-04 |
| FP-01 Pure query | Same inputs | Query functions | Same output each time | FP-01 |
| FP-02 No mutation | Appointment list | Query functions | Original list unchanged | FP-02 |
| FP-03 Named key | Appointment list | Sorting | Uses appointment_sort_key() | FP-03 |
| UI-01 Booking and cancellation | Appointment data | Console and services | Booking, cancellation and listing work | UI-01 |
| UI-02 Invalid input handling | Invalid ID, status or menu choice | Console and services | Error shown, no crash | UI-02 |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: <!-- An empty result means no appointments matched the filter. An unknown practitioner or appointment raises a LookupError. And a invalid ID or status raises a ValueError. The console converts status text into an AppointmentStatus enum before calling services. Appointments use the actual Patient and Practitioner objects.  -->

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| QRY-01 | queries.py | Only requested practitioner's appointments are returned | Pass | QRY-01 |
| QRY-02 | queries.py | Status filter works and None returns all statuses | Pass | QRY-02 |
| QRY-03 | queries.py | Appointments sorted by date/time then appointment ID | Pass | QRY-03 |
| QRY-04 | services.py | Valid practitioner returns list, invalid practitioner raises LookupError | Pass | QRY-04 |
| FP-01 | queries.py | Repeated calls return the same result | Pass | FP-01 |
| FP-02 | queries.py | Original list remains unchanged after query | Pass | FP-02 |
| FP-03 | queries.py | Sorting uses appointment_sort_key() | Pass | FP-03 |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- The query functions are pure because they do not use hidden state, global variables, input() or print(). They only use the values provided as parameters, and return results without modifying -->
What the tests do and do not establish: <!-- The tests establish that filtering, sorting status handling, and service validation work correctly. They also show that the query does not modify the source list, produces consistent results. However, passing tests do not prove absolute correctness because they only cover the cases that were tested, however won't test everycase and future ones as well  -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow |Register patient 1 practioner 1 and 2 and appioment 1 reject conflict booking made second appioment and canceled the first found patient practioner and appioment and exited |to book and cancel appioments listing and filtering correctlt |appioment was still retained after cancellation anf freed slots allowed a thrid appioment  |UI-o1 |
| UI-02 invalid-input recovery |error meassage example please incoorrect time and blank space  |eroor message displayed |the state of everythings stays unchanges as the input values are incorrect |UI-02 |
| Automated service workflow | python -m pytest -q  |all tests pass | 17 passesd |UI-03 |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.
Before A1 was canceled A1 had Scheduled but when it became cancelled it could still be found when finding the status and writing down cancelled,and with the 1st practitioner their time slot got freed up when the A1 appointment got cancelled.   

Why the same patient can book with a different practitioner is that it's based on the practitioner time if A1 is booked at the same time it will conflict and have an error however it will pass if it was under a different practitioner even if everything else is the same.  


## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- the menu was created and based of my work from an old assessment that has a menu format  -->
Actual prompt/context supplied: <!--in python how it’s documented with adding print with blanks that give it space. Some piece of the code               choice = input("Enter 1, 2, 3 or 4: ")
      if choice == "1":
       print ("maze")
       themazegame()
      elif choice == "2":
       thegussinggame()
      elif choice == "3": #Game of your choice
       rockpapersicssors()
      elif choice == "4":
        print ("Thanks for using the program.")
        break
      else:
       print("Please enter 1,2,3 or 4 only")
 -->
Actual response: <!-- all my previous work just reworked for this assessment   -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |

|wanting to add lower() to the status filters|low|low|rejected has I think it is unnecessary|no change|the status verification is not required has a error will pop up to instruct the user |

|added try and expect blocks before and after menu |invalid data for example dates and ID that are invalid   | medium |this was accepted because it one of the requirements that errors don’t crash the program  |added try and expect blocks  |Invalid inputs now are displayed with a error message  |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- Domain invariants are handled by the domain classes for example valid appointment statements changes.the shared stored collections manages collections of patient,practitioners and appointments.service condition does validation, booking,cancellation booking and patient,practitioner and appointment lookups. pure queries only filter and sort data without changing anything and lastly console responsible for user input and output as well error messages.Keeping all of these separates lets the smartcare system easier to maintain and test -->


## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- the main concern was using just one shared smartcare data store has all information was on the one.so when a new menu happens opens and closes all previous data on practitioner,patient and appointment will disappear and has nothing to do with sorting data     -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- adding lower() to the status I thought it was too much and kept it simpled as it made more sense and wosn;t overdoing it  -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- how I proved that canceled appointments remained retrievable and listable in the same session is making an appointment called A1 then quickening Canceling it I then went to list practitioner appointments when I filtered the appointments to Canceled it would show but not when Schulled it didn’t show.This showed that the appointment was still retained in the system even after being canceled   →


## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!--select_appointments is pure because it only uses values given to it as inputs as the result there is no hidden state input/output or change original list which makes it pure a side effect to break purity is modifying the original list like using appointments.sort for example  -->

2. Which explicit inputs are needed, and why avoid a global store? <!--  some explicit inputs that are needed are appointment list and Practitioner ID these are needed so that select appointments can operate which is filtering and sorting.global store is avoided because it introduces hidden states and functions would depend on outside data making it harder to test   -->

3. How can a new list reuse Appointment objects safely? <!-- a new list can reuse the objects of appointments and safely is create a new box for the objects without changing them.this is done with select_appointment and is safe because it does not modify the original list just filters it -->

4. Why use a named key, and what breaks equal-time ties? <!-- named keys lets code be easily reused as for this example python, appiomentsortkey() tells the platform(python) to sort appointments by date time then appointment ID.The appointment ID is a tie breaker for when two appointments have the same time their  each have it’s own ID to break it up  -->

5. How do default and explicit status filters differ? <!-- the default shows all appointments while explicit will show a selected amount this being all appointment for default and a example for explicit would be Completed which would show all Completed appointments  -->

6. How do empty, unknown practitioner and invalid filter cases differ? <!-- a empty results means a practitioner exists but no appointments match a filter so nothing shows.an unknow Practitioner will cause a lookup error.invalid filter means the status value is not valid which causes a invalidError   -->

7. Which console errors recover, and how is unchanged state checked? <!--console errors for example unknown appointments or booking conflicts will recover because the menu catches it and will continue running the program.Unchanged states are checked by successfully finding or listing records after an error.detailing that no data was changed from the error   -->

8. What is data integrity for registered participants, conflicts and history? <!-- data integrity means keeping data accurate.Registered practitioners and patients must exist to make an appointment practitioners must avoid double bookings at the same time and all appointments must be kept for improvement and look back this is done with changing the status to cancelled instead of deleting.To ensure that everything is correct -->

9. What is Copilot's review role, and who verifies findings? <!--Copilot's review role is just to review work and give recommendations and help finding issues. It does make the final decisions.Humans(developers) verifies findings by running,looking and testing code and with copilot people are responsible for confirming if the copilot is correct. 

10. How do pure functions and OOP responsibilities work together? <!-- Pure functions and OOP responsibilities work together by keeping each bit of a program focused on one job. Pure functions for example select_appointment() handle sorting of data while OOP more focuses on validation and stored objects.This separation of the two makes code much easier to understand,test and maintain →


## H. Review, completion and common handover

Issues and bounded branches: <!-- on the main one after the debugging branch merged  -->
PR/diff and another-member human reviewer: <!--Tobyn and Hanyia -->
Review responses and Copilot comparison: <!-- good and works -->
Integrated common Stage 9 SHA: <!-- stage 8 completed -->
Full regression command, working directory, actual count/result and evidence: <!--python - m pytest -q and 17 passed    -->
README run instructions and scope/limitations: <!--<!--python - m pytest -q and python main.py –intreactive  -->
Unresolved issues and support/action: <!-- no know unresolved issues stage nine  functionally works and operates   -->
UG common candidate / PG future branch plan: <!-- week 9 Completed -->


- [ x ] Query contracts, purity, new lists and named-key ordering verified.
- [ x ] Service empty/unknown/invalid cases and cancellation history verified.
- [ x ] Every console command and invalid-input recovery demonstrated.
- [ x ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ x ] Human design, Copilot critique, review and integration recorded honestly.
- [ x ] Reflections and ten formative responses completed.
- [ x ] README updated; earlier code/tests/records preserved.
- [ x ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
