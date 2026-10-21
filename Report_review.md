# CodeShield SDLC Security Dashboard — Report Review

## 1. Introduction and Project Description

CodeShield SDLC Security Dashboard is a web-based application developed using Python and Django to support the organization and monitoring of security-related information throughout the Software Development Life Cycle (SDLC). The project follows the SDLC Infrastructure Threat Framework (SITF), which identifies five security pillars: Endpoint/IDE, Version Control System (VCS), Continuous Integration and Continuous Delivery (CI/CD), Registry, and Production.

The current implementation provides a dashboard for presenting security-related information and includes incident-management functionality. The report must distinguish implemented features from partially implemented features and proposed future improvements. The inclusion of the five pillars in the framework does not mean that all five have been fully integrated with external security tools.

## 2. Problem Statement

Security information generated throughout the Software Development Life Cycle can be difficult to organize and monitor when it is maintained across separate tools and records. Limited visibility into security incidents and risks can make it harder to identify issues and monitor their progress. CodeShield addresses this challenge by providing a centralized dashboard for presenting and organizing supported security information and incident records. The dashboard provides a foundation for improved visibility, while advanced integrations and automated security checks remain potential future improvements.

## 3. Project Objectives

The main objective is to develop a web-based dashboard for organizing and monitoring SDLC security information.

The specific objectives are to present security-related information through a centralized dashboard, organize incident records using the available functionality, display summary information and analytics to support monitoring, and establish a foundation for future integration of security information across the five SDLC security pillars.

## 4. Project Scope

The project covers the development of a Django-based web application for displaying security-related information and managing incident records. The scope includes the dashboard interface and the incident-management features confirmed in the implementation.

The five security pillars—Endpoint/IDE, VCS, CI/CD, Registry, and Production—provide the framework guiding the project. However, their representation does not imply that external security tools, automated vulnerability scanning, or continuous security monitoring have been implemented. These capabilities are proposed as possible future enhancements where they are not supported by the current source code.

## 5. System Requirements and Setup

The application uses Python and the Django web framework. The development environment requires a compatible Python installation, Django and the project's required dependencies, the application source files, and the appropriate database configuration. A modern web browser is required to access the interface.

To run the application locally, the developer opens a terminal in the project directory, activates the configured Python environment if one is used, installs the dependencies listed in the project requirements file, and starts the Django development server using the appropriate management command. When the server starts successfully, the application can be accessed at http://127.0.0.1:8000/.

The installed Python and Django versions, dependency list, and database configuration should be verified against the actual development environment before the final report is submitted.

## 6. Testing and Evidence

Testing should establish whether the dashboard loads correctly, whether the incident-recording functionality operates as intended, whether incident records are displayed correctly, and whether the available summary information is presented accurately.

The final report should document each test case, its expected result, the actual result, and its pass or fail status. Screenshots captured from the running application should be included as evidence of the tested features. Any errors or limitations identified during testing should be documented honestly.

Testing of the dashboard does not establish that external security-tool integrations or automated vulnerability scanning are operational. Such capabilities should only be reported as implemented after they have been developed and verified.

## 7. Limitations and Future Improvements

Potential improvements include enhancing the dashboard's responsive layout, expanding incident-management capabilities, and integrating appropriate security tools across the five SDLC security pillars. Additional improvements may include automated security checks and more detailed monitoring and reporting. These features remain future work unless their implementation and successful operation can be demonstrated.

## 8. Conclusion

CodeShield SDLC Security Dashboard provides a foundation for organizing and monitoring security-related information through a centralized web interface. The final assessment of the project should be based on the dashboard features and incident-management functionality verified in the source code and running application. Documenting actual test results, screenshots, and known limitations will help ensure that the report accurately represents the project's current state and identifies realistic opportunities for future development.

## References

Wiz. (n.d.). *Software Development Lifecycle (SDLC) security and infrastructure threat framework resources*. https://www.wiz.io/

Django Software Foundation. (n.d.). *Django documentation*. https://docs.djangoproject.com/
