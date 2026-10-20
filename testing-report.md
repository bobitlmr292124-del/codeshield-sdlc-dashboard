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
| 1 | Server startup | Server starts with no errors | Server started, 0 issues | ✅ Pass |
| 2 | Dashboard overview | Summary cards show correct incident counts | Counts match the records | ✅ Pass |
| 3 | Security analytics | Charts show incidents by severity, status and SDLC pillar | All three charts render correctly | ✅ Pass |
| 4 | Report incident form | Form displays all required fields | All fields displayed | ✅ Pass |
| 5 | Incident records table | Saved incidents are listed with details and actions | Both incidents listed with Edit/Delete buttons | ✅ Pass |
| 6 | Responsive layout | Table remains fully usable on a narrow screen | Right-hand columns are cut off | ⚠️ Minor issue |

**Overall:** The core features work as expected. No functional errors or crashes were observed. Only minor UI/usability issues were noted (Section 4).

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




## 4. Errors and Issues Found

No crashes, server errors or incorrect data were found. The following minor issues were noted:

| # | Issue | Severity | Suggested fix |
|---|-------|----------|---------------|
| 1 | Records table is cut off on narrow screens (Date Reported and Actions columns hidden) | Low | Wrap the table in a horizontally scrollable container (`overflow-x: auto`) or use a stacked layout on small screens |
| 2 | Form label reads "Incident id:" (lowercase "id"), the default Django field label | Low | Set a custom label, e.g. "Incident ID" |
| 3 | Form label "Pillar" differs from the table heading "SDLC Pillar" | Low | Use consistent wording in both places |
| 4 | Incident ID is typed in manually, which risks duplicates or typos | Low | Auto-generate IDs (e.g. CS-003) or enforce a unique constraint with a clear error message |



## 5. Conclusion

The CodeShield SDLC Dashboard starts correctly and displays accurate incident counts, analytics charts, a reporting form and an incident records table. The features shown meet their expected results. The remaining work is to fix the minor UI issues listed above and to test the create, edit, delete and validation workflows.
