# STIG Security Requirements

|Requirement ID|Title|Consideration|
|--------------|-----|-------------|
|V-222400|Validity periods must be verified on all application messages using WS-Security or SAML assertions.|Not applicable, Our implementation does not contain SOAP Capabilities.|
|V-222404|The application must use both the NotBefore and NotOnOrAfter elements or OneTimeUse element when using the Conditions element in a SAML assertion.|Not applicable; our system does not require authentication to use|
|V-222612|The application must not be vulnerable to overflow attacks.|Not applicable, the languages we use are memory safe (python, javascript)|
|V-222578|The application must destroy the session ID value and/or cookie on logoff or browser close.|Not applicable, Our implementation does not use cookies|
|V-222430|The application must execute without excessive account permissions.|Not applicable, all users have the same permissions (no authentication)|
|V-222432|The application must enforce the limit of three consecutive invalid logon attempts by a user during a 15 minute time period.|Not applicable, customers require no authentication|
|V-222577|The application must not expose session IDs.|The system shall not expose session IDs|
|V-222609|The application must not be subject to input handling vulnerabilities.|The system shall validate user input before sending it to the server/database|
|V-222608|The application must not be vulnerable to XML-oriented attacks.|Not applicable; our system does not use XML|
|V-222602|The application must protect from Cross-Site Scripting (XSS) vulnerabilities.|The system shall protect against XSS vulnerabilities by validating all user input.|
|V-222601|The application must not store sensitive information in hidden fields.|The system shall first encrypt data before storing sensitive information in hidden fields|
|V-222607|The application must not be vulnerable to SQL Injection.|Not applicable our system uses a noSQL database (mongodb)|
|V-222604|The application must protect from command injection.|Not applicable; the system is not command line based|
|V-222403|The application must use the NotOnOrAfter condition when using the SubjectConfirmation element in a SAML assertion.|Not applicable; our system does not require authentication to use|
|V-222585|The application must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.|The system shall use a fail safe state in order to save data and shutdown in the event of initialization fail, shutdown fail, or abort fail.|
|V-222550|The application, when utilizing PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.|Not applicable; The system does not use authenticaiton|
|V-222522|The application must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).|Not applicable; all users are at the same level (no authentication)|
|V-222554|The application must not display passwords/PINs as clear text.|Not applicable, our system does not store passwords/pins|
|V-222596|The application must protect the confidentiality and integrity of transmitted information.|The system shall transmit data via the TCP protocol|
|V-222399|Messages protected with WS_Security must use time stamps with creation and expiration times.|Not applicable; our sysem does not contain SOAP capabilities|
|V-222658|All products must be supported by the vendor or the development team.|Not applicable; We can only support the system until the end of the semester (May 2024)|
|V-222659|The application must be decommissioned when maintenance or support is no longer available.|Not applicable; we will not be maintaining the system.|
|V-222551|The application, when using PKI-based authentication, must enforce authorized access to the corresponding private key.|Not applicable; no authentication|
|V-222620|Application web servers must be on a separate network segment from the application and database servers if it is a tiered application operating in the DoD DMZ.|Not applicable, this is out of the scope of our system. Although we are developing a web-based application we cannot enforce how the network is segmented.|
|V-222536|The application must enforce a minimum 15-character password length.|Not applicable, our system does not require authentication to use|
|V-222643|The application must have the capability to mark sensitive/classified output when required.|The system shall provide the capability to mark sensitive/classified output.|
|V-222542|The application must only store cryptographic representations of passwords.|Not applicable, our system does not store passwords|
|V-222543|The application must transmit only cryptographically-protected passwords.|Not applicable, our system does not transmit passwords|
|V-222425|The application must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.|Not applicable, our system does not require authentication to use|
|V-222642|The application must not contain embedded authentication data.|Not applicable, our system does not require authentication to use|
|V-222662|Default passwords must be changed.|Not applicable, our system does not require authentication to use|
|V-222555|The application must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.|Not applicable, our system does not use a cryptographic module|