# Web Stack Outage Postmortem

## Issue Summary:

- **Duration:** April 10th, 2024, 9:00 PM - April 11th, 2024, 3:00 AM (UTC)
- **Impact:** The web application experienced intermittent downtime and slow response times, affecting 75% of users. Users reported errors when accessing various features of the application.
- **Root Cause:** A misconfiguration in the load balancer settings led to an uneven distribution of traffic among backend servers, causing some servers to become overwhelmed and unresponsive.

## Timeline:

- **Detection:** April 10th, 2024, 9:15 PM (UTC)
  - An engineer received automated alerts indicating a spike in server response times.
- **Actions Taken:**
  - Investigation focused on backend server health and network connectivity.
  - Assumption: Initially suspected a database issue due to the reported errors.
- **Misleading Paths:**
  - Time was spent analyzing database performance and query logs, which didn't reveal abnormalities.
  - Network bandwidth was also investigated, though no issues were found.
- **Escalation:**
  - Incident was escalated to the DevOps team after initial investigations failed to identify the root cause.
- **Resolution:**
  - Load balancer configuration was reviewed and found to be distributing traffic unevenly.
  - Load balancer settings were adjusted to evenly distribute traffic among backend servers.
  - Normal server operations were restored by restarting affected services.

## Root Cause and Resolution:

- **Root Cause:**
  - Misconfigured load balancer settings led to uneven distribution of traffic among backend servers.
- **Resolution:**
  - Load balancer settings were adjusted to evenly distribute traffic among backend servers.
  - Affected services were restarted to restore normal operations.

## Corrective and Preventative Measures:

- **Improvements:**
  - Regular audits of load balancer configurations to ensure proper traffic distribution.
  - Implement automated checks for load balancer health and configuration consistency.
- **Tasks:**
  - Patch load balancer software to prevent recurrence of misconfiguration.
  - Implement additional monitoring for load balancer performance and traffic distribution.
  - Conduct training sessions for operations team members on load balancer management and troubleshooting.

## Conclusion:

The outage was caused by a misconfigured load balancer, resulting in intermittent downtime and slow response times for users. Prompt detection and collaboration among teams facilitated a quick resolution. Implementing corrective measures and proactive monitoring will help prevent similar incidents in the future, ensuring uninterrupted service for our users.
