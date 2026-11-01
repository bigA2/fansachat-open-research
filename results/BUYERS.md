# Who buys each plan, and what FansaChat can do for them

Data: O*NET 31.0 task statements (USDOL/ETA, CC BY 4.0) for the 88 fictional people in `results/SOLO.md` (28) and `results/TEAMS.md` (60), 804 person-tasks (444 different tasks). Laya scores from `results/automation.json` are shown as a signal only.

**How tasks were marked** (a human-style judgement written for this file, not a model score):

- **major**: FansaChat can do most of the task now with apps in our catalog (email, calendar, sheets, CRM, accounting, forms, social, AI step).
- minor: an automation helps one part (collecting data, drafting, reminders), but a person does the core work.
- no fit: judgement, negotiation, physical work, teaching/therapy, or work inside specialist software we do not connect.

The "automation" column is the workflow FansaChat would build for that task. Nothing here is tested yet: it is a test list.

## Summary

| plan | price (ours) | people | tasks | major | minor | no fit |
|---|---|---|---|---|---|---|
| Starter | $15 | 14 | 140 | 20 (14%) | 53 (37%) | 67 (47%) |
| Pro | $45 | 14 | 140 | 31 (22%) | 60 (42%) | 49 (35%) |
| Team | $149 | 10 | 96 | 10 (10%) | 47 (48%) | 39 (40%) |
| Scale | $299 | 50 | 428 | 115 (26%) | 186 (43%) | 127 (29%) |

Laya vs our marking: of tasks we call **no fit**, 108 had Laya automatable >= 0.7 and 174 had < 0.7. Of **major** tasks, 96 had >= 0.7 and 80 had < 0.7. Laya often scores teaching, design judgement and face-to-face work high, so it should not be used alone to choose test cases.

## Starter ($15)

**Who buys:** Event planner, Freelance bookkeeper, Freelance designer, Freelance writer, Indie software developer, Insurance agent, Personal trainer, Photographer, Real estate agent, Solo lawyer, Tax preparer, Therapist in private practice, Tutor, Virtual assistant.

**Why:** One person running a small practice or freelance business. They live in email, a calendar, a sheet and an accounting app (QuickBooks appears for most). They buy to stop doing admin by hand: bookings and reminders, invoices and payment chasing, client intake, filing documents. 2,000 runs is enough for a few daily workflows.

**Top automations for this plan** (tasks): AI first drafts (8); design asset delivery (7); keep records up to date (6); sync and check bookkeeping (5); research digests (4); client intake (4).

### Kofi Usman, Real estate agent

O*NET: Real Estate Sales Agents. Apps in our catalog: Canva, Docusign, Facebook Pages, Front, Google Ads, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft Teams, Quickbooks Online, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Prepare documents such as representation contracts, purchase agreements, closing statements, deeds, and leases. | **major** | 0.763 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Coordinate appointments to show homes to prospective buyers. | **major** | 0.639 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Generate lists of properties that are compatible with buyers' needs and financial resources. | **major** | 0.934 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Interview clients to determine what kinds of properties they are seeking. | **major** | 0.084 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Present purchase offers to sellers for consideration. | minor | 0.108 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Confer with escrow companies, lenders, home inspectors, and pest control operators to ensure that terms and conditions of purchase agreements are met before closing dates. | minor | 0.055 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Advise clients on market conditions, prices, mortgages, legal requirements, and related matters. | minor | 0.247 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Compare a property with similar properties that have recently sold to determine its competitive market price. | minor | 0.63 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Act as an intermediary in negotiations between buyers and sellers, generally representing one or the other. | no fit | 0.543 | - |
| Appraise properties to determine loan values. | no fit | 0.403 | - |

### Lena Dlamini, Tax preparer

O*NET: Tax Preparers. Apps in our catalog: Microsoft Excel 365, Microsoft Outlook, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Interview clients to obtain additional information on taxable income and deductible expenses and allowances. | **major** | 0.0 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Compute taxes owed or overpaid, using adding machines or personal computers, and complete entries on forms, following tax form instructions and tax tables. | minor | 0.872 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Furnish taxpayers with sufficient information and advice to ensure correct tax form completion. | minor | 0.469 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Review financial records, such as income statements and documentation of expenditures to determine forms needed to prepare tax returns. | minor | 0.632 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Check data input or verify totals on forms prepared by others to detect errors in arithmetic, data entry, or procedures. | minor | 0.911 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Answer questions and provide future tax planning to clients. | minor | 0.959 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Use all appropriate adjustments, deductions, and credits to keep clients' taxes to a minimum. | no fit | 0.822 | - |
| Prepare or assist in preparing simple to complex tax returns for individuals or small businesses. | no fit | 1.0 | - |
| Explain federal and state tax laws to individuals and companies. | no fit | 0.0 | - |
| Consult tax law handbooks or bulletins to determine procedures for preparation of atypical returns. | no fit | 0.051 | - |

### Mateo Khan, Freelance bookkeeper

O*NET: Bookkeeping, Accounting, and Auditing Clerks. Apps in our catalog: Dropbox, Facebook Pages, Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Operate computers programmed with accounting software to record, store, and analyze information. | **major** | 0.938 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Monitor status of loans and accounts to ensure that payments are up to date. | **major** | 0.76 | Job done or due date -> create invoice -> send -> overdue reminder |
| Reconcile records of bank transactions. | **major** | 0.8 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare and process payroll information. | minor | 0.754 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Check figures, postings, and documents for correct entry, mathematical accuracy, and proper codes. | minor | 0.862 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare bank deposits by compiling data from cashiers, verifying and balancing receipts, and sending cash, checks, or other forms of payment to banks. | minor | 0.784 | Payment received -> record in accounting + sheet -> receipt to client |
| Comply with federal, state, and company policies, procedures, and regulations. | minor | 0.093 | Recurring compliance/renewal date -> reminder + log record |
| Receive, record, and bank cash, checks, and vouchers. | minor | 0.584 | Payment received -> record in accounting + sheet -> receipt to client |
| Calculate and prepare checks for utilities, taxes, and other payments. | minor | 0.908 | Job done or due date -> create invoice -> send -> overdue reminder |
| Operate 10-key calculators, typewriters, and copy machines to perform calculations and produce documents. | no fit | 0.922 | - |

### Nadia Reyes, Photographer

O*NET: Photographers. Apps in our catalog: Facebook Pages, Google Drive, Microsoft Excel 365, Quickbooks Online, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Transfer photographs to computers for editing, archiving, and electronic transmission. | **major** | 0.949 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Manipulate and enhance scanned or digital images to create desired effects, using computers and specialized software. | minor | 0.93 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Enhance, retouch, and resize photographs and negatives, using airbrushing and other techniques. | minor | 0.86 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Adjust apertures, shutter speeds, and camera focus according to a combination of factors, such as lighting, field depth, subject motion, film type, and film speed. | no fit | 0.878 | - |
| Create artificial light, using flashes and reflectors. | no fit | 0.466 | - |
| Determine desired images and picture composition, selecting and adjusting subjects, equipment, and lighting to achieve desired effects. | no fit | 0.835 | - |
| Use traditional or digital cameras, along with a variety of equipment, such as tripods, filters, and flash attachments. | no fit | 0.13 | - |
| Take pictures of individuals, families, and small groups, either in studio or on location. | no fit | 0.713 | - |
| Test equipment prior to use to ensure that it is in good working order. | no fit | 0.214 | - |
| Estimate or measure light levels, distances, and numbers of exposures needed, using measuring devices and formulas. | no fit | 0.952 | - |

### Omar Young, Personal trainer

O*NET: Exercise Trainers and Group Fitness Instructors. Apps in our catalog: Microsoft Excel 365, Microsoft Outlook, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Monitor participants' progress and adapt programs as needed. | minor | 0.885 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Observe participants and inform them of corrective measures necessary for skill improvement. | no fit | 0.536 | - |
| Offer alternatives during classes to accommodate different levels of fitness. | no fit | 0.611 | - |
| Plan routines, choose appropriate music, and choose different movements for each set of muscles, depending on participants' capabilities and limitations. | no fit | 0.409 | - |
| Evaluate individuals' abilities, needs, and physical conditions, and develop suitable training programs to meet any special requirements. | no fit | 0.115 | - |
| Instruct participants in maintaining exertion levels to maximize benefits from exercise routines. | no fit | 0.0 | - |
| Teach and demonstrate use of gymnastic and training equipment, such as trampolines and weights. | no fit | 0.024 | - |
| Explain and enforce safety rules and regulations governing sports, recreational activities, and the use of exercise equipment. | no fit | 0.0 | - |
| Teach proper breathing techniques used during physical exertion. | no fit | 0.0 | - |
| Maintain fitness equipment. | no fit | 0.479 | - |

### Priya Novak, Event planner

O*NET: Meeting, Convention, and Event Planners. Apps in our catalog: Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft Outlook.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Maintain records of event aspects, including financial details. | **major** | 0.334 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Consult with customers to determine objectives and requirements for events, such as meetings, conferences, and conventions. | minor | 0.107 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Review event bills for accuracy and approve payment. | minor | 0.852 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Coordinate services for events, such as accommodation and transportation for participants, facilities, catering, signage, displays, special needs requirements, printing and event security. | minor | 0.493 | Event booked -> vendor/venue/attendee emails + logistics checklist |
| Arrange the availability of audio-visual equipment, transportation, displays, and other event needs. | minor | 0.661 | Event booked -> vendor/venue/attendee emails + logistics checklist |
| Confer with staff at a chosen event site to coordinate details. | minor | 0.003 | Event booked -> vendor/venue/attendee emails + logistics checklist |
| Inspect event facilities to ensure that they conform to customer requirements. | no fit | 0.221 | - |
| Monitor event activities to ensure compliance with applicable regulations and laws, satisfaction of participants, and resolution of any problems that arise. | no fit | 0.688 | - |
| Negotiate contracts with such service providers and suppliers as hotels, convention centers, and speakers. | no fit | 0.058 | - |
| Evaluate and select providers of services according to customer requirements. | no fit | 0.721 | - |

### Quinn Duarte, Tutor

O*NET: Tutors. Apps in our catalog: Facebook Pages, Google Drive, Microsoft Excel 365, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Schedule tutoring appointments with students or their parents. | **major** | 0.17 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Assess students' progress throughout tutoring sessions. | minor | 0.788 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Collaborate with students, parents, teachers, school administrators, or counselors to determine student needs, develop tutoring plans, or assess student progress. | minor | 0.049 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Provide feedback to students, using positive reinforcement techniques to encourage, motivate, or build confidence in students. | no fit | 0.151 | - |
| Review class material with students by discussing text, working solutions to problems, or reviewing worksheets or other assignments. | no fit | 0.44 | - |
| Teach students study skills, note-taking skills, and test-taking strategies. | no fit | 0.04 | - |
| Provide private instruction to individual or small groups of students to improve academic performance, improve occupational skills, or prepare for academic or occupational tests. | no fit | 0.819 | - |
| Participate in training and development sessions to improve tutoring practices or learn new tutoring techniques. | no fit | 0.104 | - |
| Monitor student performance or assist students in academic environments, such as classrooms, laboratories, or computing centers. | no fit | 0.556 | - |
| Organize tutoring environment to promote productivity and learning. | no fit | 0.905 | - |

### Rafael Turner, Insurance agent

O*NET: Insurance Sales Agents. Apps in our catalog: Facebook Pages, Front, LinkedIn, Microsoft Excel 365, Microsoft Outlook, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Perform administrative tasks, such as maintaining records and handling policy renewals. | **major** | 0.767 | Recurring compliance/renewal date -> reminder + log record |
| Explain features, advantages, and disadvantages of various policies to promote sale of insurance plans. | minor | 0.101 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Seek out new clients and develop clientele by networking to find new customers and generate lists of prospective clients. | minor | 0.168 | New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence |
| Call on policyholders to deliver and explain policy, to analyze insurance program and suggest additions or changes, or to change beneficiaries. | minor | 0.118 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Confer with clients to obtain and provide information when claims are made on a policy. | minor | 0.076 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Interview prospective clients to obtain data about their financial resources and needs, the physical condition of the person or property to be insured, and to discuss any existing coverage. | minor | 0.029 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Contact underwriter and submit forms to obtain binder coverage. | minor | 0.0 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Customize insurance programs to suit individual customers, often covering a variety of risks. | no fit | 0.055 | - |
| Sell various types of insurance policies to businesses and individuals on behalf of insurance companies, including automobile, fire, life, property, medical and dental insurance, or specialized policies, such as marine, farm/crop, and medical malpractice. | no fit | 0.937 | - |
| Select company that offers type of coverage requested by client to underwrite policy. | no fit | 0.0 | - |

### Sana Castillo, Freelance writer

O*NET: Writers and Authors. Apps in our catalog: Asana, Campaign Monitor, Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, Google Workspace, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, MySQL, Presenton, SendGrid, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Revise written material to meet personal standards and to satisfy needs of clients, publishers, directors, or producers. | minor | 0.546 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Present drafts and ideas to clients. | minor | 0.049 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher. | minor | 0.272 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Conduct research to obtain factual information and authentic detail, using sources such as newspaper accounts, diaries, and interviews. | minor | 0.038 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Vary language and tone of messages based on product and medium. | minor | 0.654 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write articles, bulletins, sales letters, speeches, and other related informative, marketing and promotional material. | minor | 0.942 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write advertising material for use by publication, broadcast, or internet media to promote the sale of goods and services. | minor | 0.498 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write to customers in their terms and on their level so that the script, story, or advertisement message is more readily received. | minor | 0.657 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Prepare works in appropriate format for publication, and send them to publishers or producers. | minor | 0.641 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Write fiction or nonfiction prose, such as short stories, novels, biographies, articles, descriptive or critical analyses, and essays. | no fit | 0.637 | - |

### Tomas Jensen, Freelance designer

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Research the target audience of projects. | minor | 0.578 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Draw and print charts, graphs, illustrations, and other artwork, using computer. | minor | 0.877 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Uma Qureshi, Therapist in private practice

O*NET: Marriage and Family Therapists. Apps in our catalog: Microsoft Excel 365, Microsoft Outlook, Microsoft Teams, Quickbooks Online, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Maintain case files that include activities, progress notes, evaluations, and recommendations. | **major** | 0.634 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Ask questions that will help clients identify their feelings and behaviors. | no fit | 0.072 | - |
| Encourage individuals and family members to develop and use skills and strategies for confronting their problems in a constructive manner. | no fit | 0.0 | - |
| Develop and implement individualized treatment plans addressing family relationship problems, destructive patterns of behavior, and other personal issues. | no fit | 0.714 | - |
| Counsel clients on concerns, such as unsatisfactory relationships, divorce and separation, child rearing, home management, or financial difficulties. | no fit | 0.029 | - |
| Determine whether clients should be counseled or referred to other specialists in such fields as medicine, psychiatry, or legal aid. | no fit | 0.826 | - |
| Supervise other counselors, social service staff, and assistants. | no fit | 0.038 | - |
| Confer with other counselors, doctors, and professionals to analyze individual cases and to coordinate counseling services. | no fit | 0.426 | - |
| Diagnose mental and emotional disorders in clients. | no fit | 0.102 | - |
| Confer with clients to develop plans for posttreatment activities. | no fit | 0.242 | - |

### Victor Xu, Solo lawyer

O*NET: Lawyers. Apps in our catalog: Cisco Webex Meetings, Front, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Interpret laws, rulings and regulations for individuals and businesses. | no fit | 0.632 | - |
| Analyze the probable outcomes of cases, using knowledge of legal precedents. | no fit | 0.105 | - |
| Gather evidence to formulate defense or to initiate legal actions by such means as interviewing clients and witnesses to ascertain the facts of a case. | no fit | 0.095 | - |
| Present and summarize cases to judges and juries. | no fit | 0.133 | - |
| Represent clients in court or before government agencies. | no fit | 0.105 | - |
| Select jurors, argue motions, meet with judges, and question witnesses during the course of a trial. | no fit | 0.48 | - |
| Evaluate findings and develop strategies and arguments in preparation for presentation of cases. | no fit | 0.078 | - |
| Present evidence to defend clients or prosecute defendants in criminal or civil litigation. | no fit | 0.1 | - |
| Advise clients concerning business transactions, claim liability, advisability of prosecuting or defending lawsuits, or legal rights and obligations. | no fit | 0.105 | - |
| Examine legal data to determine advisability of defending or prosecuting lawsuit. | no fit | 0.376 | - |

### Wen Haddad, Virtual assistant

O*NET: Secretaries and Administrative Assistants, Except Legal, Medical, and Executive. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Facebook Pages, Google Docs, Google Drive, Google Sheets, Google Slides, Google Workspace, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, Microsoft Teams, NetSuite.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Create, maintain, and enter information into databases. | **major** | 0.82 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Use computers for various applications, such as database management or word processing. | **major** | 0.804 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Set up and manage paper or electronic filing systems, recording information, updating paperwork, or maintaining documents, such as attendance records, correspondence, or other material. | **major** | 0.823 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Operate electronic mail systems and coordinate the flow of information, internally or with other organizations. | **major** | 0.787 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Schedule and confirm appointments for clients, customers, or supervisors. | **major** | 0.749 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Answer telephones and give information to callers, take messages, or transfer calls to appropriate individuals. | minor | 0.855 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Greet visitors or callers and handle their inquiries or direct them to the appropriate persons according to their needs. | minor | 0.737 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Perform payroll functions, such as maintaining timekeeping information and processing and submitting payroll. | minor | 0.792 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Collect and deposit money into accounts, disburse funds from cash accounts to pay bills or invoices, keep records of collections and disbursements, and ensure accounts are balanced. | minor | 0.901 | Payment received -> record in accounting + sheet -> receipt to client |
| Operate office equipment, such as fax machines, copiers, or phone systems and arrange for repairs when equipment malfunctions. | no fit | 0.867 | - |

### Ximena Ahmed, Indie software developer

O*NET: Software Developers. Apps in our catalog: Airtable, Apache Kafka, Azure DevOps, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Facebook Pages, Figma, GitHub, GitLab, Gmail, Google Docs, Google Drive, Google Sheets, Google Slides, JSON, LinkedIn, Microsoft Excel 365, Microsoft OneNote.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Monitor functioning of equipment to ensure system operates in conformance with specifications. | **major** | 0.651 | App/site/system check fails -> alert to email/Slack + incident task |
| Prepare reports or correspondence concerning project specifications, activities, or status. | **major** | 0.412 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Store, retrieve, and manipulate data for analysis of system capabilities and requirements. | minor | 0.908 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Analyze user needs and software requirements to determine feasibility of design within time and cost constraints. | no fit | 0.674 | - |
| Develop or direct software system testing or validation procedures, programming, or documentation. | no fit | 0.486 | - |
| Confer with systems analysts, engineers, programmers and others to design systems and to obtain information on project limitations and capabilities, performance requirements and interfaces. | no fit | 0.09 | - |
| Coordinate installation of software system. | no fit | 0.233 | - |
| Modify existing software to correct errors, adapt it to new hardware, or upgrade interfaces and improve performance. | no fit | 0.825 | - |
| Analyze information to determine, recommend, and plan installation of a new system or modification of an existing system. | no fit | 0.813 | - |
| Design, develop and modify software systems, using scientific analysis and mathematical models to predict and measure outcomes and consequences of design. | no fit | 0.812 | - |

## Pro ($45)

**Who buys:** Business consultant, Clinic front desk, Course creator and trainer, Guesthouse manager, Marketing lead, Online shop owner, PR and social specialist, Property manager, Recruiter, Restaurant manager, Sales rep, Small-firm accountant, Solo marketer, Web designer.

**Why:** A solo professional or a small owner-run business with more volume: marketers, recruiters, sales reps, property, restaurant, clinic and guesthouse managers, an online shop. They buy for customer-facing volume: answering the same questions, leads into a CRM, orders and stock, reports. More runs (10,000) and AI builds (400).

**Top automations for this plan** (tasks): scheduled reports (11); research digests (8); answer common questions (8); AI first drafts (6); sync and check bookkeeping (6); route incoming messages (5).

### Yusuf Sato, Solo marketer

O*NET: Market Research Analysts and Marketing Specialists. Apps in our catalog: Airtable, Asana, Canva, Dropbox, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, MySQL, NetSuite, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Measure and assess customer and employee satisfaction. | **major** | 0.564 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Monitor industry statistics and follow trends in trade literature. | **major** | 0.682 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Prepare reports of findings, illustrating data graphically and translating complex findings into written text. | minor | 0.881 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Seek and provide information to help companies determine their position in the marketplace. | minor | 0.929 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Conduct research on consumer opinions and marketing strategies, collaborating with marketing professionals, statisticians, pollsters, and other professionals. | minor | 0.664 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Collect and analyze data on customer demographics, preferences, needs, and buying habits to identify potential markets and factors affecting product demand. | minor | 0.827 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Devise and evaluate methods and procedures for collecting data, such as surveys, opinion polls, or questionnaires, or arrange to obtain existing data. | minor | 0.334 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Gather data on competitors and analyze their prices, sales, and method of marketing and distribution. | minor | 0.746 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Attend staff conferences to provide management with information and proposals concerning the promotion, distribution, design, and pricing of company products or services. | minor | 0.0 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Direct trained survey interviewers. | no fit | 0.055 | - |

### Zara Bose, Marketing lead

O*NET: Marketing Managers. Apps in our catalog: Airtable, Asana, Canva, Confluence, Constant Contact, Dropbox, Drupal, Facebook Pages, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Compile lists describing product or service offerings. | **major** | 0.744 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Use sales forecasting or strategic planning to ensure the sale and profitability of products, lines, or services, analyzing business developments and monitoring market trends. | minor | 0.941 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Evaluate the financial aspects of product development, such as budgets, expenditures, research and development appropriations, or return-on-investment and profit-loss projections. | minor | 0.753 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Initiate market research studies, or analyze their findings. | minor | 0.584 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Consult with buying personnel to gain advice regarding the types of products or services expected to be in demand. | minor | 0.01 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Formulate, direct, or coordinate marketing activities or policies to promote products or services, working with advertising or promotion managers. | no fit | 0.598 | - |
| Identify, develop, or evaluate marketing strategy, based on knowledge of establishment objectives, market characteristics, and cost and markup factors. | no fit | 0.815 | - |
| Direct the hiring, training, or performance evaluations of marketing or sales staff and oversee their daily activities. | no fit | 0.81 | - |
| Develop pricing strategies, balancing firm objectives and customer satisfaction. | no fit | 0.594 | - |
| Consult with product development personnel on product specifications, such as design, color, or packaging. | no fit | 0.078 | - |

### Arjun Iyer, PR and social specialist

O*NET: Public Relations Specialists. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Salesforce, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Post and update content on the company's Web site and social media outlets. | **major** | 0.604 | Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it |
| Respond to requests for information from the media or designate an appropriate spokesperson or information source. | minor | 0.147 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Plan or direct development or communication of programs to maintain favorable public or stockholder perceptions of an organization's accomplishments, agenda, or environmental responsibility. | minor | 0.099 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write press releases or other media communications to promote clients. | minor | 0.687 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Confer with other managers to identify trends or key group interests or concerns or to provide advice on business decisions. | minor | 0.041 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Prepare or edit organizational publications, such as employee newsletters or stockholders' reports, for internal or external audiences. | minor | 0.736 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Arrange public appearances, lectures, contests, or exhibits for clients to increase product or service awareness or to promote goodwill. | minor | 0.175 | Event booked -> vendor/venue/attendee emails + logistics checklist |
| Establish or maintain cooperative relationships with representatives of community, consumer, employee, or public interest groups. | no fit | 0.034 | - |
| Coach client representatives in effective communication with the public or with employees. | no fit | 0.8 | - |
| Study the objectives, promotional policies, or needs of organizations to develop public relations strategies that will influence public opinion or promote ideas, products, or services. | no fit | 0.189 | - |

### Bea Park, Recruiter

O*NET: Human Resources Specialists. Apps in our catalog: Airtable, Cisco Webex Meetings, Drupal, Facebook Pages, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Matrix, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Schedule or administer skill, intelligence, psychological, or drug tests for current or prospective employees. | **major** | 0.18 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Prepare or maintain employment records related to events, such as hiring, termination, leaves, transfers, or promotions, using human resources management system software. | **major** | 0.843 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Inform job applicants of details such as duties and responsibilities, compensation, benefits, schedules, working conditions, or promotion opportunities. | **major** | 0.0 | New application -> tracker record -> AI screen summary -> interview invite |
| Interpret and explain human resources policies, procedures, laws, standards, or regulations. | minor | 0.43 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Hire employees and process hiring-related paperwork. | minor | 0.03 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Administer employee benefit plans. | minor | 0.17 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Conduct reference or background checks on job applicants. | minor | 0.808 | New application -> tracker record -> AI screen summary -> interview invite |
| Review employment applications and job orders to match applicants with job requirements. | minor | 1.0 | New application -> tracker record -> AI screen summary -> interview invite |
| Maintain current knowledge of Equal Employment Opportunity (EEO) and affirmative action guidelines and laws, such as the Americans with Disabilities Act (ADA). | no fit | 0.0 | - |
| Address employee relations issues, such as harassment allegations, work complaints, or other employee concerns. | no fit | 0.215 | - |

### Carlos Watanabe, Business consultant

O*NET: Management Analysts. Apps in our catalog: Airtable, Apache Kafka, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Facebook Pages, GitHub, Google Docs, Google Drive, Google Slides, JSON, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft Power BI, Microsoft SQL Server, Microsoft SharePoint, Microsoft Teams.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Develop and implement records management program for filing, protection, and retrieval of records, and assure compliance with program. | **major** | 0.832 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Gather and organize information on problems or procedures. | minor | 0.836 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Analyze data gathered and develop solutions or alternative methods of proceeding. | minor | 0.857 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Document findings of study and prepare recommendations for implementation of new systems, procedures, or organizational changes. | minor | 0.351 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Design, evaluate, recommend, and approve changes of forms and reports. | minor | 0.815 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Confer with personnel concerned to ensure successful functioning of newly implemented systems or procedures. | no fit | 0.0 | - |
| Plan study of work problems and procedures, such as organizational change, communications, information flow, integrated production methods, inventory control, or cost analysis. | no fit | 0.035 | - |
| Interview personnel and conduct on-site observation to ascertain unit functions, work performed, and methods, equipment, and personnel used. | no fit | 0.037 | - |
| Prepare manuals and train workers in use of new forms, reports, procedures or equipment, according to organizational policy. | no fit | 0.029 | - |
| Review forms and reports and confer with management and users about format, distribution, and purpose, identifying problems and improvements. | no fit | 0.068 | - |

### Divya Tanaka, Sales rep

O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products. Apps in our catalog: Airtable, Cisco Webex Meetings, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Dynamics CRM, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Check stock levels and reorder merchandise as necessary. | **major** | 0.91 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Answer customers' questions about products, prices, availability, product uses, and credit terms. | **major** | 0.942 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Consult with clients after sales or contract signings to resolve problems and to provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Prepare sales contracts and order forms. | **major** | 0.631 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Provide customers with product samples and catalogs. | **major** | 0.1 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Recommend products to customers, based on customers' needs and interests. | minor | 0.159 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Estimate or quote prices, credit or contract terms, warranties, and delivery dates. | minor | 0.774 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate with retail merchants to improve product exposure, such as shelf positioning and advertising. | no fit | 0.391 | - |
| Plan, assemble, and stock product displays in retail stores, or make recommendations to retailers regarding product displays, promotional programs, and advertising. | no fit | 0.792 | - |
| Negotiate details of contracts and payments. | no fit | 0.109 | - |

### Emeka Santos, Property manager

O*NET: Property, Real Estate, and Community Association Managers. Apps in our catalog: Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Direct collection of monthly assessments, rental fees, and deposits and payment of insurance premiums, mortgage, taxes, and incurred operating expenses. | **major** | 1.0 | Job done or due date -> create invoice -> send -> overdue reminder |
| Plan, schedule, and coordinate general maintenance, major repairs, and remodeling or construction projects for commercial or residential properties. | minor | 0.838 | New client/project -> create tasks in project tool -> status updates to channel |
| Prepare detailed budgets and financial reports for properties. | minor | 0.787 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Act as liaisons between on-site managers or tenants and owners. | minor | 0.26 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Solicit and analyze bids from contractors for repairs, renovations, and maintenance. | minor | 0.361 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Manage and oversee operations, maintenance, administration, and improvement of commercial, industrial, or residential properties. | no fit | 0.223 | - |
| Meet with clients to negotiate management and service contracts, determine priorities, and discuss the financial and operational status of properties. | no fit | 0.038 | - |
| Clean common areas, change light bulbs, and make minor property repairs. | no fit | 0.714 | - |
| Inspect grounds, facilities, and equipment routinely to determine necessity of repairs or maintenance. | no fit | 0.098 | - |
| Direct and coordinate the activities of staff and contract personnel and evaluate their performance. | no fit | 0.139 | - |

### Fatima Rossi, Small-firm accountant

O*NET: Accountants and Auditors. Apps in our catalog: Facebook Pages, Google Docs, Google Sheets, Google Slides, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Tableau, Workday.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Process invoices for payment. | **major** | 0.805 | Job done or due date -> create invoice -> send -> overdue reminder |
| Review accounts for discrepancies and reconcile differences. | **major** | 0.935 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare, examine, or analyze accounting records, financial statements, or other financial reports to assess accuracy, completeness, and conformance to reporting and procedural standards. | minor | 0.688 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare adjusting journal entries. | minor | 0.087 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Inspect account books and accounting systems for efficiency, effectiveness, and use of accepted accounting procedures to record transactions. | minor | 0.463 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare detailed reports on audit findings. | minor | 0.096 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare, analyze, or verify annual reports, financial statements, and other records, using accepted accounting and statistical procedures to assess financial condition and facilitate financial planning. | minor | 0.637 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Collect and analyze data to detect deficient controls, duplicated effort, extravagance, fraud, or non-compliance with laws, regulations, and management policies. | minor | 0.298 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Review data about material assets, net worth, liabilities, capital stock, surplus, income, or expenditures. | minor | 0.118 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Compute taxes owed and prepare tax returns, ensuring compliance with payment, reporting, or other tax requirements. | no fit | 0.974 | - |

### Gabriel Zhou, Restaurant manager

O*NET: Food Service Managers. Apps in our catalog: Facebook Pages, Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Keep records required by government agencies regarding sanitation or food subsidies. | **major** | 0.948 | Recurring compliance/renewal date -> reminder + log record |
| Schedule staff hours and assign duties. | **major** | 0.043 | Staff rota in sheet -> send each person their shifts/duties + change alerts |
| Maintain food and equipment inventories, and keep inventory records. | **major** | 0.702 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Investigate and resolve complaints regarding food quality, service, or accommodations. | minor | 0.82 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Monitor budgets and payroll records, and review financial transactions to ensure that expenditures are authorized and budgeted. | minor | 0.79 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Monitor employee and patron activities to ensure liquor regulations are obeyed. | no fit | 0.845 | - |
| Greet guests, escort them to their seats, and present them with menus and wine lists. | no fit | 0.333 | - |
| Count money and make bank deposits. | no fit | 0.81 | - |
| Establish standards for personnel performance and customer service. | no fit | 0.069 | - |
| Perform some food preparation or service tasks, such as cooking, clearing tables, and serving food and drinks when necessary. | no fit | 0.666 | - |

### Hana Hughes, Clinic front desk

O*NET: Medical Secretaries and Administrative Assistants. Apps in our catalog: Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Compile and record medical charts, reports, or correspondence, using typewriter or personal computer. | **major** | 0.779 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Schedule and confirm patient diagnostic appointments, surgeries, or medical consultations. | **major** | 0.826 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Transmit correspondence or medical records by mail, e-mail, or fax. | **major** | 0.952 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Maintain medical records, technical library, or correspondence files. | **major** | 0.798 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Receive and route messages or documents, such as laboratory results, to appropriate staff. | **major** | 0.874 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Interview patients to complete documents, case histories, or forms, such as intake or insurance forms. | **major** | 0.62 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Answer telephones and direct calls to appropriate staff. | minor | 0.933 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Transcribe recorded messages or practitioners' diagnoses or recommendations into patients' medical records. | minor | 0.922 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Complete insurance or other claim forms. | minor | 0.035 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Greet visitors, ascertain purpose of visit, and direct them to appropriate staff. | no fit | 0.486 | - |

### Ivan Ortiz, Guesthouse manager

O*NET: Lodging Managers. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Monitor the revenue activity of the hotel or facility. | **major** | 0.85 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Answer inquiries pertaining to hotel policies and services, and resolve occupants' complaints. | minor | 0.894 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Confer and cooperate with other managers to ensure coordination of hotel activities. | minor | 0.136 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Greet and register guests. | minor | 0.676 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Meet with clients to schedule and plan details of conventions, banquets, receptions and other functions. | minor | 0.015 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Coordinate front-office activities of hotels or motels, and resolve problems. | minor | 0.735 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Participate in financial activities, such as the setting of room rates, the establishment of budgets, and the allocation of funds to departments. | no fit | 0.072 | - |
| Manage and maintain temporary or permanent lodging facilities. | no fit | 0.128 | - |
| Train staff members. | no fit | 0.089 | - |
| Observe and monitor staff performance to ensure efficient operations and adherence to facility's policies and procedures. | no fit | 0.09 | - |

### Jia Vargas, Course creator and trainer

O*NET: Training and Development Specialists. Apps in our catalog: Cisco Webex Meetings, Drupal, Google Drive, Google Slides, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, MySQL, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Obtain, organize, or develop training procedure manuals, guides, or course materials, such as handouts or visual materials. | minor | 0.045 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Assess training needs through surveys, interviews with employees, focus groups, or consultation with managers, instructors, or customer representatives. | minor | 0.004 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Monitor, evaluate, or record training activities or program effectiveness. | minor | 0.718 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Design, plan, organize, or direct orientation and training programs for employees or customers. | minor | 0.532 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Monitor training costs and prepare budget reports to justify expenditures. | minor | 0.673 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Present information with a variety of instructional techniques or formats, such as role playing, simulations, team exercises, group discussions, videos, or lectures. | no fit | 0.573 | - |
| Evaluate modes of training delivery, such as in-person or virtual, to optimize training effectiveness, training costs, or environmental impacts. | no fit | 0.101 | - |
| Offer specific training programs to help workers maintain or improve job skills. | no fit | 0.044 | - |
| Develop alternative training methods if expected improvements are not seen. | no fit | 0.113 | - |
| Evaluate training materials prepared by instructors, such as outlines, text, or handouts. | no fit | 0.468 | - |

### Kemal Moreau, Web designer

O*NET: Web and Digital Interface Designers. Apps in our catalog: Airtable, Apache Kafka, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, JSON, Microsoft Excel 365, Microsoft SQL Server, Microsoft SharePoint, MongoDB, MySQL, NetSuite.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Identify problems uncovered by testing or customer feedback, and correct problems or refer problems to appropriate personnel for correction. | **major** | 0.081 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Respond to user email inquiries, or set up automated systems to send responses. | **major** | 0.857 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Design, build, or maintain Web sites, using authoring or scripting languages, content creation tools, management tools, and digital media. | minor | 0.86 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Perform Web site tests according to planned schedules, or after any Web site or product revision. | minor | 0.893 | App/site/system check fails -> alert to email/Slack + incident task |
| Collaborate with web development professionals, such as front-end or back-end developers, to complete the full scope of Web development projects. | minor | 0.237 | New client/project -> create tasks in project tool -> status updates to channel |
| Develop new visual design concepts and modify concepts based on stakeholder feedback. | minor | 0.367 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Write supporting code for Web applications or Web sites. | no fit | 0.798 | - |
| Collaborate with management or users to develop e-commerce strategies and to integrate these strategies with Web sites. | no fit | 0.267 | - |
| Maintain understanding of current Web technologies or programming practices through continuing education, reading, or participation in professional conferences, workshops, or groups. | no fit | 0.044 | - |
| Create Web models or prototypes that include physical, interface, logical, or data models. | no fit | 0.612 | - |

### Lucia Kowalski, Online shop owner

O*NET: Retail Salespersons. Apps in our catalog: Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Quickbooks Online, Salesforce, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Maintain records related to sales. | **major** | 0.307 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Answer questions regarding the store and its merchandise. | **major** | 0.805 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Prepare sales slips or sales contracts. | **major** | 0.61 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Recommend, select, and help locate or obtain merchandise based on customer needs and desires. | minor | 0.876 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Compute sales prices, total purchases, and receive and process cash or credit payment. | minor | 0.849 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Greet customers and ascertain what each customer wants or needs. | no fit | 0.189 | - |
| Prepare merchandise for purchase or rental. | no fit | 0.737 | - |
| Maintain knowledge of current sales and promotions, policies regarding payment and exchanges, and security practices. | no fit | 0.135 | - |
| Open and close cash registers, performing tasks such as counting money, separating charge slips, coupons, and vouchers, balancing cash drawers, and making deposits. | no fit | 0.888 | - |
| Demonstrate use or operation of merchandise. | no fit | 0.152 | - |

## Team ($149)

**Who buys:** Account Director, Bookkeeper, Copywriter, Creative Director, Founder & Managing Director, Graphic Designer, Project Coordinator, Social Media Specialist, Web & Digital Designer.

**Why:** A 2-10 person agency (Northlane Studio). The founder buys so the team shares one set of automations: client approvals, project handoffs, social posting, invoicing. The real need is shared work, not more runs.

**Top automations for this plan** (tasks): design asset delivery (9); AI first drafts (8); approvals (6); scheduled reports (4); meeting notes and actions (4); research digests (4).

### Amara Rahman, Founder & Managing Director (Northlane Studio, Boss)

O*NET: General and Operations Managers. Apps in our catalog: Airtable, Confluence, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review financial statements, sales or activity reports, or other performance data to measure productivity or goal achievement or to identify areas needing cost reduction or program improvement. | **major** | 0.772 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare staff work schedules and assign specific duties. | **major** | 0.614 | Staff rota in sheet -> send each person their shifts/duties + change alerts |
| Perform personnel functions, such as selection, training, or evaluation. | minor | 0.033 | New application -> tracker record -> AI screen summary -> interview invite |
| Develop or implement product-marketing strategies, including advertising campaigns or sales promotions. | minor | 0.834 | New subscriber/segment -> add to email list -> campaign or sequence |
| Direct and coordinate activities of businesses or departments concerned with the production, pricing, sales, or distribution of products. | no fit | 0.75 | - |
| Manage the movement of goods into and out of production facilities to ensure efficiency, effectiveness, or sustainability of operations. | no fit | 0.838 | - |
| Direct administrative activities directly related to making products or providing services. | no fit | 0.928 | - |
| Set prices or credit terms for goods or services, based on forecasts of customer demand. | no fit | 0.899 | - |
| Direct or coordinate financial or budget activities to fund operations, maximize investments, or increase efficiency. | no fit | 0.761 | - |
| Perform sales floor work, such as greeting or assisting customers, stocking shelves, or taking inventory. | no fit | 0.604 | - |
| Plan or direct activities, such as sales promotions, that require coordination with other department managers. | no fit | 0.101 | - |
| Establish or implement departmental policies, goals, objectives, or procedures in conjunction with board members, organization officials, or staff members. | no fit | 0.03 | - |

### Bilal Mensah, Creative Director (Northlane Studio, Design head)

O*NET: Art Directors. Apps in our catalog: Confluence, Drupal, Facebook Pages, Figma, Google Slides, Microsoft Excel 365, Microsoft Outlook, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Present final layouts to clients for approval. | **major** | 0.076 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Review and approve art materials, copy materials, and proofs of printed copy developed by staff members. | **major** | 0.427 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Manage own accounts and projects, working within budget and scheduling requirements. | minor | 0.94 | New client/project -> create tasks in project tool -> status updates to channel |
| Confer with creative, art, copywriting, or production department heads to discuss client requirements and presentation concepts and to coordinate creative activities. | minor | 0.035 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Confer with clients to determine objectives, budget, background information, and presentation approaches, styles, and techniques. | minor | 0.049 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Create custom illustrations or other graphic elements. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Work with creative directors to develop design solutions. | no fit | 0.061 | - |
| Formulate basic layout design or presentation approach and specify material details, such as style and size of type, photographs, graphics, animation, video, and sound. | no fit | 0.828 | - |
| Mark up, paste, and complete layouts and write typography instructions to prepare materials for typesetting or printing. | no fit | 0.958 | - |
| Attend photo shoots and printing sessions to ensure that the products needed are obtained. | no fit | 0.0 | - |
| Review illustrative material to determine if it conforms to standards and specifications. | no fit | 0.063 | - |
| Hire, train, and direct staff members who develop design concepts into art layouts or who prepare layouts for printing. | no fit | 0.057 | - |

### Chen Nakamura, Graphic Designer (Northlane Studio, Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Dalia Usman, Graphic Designer (Northlane Studio, Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Elif Dlamini, Web & Digital Designer (Northlane Studio, Design)

O*NET: Web and Digital Interface Designers. Apps in our catalog: Airtable, Apache Kafka, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, JSON, Microsoft Excel 365, Microsoft SQL Server, Microsoft SharePoint, MongoDB, MySQL, NetSuite.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Identify problems uncovered by testing or customer feedback, and correct problems or refer problems to appropriate personnel for correction. | **major** | 0.081 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Design, build, or maintain Web sites, using authoring or scripting languages, content creation tools, management tools, and digital media. | minor | 0.86 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Perform Web site tests according to planned schedules, or after any Web site or product revision. | minor | 0.893 | App/site/system check fails -> alert to email/Slack + incident task |
| Collaborate with web development professionals, such as front-end or back-end developers, to complete the full scope of Web development projects. | minor | 0.237 | New client/project -> create tasks in project tool -> status updates to channel |
| Develop new visual design concepts and modify concepts based on stakeholder feedback. | minor | 0.367 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Write supporting code for Web applications or Web sites. | no fit | 0.798 | - |
| Collaborate with management or users to develop e-commerce strategies and to integrate these strategies with Web sites. | no fit | 0.267 | - |
| Maintain understanding of current Web technologies or programming practices through continuing education, reading, or participation in professional conferences, workshops, or groups. | no fit | 0.044 | - |

### Farhan Khan, Account Director (Northlane Studio, Client services head)

O*NET: Marketing Managers. Apps in our catalog: Airtable, Asana, Canva, Confluence, Constant Contact, Dropbox, Drupal, Facebook Pages, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Compile lists describing product or service offerings. | **major** | 0.744 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Use sales forecasting or strategic planning to ensure the sale and profitability of products, lines, or services, analyzing business developments and monitoring market trends. | minor | 0.941 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Evaluate the financial aspects of product development, such as budgets, expenditures, research and development appropriations, or return-on-investment and profit-loss projections. | minor | 0.753 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Initiate market research studies, or analyze their findings. | minor | 0.584 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Consult with buying personnel to gain advice regarding the types of products or services expected to be in demand. | minor | 0.01 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Conduct economic or commercial surveys to identify potential markets for products or services. | minor | 0.62 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Formulate, direct, or coordinate marketing activities or policies to promote products or services, working with advertising or promotion managers. | no fit | 0.598 | - |
| Identify, develop, or evaluate marketing strategy, based on knowledge of establishment objectives, market characteristics, and cost and markup factors. | no fit | 0.815 | - |
| Direct the hiring, training, or performance evaluations of marketing or sales staff and oversee their daily activities. | no fit | 0.81 | - |
| Develop pricing strategies, balancing firm objectives and customer satisfaction. | no fit | 0.594 | - |
| Consult with product development personnel on product specifications, such as design, color, or packaging. | no fit | 0.078 | - |
| Recommend modifications to products, packaging, production processes, or other characteristics to improve the environmental soundness or sustainability of products. | no fit | 0.274 | - |

### Grace Reyes, Project Coordinator (Northlane Studio, Client services)

O*NET: Business Continuity Planners. Apps in our catalog: Confluence, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, ServiceNow.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Establish, maintain, or test call trees to ensure appropriate communication during disaster. | minor | 0.628 | App/site/system check fails -> alert to email/Slack + incident task |
| Develop emergency management plans for recovery decision making and communications, continuity of critical departmental processes, or temporary shut-down of non-critical departments to ensure continuity of operation and governance. | no fit | 0.805 | - |
| Conduct or oversee collection of corporate intelligence to avoid fraud, financial crime, cyber attack, terrorism, and infrastructure failure. | no fit | 0.65 | - |
| Test documented disaster recovery strategies and plans. | no fit | 0.077 | - |
| Develop disaster recovery plans for physical locations with critical assets, such as data centers. | no fit | 0.598 | - |
| Identify opportunities for strategic improvement or mitigation of business interruption and other risks caused by business, regulatory, or industry-specific change initiatives. | no fit | 0.455 | - |
| Maintain and update organization information technology applications and network systems blueprints. | no fit | 0.773 | - |
| Review existing disaster recovery, crisis management, or business continuity plans. | no fit | 0.623 | - |

### Hiro Young, Social Media Specialist (Northlane Studio, Client services)

O*NET: Public Relations Specialists. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Salesforce, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Post and update content on the company's Web site and social media outlets. | **major** | 0.604 | Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it |
| Respond to requests for information from the media or designate an appropriate spokesperson or information source. | minor | 0.147 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Plan or direct development or communication of programs to maintain favorable public or stockholder perceptions of an organization's accomplishments, agenda, or environmental responsibility. | minor | 0.099 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write press releases or other media communications to promote clients. | minor | 0.687 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Confer with other managers to identify trends or key group interests or concerns or to provide advice on business decisions. | minor | 0.041 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Establish or maintain cooperative relationships with representatives of community, consumer, employee, or public interest groups. | no fit | 0.034 | - |
| Coach client representatives in effective communication with the public or with employees. | no fit | 0.8 | - |
| Study the objectives, promotional policies, or needs of organizations to develop public relations strategies that will influence public opinion or promote ideas, products, or services. | no fit | 0.189 | - |

### Isha Novak, Copywriter (Northlane Studio, Client services)

O*NET: Writers and Authors. Apps in our catalog: Asana, Campaign Monitor, Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, Google Workspace, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, MySQL, Presenton, SendGrid, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Revise written material to meet personal standards and to satisfy needs of clients, publishers, directors, or producers. | minor | 0.546 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Present drafts and ideas to clients. | minor | 0.049 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher. | minor | 0.272 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Conduct research to obtain factual information and authentic detail, using sources such as newspaper accounts, diaries, and interviews. | minor | 0.038 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Vary language and tone of messages based on product and medium. | minor | 0.654 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write articles, bulletins, sales letters, speeches, and other related informative, marketing and promotional material. | minor | 0.942 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write advertising material for use by publication, broadcast, or internet media to promote the sale of goods and services. | minor | 0.498 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write fiction or nonfiction prose, such as short stories, novels, biographies, articles, descriptive or critical analyses, and essays. | no fit | 0.637 | - |

### Jonas Duarte, Bookkeeper (Northlane Studio, Operations head)

O*NET: Bookkeeping, Accounting, and Auditing Clerks. Apps in our catalog: Dropbox, Facebook Pages, Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Operate computers programmed with accounting software to record, store, and analyze information. | **major** | 0.938 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Monitor status of loans and accounts to ensure that payments are up to date. | **major** | 0.76 | Job done or due date -> create invoice -> send -> overdue reminder |
| Reconcile records of bank transactions. | **major** | 0.8 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare and process payroll information. | minor | 0.754 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Check figures, postings, and documents for correct entry, mathematical accuracy, and proper codes. | minor | 0.862 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare bank deposits by compiling data from cashiers, verifying and balancing receipts, and sending cash, checks, or other forms of payment to banks. | minor | 0.784 | Payment received -> record in accounting + sheet -> receipt to client |
| Comply with federal, state, and company policies, procedures, and regulations. | minor | 0.093 | Recurring compliance/renewal date -> reminder + log record |
| Receive, record, and bank cash, checks, and vouchers. | minor | 0.584 | Payment received -> record in accounting + sheet -> receipt to client |
| Calculate and prepare checks for utilities, taxes, and other payments. | minor | 0.908 | Job done or due date -> create invoice -> send -> overdue reminder |
| Compile budget data and documents, based on estimated revenues and expenses and previous budgets. | minor | 0.731 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Code documents according to company procedures. | minor | 0.39 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Operate 10-key calculators, typewriters, and copy machines to perform calculations and produce documents. | no fit | 0.922 | - |

## Scale ($299)

**Who buys:** Accountant, B2B Sales Rep, Bookkeeper, CEO, Content Writer, Customer Service Rep, Email Marketing Specialist, Graphic Designer, HR Specialist, Head of Design, Head of Finance, Head of Marketing, Head of Operations, Head of Sales, Head of Support, Logistics Coordinator, Market Research Analyst, Payroll Clerk, Product Photographer, Purchasing Agent, SEO & Search Marketer, Sales Development Rep, Social Media Manager, Supply Chain Manager, Systems & Analytics Analyst, Video Editor, Warehouse & Shipping Clerk, Web Designer, Wholesale Account Manager.

**Why:** A ~50 person company with departments (Brightpath Home Co.: marketing, design, sales, support, operations, finance & people). The CEO or a department head buys so each department runs its own workflows: support tickets, orders and shipping, stock alerts, payroll inputs, KPI reports. They need per-department control.

**Top automations for this plan** (tasks): complaints to tickets (31); AI first drafts (27); scheduled reports (23); design asset delivery (19); research digests (17); quotes and price lists (13).

### Kofi Turner, CEO (Brightpath Home Co., Boss)

O*NET: Chief Executives. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Presenton, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with board members, organization officials, or staff members to discuss issues, coordinate activities, or resolve problems. | minor | 0.027 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Prepare budgets for approval, including those for funding or implementation of programs. | minor | 0.572 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare or present reports concerning activities, expenses, budgets, government statutes or rulings, or other items affecting businesses or program services. | minor | 0.715 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Analyze operations to evaluate performance of a company or its staff in meeting objectives or to determine areas of potential cost reduction, program improvement, or policy change. | minor | 0.851 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Review reports submitted by staff members to recommend approval or to suggest changes. | minor | 0.317 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Direct or coordinate an organization's financial or budget activities to fund operations, maximize investments, or increase efficiency. | no fit | 0.753 | - |
| Direct, plan, or implement policies, objectives, or activities of organizations or businesses to ensure continuing operations, to maximize returns on investments, or to increase productivity. | no fit | 0.257 | - |
| Implement corrective action plans to solve organizational or departmental problems. | no fit | 0.105 | - |
| Direct or coordinate activities of businesses or departments concerned with production, pricing, sales, or distribution of products. | no fit | 0.532 | - |
| Direct human resources activities, including the approval of human resource plans or activities, the selection of directors or other high-level staff, or establishment or organization of major departments. | no fit | 0.105 | - |
| Appoint department heads or managers and assign or delegate responsibilities to them. | no fit | 0.082 | - |
| Interpret and explain policies, rules, regulations, or laws to organizations, government or corporate officials, or individuals. | no fit | 0.089 | - |

### Lena Castillo, Head of Marketing (Brightpath Home Co., Marketing head)

O*NET: Marketing Managers. Apps in our catalog: Airtable, Asana, Canva, Confluence, Constant Contact, Dropbox, Drupal, Facebook Pages, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Compile lists describing product or service offerings. | **major** | 0.744 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Use sales forecasting or strategic planning to ensure the sale and profitability of products, lines, or services, analyzing business developments and monitoring market trends. | minor | 0.941 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Evaluate the financial aspects of product development, such as budgets, expenditures, research and development appropriations, or return-on-investment and profit-loss projections. | minor | 0.753 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Initiate market research studies, or analyze their findings. | minor | 0.584 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Consult with buying personnel to gain advice regarding the types of products or services expected to be in demand. | minor | 0.01 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Conduct economic or commercial surveys to identify potential markets for products or services. | minor | 0.62 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Formulate, direct, or coordinate marketing activities or policies to promote products or services, working with advertising or promotion managers. | no fit | 0.598 | - |
| Identify, develop, or evaluate marketing strategy, based on knowledge of establishment objectives, market characteristics, and cost and markup factors. | no fit | 0.815 | - |
| Direct the hiring, training, or performance evaluations of marketing or sales staff and oversee their daily activities. | no fit | 0.81 | - |
| Develop pricing strategies, balancing firm objectives and customer satisfaction. | no fit | 0.594 | - |
| Consult with product development personnel on product specifications, such as design, color, or packaging. | no fit | 0.078 | - |
| Recommend modifications to products, packaging, production processes, or other characteristics to improve the environmental soundness or sustainability of products. | no fit | 0.274 | - |

### Mateo Jensen, SEO & Search Marketer (Brightpath Home Co., Marketing)

O*NET: Search Marketing Strategists. Apps in our catalog: Drupal, Facebook Pages, Google Ads, Google Search, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, MySQL, Pinterest, Tableau, Twitter, WhatsApp Business, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Manage tracking and reporting of search-related activities and provide analyses to marketing executives. | **major** | 0.93 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Collect and analyze Web metrics, such as visits, time on site, page views per visit, transaction volume and revenue, traffic mix, click-through rates, conversion rates, cost per acquisition, or cost per click. | **major** | 0.806 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Identify appropriate Key Performance Indicators (KPIs) and report key metrics from digital campaigns. | **major** | 0.558 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Optimize digital assets, such as text, graphics, or multimedia assets, for search engine optimization (SEO) or for display and usability on internet-connected devices. | minor | 0.823 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Optimize Web site exposure by analyzing search engine patterns to direct online placement of keywords or other content. | minor | 0.908 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Assist in setting up or optimizing analytics tools for tracking visitors' behaviors. | minor | 0.811 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Participate in the development or implementation of online marketing strategy. | no fit | 0.427 | - |
| Coordinate with developers to optimize Web site architecture, server configuration, or page construction for search engine consumption and optimal visibility. | no fit | 0.5 | - |

### Nadia Qureshi, SEO & Search Marketer (Brightpath Home Co., Marketing)

O*NET: Search Marketing Strategists. Apps in our catalog: Drupal, Facebook Pages, Google Ads, Google Search, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, MySQL, Pinterest, Tableau, Twitter, WhatsApp Business, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Manage tracking and reporting of search-related activities and provide analyses to marketing executives. | **major** | 0.93 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Collect and analyze Web metrics, such as visits, time on site, page views per visit, transaction volume and revenue, traffic mix, click-through rates, conversion rates, cost per acquisition, or cost per click. | **major** | 0.806 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Identify appropriate Key Performance Indicators (KPIs) and report key metrics from digital campaigns. | **major** | 0.558 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Optimize digital assets, such as text, graphics, or multimedia assets, for search engine optimization (SEO) or for display and usability on internet-connected devices. | minor | 0.823 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Optimize Web site exposure by analyzing search engine patterns to direct online placement of keywords or other content. | minor | 0.908 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Assist in setting up or optimizing analytics tools for tracking visitors' behaviors. | minor | 0.811 | Daily/weekly -> pull ad/web/social metrics -> sheet or dashboard + alert on drops |
| Participate in the development or implementation of online marketing strategy. | no fit | 0.427 | - |
| Coordinate with developers to optimize Web site architecture, server configuration, or page construction for search engine consumption and optimal visibility. | no fit | 0.5 | - |

### Omar Xu, Market Research Analyst (Brightpath Home Co., Marketing)

O*NET: Market Research Analysts and Marketing Specialists. Apps in our catalog: Airtable, Asana, Canva, Dropbox, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, MySQL, NetSuite, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Measure and assess customer and employee satisfaction. | **major** | 0.564 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Monitor industry statistics and follow trends in trade literature. | **major** | 0.682 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Prepare reports of findings, illustrating data graphically and translating complex findings into written text. | minor | 0.881 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Seek and provide information to help companies determine their position in the marketplace. | minor | 0.929 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Conduct research on consumer opinions and marketing strategies, collaborating with marketing professionals, statisticians, pollsters, and other professionals. | minor | 0.664 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Collect and analyze data on customer demographics, preferences, needs, and buying habits to identify potential markets and factors affecting product demand. | minor | 0.827 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Devise and evaluate methods and procedures for collecting data, such as surveys, opinion polls, or questionnaires, or arrange to obtain existing data. | minor | 0.334 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Gather data on competitors and analyze their prices, sales, and method of marketing and distribution. | minor | 0.746 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |

### Priya Haddad, Social Media Manager (Brightpath Home Co., Marketing)

O*NET: Public Relations Specialists. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Salesforce, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Post and update content on the company's Web site and social media outlets. | **major** | 0.604 | Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it |
| Respond to requests for information from the media or designate an appropriate spokesperson or information source. | minor | 0.147 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Plan or direct development or communication of programs to maintain favorable public or stockholder perceptions of an organization's accomplishments, agenda, or environmental responsibility. | minor | 0.099 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write press releases or other media communications to promote clients. | minor | 0.687 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Confer with other managers to identify trends or key group interests or concerns or to provide advice on business decisions. | minor | 0.041 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Establish or maintain cooperative relationships with representatives of community, consumer, employee, or public interest groups. | no fit | 0.034 | - |
| Coach client representatives in effective communication with the public or with employees. | no fit | 0.8 | - |
| Study the objectives, promotional policies, or needs of organizations to develop public relations strategies that will influence public opinion or promote ideas, products, or services. | no fit | 0.189 | - |

### Quinn Ahmed, Social Media Manager (Brightpath Home Co., Marketing)

O*NET: Public Relations Specialists. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Salesforce, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Post and update content on the company's Web site and social media outlets. | **major** | 0.604 | Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it |
| Respond to requests for information from the media or designate an appropriate spokesperson or information source. | minor | 0.147 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Plan or direct development or communication of programs to maintain favorable public or stockholder perceptions of an organization's accomplishments, agenda, or environmental responsibility. | minor | 0.099 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write press releases or other media communications to promote clients. | minor | 0.687 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Confer with other managers to identify trends or key group interests or concerns or to provide advice on business decisions. | minor | 0.041 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Establish or maintain cooperative relationships with representatives of community, consumer, employee, or public interest groups. | no fit | 0.034 | - |
| Coach client representatives in effective communication with the public or with employees. | no fit | 0.8 | - |
| Study the objectives, promotional policies, or needs of organizations to develop public relations strategies that will influence public opinion or promote ideas, products, or services. | no fit | 0.189 | - |

### Rafael Sato, Social Media Manager (Brightpath Home Co., Marketing)

O*NET: Public Relations Specialists. Apps in our catalog: Airtable, Canva, Cisco Webex Meetings, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Salesforce, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Post and update content on the company's Web site and social media outlets. | **major** | 0.604 | Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it |
| Respond to requests for information from the media or designate an appropriate spokesperson or information source. | minor | 0.147 | Incoming email/message/document -> classify -> forward to the right person or channel |
| Plan or direct development or communication of programs to maintain favorable public or stockholder perceptions of an organization's accomplishments, agenda, or environmental responsibility. | minor | 0.099 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write press releases or other media communications to promote clients. | minor | 0.687 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Confer with other managers to identify trends or key group interests or concerns or to provide advice on business decisions. | minor | 0.041 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Establish or maintain cooperative relationships with representatives of community, consumer, employee, or public interest groups. | no fit | 0.034 | - |
| Coach client representatives in effective communication with the public or with employees. | no fit | 0.8 | - |
| Study the objectives, promotional policies, or needs of organizations to develop public relations strategies that will influence public opinion or promote ideas, products, or services. | no fit | 0.189 | - |

### Sana Bose, Content Writer (Brightpath Home Co., Marketing)

O*NET: Writers and Authors. Apps in our catalog: Asana, Campaign Monitor, Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, Google Workspace, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, MySQL, Presenton, SendGrid, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Revise written material to meet personal standards and to satisfy needs of clients, publishers, directors, or producers. | minor | 0.546 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Present drafts and ideas to clients. | minor | 0.049 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher. | minor | 0.272 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Conduct research to obtain factual information and authentic detail, using sources such as newspaper accounts, diaries, and interviews. | minor | 0.038 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Vary language and tone of messages based on product and medium. | minor | 0.654 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write articles, bulletins, sales letters, speeches, and other related informative, marketing and promotional material. | minor | 0.942 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write advertising material for use by publication, broadcast, or internet media to promote the sale of goods and services. | minor | 0.498 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write fiction or nonfiction prose, such as short stories, novels, biographies, articles, descriptive or critical analyses, and essays. | no fit | 0.637 | - |

### Tomas Iyer, Content Writer (Brightpath Home Co., Marketing)

O*NET: Writers and Authors. Apps in our catalog: Asana, Campaign Monitor, Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, Google Workspace, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, MySQL, Presenton, SendGrid, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Revise written material to meet personal standards and to satisfy needs of clients, publishers, directors, or producers. | minor | 0.546 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Present drafts and ideas to clients. | minor | 0.049 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher. | minor | 0.272 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Conduct research to obtain factual information and authentic detail, using sources such as newspaper accounts, diaries, and interviews. | minor | 0.038 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Vary language and tone of messages based on product and medium. | minor | 0.654 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write articles, bulletins, sales letters, speeches, and other related informative, marketing and promotional material. | minor | 0.942 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write advertising material for use by publication, broadcast, or internet media to promote the sale of goods and services. | minor | 0.498 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write fiction or nonfiction prose, such as short stories, novels, biographies, articles, descriptive or critical analyses, and essays. | no fit | 0.637 | - |

### Uma Park, Content Writer (Brightpath Home Co., Marketing)

O*NET: Writers and Authors. Apps in our catalog: Asana, Campaign Monitor, Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, Google Workspace, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, MySQL, Presenton, SendGrid, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Revise written material to meet personal standards and to satisfy needs of clients, publishers, directors, or producers. | minor | 0.546 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Present drafts and ideas to clients. | minor | 0.049 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Edit or rewrite existing written material as necessary, and submit written material for approval by supervisor, editor, or publisher. | minor | 0.272 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Conduct research to obtain factual information and authentic detail, using sources such as newspaper accounts, diaries, and interviews. | minor | 0.038 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Vary language and tone of messages based on product and medium. | minor | 0.654 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write articles, bulletins, sales letters, speeches, and other related informative, marketing and promotional material. | minor | 0.942 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write advertising material for use by publication, broadcast, or internet media to promote the sale of goods and services. | minor | 0.498 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Write fiction or nonfiction prose, such as short stories, novels, biographies, articles, descriptive or critical analyses, and essays. | no fit | 0.637 | - |

### Victor Watanabe, Email Marketing Specialist (Brightpath Home Co., Marketing)

O*NET: Market Research Analysts and Marketing Specialists. Apps in our catalog: Airtable, Asana, Canva, Dropbox, Drupal, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, Instagram for Business, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, MySQL, NetSuite, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Measure and assess customer and employee satisfaction. | **major** | 0.564 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Monitor industry statistics and follow trends in trade literature. | **major** | 0.682 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Prepare reports of findings, illustrating data graphically and translating complex findings into written text. | minor | 0.881 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Seek and provide information to help companies determine their position in the marketplace. | minor | 0.929 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Conduct research on consumer opinions and marketing strategies, collaborating with marketing professionals, statisticians, pollsters, and other professionals. | minor | 0.664 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Collect and analyze data on customer demographics, preferences, needs, and buying habits to identify potential markets and factors affecting product demand. | minor | 0.827 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Devise and evaluate methods and procedures for collecting data, such as surveys, opinion polls, or questionnaires, or arrange to obtain existing data. | minor | 0.334 | After session/visit -> send survey -> collect answers in sheet -> summary |
| Gather data on competitors and analyze their prices, sales, and method of marketing and distribution. | minor | 0.746 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |

### Wen Tanaka, Head of Design (Brightpath Home Co., Design head)

O*NET: Art Directors. Apps in our catalog: Confluence, Drupal, Facebook Pages, Figma, Google Slides, Microsoft Excel 365, Microsoft Outlook, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Present final layouts to clients for approval. | **major** | 0.076 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Review and approve art materials, copy materials, and proofs of printed copy developed by staff members. | **major** | 0.427 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Manage own accounts and projects, working within budget and scheduling requirements. | minor | 0.94 | New client/project -> create tasks in project tool -> status updates to channel |
| Confer with creative, art, copywriting, or production department heads to discuss client requirements and presentation concepts and to coordinate creative activities. | minor | 0.035 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Confer with clients to determine objectives, budget, background information, and presentation approaches, styles, and techniques. | minor | 0.049 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Create custom illustrations or other graphic elements. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Work with creative directors to develop design solutions. | no fit | 0.061 | - |
| Formulate basic layout design or presentation approach and specify material details, such as style and size of type, photographs, graphics, animation, video, and sound. | no fit | 0.828 | - |
| Mark up, paste, and complete layouts and write typography instructions to prepare materials for typesetting or printing. | no fit | 0.958 | - |
| Attend photo shoots and printing sessions to ensure that the products needed are obtained. | no fit | 0.0 | - |
| Review illustrative material to determine if it conforms to standards and specifications. | no fit | 0.063 | - |
| Hire, train, and direct staff members who develop design concepts into art layouts or who prepare layouts for printing. | no fit | 0.057 | - |

### Ximena Santos, Graphic Designer (Brightpath Home Co., Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Yusuf Rossi, Graphic Designer (Brightpath Home Co., Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Zara Zhou, Graphic Designer (Brightpath Home Co., Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Arjun Hughes, Graphic Designer (Brightpath Home Co., Design)

O*NET: Graphic Designers. Apps in our catalog: Canva, Drupal, Facebook Pages, Figma, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Quickbooks Online, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review final layouts and suggest improvements, as needed. | minor | 0.525 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Develop graphics and layouts for product illustrations, company logos, and Web sites. | minor | 0.913 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Create designs, concepts, and sample layouts, based on knowledge of layout principles and esthetic design concepts. | minor | 1.0 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Use computer software to generate new images. | minor | 0.948 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Prepare digital files for printing. | minor | 0.818 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Confer with clients to discuss and determine layout design. | minor | 0.119 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Key information into computer equipment to create layouts for client or supervisor. | no fit | 0.872 | - |
| Determine size and arrangement of illustrative material and copy, and select style and size of type. | no fit | 0.812 | - |

### Bea Ortiz, Video Editor (Brightpath Home Co., Design)

O*NET: Film and Video Editors. Apps in our catalog: Instagram for Business, Microsoft Excel 365, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Organize and string together raw footage into a continuous whole according to scripts or the instructions of directors and producers. | no fit | 0.843 | - |
| Edit films and videotapes to insert music, dialogue, and sound effects, to arrange films into sequences, and to correct errors, using editing equipment. | no fit | 0.883 | - |
| Select and combine the most effective shots of each scene to form a logical and smoothly running story. | no fit | 0.806 | - |
| Review footage sequence by sequence to become familiar with it before assembling it into a final product. | no fit | 0.823 | - |
| Set up and operate computer editing systems, electronic titling systems, video switching equipment, and digital video effects units to produce a final product. | no fit | 0.935 | - |
| Trim film segments to specified lengths and reassemble segments in sequences that present stories with maximum effect. | no fit | 0.929 | - |
| Cut shot sequences to different angles at specific points in scenes, making each individual cut as fluid and seamless as possible. | no fit | 0.926 | - |
| Review assembled films or edited videotapes on screens or monitors to determine if corrections are necessary. | no fit | 0.884 | - |

### Carlos Vargas, Video Editor (Brightpath Home Co., Design)

O*NET: Film and Video Editors. Apps in our catalog: Instagram for Business, Microsoft Excel 365, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Organize and string together raw footage into a continuous whole according to scripts or the instructions of directors and producers. | no fit | 0.843 | - |
| Edit films and videotapes to insert music, dialogue, and sound effects, to arrange films into sequences, and to correct errors, using editing equipment. | no fit | 0.883 | - |
| Select and combine the most effective shots of each scene to form a logical and smoothly running story. | no fit | 0.806 | - |
| Review footage sequence by sequence to become familiar with it before assembling it into a final product. | no fit | 0.823 | - |
| Set up and operate computer editing systems, electronic titling systems, video switching equipment, and digital video effects units to produce a final product. | no fit | 0.935 | - |
| Trim film segments to specified lengths and reassemble segments in sequences that present stories with maximum effect. | no fit | 0.929 | - |
| Cut shot sequences to different angles at specific points in scenes, making each individual cut as fluid and seamless as possible. | no fit | 0.926 | - |
| Review assembled films or edited videotapes on screens or monitors to determine if corrections are necessary. | no fit | 0.884 | - |

### Divya Moreau, Web Designer (Brightpath Home Co., Design)

O*NET: Web and Digital Interface Designers. Apps in our catalog: Airtable, Apache Kafka, Cisco Webex Meetings, Confluence, Dropbox, Drupal, Figma, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, JSON, Microsoft Excel 365, Microsoft SQL Server, Microsoft SharePoint, MongoDB, MySQL, NetSuite.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Identify problems uncovered by testing or customer feedback, and correct problems or refer problems to appropriate personnel for correction. | **major** | 0.081 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Design, build, or maintain Web sites, using authoring or scripting languages, content creation tools, management tools, and digital media. | minor | 0.86 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Perform Web site tests according to planned schedules, or after any Web site or product revision. | minor | 0.893 | App/site/system check fails -> alert to email/Slack + incident task |
| Collaborate with web development professionals, such as front-end or back-end developers, to complete the full scope of Web development projects. | minor | 0.237 | New client/project -> create tasks in project tool -> status updates to channel |
| Develop new visual design concepts and modify concepts based on stakeholder feedback. | minor | 0.367 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Write supporting code for Web applications or Web sites. | no fit | 0.798 | - |
| Collaborate with management or users to develop e-commerce strategies and to integrate these strategies with Web sites. | no fit | 0.267 | - |
| Maintain understanding of current Web technologies or programming practices through continuing education, reading, or participation in professional conferences, workshops, or groups. | no fit | 0.044 | - |

### Emeka Kowalski, Product Photographer (Brightpath Home Co., Design)

O*NET: Photographers. Apps in our catalog: Facebook Pages, Google Drive, Microsoft Excel 365, Quickbooks Online, Twitter, WordPress, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Transfer photographs to computers for editing, archiving, and electronic transmission. | **major** | 0.949 | New file/attachment -> rename -> save to the right Drive/Dropbox folder |
| Manipulate and enhance scanned or digital images to create desired effects, using computers and specialized software. | minor | 0.93 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Enhance, retouch, and resize photographs and negatives, using airbrushing and other techniques. | minor | 0.86 | Design/photo ready -> export/resize/AI image -> deliver to client folder |
| Adjust apertures, shutter speeds, and camera focus according to a combination of factors, such as lighting, field depth, subject motion, film type, and film speed. | no fit | 0.878 | - |
| Create artificial light, using flashes and reflectors. | no fit | 0.466 | - |
| Determine desired images and picture composition, selecting and adjusting subjects, equipment, and lighting to achieve desired effects. | no fit | 0.835 | - |
| Use traditional or digital cameras, along with a variety of equipment, such as tripods, filters, and flash attachments. | no fit | 0.13 | - |
| Take pictures of individuals, families, and small groups, either in studio or on location. | no fit | 0.713 | - |

### Fatima Quiroga, Head of Sales (Brightpath Home Co., Sales head)

O*NET: Sales Managers. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Salesforce, Tableau, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Resolve customer complaints regarding sales and service. | minor | 0.593 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Monitor customer preferences to determine focus of sales efforts. | minor | 0.456 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Confer with potential customers regarding equipment needs, and advise customers on types of equipment to purchase. | minor | 0.307 | New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence |
| Review operational records and reports to project sales and determine profitability. | minor | 0.592 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare budgets and approve budget expenditures. | minor | 0.58 | Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no |
| Confer or consult with department heads to plan advertising services and to secure information on equipment and customer specifications. | minor | 0.116 | Meeting ends -> notes/agenda doc -> action items to tasks + recap email |
| Oversee regional and local sales managers and their staffs. | no fit | 0.067 | - |
| Plan and direct staffing, training, and performance evaluations to develop and control sales and service programs. | no fit | 0.091 | - |
| Direct and coordinate activities involving sales of manufactured products, services, commodities, real estate, or other subjects of sale. | no fit | 0.847 | - |
| Determine price schedules and discount rates. | no fit | 0.878 | - |
| Visit franchised dealers to stimulate interest in establishment or expansion of leasing programs. | no fit | 0.0 | - |
| Represent company at trade association meetings to promote products. | no fit | 0.022 | - |

### Gabriel Yilmaz, B2B Sales Rep (Brightpath Home Co., Sales)

O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products. Apps in our catalog: Airtable, Cisco Webex Meetings, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Dynamics CRM, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Check stock levels and reorder merchandise as necessary. | **major** | 0.91 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Answer customers' questions about products, prices, availability, product uses, and credit terms. | **major** | 0.942 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Consult with clients after sales or contract signings to resolve problems and to provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Recommend products to customers, based on customers' needs and interests. | minor | 0.159 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Estimate or quote prices, credit or contract terms, warranties, and delivery dates. | minor | 0.774 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate with retail merchants to improve product exposure, such as shelf positioning and advertising. | no fit | 0.391 | - |
| Plan, assemble, and stock product displays in retail stores, or make recommendations to retailers regarding product displays, promotional programs, and advertising. | no fit | 0.792 | - |
| Negotiate details of contracts and payments. | no fit | 0.109 | - |

### Hana Gupta, B2B Sales Rep (Brightpath Home Co., Sales)

O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products. Apps in our catalog: Airtable, Cisco Webex Meetings, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Dynamics CRM, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Check stock levels and reorder merchandise as necessary. | **major** | 0.91 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Answer customers' questions about products, prices, availability, product uses, and credit terms. | **major** | 0.942 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Consult with clients after sales or contract signings to resolve problems and to provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Recommend products to customers, based on customers' needs and interests. | minor | 0.159 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Estimate or quote prices, credit or contract terms, warranties, and delivery dates. | minor | 0.774 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate with retail merchants to improve product exposure, such as shelf positioning and advertising. | no fit | 0.391 | - |
| Plan, assemble, and stock product displays in retail stores, or make recommendations to retailers regarding product displays, promotional programs, and advertising. | no fit | 0.792 | - |
| Negotiate details of contracts and payments. | no fit | 0.109 | - |

### Ivan Nguyen, B2B Sales Rep (Brightpath Home Co., Sales)

O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products. Apps in our catalog: Airtable, Cisco Webex Meetings, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Dynamics CRM, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Check stock levels and reorder merchandise as necessary. | **major** | 0.91 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Answer customers' questions about products, prices, availability, product uses, and credit terms. | **major** | 0.942 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Consult with clients after sales or contract signings to resolve problems and to provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Recommend products to customers, based on customers' needs and interests. | minor | 0.159 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Estimate or quote prices, credit or contract terms, warranties, and delivery dates. | minor | 0.774 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate with retail merchants to improve product exposure, such as shelf positioning and advertising. | no fit | 0.391 | - |
| Plan, assemble, and stock product displays in retail stores, or make recommendations to retailers regarding product displays, promotional programs, and advertising. | no fit | 0.792 | - |
| Negotiate details of contracts and payments. | no fit | 0.109 | - |

### Jia Ueda, B2B Sales Rep (Brightpath Home Co., Sales)

O*NET: Sales Representatives, Wholesale and Manufacturing, Except Technical and Scientific Products. Apps in our catalog: Airtable, Cisco Webex Meetings, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Dynamics CRM, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Check stock levels and reorder merchandise as necessary. | **major** | 0.91 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Answer customers' questions about products, prices, availability, product uses, and credit terms. | **major** | 0.942 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Consult with clients after sales or contract signings to resolve problems and to provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Recommend products to customers, based on customers' needs and interests. | minor | 0.159 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Estimate or quote prices, credit or contract terms, warranties, and delivery dates. | minor | 0.774 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate with retail merchants to improve product exposure, such as shelf positioning and advertising. | no fit | 0.391 | - |
| Plan, assemble, and stock product displays in retail stores, or make recommendations to retailers regarding product displays, promotional programs, and advertising. | no fit | 0.792 | - |
| Negotiate details of contracts and payments. | no fit | 0.109 | - |

### Kemal Lindqvist, Sales Development Rep (Brightpath Home Co., Sales)

O*NET: Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel. Apps in our catalog: HubSpot, Microsoft Excel 365, Microsoft Outlook, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Consult with clients after sales or contract signings to resolve problems and provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Answer customers' questions about services, prices, availability, or credit terms. | **major** | 0.945 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Create forms or agreements to complete sales. | **major** | 0.844 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Contact prospective or existing customers to discuss how services can meet their needs. | **major** | 0.157 | New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence |
| Quote prices, credit terms, contract terms, or fulfillment dates for services. | **major** | 0.288 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Maintain customer records using automated systems. | **major** | 0.894 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Develop sales presentations or proposals to explain service specifications. | minor | 0.809 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate prices or terms of sales or service agreements. | no fit | 0.123 | - |

### Lucia Ibrahim, Wholesale Account Manager (Brightpath Home Co., Sales)

O*NET: Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel. Apps in our catalog: HubSpot, Microsoft Excel 365, Microsoft Outlook, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Consult with clients after sales or contract signings to resolve problems and provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Answer customers' questions about services, prices, availability, or credit terms. | **major** | 0.945 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Create forms or agreements to complete sales. | **major** | 0.844 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Contact prospective or existing customers to discuss how services can meet their needs. | **major** | 0.157 | New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence |
| Quote prices, credit terms, contract terms, or fulfillment dates for services. | **major** | 0.288 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Maintain customer records using automated systems. | **major** | 0.894 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Develop sales presentations or proposals to explain service specifications. | minor | 0.809 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate prices or terms of sales or service agreements. | no fit | 0.123 | - |

### Malik Petrov, Wholesale Account Manager (Brightpath Home Co., Sales)

O*NET: Sales Representatives of Services, Except Advertising, Insurance, Financial Services, and Travel. Apps in our catalog: HubSpot, Microsoft Excel 365, Microsoft Outlook, Salesforce.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Consult with clients after sales or contract signings to resolve problems and provide ongoing support. | **major** | 0.117 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Answer customers' questions about services, prices, availability, or credit terms. | **major** | 0.945 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Create forms or agreements to complete sales. | **major** | 0.844 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Contact prospective or existing customers to discuss how services can meet their needs. | **major** | 0.157 | New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence |
| Quote prices, credit terms, contract terms, or fulfillment dates for services. | **major** | 0.288 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Maintain customer records using automated systems. | **major** | 0.894 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Develop sales presentations or proposals to explain service specifications. | minor | 0.809 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Negotiate prices or terms of sales or service agreements. | no fit | 0.123 | - |

### Noor Wolfe, Head of Support (Brightpath Home Co., Customer support head)

O*NET: First-Line Supervisors of Office and Administrative Support Workers. Apps in our catalog: Dropbox, Facebook Pages, Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, Tableau, YouTube.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Resolve customer complaints or answer customers' questions regarding policies and procedures. | **major** | 0.673 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Prepare and issue work schedules, deadlines, and duty assignments for office or administrative staff. | **major** | 0.59 | Staff rota in sheet -> send each person their shifts/duties + change alerts |
| Review records or reports pertaining to activities such as production, payroll, or shipping to verify details, monitor work activities, or evaluate performance. | minor | 0.852 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Recruit, interview, and select employees. | minor | 0.099 | New application -> tracker record -> AI screen summary -> interview invite |
| Interpret and communicate work procedures and company policies to staff. | minor | 0.609 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Develop work schedules according to budgets and workloads. | minor | 0.882 | Staff rota in sheet -> send each person their shifts/duties + change alerts |
| Research, compile, and prepare reports, manuals, correspondence, or other information required by management or governmental agencies. | minor | 0.457 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Supervise the work of office, administrative, or customer service employees to ensure adherence to quality standards, deadlines, and proper procedures, correcting errors or problems. | no fit | 0.099 | - |
| Provide employees with guidance in handling difficult or complex problems or in resolving escalated complaints or disputes. | no fit | 0.051 | - |
| Discuss job performance problems with employees to identify causes and issues and to work on resolving problems. | no fit | 0.0 | - |
| Evaluate employees' job performance and conformance to regulations and recommend appropriate personnel action. | no fit | 0.028 | - |
| Train or instruct employees in job duties or company policies or arrange for training to be provided. | no fit | 0.051 | - |

### Olu Farouk, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Paula Mwangi, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Reza Tran, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Sofia Okafor, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Tariq Costa, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Vera Osei, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Wanjiru Varga, Customer Service Rep (Brightpath Home Co., Customer support)

O*NET: Customer Service Representatives. Apps in our catalog: Airtable, Dropbox, Facebook Pages, Google Docs, Google Drive, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SharePoint, Microsoft Teams, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack, YouTube, Zoom.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Confer with customers by telephone or in person to provide information about products or services, take or enter orders, cancel accounts, or obtain details of complaints. | **major** | 0.71 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Keep records of customer interactions or transactions, recording details of inquiries, complaints, or comments, as well as actions taken. | **major** | 0.743 | Form/email/app event -> create or update a record in sheet/Airtable/CRM |
| Check to ensure that appropriate changes were made to resolve customers' problems. | **major** | 0.359 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Contact customers to respond to inquiries or to notify them of claim investigation results or any planned adjustments. | **major** | 0.317 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Determine charges for services requested, collect deposits or payments, or arrange for billing. | **major** | 0.72 | Job done or due date -> create invoice -> send -> overdue reminder |
| Complete contract forms, prepare change of address records, or issue service discontinuance orders, using computers. | **major** | 0.921 | Collected answers -> pre-fill a standard form/claim -> human checks and submits |
| Refer unresolved customer grievances to designated departments for further investigation. | **major** | 0.105 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Resolve customers' service or billing complaints by performing activities such as exchanging merchandise, refunding money, or adjusting bills. | minor | 0.644 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |

### Yara Eriksen, Head of Operations (Brightpath Home Co., Operations head)

O*NET: General and Operations Managers. Apps in our catalog: Airtable, Confluence, Dropbox, Facebook Pages, Google Ads, Google Docs, Google Drive, Google Slides, HubSpot, LinkedIn, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Review financial statements, sales or activity reports, or other performance data to measure productivity or goal achievement or to identify areas needing cost reduction or program improvement. | **major** | 0.772 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare staff work schedules and assign specific duties. | **major** | 0.614 | Staff rota in sheet -> send each person their shifts/duties + change alerts |
| Perform personnel functions, such as selection, training, or evaluation. | minor | 0.033 | New application -> tracker record -> AI screen summary -> interview invite |
| Develop or implement product-marketing strategies, including advertising campaigns or sales promotions. | minor | 0.834 | New subscriber/segment -> add to email list -> campaign or sequence |
| Direct and coordinate activities of businesses or departments concerned with the production, pricing, sales, or distribution of products. | no fit | 0.75 | - |
| Manage the movement of goods into and out of production facilities to ensure efficiency, effectiveness, or sustainability of operations. | no fit | 0.838 | - |
| Direct administrative activities directly related to making products or providing services. | no fit | 0.928 | - |
| Set prices or credit terms for goods or services, based on forecasts of customer demand. | no fit | 0.899 | - |
| Direct or coordinate financial or budget activities to fund operations, maximize investments, or increase efficiency. | no fit | 0.761 | - |
| Perform sales floor work, such as greeting or assisting customers, stocking shelves, or taking inventory. | no fit | 0.604 | - |
| Plan or direct activities, such as sales promotions, that require coordination with other department managers. | no fit | 0.101 | - |
| Establish or implement departmental policies, goals, objectives, or procedures in conjunction with board members, organization officials, or staff members. | no fit | 0.03 | - |

### Zubair Lopez, Logistics Coordinator (Brightpath Home Co., Operations)

O*NET: Logisticians. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Maintain and develop positive business relationships with a customer's key personnel involved in, or directly relevant to, a logistics activity. | minor | 0.0 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Develop an understanding of customers' needs and take actions to ensure that such needs are met. | minor | 0.084 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Manage subcontractor activities, reviewing proposals, developing performance specifications, and serving as liaisons between subcontractors and organizations. | minor | 0.599 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Develop proposals that include documentation for estimates. | minor | 0.7 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Review logistics performance with customers against targets, benchmarks, and service agreements. | minor | 0.075 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Direct availability and allocation of materials, supplies, and finished products. | minor | 0.891 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Explain proposed solutions to customers, management, or other interested parties through written proposals and oral presentations. | minor | 0.184 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Redesign the movement of goods to maximize value and minimize costs. | no fit | 0.947 | - |

### Anika Silva, Logistics Coordinator (Brightpath Home Co., Operations)

O*NET: Logisticians. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Maintain and develop positive business relationships with a customer's key personnel involved in, or directly relevant to, a logistics activity. | minor | 0.0 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Develop an understanding of customers' needs and take actions to ensure that such needs are met. | minor | 0.084 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Manage subcontractor activities, reviewing proposals, developing performance specifications, and serving as liaisons between subcontractors and organizations. | minor | 0.599 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Develop proposals that include documentation for estimates. | minor | 0.7 | Quote request -> fill quote/price list template -> send to client -> follow up |
| Review logistics performance with customers against targets, benchmarks, and service agreements. | minor | 0.075 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Direct availability and allocation of materials, supplies, and finished products. | minor | 0.891 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Explain proposed solutions to customers, management, or other interested parties through written proposals and oral presentations. | minor | 0.184 | Brief or trigger -> AI drafts text (post, article, email) -> doc for human review |
| Redesign the movement of goods to maximize value and minimize costs. | no fit | 0.947 | - |

### Amara Okafor, Warehouse & Shipping Clerk (Brightpath Home Co., Operations)

O*NET: Shipping, Receiving, and Inventory Clerks. Apps in our catalog: Microsoft Excel 365, Microsoft Outlook.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Prepare documents, such as work orders, bills of lading, or shipping orders, to route materials. | **major** | 0.493 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Record shipment data, such as weight, charges, space availability, damages, or discrepancies, for reporting, accounting, or recordkeeping purposes. | **major** | 0.769 | Order shipped -> tracking to customer + record shipment data |
| Contact carrier representatives to make arrangements or to issue instructions for shipping and delivery of materials. | **major** | 0.869 | Order shipped -> tracking to customer + record shipment data |
| Examine shipment contents and compare with records, such as manifests, invoices, or orders, to verify accuracy. | minor | 0.337 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Requisition and store shipping materials and supplies to maintain inventory of stock. | minor | 0.61 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Confer or correspond with establishment representatives to rectify problems, such as damages, shortages, or nonconformance to specifications. | minor | 0.029 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Pack, seal, label, or affix postage to prepare materials for shipping, using hand tools, power tools, or postage meter. | no fit | 0.895 | - |
| Deliver or route materials to departments using handtruck, conveyor, or sorting bins. | no fit | 0.908 | - |

### Bilal Costa, Warehouse & Shipping Clerk (Brightpath Home Co., Operations)

O*NET: Shipping, Receiving, and Inventory Clerks. Apps in our catalog: Microsoft Excel 365, Microsoft Outlook.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Prepare documents, such as work orders, bills of lading, or shipping orders, to route materials. | **major** | 0.493 | Deal or form data -> fill a document template -> send for e-signature -> file it |
| Record shipment data, such as weight, charges, space availability, damages, or discrepancies, for reporting, accounting, or recordkeeping purposes. | **major** | 0.769 | Order shipped -> tracking to customer + record shipment data |
| Contact carrier representatives to make arrangements or to issue instructions for shipping and delivery of materials. | **major** | 0.869 | Order shipped -> tracking to customer + record shipment data |
| Examine shipment contents and compare with records, such as manifests, invoices, or orders, to verify accuracy. | minor | 0.337 | New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment |
| Requisition and store shipping materials and supplies to maintain inventory of stock. | minor | 0.61 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Confer or correspond with establishment representatives to rectify problems, such as damages, shortages, or nonconformance to specifications. | minor | 0.029 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Pack, seal, label, or affix postage to prepare materials for shipping, using hand tools, power tools, or postage meter. | no fit | 0.895 | - |
| Deliver or route materials to departments using handtruck, conveyor, or sorting bins. | no fit | 0.908 | - |

### Chen Osei, Supply Chain Manager (Brightpath Home Co., Operations)

O*NET: Supply Chain Managers. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Manage activities related to strategic or tactical purchasing, material requirements planning, controlling inventory, warehousing, or receiving. | minor | 0.922 | Stock below threshold -> alert + draft reorder/PO to supplier |
| Define performance metrics for measurement, comparison, or evaluation of supply chain factors, such as product cost or quality. | minor | 0.597 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Confer with supply chain planners to forecast demand or create supply plans that ensure availability of materials or products. | minor | 0.68 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Analyze inventories to determine how to increase inventory turns, reduce waste, or optimize customer service. | minor | 0.681 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Determine appropriate equipment and staffing levels to load, unload, move, or store materials. | no fit | 0.541 | - |
| Select transportation routes to maximize economy by combining shipments or consolidating warehousing and distribution. | no fit | 0.851 | - |
| Implement new or improved supply chain processes to improve efficiency or performance. | no fit | 0.672 | - |
| Develop procedures for coordination of supply chain management with other functional areas, such as sales, marketing, finance, production, or quality assurance. | no fit | 0.624 | - |

### Dalia Varga, Purchasing Agent (Brightpath Home Co., Operations)

O*NET: Purchasing Agents, Except Wholesale, Retail, and Farm Products. Apps in our catalog: Facebook Pages, Google Ads, Google Docs, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Prepare purchase orders, solicit bid proposals, and review requisitions for goods and services. | **major** | 0.798 | Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply |
| Monitor and follow applicable laws and regulations. | minor | 0.683 | Recurring compliance/renewal date -> reminder + log record |
| Analyze price proposals, financial reports, and other data and information to determine reasonable prices. | minor | 0.787 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Research and evaluate suppliers, based on price, quality, selection, service, support, availability, reliability, production and distribution capabilities, and the supplier's reputation and history. | minor | 0.495 | Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email |
| Purchase the highest quality merchandise at the lowest possible price and in correct amounts. | no fit | 0.845 | - |
| Formulate policies and procedures for bid proposals and procurement of goods and services. | no fit | 0.495 | - |
| Write and review product specifications, maintaining a working technical knowledge of the goods or services to be purchased. | no fit | 0.662 | - |
| Hire, train, or supervise purchasing clerks, buyers, and expediters. | no fit | 0.632 | - |

### Elif Eriksen, Head of Finance (Brightpath Home Co., Finance & people head)

O*NET: Financial Managers. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Tableau, Workday.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Establish and maintain relationships with individual or business customers or provide assistance with problems these customers may encounter. | minor | 0.479 | After sale/visit/closing -> timed check-in email -> log reply in CRM |
| Communicate with stockholders or other investors to provide information or to raise capital. | minor | 0.136 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Oversee the flow of cash or financial instruments. | minor | 0.277 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Develop or analyze information to assess the current or future financial status of firms. | minor | 0.854 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare financial or regulatory reports required by laws, regulations, or boards of directors. | minor | 0.635 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Examine, evaluate, or process loan applications. | minor | 0.832 | New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting |
| Recruit staff members. | minor | 0.022 | New application -> tracker record -> AI screen summary -> interview invite |
| Establish procedures for custody or control of assets, records, loan collateral, or securities to ensure safekeeping. | no fit | 0.357 | - |
| Plan, direct, or coordinate the activities of workers in branches, offices, or departments of establishments, such as branch banks, brokerage firms, risk and insurance departments, or credit departments. | no fit | 0.204 | - |
| Approve, reject, or coordinate the approval or rejection of lines of credit or commercial, real estate, or personal loans. | no fit | 0.901 | - |
| Evaluate financial reporting systems, accounting or collection procedures, or investment activities and make recommendations for changes to procedures, operating systems, budgets, or other financial control functions. | no fit | 0.894 | - |
| Network within communities to find and attract new business. | no fit | 0.131 | - |

### Farhan Lopez, Accountant (Brightpath Home Co., Finance & people)

O*NET: Accountants and Auditors. Apps in our catalog: Facebook Pages, Google Docs, Google Sheets, Google Slides, Microsoft Excel 365, Microsoft OneNote, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Tableau, Workday.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Process invoices for payment. | **major** | 0.805 | Job done or due date -> create invoice -> send -> overdue reminder |
| Review accounts for discrepancies and reconcile differences. | **major** | 0.935 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare, examine, or analyze accounting records, financial statements, or other financial reports to assess accuracy, completeness, and conformance to reporting and procedural standards. | minor | 0.688 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare adjusting journal entries. | minor | 0.087 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Inspect account books and accounting systems for efficiency, effectiveness, and use of accepted accounting procedures to record transactions. | minor | 0.463 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare detailed reports on audit findings. | minor | 0.096 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Prepare, analyze, or verify annual reports, financial statements, and other records, using accepted accounting and statistical procedures to assess financial condition and facilitate financial planning. | minor | 0.637 | Schedule -> pull numbers from apps -> summary report by email/Slack |
| Compute taxes owed and prepare tax returns, ensuring compliance with payment, reporting, or other tax requirements. | no fit | 0.974 | - |

### Grace Silva, Bookkeeper (Brightpath Home Co., Finance & people)

O*NET: Bookkeeping, Accounting, and Auditing Clerks. Apps in our catalog: Dropbox, Facebook Pages, Google Docs, Google Drive, Microsoft Excel 365, Microsoft Outlook, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Operate computers programmed with accounting software to record, store, and analyze information. | **major** | 0.938 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare and process payroll information. | minor | 0.754 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Check figures, postings, and documents for correct entry, mathematical accuracy, and proper codes. | minor | 0.862 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Prepare bank deposits by compiling data from cashiers, verifying and balancing receipts, and sending cash, checks, or other forms of payment to banks. | minor | 0.784 | Payment received -> record in accounting + sheet -> receipt to client |
| Comply with federal, state, and company policies, procedures, and regulations. | minor | 0.093 | Recurring compliance/renewal date -> reminder + log record |
| Receive, record, and bank cash, checks, and vouchers. | minor | 0.584 | Payment received -> record in accounting + sheet -> receipt to client |
| Calculate and prepare checks for utilities, taxes, and other payments. | minor | 0.908 | Job done or due date -> create invoice -> send -> overdue reminder |
| Operate 10-key calculators, typewriters, and copy machines to perform calculations and produce documents. | no fit | 0.922 | - |

### Hiro Rahman, HR Specialist (Brightpath Home Co., Finance & people)

O*NET: Human Resources Specialists. Apps in our catalog: Airtable, Cisco Webex Meetings, Drupal, Facebook Pages, GitHub, Google Ads, Google Docs, Google Drive, Google Slides, LinkedIn, Matrix, Microsoft Excel 365, Microsoft Outlook, Microsoft SQL Server, Microsoft SharePoint, NetSuite, Oracle Database, Quickbooks Online, Salesforce, Slack.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Schedule or administer skill, intelligence, psychological, or drug tests for current or prospective employees. | **major** | 0.18 | Booking form or calendar event -> confirmation + reminder email/SMS |
| Prepare or maintain employment records related to events, such as hiring, termination, leaves, transfers, or promotions, using human resources management system software. | **major** | 0.843 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Interpret and explain human resources policies, procedures, laws, standards, or regulations. | minor | 0.43 | New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review |
| Hire employees and process hiring-related paperwork. | minor | 0.03 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Administer employee benefit plans. | minor | 0.17 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Conduct reference or background checks on job applicants. | minor | 0.808 | New application -> tracker record -> AI screen summary -> interview invite |
| Maintain current knowledge of Equal Employment Opportunity (EEO) and affirmative action guidelines and laws, such as the Americans with Disabilities Act (ADA). | no fit | 0.0 | - |
| Address employee relations issues, such as harassment allegations, work complaints, or other employee concerns. | no fit | 0.215 | - |

### Isha Mensah, Payroll Clerk (Brightpath Home Co., Finance & people)

O*NET: Payroll and Timekeeping Clerks. Apps in our catalog: Facebook Pages, Microsoft Excel 365, Microsoft Outlook, NetSuite, Quickbooks Online, Workday.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Process paperwork for new employees and enter employee information into the payroll system. | **major** | 0.68 | New hire/employee change -> HR record + checklist tasks + welcome email |
| Distribute and collect timecards each pay period. | **major** | 0.09 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Verify attendance, hours worked, and pay adjustments, and post information onto designated records. | minor | 0.893 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Process and issue employee paychecks and statements of earnings and deductions. | minor | 0.888 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Compute wages and deductions, and enter data into computers. | minor | 0.833 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Prepare and file payroll tax returns. | minor | 0.419 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |
| Prepare and balance period-end reports, and reconcile issued payrolls to bank statements. | minor | 0.78 | New transactions -> sync to accounting/sheet -> flag mismatches for review |
| Review time sheets, work charts, wage computation, and other information to detect and reconcile payroll discrepancies. | minor | 0.089 | Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve |

### Jonas Nakamura, Systems & Analytics Analyst (Brightpath Home Co., Finance & people)

O*NET: Computer Systems Analysts. Apps in our catalog: Apache Kafka, Cisco Webex Meetings, Confluence, Drupal, Facebook Pages, GitHub, Google Docs, JSON, Microsoft Excel 365, Microsoft Outlook, Microsoft Power BI, Microsoft SQL Server, Microsoft SharePoint, Microsoft Teams, MongoDB, MySQL, NetSuite, Omni, OpenAI, Oracle Database.

| task | fit | Laya auto | automation |
|---|---|---|---|
| Troubleshoot program and system malfunctions to restore normal functioning. | minor | 0.527 | App/site/system check fails -> alert to email/Slack + incident task |
| Provide staff and users with assistance solving computer-related problems, such as malfunctions and program problems. | minor | 0.153 | Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved |
| Test, maintain, and monitor computer programs and systems, including coordinating the installation of computer programs and systems. | minor | 0.741 | App/site/system check fails -> alert to email/Slack + incident task |
| Coordinate and link the computer systems within an organization to increase compatibility so that information can be shared. | minor | 0.692 | App/site/system check fails -> alert to email/Slack + incident task |
| Review and analyze computer printouts and performance indicators to locate code problems, and correct errors by correcting codes. | minor | 0.732 | App/site/system check fails -> alert to email/Slack + incident task |
| Use the computer in the analysis and solution of business problems, such as development of integrated production and inventory control and cost analysis systems. | no fit | 0.934 | - |
| Use object-oriented programming languages, as well as client and server applications development processes and multimedia and Internet technology. | no fit | 0.544 | - |
| Analyze information processing or computation needs and plan and design computer systems, using techniques such as structured analysis, data modeling, and information engineering. | no fit | 0.318 | - |

## The 30 most common automations across all 88 people

Counted from the "automation" column above: how many people have at least one task it fits, how many tasks, and how many of those are **major**.

| # | automation | people | tasks | major | example roles |
|---|---|---|---|---|---|
| 1 | **scheduled reports**: Schedule -> pull numbers from apps -> summary report by email/Slack | 24 | 39 | 4 | Account Director, Accountant, Bookkeeper, Business consultant |
| 2 | **AI first drafts**: Brief or trigger -> AI drafts text (post, article, email) -> doc for human review | 22 | 49 | 0 | Business consultant, Content Writer, Copywriter, Course creator and trainer |
| 3 | **approvals**: Draft/design/bill ready -> ask approver (email/Slack) -> route on yes/no | 20 | 22 | 4 | CEO, Content Writer, Copywriter, Creative Director |
| 4 | **keep records up to date**: Form/email/app event -> create or update a record in sheet/Airtable/CRM | 18 | 20 | 16 | Bookkeeper, Clinic front desk, Customer Service Rep, Event planner |
| 5 | **meeting notes and actions**: Meeting ends -> notes/agenda doc -> action items to tasks + recap email | 17 | 17 | 0 | CEO, Creative Director, Freelance designer, Graphic Designer |
| 6 | **complaints to tickets**: Complaint/issue -> ticket or task -> notify owner -> tell customer when resolved | 15 | 36 | 24 | Customer Service Rep, Guesthouse manager, Head of Sales, Insurance agent |
| 7 | **research digests**: Schedule or request -> fetch listings/news/competitor data -> AI summary to sheet/email | 15 | 33 | 4 | Account Director, Business consultant, Content Writer, Copywriter |
| 8 | **answer common questions**: New email/chat question -> AI drafts reply from your FAQ/price list -> send or hold for review | 15 | 23 | 12 | B2B Sales Rep, Guesthouse manager, HR Specialist, Head of Support |
| 9 | **quotes and price lists**: Quote request -> fill quote/price list template -> send to client -> follow up | 13 | 16 | 6 | Account Director, B2B Sales Rep, Head of Marketing, Logistics Coordinator |
| 10 | **invoices and payment reminders**: Job done or due date -> create invoice -> send -> overdue reminder | 13 | 15 | 12 | Accountant, Bookkeeper, Customer Service Rep, Freelance bookkeeper |
| 11 | **client check-ins**: After sale/visit/closing -> timed check-in email -> log reply in CRM | 13 | 15 | 8 | B2B Sales Rep, Head of Finance, Insurance agent, Logistics Coordinator |
| 12 | **design asset delivery**: Design/photo ready -> export/resize/AI image -> deliver to client folder | 11 | 35 | 0 | Creative Director, Freelance designer, Graphic Designer, Head of Design |
| 13 | **pre-fill forms**: Collected answers -> pre-fill a standard form/claim -> human checks and submits | 11 | 11 | 7 | Business consultant, Clinic front desk, Customer Service Rep, Insurance agent |
| 14 | **stock alerts and reorders**: Stock below threshold -> alert + draft reorder/PO to supplier | 11 | 11 | 6 | B2B Sales Rep, Logistics Coordinator, Restaurant manager, Sales rep |
| 15 | **order processing**: New order -> confirm to customer -> record in sheet/accounting -> notify fulfilment | 10 | 10 | 7 | Customer Service Rep, Online shop owner, Warehouse & Shipping Clerk |
| 16 | **sync and check bookkeeping**: New transactions -> sync to accounting/sheet -> flag mismatches for review | 9 | 22 | 7 | Accountant, Bookkeeper, Freelance bookkeeper, Head of Finance |
| 17 | **route incoming messages**: Incoming email/message/document -> classify -> forward to the right person or channel | 8 | 12 | 3 | Clinic front desk, PR and social specialist, Property manager, Social Media Manager |
| 18 | **documents from templates + e-sign**: Deal or form data -> fill a document template -> send for e-signature -> file it | 8 | 9 | 8 | Online shop owner, Real estate agent, Sales Development Rep, Sales rep |
| 19 | **client intake**: New client -> intake form -> answers to CRM/sheet -> prepared summary for the meeting | 8 | 8 | 3 | Clinic front desk, Creative Director, Event planner, Head of Design |
| 20 | **bookings and reminders**: Booking form or calendar event -> confirmation + reminder email/SMS | 7 | 8 | 6 | Clinic front desk, Guesthouse manager, HR Specialist, Real estate agent |
| 21 | **system alerts**: App/site/system check fails -> alert to email/Slack + incident task | 6 | 9 | 1 | Indie software developer, Project Coordinator, Systems & Analytics Analyst, Web & Digital Designer |
| 22 | **hiring pipeline**: New application -> tracker record -> AI screen summary -> interview invite | 6 | 8 | 1 | Founder & Managing Director, HR Specialist, Head of Finance, Head of Operations |
| 23 | **project tasks**: New client/project -> create tasks in project tool -> status updates to channel | 6 | 6 | 0 | Creative Director, Head of Design, Property manager, Web & Digital Designer |
| 24 | **file filing**: New file/attachment -> rename -> save to the right Drive/Dropbox folder | 6 | 6 | 5 | Business consultant, Clinic front desk, Freelance writer, Photographer |
| 25 | **compliance reminders**: Recurring compliance/renewal date -> reminder + log record | 6 | 6 | 2 | Bookkeeper, Freelance bookkeeper, Insurance agent, Purchasing Agent |
| 26 | **supplier emails and POs**: Purchase need or issue -> email supplier/vendor (PO, bid, claim) -> track reply | 6 | 6 | 1 | Logistics Coordinator, Property manager, Purchasing Agent, Warehouse & Shipping Clerk |
| 27 | **payroll inputs**: Collect hours/timecards from form or sheet -> payroll sheet -> reminder to approve | 5 | 10 | 1 | Bookkeeper, Freelance bookkeeper, Payroll Clerk, Virtual assistant |
| 28 | **surveys**: After session/visit -> send survey -> collect answers in sheet -> summary | 5 | 10 | 3 | Course creator and trainer, Email Marketing Specialist, Market Research Analyst, Solo marketer |
| 29 | **publish social posts**: Approved post (sheet/Canva/Drive) -> publish or schedule on social pages -> log it | 5 | 5 | 5 | PR and social specialist, Social Media Manager, Social Media Specialist |
| 30 | **leads to CRM + follow-up**: New lead (form/ad/email) -> CRM record -> notify owner -> follow-up sequence | 5 | 5 | 3 | Head of Sales, Insurance agent, Sales Development Rep, Wholesale Account Manager |

There are 37 automation types in total; the 7 not shown are the rarest. Next step: turn the top 30 into build-eval prompts (one sentence each) and check FansaChat builds a working workflow for each.
