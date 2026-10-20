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

![Server startup](screenshots/01-server-startup.jpg)

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

![Dashboard overview](screenshots/02-dashboard-overview.jpg)

---

### 3.3 Security Analytics

**Expected:** Three charts visualise the incident data by severity, status and SDLC pillar.

**Actual:**

- **Incidents by Severity:** one High and one Critical incident.
- **Incidents by Status:** split evenly between Investigating and Open.
- **Incidents by SDLC Pillar:** one in Version Control and one in Package Registry.

All charts match the data in the incident records.

![Security analytics](screenshots/03-security-analytics.jpg)

---

### 3.4 Report a Security Incident (Form)

**Expected:** The form provides fields to record an incident: Incident ID, Title, Description, Pillar, Severity and Status, with a **Save Incident** button.

**Actual:** All fields are displayed correctly. The Pillar and Severity dropdowns show a "- Select an option -" placeholder, and the Status dropdown and Save Incident button appear below them (see the next screenshot).

![Report incident form](screenshots/04-report-incident-form.jpg)

---

### 3.5 Incident Records

**Expected:** Saved incidents appear in a table showing ID, title and description, SDLC pillar, severity, status, date reported and Edit/Delete actions. The newest incident is listed first.

**Actual:** Two incidents are listed, newest first:

| ID | Title | Pillar | Severity | Status | Date reported |
|----|-------|--------|----------|--------|---------------|
| CS-002 | Unusual repository access | Version Control | High | Investigating | 13 Oct 2026, 10:42 |
| CS-001 | Suspicious package dependency | Package Registry | Critical | Open | 13 Oct 2026, 10:35 |

Severity and status are shown as colour-coded badges, and each row has **Edit** and **Delete** buttons.

![Incident records](screenshots/05-incident-records.jpg)

---

### 3.6 Incident Records on a Narrow Screen

**Expected:** The table stays readable and all columns are reachable on smaller screens.

**Actual:** On a narrower viewport the table is cut off on the right, so the Date Reported and Actions columns are not visible without scrolling horizontally. The rest of the table displays correctly.

![Incident records on a narrow screen](screenshots/06-incident-records-narrow-view.jpg)

## 4. Errors and Issues Found

No crashes, server errors or incorrect data were found. The following minor issues were noted:

| # | Issue | Severity | Suggested fix |
|---|-------|----------|---------------|
| 1 | Records table is cut off on narrow screens (Date Reported and Actions columns hidden) | Low | Wrap the table in a horizontally scrollable container (`overflow-x: auto`) or use a stacked layout on small screens |
| 2 | Form label reads "Incident id:" (lowercase "id"), the default Django field label | Low | Set a custom label, e.g. "Incident ID" |
| 3 | Form label "Pillar" differs from the table heading "SDLC Pillar" | Low | Use consistent wording in both places |
| 4 | Incident ID is typed in manually, which risks duplicates or typos | Low | Auto-generate IDs (e.g. CS-003) or enforce a unique constraint with a clear error message |

## 5. Not Verified

The screenshots do not show the following, so they should be tested separately:

- Submitting a new incident and confirming it appears in the table and updates the dashboard counts
- Editing an existing incident
- Deleting an incident (including any confirmation prompt)
- Form validation for empty fields or a duplicate Incident ID
- Dashboard behaviour when an incident is set to "Resolved"

## 6. Conclusion

The CodeShield SDLC Dashboard starts correctly and displays accurate incident counts, analytics charts, a reporting form and an incident records table. The features shown meet their expected results. The remaining work is to fix the minor UI issues listed above and to test the create, edit, delete and validation workflows.
