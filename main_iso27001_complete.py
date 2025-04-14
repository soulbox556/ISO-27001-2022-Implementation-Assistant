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
        self.controls = self.load_all_controls()
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

    def load_all_controls(self):
        return {
            # Organizational Controls (A.5)
            "A.5.1": {
                "title": "Information security policies",
                "description": "To provide management direction and support for information security in accordance with business requirements and relevant laws and regulations.",
                "recommendation": "Develop and implement an information security policy.",
                "domain": "Organizational"
            },
            "A.5.2": {
                "title": "Information security roles and responsibilities",
                "description": "To ensure that information security responsibilities are defined and allocated.",
                "recommendation": "Define and allocate information security responsibilities.",
                "domain": "Organizational"
            },
            "A.5.3": {
                "title": "Segregation of duties",
                "description": "To reduce opportunities for unauthorized or unintentional modification or misuse of the organization's assets.",
                "recommendation": "Implement appropriate segregation of duties.",
                "domain": "Organizational"
            },
            "A.5.4": {
                "title": "Management responsibilities",
                "description": "To ensure that management demonstrates support for information security.",
                "recommendation": "Assign and support management responsibilities for information security.",
                "domain": "Organizational"
            },
            "A.5.5": {
                "title": "Contact with authorities",
                "description": "To ensure appropriate and timely interaction with relevant authorities.",
                "recommendation": "Establish and maintain contact with relevant authorities.",
                "domain": "Organizational"
            },
            "A.5.6": {
                "title": "Contact with special interest groups",
                "description": "To ensure appropriate and timely information sharing with special interest groups.",
                "recommendation": "Maintain contact with relevant special interest groups.",
                "domain": "Organizational"
            },
            "A.5.7": {
                "title": "Threat intelligence",
                "description": "To provide awareness of threat levels and vectors.",
                "recommendation": "Collect and use threat intelligence to inform decisions.",
                "domain": "Organizational"
            },
            "A.5.8": {
                "title": "Information security in project management",
                "description": "To ensure information security is integrated into project management.",
                "recommendation": "Include information security considerations in project management.",
                "domain": "Organizational"
            },
            "A.5.9": {
                "title": "Inventory of information and other associated assets",
                "description": "To identify and manage information and other associated assets.",
                "recommendation": "Maintain an up-to-date inventory of assets.",
                "domain": "Organizational"
            },
            "A.5.10": {
                "title": "Acceptable use of information and associated assets",
                "description": "To ensure proper use of information and associated assets.",
                "recommendation": "Define and communicate acceptable use policies.",
                "domain": "Organizational"
            },
            "A.5.11": {
                "title": "Return of assets",
                "description": "To ensure return of assets upon termination or change of employment.",
                "recommendation": "Implement processes to recover assets when no longer needed.",
                "domain": "Organizational"
            },
            "A.5.12": {
                "title": "Classification of information",
                "description": "To ensure information receives an appropriate level of protection.",
                "recommendation": "Implement an information classification scheme.",
                "domain": "Organizational"
            },
            "A.5.13": {
                "title": "Labeling of information",
                "description": "To support the implementation of information classification.",
                "recommendation": "Label information according to classification scheme.",
                "domain": "Organizational"
            },
            "A.5.14": {
                "title": "Information transfer",
                "description": "To maintain security when transferring information within or outside the organization.",
                "recommendation": "Establish secure information transfer procedures.",
                "domain": "Organizational"
            },
            "A.5.15": {
                "title": "Access control",
                "description": "To ensure appropriate access to information and associated assets.",
                "recommendation": "Implement access control policies and procedures.",
                "domain": "Organizational"
            },
            "A.5.16": {
                "title": "Identity management",
                "description": "To ensure unique identification and authentication of users.",
                "recommendation": "Implement identity management processes.",
                "domain": "Organizational"
            },
            "A.5.17": {
                "title": "Authentication information",
                "description": "To ensure authentication information remains confidential and secure.",
                "recommendation": "Protect authentication information.",
                "domain": "Organizational"
            },
            "A.5.18": {
                "title": "Access rights",
                "description": "To ensure appropriate access rights are granted and managed.",
                "recommendation": "Implement access rights management processes.",
                "domain": "Organizational"
            },
            "A.5.19": {
                "title": "Information security in supplier relationships",
                "description": "To maintain an agreed level of information security with suppliers.",
                "recommendation": "Include security requirements in supplier agreements.",
                "domain": "Organizational"
            },
            "A.5.20": {
                "title": "Addressing information security within supplier agreements",
                "description": "To ensure suppliers meet the organization's information security requirements.",
                "recommendation": "Define security requirements in supplier contracts.",
                "domain": "Organizational"
            },
            "A.5.21": {
                "title": "Managing information security in the ICT supply chain",
                "description": "To maintain security in the ICT products and services supply chain.",
                "recommendation": "Assess and manage ICT supply chain risks.",
                "domain": "Organizational"
            },
            "A.5.22": {
                "title": "Monitoring, review and change management of supplier services",
                "description": "To ensure supplier services continue to meet requirements.",
                "recommendation": "Monitor and review supplier services regularly.",
                "domain": "Organizational"
            },
            "A.5.23": {
                "title": "Information security for use of cloud services",
                "description": "To ensure security when using cloud services.",
                "recommendation": "Implement specific controls for cloud service usage.",
                "domain": "Organizational"
            },
            "A.5.24": {
                "title": "Information security incident management planning and preparation",
                "description": "To ensure readiness to manage information security incidents.",
                "recommendation": "Develop and maintain incident response plans.",
                "domain": "Organizational"
            },
            "A.5.25": {
                "title": "Assessment and decision on information security events",
                "description": "To determine if events should be classified as incidents.",
                "recommendation": "Establish incident assessment criteria.",
                "domain": "Organizational"
            },
            "A.5.26": {
                "title": "Response to information security incidents",
                "description": "To contain, recover from and learn from incidents.",
                "recommendation": "Implement incident response procedures.",
                "domain": "Organizational"
            },
            "A.5.27": {
                "title": "Learning from information security incidents",
                "description": "To improve security based on incident experience.",
                "recommendation": "Analyze incidents and implement improvements.",
                "domain": "Organizational"
            },
            "A.5.28": {
                "title": "Collection of evidence",
                "description": "To ensure evidence is collected for investigations.",
                "recommendation": "Establish procedures for evidence collection.",
                "domain": "Organizational"
            },
            "A.5.29": {
                "title": "Information security during disruption",
                "description": "To maintain information security during disruptive events.",
                "recommendation": "Include security in business continuity plans.",
                "domain": "Organizational"
            },
            "A.5.30": {
                "title": "ICT readiness for business continuity",
                "description": "To ensure ICT can support business continuity.",
                "recommendation": "Implement ICT continuity measures.",
                "domain": "Organizational"
            },
            "A.5.31": {
                "title": "Legal, statutory, regulatory and contractual requirements",
                "description": "To ensure compliance with legal and contractual obligations.",
                "recommendation": "Identify and track applicable requirements.",
                "domain": "Organizational"
            },
            "A.5.32": {
                "title": "Intellectual property rights",
                "description": "To protect intellectual property.",
                "recommendation": "Implement processes to protect IP rights.",
                "domain": "Organizational"
            },
            "A.5.33": {
                "title": "Protection of records",
                "description": "To ensure records are protected from loss or damage.",
                "recommendation": "Implement records protection measures.",
                "domain": "Organizational"
            },
            "A.5.34": {
                "title": "Privacy and protection of PII",
                "description": "To ensure protection of personally identifiable information.",
                "recommendation": "Implement PII protection measures.",
                "domain": "Organizational"
            },
            "A.5.35": {
                "title": "Independent review of information security",
                "description": "To ensure security controls remain effective.",
                "recommendation": "Conduct regular independent security reviews.",
                "domain": "Organizational"
            },
            "A.5.36": {
                "title": "Compliance with policies, rules and standards for information security",
                "description": "To ensure compliance with security requirements.",
                "recommendation": "Monitor and enforce security compliance.",
                "domain": "Organizational"
            },
            "A.5.37": {
                "title": "Documented operating procedures",
                "description": "To ensure consistent and secure operations.",
                "recommendation": "Document and maintain operational procedures.",
                "domain": "Organizational"
            },

            # People Controls (A.6)
            "A.6.1": {
                "title": "Screening",
                "description": "To ensure the suitability of candidates for employment.",
                "recommendation": "Conduct background checks according to risk and laws.",
                "domain": "People"
            },
            "A.6.2": {
                "title": "Terms and conditions of employment",
                "description": "To ensure that employees and contractors understand their information security responsibilities.",
                "recommendation": "Include security responsibilities in contracts.",
                "domain": "People"
            },
            "A.6.3": {
                "title": "Information security awareness, education and training",
                "description": "To ensure that all personnel are aware of and meet their responsibilities.",
                "recommendation": "Provide regular training and awareness programs.",
                "domain": "People"
            },
            "A.6.4": {
                "title": "Disciplinary process",
                "description": "To take appropriate action against violations of information security.",
                "recommendation": "Establish and communicate a disciplinary process.",
                "domain": "People"
            },
            "A.6.5": {
                "title": "Responsibilities after termination or change of employment",
                "description": "To protect the organization's interests after employment changes.",
                "recommendation": "Ensure ongoing protection of information after employment ends.",
                "domain": "People"
            },
            "A.6.6": {
                "title": "Confidentiality or non-disclosure agreements",
                "description": "To protect confidential information.",
                "recommendation": "Require confidentiality agreements where appropriate.",
                "domain": "People"
            },
            "A.6.7": {
                "title": "Remote working",
                "description": "To ensure security when working remotely.",
                "recommendation": "Implement security measures for remote work.",
                "domain": "People"
            },
            "A.6.8": {
                "title": "Information security event reporting",
                "description": "To ensure security events are reported.",
                "recommendation": "Establish security event reporting procedures.",
                "domain": "People"
            },

            # Physical Controls (A.7)
            "A.7.1": {
                "title": "Physical security perimeter",
                "description": "To protect areas that contain information and other associated assets.",
                "recommendation": "Establish secure perimeters with appropriate entry controls.",
                "domain": "Physical"
            },
            "A.7.2": {
                "title": "Physical entry",
                "description": "To ensure only authorized access to secure areas.",
                "recommendation": "Implement controlled entry mechanisms.",
                "domain": "Physical"
            },
            "A.7.3": {
                "title": "Securing offices, rooms and facilities",
                "description": "To protect information within physical locations.",
                "recommendation": "Apply security measures based on risk.",
                "domain": "Physical"
            },
            "A.7.4": {
                "title": "Physical security monitoring",
                "description": "To detect unauthorized physical access.",
                "recommendation": "Use CCTV or similar systems for surveillance.",
                "domain": "Physical"
            },
            "A.7.5": {
                "title": "Protection against physical and environmental threats",
                "description": "To prevent loss or damage from physical or environmental events.",
                "recommendation": "Design facilities to withstand known threats.",
                "domain": "Physical"
            },
            "A.7.6": {
                "title": "Working in secure areas",
                "description": "To prevent unauthorized access and leakage of information.",
                "recommendation": "Restrict and monitor activities in secure areas.",
                "domain": "Physical"
            },
            "A.7.7": {
                "title": "Clear desk and clear screen",
                "description": "To reduce risks of unauthorized access and loss.",
                "recommendation": "Enforce a clean desk and screen policy.",
                "domain": "Physical"
            },
            "A.7.8": {
                "title": "Equipment siting and protection",
                "description": "To protect equipment from threats and hazards.",
                "recommendation": "Position and protect equipment appropriately.",
                "domain": "Physical"
            },
            "A.7.9": {
                "title": "Security of assets off-premises",
                "description": "To protect assets used outside organization premises.",
                "recommendation": "Implement security measures for off-premises assets.",
                "domain": "Physical"
            },
            "A.7.10": {
                "title": "Storage media",
                "description": "To prevent unauthorized access to stored information.",
                "recommendation": "Implement secure storage media handling.",
                "domain": "Physical"
            },
            "A.7.11": {
                "title": "Supporting utilities",
                "description": "To ensure continuous availability of supporting utilities.",
                "recommendation": "Protect and maintain critical utilities.",
                "domain": "Physical"
            },
            "A.7.12": {
                "title": "Cabling security",
                "description": "To prevent interception or damage to cabling.",
                "recommendation": "Protect cabling from interception or damage.",
                "domain": "Physical"
            },
            "A.7.13": {
                "title": "Equipment maintenance",
                "description": "To ensure equipment remains in working order.",
                "recommendation": "Perform regular equipment maintenance.",
                "domain": "Physical"
            },
            "A.7.14": {
                "title": "Secure disposal or re-use of equipment",
                "description": "To prevent leakage of information from disposed equipment.",
                "recommendation": "Implement secure disposal procedures.",
                "domain": "Physical"
            },

            # Technological Controls (A.8)
            "A.8.1": {
                "title": "User endpoint devices",
                "description": "To protect information processed by endpoint devices.",
                "recommendation": "Implement security controls for endpoint devices.",
                "domain": "Technological"
            },
            "A.8.2": {
                "title": "Privileged access rights",
                "description": "To restrict and control privileged access rights.",
                "recommendation": "Implement strict controls for privileged access.",
                "domain": "Technological"
            },
            "A.8.3": {
                "title": "Information access restriction",
                "description": "To restrict access to information according to policy.",
                "recommendation": "Implement access restrictions based on need-to-know.",
                "domain": "Technological"
            },
            "A.8.4": {
                "title": "Access to source code",
                "description": "To restrict access to source code.",
                "recommendation": "Control access to source code repositories.",
                "domain": "Technological"
            },
            "A.8.5": {
                "title": "Secure authentication",
                "description": "To ensure secure authentication methods are used.",
                "recommendation": "Implement strong authentication mechanisms.",
                "domain": "Technological"
            },
            "A.8.6": {
                "title": "Capacity management",
                "description": "To ensure adequate capacity for systems.",
                "recommendation": "Monitor and manage system capacity.",
                "domain": "Technological"
            },
            "A.8.7": {
                "title": "Protection against malware",
                "description": "To protect systems against malicious code.",
                "recommendation": "Implement anti-malware solutions.",
                "domain": "Technological"
            },
            "A.8.8": {
                "title": "Management of technical vulnerabilities",
                "description": "To prevent exploitation of technical vulnerabilities.",
                "recommendation": "Implement vulnerability management processes.",
                "domain": "Technological"
            },
            "A.8.9": {
                "title": "Configuration management",
                "description": "To ensure secure system configurations.",
                "recommendation": "Implement configuration management processes.",
                "domain": "Technological"
            },
            "A.8.10": {
                "title": "Information deletion",
                "description": "To prevent unnecessary retention of information.",
                "recommendation": "Implement secure deletion procedures.",
                "domain": "Technological"
            },
            "A.8.11": {
                "title": "Data masking",
                "description": "To protect sensitive data.",
                "recommendation": "Implement data masking where appropriate.",
                "domain": "Technological"
            },
            "A.8.12": {
                "title": "Data leakage prevention",
                "description": "To prevent unauthorized data disclosure.",
                "recommendation": "Implement data leakage prevention measures.",
                "domain": "Technological"
            },
            "A.8.13": {
                "title": "Information backup",
                "description": "To protect against data loss.",
                "recommendation": "Implement regular backup procedures.",
                "domain": "Technological"
            },
            "A.8.14": {
                "title": "Redundancy of information processing facilities",
                "description": "To ensure availability of information processing.",
                "recommendation": "Implement redundant processing facilities.",
                "domain": "Technological"
            },
            "A.8.15": {
                "title": "Logging",
                "description": "To record events for monitoring and investigation.",
                "recommendation": "Implement comprehensive logging.",
                "domain": "Technological"
            },
            "A.8.16": {
                "title": "Monitoring activities",
                "description": "To detect unusual or unauthorized activities.",
                "recommendation": "Implement system monitoring.",
                "domain": "Technological"
            },
            "A.8.17": {
                "title": "Clock synchronization",
                "description": "To ensure accurate time stamps.",
                "recommendation": "Synchronize system clocks.",
                "domain": "Technological"
            },
            "A.8.18": {
                "title": "Installation of software on operational systems",
                "description": "To prevent unauthorized software installation.",
                "recommendation": "Control software installation.",
                "domain": "Technological"
            },
            "A.8.19": {
                "title": "Networks security",
                "description": "To protect network services.",
                "recommendation": "Implement network security controls.",
                "domain": "Technological"
            },
            "A.8.20": {
                "title": "Security of network services",
                "description": "To ensure security of network services.",
                "recommendation": "Protect network services.",
                "domain": "Technological"
            },
            "A.8.21": {
                "title": "Segregation in networks",
                "description": "To limit network access.",
                "recommendation": "Implement network segmentation.",
                "domain": "Technological"
            },
            "A.8.22": {
                "title": "Web filtering",
                "description": "To restrict access to harmful web content.",
                "recommendation": "Implement web content filtering.",
                "domain": "Technological"
            },
            "A.8.23": {
                "title": "Use of cryptography",
                "description": "To protect information confidentiality and integrity.",
                "recommendation": "Implement appropriate cryptographic controls.",
                "domain": "Technological"
            },
            "A.8.24": {
                "title": "Secure development lifecycle",
                "description": "To ensure security in development processes.",
                "recommendation": "Implement secure development practices.",
                "domain": "Technological"
            },
            "A.8.25": {
                "title": "Application security requirements",
                "description": "To ensure security is considered in applications.",
                "recommendation": "Define application security requirements.",
                "domain": "Technological"
            },
            "A.8.26": {
                "title": "Secure system architecture and engineering principles",
                "description": "To ensure security is built into systems.",
                "recommendation": "Apply secure architecture principles.",
                "domain": "Technological"
            },
            "A.8.27": {
                "title": "Secure coding",
                "description": "To prevent security vulnerabilities in code.",
                "recommendation": "Implement secure coding standards.",
                "domain": "Technological"
            },
            "A.8.28": {
                "title": "Security testing in development",
                "description": "To identify security weaknesses during development.",
                "recommendation": "Perform security testing throughout development.",
                "domain": "Technological"
            },
            "A.8.29": {
                "title": "Outsourced development",
                "description": "To ensure security in outsourced development.",
                "recommendation": "Include security requirements in outsourced development.",
                "domain": "Technological"
            },
            "A.8.30": {
                "title": "Separation of development, test and production environments",
                "description": "To prevent unauthorized access or changes.",
                "recommendation": "Maintain separate environments.",
                "domain": "Technological"
            },
            "A.8.31": {
                "title": "Change management",
                "description": "To control changes to systems.",
                "recommendation": "Implement formal change management.",
                "domain": "Technological"
            },
            "A.8.32": {
                "title": "Test information",
                "description": "To protect test information.",
                "recommendation": "Protect sensitive test data.",
                "domain": "Technological"
            },
            "A.8.33": {
                "title": "Acceptance testing",
                "description": "To ensure security requirements are met.",
                "recommendation": "Perform security acceptance testing.",
                "domain": "Technological"
            },
            "A.8.34": {
                "title": "Protection of information systems during audit testing",
                "description": "To ensure that audit testing does not compromise the security of information systems.",
                "recommendation": "Implement measures to protect information systems during audit testing.",
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
                ]
            },
            {
                "phase": 2,
                "name": "Risk Assessment",
                "tasks": [
                    "Asset identification",
                    "Risk analysis",
                    "Risk treatment plan"
                ]
            },
            {
                "phase": 3,
                "name": "Control Implementation",
                "tasks": [
                    "Organizational controls (A.5)",
                    "People controls (A.6)",
                    "Physical controls (A.7)",
                    "Technological controls (A.8)"
                ]
            },
            {
                "phase": 4,
                "name": "Certification Preparation",
                "tasks": [
                    "Internal audit",
                    "Management review",
                    "Stage 1 audit",
                    "Stage 2 audit"
                ]
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
            print("6. Exit")

            choice = input("\nSelect option (1-6): ")

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
                print("\nExiting... Your progress has been saved.")
                break
            else:
                print("Invalid option, please try again.")

    def view_all_controls(self):
        print("\n=== All ISO 27001 Controls ===")
        for control_id, details in self.controls.items():
            status = self.get_control_status(control_id)
            print(f"\n{control_id}: {details['title']}")
            print(f"Status: {status.value}")
            print(f"Domain: {details['domain']}")
            print(f"Recommendation: {details['recommendation']}")
            note = self.get_control_note(control_id)
            if note:
                print(f"Note: {note}")
            print("-" * 60)

    def view_controls_by_domain(self):
        print("\n=== View Controls by Domain ===")
        print("1. Organizational (A.5)")
        print("2. People (A.6)")
        print("3. Physical (A.7)")
        print("4. Technological (A.8)")
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
                    print(f"Recommendation: {details['recommendation']}")
                    print("-" * 50)
        else:
            print("Invalid option, please try again.")

    def update_control_status(self):
        print("\n=== Update Control Status ===")
        control_id = input("Enter control ID (e.g., A.5.1): ").upper()

        if control_id not in self.controls:
            print("Invalid control ID. Please try again.")
            return

        print(f"\nCurrent status for {control_id}: {self.get_control_status(control_id).value}")
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

        # Option to add a note
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
            status = ControlStatus[data['controls_status'].get(control_id, "NOT_STARTED")]
            status_counts[status] += 1

        print(f"\nTotal Controls: {total_controls}")
        for status, count in status_counts.items():
            percentage = (count / total_controls) * 100
            print(f"{status.value}: {count} ({percentage:.1f}%)")

        print("\nControls Needing Attention:")
        for control_id, status in data['controls_status'].items():
            if status in ["NOT_STARTED", "IN_PROGRESS"]:
                print(f" - {control_id}: {self.controls[control_id]['title']} ({status})")

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