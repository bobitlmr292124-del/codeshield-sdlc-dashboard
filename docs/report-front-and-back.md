# CodeShield SDLC Security Dashboard: Front-End and Back-End Implementation

## 1. Introduction

CodeShield is a web-based Software Development Life Cycle (SDLC) Security Dashboard developed using the Django framework. The system provides a centralized interface for recording, monitoring and managing security incidents across the five SDLC security pillars: Endpoint/IDE, Version Control System (VCS), CI/CD, Registry/Package Registry and Production.

The dashboard enables users to view recorded incidents, assess their severity, monitor their status and maintain a structured record of security risks throughout the software development process.

## 2. Front-End Implementation

The front end provides the user interface through which users interact with the CodeShield dashboard. It is implemented using HTML templates rendered by Django, together with CSS for styling and presentation.

The dashboard presents security information in an organized format. It includes summary cards displaying the total number of incidents, open incidents, critical incidents and resolved incidents. These summaries allow users to quickly understand the current security situation.

The interface also displays incident records containing important information such as the incident ID, title, description, SDLC pillar, severity, status and date created. Users can navigate the available incident management functions to add new incidents, edit existing records and delete records.

The incident form provides fields for entering incident information. Dropdown selections are used for incident pillar, severity and status to promote consistency when recording security incidents.

## 3. Back-End Implementation

The back end is developed using Python and the Django web framework. It handles application logic, form processing, data validation, database operations and communication between the user interface and the database.

Django views process user requests and retrieve incident records for display on the dashboard. The application supports the creation, retrieval, updating and deletion of incident records.

When a user submits a new incident, the back end processes the submitted information through Django forms and saves valid records to the database. When an existing incident is edited, the system updates its stored information. The delete function removes the selected incident record.

The dashboard also uses database queries and aggregation functions to calculate incident totals and summarize incidents according to severity, status and SDLC pillar.

## 4. Database Management

The application uses Django's database integration and ORM (Object-Relational Mapper) to manage incident records. The incident model defines the structure of the information stored by the system.

The incident record contains the following fields:

- **Incident ID:** A unique identifier for each incident.
- **Title:** A short description of the security incident.
- **Description:** Additional information about the incident.
- **Pillar:** Identifies the SDLC security area affected.
- **Severity:** Indicates the level of risk, categorized as Low, Medium, High or Critical.
- **Status:** Indicates whether the incident is Open, Investigating or Resolved.
- **Created At:** Records when the incident was created.

The use of Django ORM simplifies database operations and allows the application to interact with stored records through Python objects instead of requiring manually written SQL queries for every operation.

## 5. Integration Between Front End and Back End

The front end and back end work together to provide the dashboard's incident management functionality. Users interact with the HTML forms and dashboard pages, while Django views receive requests and process the required operations.

The Django forms validate submitted information before it is stored. The ORM communicates with the database and retrieves updated records. The views then provide the relevant data to the HTML templates for presentation.

This interaction ensures that incident information displayed on the dashboard reflects the records stored in the database.

## 6. Security and Reliability Considerations

CodeShield uses Django's built-in form handling, validation and security mechanisms to support safer application processing. The application uses Django's ORM to manage database interactions and reduce the need for manually constructed SQL queries.

The incident model also enforces a unique incident identifier, helping prevent duplicate incident IDs. The use of predefined choices for severity, status and SDLC pillar promotes consistency in the information recorded.

The dashboard is intended to support security incident monitoring and management. It does not automatically integrate with external security platforms or independently detect threats. Incident records are entered and managed through the application's available functions.

## 7. Conclusion

The CodeShield front end and back end provide an integrated web-based environment for recording and managing SDLC security incidents. The Django framework supports request processing, validation, database management and presentation of incident information. Through its dashboard summaries and incident management functions, the system provides a centralized way to monitor security risks across the five SDLC security pillars.
