​Software Architecture and Design Justification


​1. Introduction and Architectural Style


​For the CodeShield SDLC Security Dashboard, we selected a Modular Monolithic Architecture powered by the Django Framework (Python).


​Given the project's scope—tracking security metrics, viewing historical vulnerability trends, and displaying security postures across different SDLC stages—a full microservices architecture would introduce unnecessary infrastructure overhead and deployment complexity. Instead, a modular monolith allows us to logically separate concerns into distinct Django apps (such as authentication, dashboard metrics, and vulnerability logs) within a single, highly maintainable deployment unit. This ensures clean separation of business logic while keeping local setup and CI/CD pipelines straightforward.


​2. Alignment with SDLC Security Pillars


​The architecture is specifically structured to map directly to the five core SDLC security pillars we analyzed in Part One:




​Endpoint/IDE & Version Control System (VCS): The backend models are designed to ingest and store metadata logs coming from early-stage developer tools (e.g., static code analysis summaries and commit hooks).



​CI/CD Pipeline Integration: Django's robust management command structure and built-in test runner (python manage.py test) allow automated pipelines (like Jenkins) to seamlessly execute code validation and unit tests on every build.



​Registry & Production Views: The database schema maintains structured tables for tracking dependency scan reports and container artifact statuses, which the dashboard renders using secure server-side templates.




​3. Key Design Decisions


​3.1 Django MVT (Model-View-Template) Pattern


​CodeShield utilizes Django’s native MVT pattern:





​Models (models.py): Define the relational database schema using Django ORM, securely handling data constraints for security logs, scan results, and user permissions.




​Views (views.py): Handle HTTP request processing, enforce access control restrictions (ensuring only authenticated team members or pipelines interact with endpoints), and feed context data to the templates.



​Templates (HTML/CSS): Render the user interface dashboards cleanly using server-side rendering, avoiding complex client-side single-page application (SPA) vulnerabilities while maintaining a responsive layout.




​3.2 Security-First Design Considerations


​In alignment with our project rules—only describing features that really exist and avoiding false claims of live automated scanning—the architecture is designed around auditing and visualization rather than active execution:




​Read-Only Data Integrity: The dashboard serves as a visualization layer for pre-collected metrics and security reports. This prevents untrusted inputs from executing arbitrary code on the server.


​Built-in Authentication & CSRF Protection: Django’s robust built-in authentication system and Cross-Site Request Forgery (CSRF) tokens protect all dashboard modification endpoints, securing administrative controls.




​4. Conclusion


​The chosen Django modular monolithic architecture successfully balances development velocity, maintainability, and security. By strictly aligning our data models and views with real, existing dashboard capabilities, CodeShield provides a reliable, transparent, and easily testable platform for SDLC security oversight.


