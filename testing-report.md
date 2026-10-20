# CodeShield SDLC Dashboard – Testing Report

| | |
|---|---|
| **Project** | codeshield-sdlc-dashboard |
| **Framework** | Django 6.1.2 (Python) |
| **Test date** | 20 October 2026 |
| **Environment** | Local development server (`http://127.0.0.1:8000/`) |
| **Tested by** | Peter Karanja Kibe |

## 1. Purpose

CodeShield is a Django web application for monitoring, reporting and managing security incidents across the Software Development Life Cycle (SDLC). This report records the features that were tested, the expected results, the actual results and any errors or issues observed.

## 2. Summary of Results

| # | Feature | Expected | Actual | Status |
|---|---------|----------|--------|--------|
| 1 | Server startup | Server starts with no errors | Server started, and the Django system check reported no issues | ✅ Pass |
| 2 | Dashboard overview | Summary cards show correct incident counts | Counts match the displayed incident records | ✅ Pass |
| 3 | Security analytics | Charts show incidents by severity, status and SDLC pillar | All three charts render correctly and match the displayed records | ✅ Pass |
| 4 | Report incident form | Form displays all required fields | All expected fields are displayed | ✅ Pass |
| 5 | Incident records table | Saved incidents are listed with details and actions | Two incidents are listed with Edit/Delete buttons | ✅ Pass |
| 6 | Responsive layout | Table remains usable on a narrow screen | Right-hand columns are cut off in the tested viewport | ⚠️ Minor issue |
| 7 | Create incident | New incident is saved and displayed | Incident creation was tested and worked as expected | ✅ Pass |
| 8 | Edit incident | Changes to an existing incident are saved | Incident editing was tested and worked as expected | ✅ Pass |
| 9 | Delete incident | Selected incident is deleted as intended | Incident deletion was tested and worked as expected | ✅ Pass |
| 10 | Input validation | Invalid or duplicate values are handled appropriately | Not verified in the tests documented in this report | Not Tested |

**Overall:** The dashboard display and the tested incident-management workflows operated as expected. A responsive-layout issue and several minor usability improvements were identified. Input validation requires separate testing before its behaviour can be confirmed.

## 3. Detailed Test Results

### 3.1 Server Startup

**Expected:** The Django development server starts without errors.

**Actual:** The system check reported no issues, and the server started on Django 6.1.2 at `http://127.0.0.1:8000/`.

<img width="463" height="95" alt="WhatsApp Image 2026-10-20 at 13 33 26" src="https://github.com/user-attachments/assets/8da7fcef-e112-465b-89a0-f149f1324457" />


---

### 3.2 Dashboard Overview

**Expected:** The dashboard shows summary cards for Total, Open, Critical and Resolved incidents, matching the stored records.

**Actual:**

| Card | Value shown |
|------|-------------|
| Total Incidents | 2 |
| Open Incidents | 1 |
| Critical Incidents | 1 |
| Resolved Incidents | 0 |

These values are consistent with the two records in the table (CS-001 is Critical/Open, CS-002 is High/Investigating).

<img width="651" height="596" alt="WhatsApp Image 2026-10-20 at 13 33 24" src="https://github.com/user-attachments/assets/c408b940-d1d0-4039-bc00-1503759686f8" />


---

### 3.3 Security Analytics

**Expected:** Three charts visualise the incident data by severity, status and SDLC pillar.

**Actual:**

- **Incidents by Severity:** one High and one Critical incident.
- **Incidents by Status:** split evenly between Investigating and Open.
- **Incidents by SDLC Pillar:** one in Version Control and one in Package Registry.

All charts match the data in the incident records.

<img width="1266" height="492" alt="WhatsApp Image 2026-10-20 at 13 33 24 (1)" src="https://github.com/user-attachments/assets/d77800fc-7c8f-4920-9877-2910d9b7ca78" />


---

### 3.4 Report a Security Incident (Form)

**Expected:** The form provides fields to record an incident: Incident ID, Title, Description, Pillar, Severity and Status, with a **Save Incident** button.

**Actual:** All fields are displayed correctly. The Pillar and Severity dropdowns show a "- Select an option -" placeholder, and the Status dropdown and Save Incident button appear below them (see the next screenshot).

<img width="1214" height="606" alt="WhatsApp Image 2026-10-20 at 13 33 25" src="https://github.com/user-attachments/assets/c2d0ad47-2565-4cf7-a5be-4503b22cbf45" />


---

### 3.5 Incident Records

**Expected:** Saved incidents appear in a table showing ID, title and description, SDLC pillar, severity, status, date reported and Edit/Delete actions. The newest incident is listed first.

**Actual:** Two incidents are listed, newest first:

| ID | Title | Pillar | Severity | Status | Date reported |
|----|-------|--------|----------|--------|---------------|
| CS-002 | Unusual repository access | Version Control | High | Investigating | 13 Oct 2026, 10:42 |
| CS-001 | Suspicious package dependency | Package Registry | Critical | Open | 13 Oct 2026, 10:35 |

Severity and status are shown as colour-coded badges, and each row has **Edit** and **Delete** buttons.

<img width="902" height="458" alt="WhatsApp Image 2026-10-20 at 13 33 26 (1)" src="https://github.com/user-attachments/assets/88fb6779-e0f5-4441-b27f-43c63d64ad3b" />

---

### 3.6 Incident Records on a Narrow Screen

**Expected:** The table stays readable and all columns are reachable on smaller screens.

**Actual:** On a narrower viewport the table is cut off on the right, so the Date Reported and Actions columns are not visible without scrolling horizontally. The rest of the table displays correctly.

<img width="1200" height="468" alt="WhatsApp Image 2026-10-20 at 13 33 25 (1)" src="https://github.com/user-attachments/assets/7003d841-bb5f-449f-a17a-cced4c492c89" />

### 3.7 Create an Incident

**Expected:** A user can submit a security incident through the reporting form, and the new record appears in the incident table.

**Actual:** Incident creation was tested and worked as expected.

**Status:** ✅ Pass

### 3.8 Edit an Incident

**Expected:** A user can edit an existing incident and save the changes successfully.

**Actual:** Incident editing was tested and worked as expected.

**Status:** ✅ Pass

### 3.9 Delete an Incident

**Expected:** A user can delete the selected incident, and it is removed from the records table as intended.

**Actual:** Incident deletion was tested and worked as expected.

**Status:** ✅ Pass

Supporting screenshots should be included for these tests where available. The results should reflect the actual behaviour observed during testing.


## 4. Errors and Issues Found

No crashes, server errors or incorrect data were found. The following minor issues were noted:

| # | Issue | Severity | Suggested fix |
|---|-------|----------|---------------|
| 1 | Records table is cut off on narrow screens (Date Reported and Actions columns hidden) | Low | Wrap the table in a horizontally scrollable container (`overflow-x: auto`) or use a stacked layout on small screens |
| 2 | Form label reads "Incident id:" (lowercase "id"), the default Django field label | Low | Set a custom label, e.g. "Incident ID" |
| 3 | Form label "Pillar" differs from the table heading "SDLC Pillar" | Low | Use consistent wording in both places |
| 4 | Incident ID is entered manually, which may lead to duplicates or typing errors | Low | Consider automatically generating incident IDs or enforcing uniqueness with clear validation feedback. Duplicate-ID handling has not been verified in this report. |

## 5. Conclusion

The CodeShield SDLC Dashboard starts correctly and displays the dashboard overview, security analytics, incident reporting form and incident records table as expected in the tested environment. Testing also confirmed that creating, editing and deleting incidents worked as expected.

A responsive-layout issue and several minor usability improvements were identified, particularly regarding table visibility on narrow screens, form labels and incident ID handling. Input validation requires further testing before its behaviour can be confirmed.

Overall, the tested components operated as expected within the scope of this assessment. Further improvements and testing are recommended, and these results do not establish that every feature is defect-free or that the application's security has been comprehensively verified.
