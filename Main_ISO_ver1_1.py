import json
import os
from datetime import datetime
from enum import Enum


class ControlStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    IMPLEMENTED = "Implemented"
    NOT_APPLICABLE = "Not Applicable"


class ISO27001ImplementationAssistant:
    def __init__(self):
        self.data_file = "iso27001_data.json"
        self.initialize_data()
        self.controls = self.load_all_controls_with_27002_guidance()
        self.phases = self.load_implementation_phases()

    def initialize_data(self):
        if not os.path.exists(self.data_file):
            base_structure = {
                "progress": {},
                "controls_status": {},
                "control_notes": {},
                "last_updated": str(datetime.now())
            }
            with open(self.data_file, 'w') as f:
                json.dump(base_structure, f)

    def load_all_controls_with_27002_guidance(self):
        return {
            # ==================== Organizational Controls (A.5) ====================
            "A.5.1": {
                "title": "Information security policies",
                "description": "To provide management direction and support for information security.",
                "implementation": [
                    "Establish an information security policy approved by management",
                    "Align policy with organizational objectives and context",
                    "Document the policy and make it available to all relevant parties",
                    "Review the policy at planned intervals or when significant changes occur"
                ],
                "27002_guidance": "ISO 27002 recommends the policy should be appropriate to the organization's purpose, communicated to all employees, reviewed annually, and supported by topic-specific policies.",
                "domain": "Organizational"
            },
            "A.5.2": {
                "title": "Information security roles and responsibilities",
                "description": "To ensure security responsibilities are properly assigned.",
                "implementation": [
                    "Define security roles and responsibilities",
                    "Assign responsibility for implementing specific controls",
                    "Document accountability for assets and processes",
                    "Establish authorization processes for specific activities"
                ],
                "27002_guidance": "ISO 27002 suggests clearly defining all security roles, separating conflicting duties, documenting responsibilities in job descriptions, and implementing least privilege.",
                "domain": "Organizational"
            },
            "A.5.3": {
                "title": "Segregation of duties",
                "description": "To prevent conflicts of interest and fraud.",
                "implementation": [
                    "Identify functions requiring separation",
                    "Define incompatible duties",
                    "Implement technical controls to enforce separation",
                    "Monitor for potential conflicts"
                ],
                "27002_guidance": "ISO 27002 recommends separating initiation, authorization, and execution of critical actions, dividing knowledge for sensitive operations, and implementing dual control for critical functions.",
                "domain": "Organizational"
            },
            "A.5.4": {
                "title": "Management responsibilities",
                "description": "To ensure management demonstrates support for information security.",
                "implementation": [
                    "Define management security responsibilities",
                    "Include security in management objectives",
                    "Provide resources for security initiatives",
                    "Monitor management security performance"
                ],
                "27002_guidance": "ISO 27002 suggests management should actively promote security, ensure adequate resources, and integrate security into business processes.",
                "domain": "Organizational"
            },
            "A.5.5": {
                "title": "Contact with authorities",
                "description": "To ensure appropriate interaction with relevant authorities.",
                "implementation": [
                    "Identify relevant regulatory authorities",
                    "Establish communication channels",
                    "Define reporting procedures",
                    "Maintain contact records"
                ],
                "27002_guidance": "ISO 27002 recommends establishing procedures for mandatory reporting to authorities and maintaining relationships with law enforcement.",
                "domain": "Organizational"
            },
            "A.5.6": {
                "title": "Contact with special interest groups",
                "description": "To ensure appropriate information sharing with special interest groups.",
                "implementation": [
                    "Identify relevant special interest groups",
                    "Establish participation guidelines",
                    "Define information sharing protocols",
                    "Monitor group participation"
                ],
                "27002_guidance": "ISO 27002 suggests participating in industry forums while protecting sensitive information and verifying the legitimacy of groups.",
                "domain": "Organizational"
            },
            "A.5.7": {
                "title": "Threat intelligence",
                "description": "To provide awareness of threat levels and vectors.",
                "implementation": [
                    "Identify relevant threat intelligence sources",
                    "Establish collection and analysis processes",
                    "Distribute intelligence to stakeholders",
                    "Integrate intelligence into risk assessments"
                ],
                "27002_guidance": "ISO 27002 recommends collecting intelligence from reliable sources, analyzing relevance to the organization, and using it to inform security decisions.",
                "domain": "Organizational"
            },
            "A.5.8": {
                "title": "Information security in project management",
                "description": "To ensure information security is integrated into project management.",
                "implementation": [
                    "Include security requirements in project charters",
                    "Assign security responsibilities in project teams",
                    "Conduct security reviews at project phases",
                    "Document security outcomes"
                ],
                "27002_guidance": "ISO 27002 suggests applying security management practices throughout the project lifecycle and considering security in all project decisions.",
                "domain": "Organizational"
            },
            "A.5.9": {
                "title": "Inventory of information and other associated assets",
                "description": "To identify and manage information and other associated assets.",
                "implementation": [
                    "Identify all information assets",
                    "Document ownership and classification",
                    "Maintain an up-to-date inventory",
                    "Review inventory regularly"
                ],
                "27002_guidance": "ISO 27002 recommends creating and maintaining a complete inventory of assets, including owners and acceptable use requirements.",
                "domain": "Organizational"
            },
            "A.5.10": {
                "title": "Acceptable use of information and associated assets",
                "description": "To ensure proper use of information and associated assets.",
                "implementation": [
                    "Define acceptable use policies",
                    "Communicate policies to all users",
                    "Implement technical controls to enforce policies",
                    "Monitor compliance"
                ],
                "27002_guidance": "ISO 27002 suggests policies should cover authorized use, prohibited activities, and consequences for policy violations.",
                "domain": "Organizational"
            },
            "A.5.11": {
                "title": "Return of assets",
                "description": "To ensure return of assets upon termination or change of employment.",
                "implementation": [
                    "Maintain records of assigned assets",
                    "Establish return procedures",
                    "Verify returned assets",
                    "Disable access upon return"
                ],
                "27002_guidance": "ISO 27002 recommends having formal procedures for returning all organizational assets when no longer required.",
                "domain": "Organizational"
            },
            "A.5.12": {
                "title": "Classification of information",
                "description": "To ensure information receives an appropriate level of protection.",
                "implementation": [
                    "Define classification scheme",
                    "Assign classification levels",
                    "Document handling requirements",
                    "Train staff on classification"
                ],
                "27002_guidance": "ISO 27002 suggests classification should consider legal requirements, value, sensitivity, and criticality to the organization.",
                "domain": "Organizational"
            },
            "A.5.13": {
                "title": "Labeling of information",
                "description": "To support the implementation of information classification.",
                "implementation": [
                    "Develop labeling standards",
                    "Label information according to classification",
                    "Include labels in metadata",
                    "Ensure labels remain with information"
                ],
                "27002_guidance": "ISO 27002 recommends labeling should be visible and durable, with electronic labeling for digital information.",
                "domain": "Organizational"
            },
            "A.5.14": {
                "title": "Information transfer",
                "description": "To maintain security when transferring information within or outside the organization.",
                "implementation": [
                    "Identify transfer methods and risks",
                    "Define security requirements",
                    "Implement transfer controls",
                    "Monitor transfer activities"
                ],
                "27002_guidance": "ISO 27002 suggests considering confidentiality, integrity, and availability requirements when transferring information.",
                "domain": "Organizational"
            },
            "A.5.15": {
                "title": "Access control",
                "description": "To ensure appropriate access to information and associated assets.",
                "implementation": [
                    "Define access control policy",
                    "Implement user access management",
                    "Enforce least privilege",
                    "Review access rights regularly"
                ],
                "27002_guidance": "ISO 27002 recommends access controls based on business requirements, with regular review and removal of unnecessary access.",
                "domain": "Organizational"
            },
            "A.5.16": {
                "title": "Identity management",
                "description": "To ensure unique identification and authentication of users.",
                "implementation": [
                    "Establish identity verification procedures",
                    "Assign unique identifiers",
                    "Implement authentication mechanisms",
                    "Manage identity lifecycle"
                ],
                "27002_guidance": "ISO 27002 suggests strong identity proofing, unique identifiers, and secure authentication methods.",
                "domain": "Organizational"
            },
            "A.5.17": {
                "title": "Authentication information",
                "description": "To ensure authentication information remains confidential and secure.",
                "implementation": [
                    "Define authentication information requirements",
                    "Implement secure storage",
                    "Enforce secure transmission",
                    "Monitor for compromise"
                ],
                "27002_guidance": "ISO 27002 recommends protecting authentication information from unauthorized disclosure and implementing secure reset procedures.",
                "domain": "Organizational"
            },
            "A.5.18": {
                "title": "Access rights",
                "description": "To ensure appropriate access rights are granted and managed.",
                "implementation": [
                    "Define access rights model",
                    "Implement provisioning processes",
                    "Enforce segregation of duties",
                    "Review access regularly"
                ],
                "27002_guidance": "ISO 27002 suggests granting minimum necessary access, reviewing rights periodically, and revoking promptly when no longer needed.",
                "domain": "Organizational"
            },
            "A.5.19": {
                "title": "Information security in supplier relationships",
                "description": "To maintain an agreed level of information security with suppliers.",
                "implementation": [
                    "Identify supplier security risks",
                    "Define security requirements",
                    "Include requirements in contracts",
                    "Monitor supplier compliance"
                ],
                "27002_guidance": "ISO 27002 recommends addressing security throughout the supplier lifecycle, from selection to termination.",
                "domain": "Organizational"
            },
            "A.5.20": {
                "title": "Addressing information security within supplier agreements",
                "description": "To ensure suppliers meet the organization's information security requirements.",
                "implementation": [
                    "Document security requirements",
                    "Include requirements in agreements",
                    "Define monitoring processes",
                    "Establish remedies for non-compliance"
                ],
                "27002_guidance": "ISO 27002 suggests agreements should cover confidentiality, incident management, and audit rights.",
                "domain": "Organizational"
            },
            "A.5.21": {
                "title": "Managing information security in the ICT supply chain",
                "description": "To maintain security in the ICT products and services supply chain.",
                "implementation": [
                    "Map the ICT supply chain",
                    "Assess supplier security practices",
                    "Implement security requirements",
                    "Monitor for risks"
                ],
                "27002_guidance": "ISO 27002 recommends considering security throughout the procurement lifecycle and verifying supplier security claims.",
                "domain": "Organizational"
            },
            "A.5.22": {
                "title": "Monitoring, review and change management of supplier services",
                "description": "To ensure supplier services continue to meet requirements.",
                "implementation": [
                    "Define monitoring processes",
                    "Conduct regular reviews",
                    "Manage changes to services",
                    "Maintain audit rights"
                ],
                "27002_guidance": "ISO 27002 suggests regular performance reviews, change management procedures, and right-to-audit clauses.",
                "domain": "Organizational"
            },
            "A.5.23": {
                "title": "Information security for use of cloud services",
                "description": "To ensure security when using cloud services.",
                "implementation": [
                    "Assess cloud service risks",
                    "Define security requirements",
                    "Select appropriate service models",
                    "Monitor service performance"
                ],
                "27002_guidance": "ISO 27002 recommends understanding shared responsibility models and ensuring contractual protections for cloud services.",
                "domain": "Organizational"
            },
            "A.5.24": {
                "title": "Information security incident management planning and preparation",
                "description": "To ensure readiness to manage information security incidents.",
                "implementation": [
                    "Establish incident response team",
                    "Develop response plans",
                    "Define communication procedures",
                    "Conduct training and testing"
                ],
                "27002_guidance": "ISO 27002 suggests having documented procedures, trained personnel, and communication plans for incident management.",
                "domain": "Organizational"
            },
            "A.5.25": {
                "title": "Assessment and decision on information security events",
                "description": "To determine if events should be classified as incidents.",
                "implementation": [
                    "Define incident classification criteria",
                    "Establish assessment procedures",
                    "Document decision-making",
                    "Maintain event records"
                ],
                "27002_guidance": "ISO 27002 recommends having clear criteria for assessing events and documenting all decisions.",
                "domain": "Organizational"
            },
            "A.5.26": {
                "title": "Response to information security incidents",
                "description": "To contain, recover from and learn from incidents.",
                "implementation": [
                    "Implement containment measures",
                    "Eradicate incident causes",
                    "Recover affected systems",
                    "Document lessons learned"
                ],
                "27002_guidance": "ISO 27002 suggests following a structured approach to incident response with clear roles and responsibilities.",
                "domain": "Organizational"
            },
            "A.5.27": {
                "title": "Learning from information security incidents",
                "description": "To improve security based on incident experience.",
                "implementation": [
                    "Analyze incident root causes",
                    "Identify corrective actions",
                    "Implement improvements",
                    "Share lessons learned"
                ],
                "27002_guidance": "ISO 27002 recommends conducting post-incident reviews and using findings to strengthen security.",
                "domain": "Organizational"
            },
            "A.5.28": {
                "title": "Collection of evidence",
                "description": "To ensure evidence is collected for investigations.",
                "implementation": [
                    "Define evidence collection procedures",
                    "Train staff on handling evidence",
                    "Maintain chain of custody",
                    "Protect evidence integrity"
                ],
                "27002_guidance": "ISO 27002 suggests following legally admissible procedures for evidence collection and preservation.",
                "domain": "Organizational"
            },
            "A.5.29": {
                "title": "Information security during disruption",
                "description": "To maintain information security during disruptive events.",
                "implementation": [
                    "Identify critical security processes",
                    "Develop continuity plans",
                    "Define fallback arrangements",
                    "Test recovery procedures"
                ],
                "27002_guidance": "ISO 27002 recommends integrating security into business continuity plans and testing them regularly.",
                "domain": "Organizational"
            },
            "A.5.30": {
                "title": "ICT readiness for business continuity",
                "description": "To ensure ICT can support business continuity.",
                "implementation": [
                    "Identify critical ICT systems",
                    "Develop recovery strategies",
                    "Implement redundancy",
                    "Test recovery capabilities"
                ],
                "27002_guidance": "ISO 27002 suggests having alternative processing arrangements and regularly testing ICT continuity arrangements.",
                "domain": "Organizational"
            },
            "A.5.31": {
                "title": "Legal, statutory, regulatory and contractual requirements",
                "description": "To ensure compliance with legal and contractual obligations.",
                "implementation": [
                    "Identify applicable requirements",
                    "Document compliance obligations",
                    "Implement compliance measures",
                    "Monitor for changes"
                ],
                "27002_guidance": "ISO 27002 recommends maintaining an inventory of requirements and assigning compliance responsibilities.",
                "domain": "Organizational"
            },
            "A.5.32": {
                "title": "Intellectual property rights",
                "description": "To protect intellectual property.",
                "implementation": [
                    "Identify intellectual property assets",
                    "Implement protection measures",
                    "Educate staff on IP rights",
                    "Monitor for violations"
                ],
                "27002_guidance": "ISO 27002 suggests implementing procedures to protect IP rights and comply with licensing agreements.",
                "domain": "Organizational"
            },
            "A.5.33": {
                "title": "Protection of records",
                "description": "To ensure records are protected from loss or damage.",
                "implementation": [
                    "Identify critical records",
                    "Define retention periods",
                    "Implement protection measures",
                    "Establish disposal procedures"
                ],
                "27002_guidance": "ISO 27002 recommends protecting records according to their value, legal requirements, and business needs.",
                "domain": "Organizational"
            },
            "A.5.34": {
                "title": "Privacy and protection of PII",
                "description": "To ensure protection of personally identifiable information.",
                "implementation": [
                    "Identify PII processing activities",
                    "Implement privacy controls",
                    "Document compliance with regulations",
                    "Train staff on PII protection"
                ],
                "27002_guidance": "ISO 27002 suggests implementing privacy by design and default, with consideration of applicable privacy laws.",
                "domain": "Organizational"
            },
            "A.5.35": {
                "title": "Independent review of information security",
                "description": "To ensure security controls remain effective.",
                "implementation": [
                    "Define review scope and frequency",
                    "Select qualified reviewers",
                    "Document findings and recommendations",
                    "Implement improvements"
                ],
                "27002_guidance": "ISO 27002 recommends independent reviews should be conducted by personnel not responsible for the area being reviewed.",
                "domain": "Organizational"
            },
            "A.5.36": {
                "title": "Compliance with policies, rules and standards for information security",
                "description": "To ensure compliance with security requirements.",
                "implementation": [
                    "Monitor compliance with policies",
                    "Identify non-compliance issues",
                    "Implement corrective actions",
                    "Report on compliance status"
                ],
                "27002_guidance": "ISO 27002 suggests regular compliance checks and management reporting on compliance status.",
                "domain": "Organizational"
            },
            "A.5.37": {
                "title": "Documented operating procedures",
                "description": "To ensure consistent and secure operations.",
                "implementation": [
                    "Document critical operational procedures",
                    "Make procedures available to staff",
                    "Review and update regularly",
                    "Train staff on procedures"
                ],
                "27002_guidance": "ISO 27002 recommends procedures should be clear, current, and approved, with version control.",
                "domain": "Organizational"
            },

            # ==================== People Controls (A.6) ====================
            "A.6.1": {
                "title": "Screening",
                "description": "To ensure employees and contractors are suitable for roles.",
                "implementation": [
                    "Define screening criteria based on role requirements",
                    "Verify qualifications and references",
                    "Conduct background checks where appropriate",
                    "Document screening results"
                ],
                "27002_guidance": "ISO 27002 suggests screening should be proportional to role risk level, include identity verification, and be specified in third-party contracts.",
                "domain": "People"
            },
            "A.6.2": {
                "title": "Terms and conditions of employment",
                "description": "To ensure personnel understand their security responsibilities.",
                "implementation": [
                    "Include security clauses in contracts",
                    "Define acceptable use of assets",
                    "Specify confidentiality obligations",
                    "Document disciplinary processes"
                ],
                "27002_guidance": "ISO 27002 recommends contracts should clearly state security responsibilities and consequences for violations.",
                "domain": "People"
            },
            "A.6.3": {
                "title": "Information security awareness, education and training",
                "description": "To ensure personnel are aware of security risks and requirements.",
                "implementation": [
                    "Assess training needs",
                    "Develop awareness materials",
                    "Deliver role-specific training",
                    "Evaluate effectiveness"
                ],
                "27002_guidance": "ISO 27002 suggests training should be relevant, engaging, and regularly updated to reflect current threats.",
                "domain": "People"
            },
            "A.6.4": {
                "title": "Disciplinary process",
                "description": "To take action against security policy violations.",
                "implementation": [
                    "Define violation categories",
                    "Establish investigation procedures",
                    "Document disciplinary actions",
                    "Ensure consistent application"
                ],
                "27002_guidance": "ISO 27002 recommends a fair, consistent process that considers severity and intent of violations.",
                "domain": "People"
            },
            "A.6.5": {
                "title": "Responsibilities after termination or change of employment",
                "description": "To protect the organization's interests after employment changes.",
                "implementation": [
                    "Define termination procedures",
                    "Revoke access promptly",
                    "Retrieve organizational assets",
                    "Conduct exit interviews"
                ],
                "27002_guidance": "ISO 27002 suggests having formal procedures for employment termination that address all security aspects.",
                "domain": "People"
            },
            "A.6.6": {
                "title": "Confidentiality or non-disclosure agreements",
                "description": "To protect confidential information.",
                "implementation": [
                    "Identify information requiring protection",
                    "Develop standard agreements",
                    "Ensure proper signing",
                    "Monitor compliance"
                ],
                "27002_guidance": "ISO 27002 recommends NDAs should be appropriate to the information's sensitivity and reviewed periodically.",
                "domain": "People"
            },
            "A.6.7": {
                "title": "Remote working",
                "description": "To ensure security when working remotely.",
                "implementation": [
                    "Define remote work policies",
                    "Implement secure access methods",
                    "Provide secure equipment",
                    "Monitor remote activities"
                ],
                "27002_guidance": "ISO 27002 suggests considering physical security, secure communications, and family member access for remote work.",
                "domain": "People"
            },
            "A.6.8": {
                "title": "Information security event reporting",
                "description": "To ensure security events are reported.",
                "implementation": [
                    "Establish reporting channels",
                    "Define reportable events",
                    "Train staff on reporting",
                    "Protect reporters"
                ],
                "27002_guidance": "ISO 27002 recommends making reporting easy, encouraging reporting, and not penalizing good-faith reports.",
                "domain": "People"
            },

            # ==================== Physical Controls (A.7) ====================
            "A.7.1": {
                "title": "Physical security perimeter",
                "description": "To protect sensitive areas from unauthorized access.",
                "implementation": [
                    "Identify security perimeters for sensitive areas",
                    "Implement appropriate perimeter barriers",
                    "Control physical entry points",
                    "Monitor perimeter security"
                ],
                "27002_guidance": "ISO 27002 recommends defining clear security perimeters with barriers, implementing entry controls, and protecting against environmental threats.",
                "domain": "Physical"
            },
            "A.7.2": {
                "title": "Physical entry",
                "description": "To ensure only authorized access to secure areas.",
                "implementation": [
                    "Implement access control systems",
                    "Issue access credentials",
                    "Monitor entry and exit",
                    "Review access rights regularly"
                ],
                "27002_guidance": "ISO 27002 suggests using authentication methods appropriate to the area's sensitivity and logging physical access.",
                "domain": "Physical"
            },
            "A.7.3": {
                "title": "Securing offices, rooms and facilities",
                "description": "To protect information within physical locations.",
                "implementation": [
                    "Assess area security requirements",
                    "Implement appropriate security measures",
                    "Control visitor access",
                    "Monitor sensitive areas"
                ],
                "27002_guidance": "ISO 27002 recommends considering walls, doors, ceilings, and floors when securing physical spaces.",
                "domain": "Physical"
            },
            "A.7.4": {
                "title": "Physical security monitoring",
                "description": "To detect unauthorized physical access.",
                "implementation": [
                    "Install monitoring equipment",
                    "Define monitoring procedures",
                    "Review monitoring records",
                    "Respond to alerts"
                ],
                "27002_guidance": "ISO 27002 suggests monitoring should be continuous, with protection of monitoring equipment and records.",
                "domain": "Physical"
            },
            "A.7.5": {
                "title": "Protection against physical and environmental threats",
                "description": "To prevent loss or damage from physical or environmental events.",
                "implementation": [
                    "Identify potential threats",
                    "Implement protective measures",
                    "Monitor environmental conditions",
                    "Test protection systems"
                ],
                "27002_guidance": "ISO 27002 recommends protection against fire, flood, earthquake, explosion, and other environmental threats.",
                "domain": "Physical"
            },
            "A.7.6": {
                "title": "Working in secure areas",
                "description": "To prevent unauthorized access and leakage of information.",
                "implementation": [
                    "Define secure area rules",
                    "Control activities in secure areas",
                    "Restrict personal devices",
                    "Monitor secure areas"
                ],
                "27002_guidance": "ISO 27002 suggests limiting activities in secure areas and controlling information entering/leaving these areas.",
                "domain": "Physical"
            },
            "A.7.7": {
                "title": "Clear desk and clear screen",
                "description": "To reduce risks of unauthorized access and loss.",
                "implementation": [
                    "Establish clear desk policy",
                    "Implement clear screen requirements",
                    "Provide secure storage",
                    "Monitor compliance"
                ],
                "27002_guidance": "ISO 27002 recommends policies for locking workstations and securing sensitive information when unattended.",
                "domain": "Physical"
            },
            "A.7.8": {
                "title": "Equipment siting and protection",
                "description": "To protect equipment from threats and hazards.",
                "implementation": [
                    "Assess equipment placement risks",
                    "Implement protective measures",
                    "Control environmental conditions",
                    "Maintain equipment security"
                ],
                "27002_guidance": "ISO 27002 suggests considering power, temperature, humidity, and physical security for equipment placement.",
                "domain": "Physical"
            },
            "A.7.9": {
                "title": "Security of assets off-premises",
                "description": "To protect assets used outside organization premises.",
                "implementation": [
                    "Inventory off-premises assets",
                    "Implement security measures",
                    "Track asset locations",
                    "Define acceptable use"
                ],
                "27002_guidance": "ISO 27002 recommends additional security for assets used outside premises, including insurance requirements.",
                "domain": "Physical"
            },
            "A.7.10": {
                "title": "Storage media",
                "description": "To prevent unauthorized access to stored information.",
                "implementation": [
                    "Inventory storage media",
                    "Classify media by sensitivity",
                    "Implement access controls",
                    "Define disposal procedures"
                ],
                "27002_guidance": "ISO 27002 suggests secure storage, transportation, and disposal of media based on classification.",
                "domain": "Physical"
            },
            "A.7.11": {
                "title": "Supporting utilities",
                "description": "To ensure continuous availability of supporting utilities.",
                "implementation": [
                    "Identify critical utilities",
                    "Implement redundancy",
                    "Monitor utility quality",
                    "Establish backup arrangements"
                ],
                "27002_guidance": "ISO 27002 recommends uninterruptible power supplies, alternative water sources, and other utility backups.",
                "domain": "Physical"
            },
            "A.7.12": {
                "title": "Cabling security",
                "description": "To prevent interception or damage to cabling.",
                "implementation": [
                    "Protect network cabling",
                    "Implement cable management",
                    "Monitor for tampering",
                    "Label cables clearly"
                ],
                "27002_guidance": "ISO 27002 suggests physical protection for cables and separation from electromagnetic interference sources.",
                "domain": "Physical"
            },
            "A.7.13": {
                "title": "Equipment maintenance",
                "description": "To ensure equipment remains in working order.",
                "implementation": [
                    "Establish maintenance schedules",
                    "Use authorized maintenance personnel",
                    "Control maintenance access",
                    "Document maintenance activities"
                ],
                "27002_guidance": "ISO 27002 recommends following manufacturer instructions and ensuring security during maintenance activities.",
                "domain": "Physical"
            },
            "A.7.14": {
                "title": "Secure disposal or re-use of equipment",
                "description": "To prevent leakage of information from disposed equipment.",
                "implementation": [
                    "Define disposal procedures",
                    "Implement secure erasure",
                    "Verify disposal effectiveness",
                    "Document disposal"
                ],
                "27002_guidance": "ISO 27002 suggests verifying that all sensitive information is removed before disposal or reuse.",
                "domain": "Physical"
            },

            # ==================== Technological Controls (A.8) ====================
            "A.8.1": {
                "title": "User endpoint devices",
                "description": "To secure devices used to access organizational information.",
                "implementation": [
                    "Inventory all endpoint devices",
                    "Implement device security policies",
                    "Enforce secure configuration standards",
                    "Monitor device compliance"
                ],
                "27002_guidance": "ISO 27002 suggests implementing device authentication, enforcing encryption, restricting unauthorized software, and providing secure disposal procedures.",
                "domain": "Technological"
            },
            "A.8.2": {
                "title": "Privileged access rights",
                "description": "To restrict and control privileged access rights.",
                "implementation": [
                    "Identify privileged accounts and roles",
                    "Implement just-in-time privileged access",
                    "Monitor privileged account usage",
                    "Review privileges regularly"
                ],
                "27002_guidance": "ISO 27002 recommends implementing strict controls for privileged access, including multi-factor authentication and regular review of privileges.",
                "domain": "Technological"
            },
            "A.8.3": {
                "title": "Information access restriction",
                "description": "To restrict access to information according to policy.",
                "implementation": [
                    "Implement access control lists",
                    "Enforce need-to-know principle",
                    "Monitor access patterns",
                    "Review access rights regularly"
                ],
                "27002_guidance": "ISO 27002 suggests access controls based on user roles, with regular review and removal of unnecessary access.",
                "domain": "Technological"
            },
            "A.8.4": {
                "title": "Access to source code",
                "description": "To restrict access to source code.",
                "implementation": [
                    "Inventory source code repositories",
                    "Implement access controls",
                    "Monitor code changes",
                    "Review access regularly"
                ],
                "27002_guidance": "ISO 27002 recommends strict control over source code access with logging of all changes.",
                "domain": "Technological"
            },
            "A.8.5": {
                "title": "Secure authentication",
                "description": "To ensure secure authentication methods are used.",
                "implementation": [
                    "Implement multi-factor authentication",
                    "Enforce strong password policies",
                    "Protect authentication credentials",
                    "Monitor authentication attempts"
                ],
                "27002_guidance": "ISO 27002 suggests using strong authentication methods appropriate to the sensitivity of the accessed information.",
                "domain": "Technological"
            },
            "A.8.6": {
                "title": "Capacity management",
                "description": "To ensure adequate capacity for systems.",
                "implementation": [
                    "Monitor system resource usage",
                    "Forecast capacity needs",
                    "Implement scaling solutions",
                    "Test capacity limits"
                ],
                "27002_guidance": "ISO 27002 recommends proactive capacity planning with monitoring and adjustment of resources.",
                "domain": "Technological"
            },
            "A.8.7": {
                "title": "Protection against malware",
                "description": "To protect systems against malicious code.",
                "implementation": [
                    "Implement anti-malware solutions",
                    "Keep signatures updated",
                    "Scan incoming files",
                    "Educate users about malware"
                ],
                "27002_guidance": "ISO 27002 suggests layered defenses including prevention, detection, and recovery controls against malware.",
                "domain": "Technological"
            },
            "A.8.8": {
                "title": "Management of technical vulnerabilities",
                "description": "To prevent exploitation of technical vulnerabilities.",
                "implementation": [
                    "Identify vulnerability sources",
                    "Assess vulnerability severity",
                    "Apply patches promptly",
                    "Verify patch effectiveness"
                ],
                "27002_guidance": "ISO 27002 recommends regular vulnerability scanning, risk-based patching, and verification of fixes.",
                "domain": "Technological"
            },
            "A.8.9": {
                "title": "Configuration management",
                "description": "To ensure secure system configurations.",
                "implementation": [
                    "Define baseline configurations",
                    "Implement change control",
                    "Monitor configuration compliance",
                    "Document all changes"
                ],
                "27002_guidance": "ISO 27002 suggests maintaining secure configurations throughout the system lifecycle with version control.",
                "domain": "Technological"
            },
            "A.8.10": {
                "title": "Information deletion",
                "description": "To prevent unnecessary retention of information.",
                "implementation": [
                    "Define retention periods",
                    "Implement secure deletion",
                    "Verify deletion effectiveness",
                    "Document deletion activities"
                ],
                "27002_guidance": "ISO 27002 recommends secure deletion methods that prevent reconstruction of deleted information.",
                "domain": "Technological"
            },
            "A.8.11": {
                "title": "Data masking",
                "description": "To protect sensitive data.",
                "implementation": [
                    "Identify sensitive data elements",
                    "Implement masking techniques",
                    "Control access to unmasked data",
                    "Monitor masking effectiveness"
                ],
                "27002_guidance": "ISO 27002 suggests using appropriate masking techniques based on data sensitivity and usage requirements.",
                "domain": "Technological"
            },
            "A.8.12": {
                "title": "Data leakage prevention",
                "description": "To prevent unauthorized data disclosure.",
                "implementation": [
                    "Identify sensitive data",
                    "Monitor data flows",
                    "Implement prevention controls",
                    "Respond to leakage attempts"
                ],
                "27002_guidance": "ISO 27002 recommends combining technical controls with policies and training for effective data leakage prevention.",
                "domain": "Technological"
            },
            "A.8.13": {
                "title": "Information backup",
                "description": "To protect against data loss.",
                "implementation": [
                    "Define backup policies",
                    "Implement backup procedures",
                    "Test backup restoration",
                    "Protect backup media"
                ],
                "27002_guidance": "ISO 27002 suggests regular, tested backups stored securely with appropriate retention periods.",
                "domain": "Technological"
            },
            "A.8.14": {
                "title": "Redundancy of information processing facilities",
                "description": "To ensure availability of information processing.",
                "implementation": [
                    "Identify critical systems",
                    "Implement redundant components",
                    "Test failover capabilities",
                    "Monitor system availability"
                ],
                "27002_guidance": "ISO 27002 recommends redundancy appropriate to business needs with regular testing of failover mechanisms.",
                "domain": "Technological"
            },
            "A.8.15": {
                "title": "Logging",
                "description": "To record events for monitoring and investigation.",
                "implementation": [
                    "Define logging requirements",
                    "Implement centralized logging",
                    "Protect log integrity",
                    "Retain logs appropriately"
                ],
                "27002_guidance": "ISO 27002 suggests logging security-relevant events with protection against tampering.",
                "domain": "Technological"
            },
            "A.8.16": {
                "title": "Monitoring activities",
                "description": "To detect unusual or unauthorized activities.",
                "implementation": [
                    "Define monitoring scope",
                    "Implement monitoring tools",
                    "Analyze monitoring data",
                    "Respond to anomalies"
                ],
                "27002_guidance": "ISO 27002 recommends continuous monitoring with alerting for suspicious activities.",
                "domain": "Technological"
            },
            "A.8.17": {
                "title": "Clock synchronization",
                "description": "To ensure accurate time stamps.",
                "implementation": [
                    "Identify time sources",
                    "Implement synchronization",
                    "Monitor clock drift",
                    "Protect time servers"
                ],
                "27002_guidance": "ISO 27002 suggests synchronizing all systems to a trusted time source with appropriate accuracy.",
                "domain": "Technological"
            },
            "A.8.18": {
                "title": "Installation of software on operational systems",
                "description": "To prevent unauthorized software installation.",
                "implementation": [
                    "Define approved software",
                    "Implement installation controls",
                    "Monitor for unauthorized software",
                    "Enforce removal of prohibited software"
                ],
                "27002_guidance": "ISO 27002 recommends formal approval processes for software installation with technical controls.",
                "domain": "Technological"
            },
            "A.8.19": {
                "title": "Networks security",
                "description": "To protect network services.",
                "implementation": [
                    "Segment networks appropriately",
                    "Implement network access controls",
                    "Monitor network traffic",
                    "Protect network infrastructure"
                ],
                "27002_guidance": "ISO 27002 suggests layered network defenses including firewalls, intrusion detection, and traffic filtering.",
                "domain": "Technological"
            },
            "A.8.20": {
                "title": "Security of network services",
                "description": "To ensure security of network services.",
                "implementation": [
                    "Inventory network services",
                    "Secure service configurations",
                    "Monitor service activity",
                    "Update service software"
                ],
                "27002_guidance": "ISO 27002 recommends securing all network services with appropriate authentication and encryption.",
                "domain": "Technological"
            },
            "A.8.21": {
                "title": "Segregation in networks",
                "description": "To limit network access.",
                "implementation": [
                    "Define network zones",
                    "Implement segmentation controls",
                    "Monitor zone crossings",
                    "Review segmentation regularly"
                ],
                "27002_guidance": "ISO 27002 suggests network segmentation based on trust levels with controlled gateways between segments.",
                "domain": "Technological"
            },
            "A.8.22": {
                "title": "Web filtering",
                "description": "To restrict access to harmful web content.",
                "implementation": [
                    "Define filtering policies",
                    "Implement filtering solutions",
                    "Update filtering rules",
                    "Monitor filtering effectiveness"
                ],
                "27002_guidance": "ISO 27002 recommends filtering malicious websites while considering business needs and user privacy.",
                "domain": "Technological"
            },
            "A.8.23": {
                "title": "Use of cryptography",
                "description": "To protect information confidentiality and integrity.",
                "implementation": [
                    "Define cryptographic requirements",
                    "Implement encryption solutions",
                    "Manage cryptographic keys",
                    "Monitor cryptographic controls"
                ],
                "27002_guidance": "ISO 27002 suggests using approved cryptographic algorithms with proper key management.",
                "domain": "Technological"
            },
            "A.8.24": {
                "title": "Secure development lifecycle",
                "description": "To ensure security in development processes.",
                "implementation": [
                    "Integrate security into SDLC",
                    "Train developers in secure coding",
                    "Implement security checkpoints",
                    "Review security throughout development"
                ],
                "27002_guidance": "ISO 27002 recommends security requirements, threat modeling, and security testing throughout development.",
                "domain": "Technological"
            },
            "A.8.25": {
                "title": "Application security requirements",
                "description": "To ensure security is considered in applications.",
                "implementation": [
                    "Define security requirements",
                    "Document security architecture",
                    "Validate requirements implementation",
                    "Maintain requirements traceability"
                ],
                "27002_guidance": "ISO 27002 suggests security requirements covering confidentiality, integrity, availability, and accountability.",
                "domain": "Technological"
            },
            "A.8.26": {
                "title": "Secure system architecture and engineering principles",
                "description": "To ensure security is built into systems.",
                "implementation": [
                    "Define security principles",
                    "Implement secure design patterns",
                    "Apply defense in depth",
                    "Document security architecture"
                ],
                "27002_guidance": "ISO 27002 recommends principles like least privilege, fail securely, and separation of duties in system design.",
                "domain": "Technological"
            },
            "A.8.27": {
                "title": "Secure coding",
                "description": "To prevent security vulnerabilities in code.",
                "implementation": [
                    "Establish coding standards",
                    "Implement code reviews",
                    "Use static analysis tools",
                    "Train developers regularly"
                ],
                "27002_guidance": "ISO 27002 suggests addressing common vulnerabilities (OWASP Top 10) in coding standards.",
                "domain": "Technological"
            },
            "A.8.28": {
                "title": "Security testing in development",
                "description": "To identify security weaknesses during development.",
                "implementation": [
                    "Define testing requirements",
                    "Implement static and dynamic analysis",
                    "Conduct penetration testing",
                    "Remediate identified vulnerabilities"
                ],
                "27002_guidance": "ISO 27002 recommends testing throughout development with increasing rigor as the system matures.",
                "domain": "Technological"
            },
            "A.8.29": {
                "title": "Outsourced development",
                "description": "To ensure security in outsourced development.",
                "implementation": [
                    "Define security requirements",
                    "Assess vendor security capabilities",
                    "Monitor development activities",
                    "Verify delivered code"
                ],
                "27002_guidance": "ISO 27002 suggests including security requirements in contracts and verifying their implementation.",
                "domain": "Technological"
            },
            "A.8.30": {
                "title": "Separation of development, test and production environments",
                "description": "To prevent unauthorized access or changes.",
                "implementation": [
                    "Maintain separate environments",
                    "Control data between environments",
                    "Restrict access appropriately",
                    "Monitor environment interactions"
                ],
                "27002_guidance": "ISO 27002 recommends physical or logical separation with controlled promotion of changes between environments.",
                "domain": "Technological"
            },
            "A.8.31": {
                "title": "Change management",
                "description": "To control changes to systems.",
                "implementation": [
                    "Document change procedures",
                    "Assess change impact",
                    "Authorize changes formally",
                    "Verify changes after implementation"
                ],
                "27002_guidance": "ISO 27002 suggests formal processes for reviewing, approving, testing, and documenting all changes.",
                "domain": "Technological"
            },
            "A.8.32": {
                "title": "Test information",
                "description": "To protect test information.",
                "implementation": [
                    "Identify sensitive test data",
                    "Implement data masking/anonymization",
                    "Control access to test data",
                    "Secure test environments"
                ],
                "27002_guidance": "ISO 27002 recommends using sanitized or synthetic data for testing when possible.",
                "domain": "Technological"
            },
            "A.8.33": {
                "title": "Acceptance testing",
                "description": "To ensure security requirements are met.",
                "implementation": [
                    "Define acceptance criteria",
                    "Conduct security testing",
                    "Verify requirement fulfillment",
                    "Document test results"
                ],
                "27002_guidance": "ISO 27002 suggests independent security testing before system acceptance.",
                "domain": "Technological"
            },
            "A.8.34": {
                "title": "Protection of information systems during audit testing",
                "description": "To ensure that audit testing does not compromise the security of information systems.",
                "implementation": [
                    "Define audit testing procedures",
                    "Isolate test environments",
                    "Monitor audit activities",
                    "Review audit logs"
                ],
                "27002_guidance": "ISO 27002 recommends conducting audits in isolated environments when possible and restricting audit tools to authorized personnel.",
                "domain": "Technological"
            }
        }

    def load_implementation_phases(self):
        return [
            {
                "phase": 1,
                "name": "Preparation & Scoping",
                "tasks": [
                    "Define ISMS scope",
                    "Obtain management commitment",
                    "Develop initial policies"
                    """
                ISO/IEC 27002:2022 - Detailed Implementation Guide

                A.5 - Organizational Controls (37 Controls)
                Focus: Governance, policies, roles, and risk management.

                Key Activities:
                1. Establish information security policies (A.5.1)
                - Develop comprehensive policies covering all security domains
                - Obtain formal management approval
                - Communicate to all stakeholders
                
                2. Define security roles (A.5.2)
                - Assign clear information security responsibilities
                - Document accountability for all assets
                
                3. Conduct initial risk assessment
                - Identify organizational assets
                - Assess threats and vulnerabilities
                - Determine risk treatment plan
                """
                ],
            },
            {
                "phase": 2,
                "name": "Risk Assessment",
                "tasks": [
                    "Asset identification",
                    "Risk analysis",
                    "Risk treatment plan"
                    """
                Risk Management Implementation Guidance:

                1. Asset Identification (A.5.9)
                - Create inventory of all information assets
                - Classify assets by sensitivity (Public, Internal, Confidential, Restricted)
                - Assign ownership for each asset

                2. Threat Assessment (A.5.7)
                - Subscribe to threat intelligence feeds (CISA, commercial providers)
                - Analyze threats specific to your industry
                - Maintain threat library with likelihood/impact ratings

                3. Risk Treatment (A.5.3)
                - Select controls based on risk assessment
                - Document risk acceptance for residual risks
                - Implement segregation of duties for critical processes
                """
                ],
            },
            {
                "phase": 3,
                "name": "Control Implementation",
                "tasks": [
                    "Organizational controls (A.5)",
                    "People controls (A.6)",
                    "Physical controls (A.7)",
                    "Technological controls (A.8)"
                    """
                Control Implementation Best Practices:

                A.5 Organizational Controls:
                - A.5.23 Cloud Security: Implement CASB solutions, review CSP SLAs
                - A.5.24 Incident Management: Establish CSIRT team, test playbooks

                A.6 People Controls:
                - A.6.1 Screening: Background checks for all privileged roles
                - A.6.3 Training: Annual security awareness program

                A.7 Physical Controls:
                - A.7.1 Physical Security: Badge access systems, CCTV monitoring
                - A.7.4 Clear Desk: Automatic screen locking, clean desk audits

                A.8 Technological Controls:
                - A.8.1 Endpoints: Enforce encryption, EDR solutions
                - A.8.12 DLP: Monitor data flows, block unauthorized transfers
                """
                ],
            },
            {
                "phase": 4,
                "name": "Certification Preparation",
                "tasks": [
                    "Internal audit",
                    "Management review",
                    "Stage 1 audit",
                    "Stage 2 audit"
                    """
                Certification Roadmap:

                1. Internal Audit (2-3 months before certification)
                - Conduct gap analysis against all 93 controls
                - Verify implementation evidence exists
                - Remediate any major non-conformities

                2. Management Review (1 month before)
                - Review ISMS performance metrics
                - Approve any required changes
                - Confirm readiness for certification

                3. Stage 1 Audit (Documentation Review)
                - Verify all required policies/procedures exist
                - Confirm risk assessment methodology
                - Address any documentation gaps

                4. Stage 2 Audit (Implementation Verification)
                - Demonstrate control effectiveness
                - Provide records of monitoring activities
                - Show continuous improvement processes
                """
                ],
            }
        ]

    def show_main_menu(self):
        while True:
            print("\n=== ISO 27001:2022 Implementation Assistant ===")
            print("1. View All Controls")
            print("2. View Controls by Domain")
            print("3. Update Control Status")
            print("4. View Implementation Roadmap")
            print("5. Generate Compliance Report")
            print("6. View Control Details")
            print("7. Exit")

            choice = input("\nSelect option (1-7): ")

            if choice == '1':
                self.view_all_controls()
            elif choice == '2':
                self.view_controls_by_domain()
            elif choice == '3':
                self.update_control_status()
            elif choice == '4':
                self.view_implementation_roadmap()
            elif choice == '5':
                self.generate_compliance_report()
            elif choice == '6':
                self.view_control_details()
            elif choice == '7':
                print("\nExiting... Your progress has been saved.")
                break
            else:
                print("Invalid option, please try again.")

    def view_all_controls(self):
        print("\n=== All ISO 27001:2022 93 Controls ===")
        for control_id, details in self.controls.items():
            status = self.get_control_status(control_id)
            print(f"\n{control_id}: {details['title']}")
            print(f"Status: {status.value}")
            print(f"Domain: {details['domain']}")
            print("-" * 60)

    def view_control_details(self):
        print("\n=== Control Details ===")
        control_id = input("Enter control ID (e.g., A.5.1): ").upper()

        if control_id not in self.controls:
            print("Invalid control ID. Please try again.")
            return

        details = self.controls[control_id]
        status = self.get_control_status(control_id)

        print(f"\n=== {control_id}: {details['title']} ===")
        print(f"\nStatus: {status.value}")
        print(f"\nDescription: {details['description']}")

        print("\nImplementation Steps:")
        for i, step in enumerate(details['implementation'], 1):
            print(f"{i}. {step}")

        print("\nISO 27002 Guidance:")
        print(details['27002_guidance'])

        note = self.get_control_note(control_id)
        if note:
            print(f"\nYour Notes: {note}")

        input("\nPress Enter to continue...")

    def view_controls_by_domain(self):
        print("\n=== View Controls by Domain ===")
        print("1. Organizational (A.5) – 37 controls")
        print("2. People (A.6) – 8 controls")
        print("3. Physical (A.7) – 14 controls")
        print("4. Technological (A.8) – 34 controls")
        print("5. Back to Main Menu")

        choice = input("\nSelect domain (1-5): ")

        domains = {
            '1': 'Organizational',
            '2': 'People',
            '3': 'Physical',
            '4': 'Technological'
        }

        if choice == '5':
            return
        elif choice in domains:
            domain = domains[choice]
            print(f"\n=== {domain} Controls ===")
            for control_id, details in self.controls.items():
                if details['domain'] == domain:
                    status = self.get_control_status(control_id)
                    print(f"\n{control_id}: {details['title']}")
                    print(f"Status: {status.value}")
                    print("-" * 50)
        else:
            print("Invalid option, please try again.")

    def update_control_status(self):
        print("\n=== Update Control Status ===")
        control_id = input("Enter control ID (e.g., A.5.1): ").upper()

        if control_id not in self.controls:
            print("Invalid control ID. Please try again.")
            return

        print(
            f"\nCurrent status for {control_id}: {self.get_control_status(control_id).value}")
        print("\nAvailable statuses:")
        for i, status in enumerate(ControlStatus, 1):
            print(f"{i}. {status.value}")

        try:
            choice = int(input("\nSelect new status (1-4): "))
            new_status = list(ControlStatus)[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection. No changes made.")
            return

        with open(self.data_file, 'r+') as f:
            data = json.load(f)
            data['controls_status'][control_id] = new_status.name
            data['last_updated'] = str(datetime.now())
            f.seek(0)
            json.dump(data, f)
            f.truncate()

        print(f"\nStatus for {control_id} updated to: {new_status.value}")

        add_note = input("Would you like to add a note? (y/n): ").lower()
        if add_note == 'y':
            note = input("Enter your note: ")
            with open(self.data_file, 'r+') as f:
                data = json.load(f)
                data['control_notes'][control_id] = note
                data['last_updated'] = str(datetime.now())
                f.seek(0)
                json.dump(data, f)
                f.truncate()
            print("Note added successfully.")

    def view_implementation_roadmap(self):
        print("\n=== ISO 27001 Implementation Roadmap ===")
        for phase in self.phases:
            print(f"\nPhase {phase['phase']}: {phase['name']}")
            print("Tasks:")
            for task in phase['tasks']:
                print(f" - {task}")
        print("\n")

    def generate_compliance_report(self):
        print("\n=== Compliance Report ===")
        total_controls = len(self.controls)
        status_counts = {status: 0 for status in ControlStatus}

        with open(self.data_file, 'r') as f:
            data = json.load(f)

        for control_id in self.controls:
            status = ControlStatus[data['controls_status'].get(
                control_id, "NOT_STARTED")]
            status_counts[status] += 1

        print(f"\nTotal Controls: {total_controls}")
        for status, count in status_counts.items():
            percentage = (count / total_controls) * 100
            print(f"{status.value}: {count} ({percentage:.1f}%)")

        print("\nControls Needing Attention:")
        for control_id, status in data['controls_status'].items():
            if status in ["NOT_STARTED", "IN_PROGRESS"]:
                print(
                    f" - {control_id}: {self.controls[control_id]['title']} ({status})")

        print("\nLast Updated:", data.get('last_updated', 'Never'))

    def get_control_status(self, control_id):
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        status = data['controls_status'].get(control_id, "NOT_STARTED")
        return ControlStatus[status]

    def get_control_note(self, control_id):
        with open(self.data_file, 'r') as f:
            data = json.load(f)
        return data.get('control_notes', {}).get(control_id, "")


if __name__ == "__main__":
    print("=== ISO 27001:2022 Implementation Assistant ===")
    assistant = ISO27001ImplementationAssistant()
    assistant.show_main_menu()
