# CodeShield SDLC Dashboard – Test Plan

| | |
|---|---|
| **Project** | codeshield-sdlc-dashboard |
| **Framework** | Django 6.1.2 (Python) |
| **Environment** | Local development server, `http://127.0.0.1:8000/` |
| **Test date** | 20 October 2026 |
| **Tested by** | Peter Karanja Kibe |

## 1. Objective

To verify that the core logic behind the CodeShield dashboard works correctly: that the summary counts are calculated from the stored incidents, and that incident records are listed accurately and in the right order.

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Dashboard summary counts (Total, Open, Critical, Resolved) | Creating, editing and deleting incidents |
| Incident records listing (fields, ordering, actions) | Form validation |
| | Responsive layout and performance |

## 3. Test Data

Two incidents were stored in the database before testing:

| ID | Title | Pillar | Severity | Status |
|----|-------|--------|----------|--------|
| CS-001 | Suspicious package dependency | Package Registry | Critical | Open |
| CS-002 | Unusual repository access | Version Control | High | Investigating |

## 4. Test Case Summary

| ID | Test case | Result |
|----|-----------|--------|
| TC-01 | Dashboard summary counts are calculated correctly | ✅ Pass |
| TC-02 | Incident records are listed newest first with all fields | ✅ Pass |

## 5. Test Cases

### TC-01: Dashboard summary counts

**Objective:** Confirm the dashboard counts match the incidents stored in the database.

**Steps:**
1. Start the server with `python manage.py runserver`.
2. Open the dashboard at `http://127.0.0.1:8000/`.
3. Read the four cards under *Incident Overview*.

| | Total | Open | Critical | Resolved |
|---|-------|------|----------|----------|
| **Expected** | 2 | 1 | 1 | 0 |
| **Actual** | 2 | 1 | 1 | 0 |

Open is 1 because only CS-001 has the status *Open*. CS-002 is *Investigating*. Critical is 1 because only CS-001 is Critical. No incident is Resolved.

**Result:** ✅ Pass

![TC-01 dashboard overview](../screenshots/02-dashboard-overview.jpg)

---

### TC-02: Incident records listing and ordering

**Objective:** Confirm saved incidents are listed with the correct details and that the newest incident appears first.

**Steps:**
1. Open the dashboard and scroll to *Incident Records*.
2. Check the order of the rows and the details shown for each incident.

| | Expected | Actual |
|---|----------|--------|
| **Row order** | CS-002 (10:42) above CS-001 (10:35) | CS-002 above CS-001 |
| **Fields per row** | ID, title, description, pillar, severity, status, date reported | All fields shown, matching the test data |
| **Actions** | Edit and Delete buttons on each row | Both buttons shown on each row |

**Result:** ✅ Pass

![TC-02 incident records](../screenshots/05-incident-records.jpg)

## 6. Results Summary

| Total | Passed | Failed |
|-------|--------|--------|
| 2 | 2 | 0 |

Both test cases produced the expected results, and no errors were observed. The Edit and Delete actions were confirmed to be present but their behaviour was not tested.
