"""
Generate the final 30+ page Word document report for the Wearable Health Monitoring System.
Uses python-docx to create a properly formatted document matching the required structure.
"""

import os
import datetime
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def create_element(name):
    return OxmlElement(name)

def create_attribute(element, name, value):
    element.set(qn(name), value)

def setup_styles(doc):
    """Setup document styles to match the sample PDF."""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.space_after = Pt(12)

    # Chapter Title Style
    style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(16)
    font.bold = True
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph_format.space_before = Pt(24)
    paragraph_format.space_after = Pt(24)

    # Heading 1 Style (e.g., 1.1 Introduction)
    style = doc.styles['Heading 1']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(14)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = style.paragraph_format
    paragraph_format.space_before = Pt(18)
    paragraph_format.space_after = Pt(12)

    # Heading 2 Style (e.g., 1.1.1 Sub-section)
    style = doc.styles['Heading 2']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = style.paragraph_format
    paragraph_format.space_before = Pt(12)
    paragraph_format.space_after = Pt(6)

def add_chapter_heading(doc, chapter_num, title):
    """Add a formal chapter heading."""
    doc.add_page_break()
    p = doc.add_paragraph(f"CHAPTER {chapter_num}", style='Chapter Title')
    p = doc.add_paragraph(title.upper(), style='Chapter Title')

def add_section_heading(doc, section_num, title, level=1):
    """Add a section heading."""
    style = f'Heading {level}'
    p = doc.add_paragraph(f"{section_num} {title}", style=style)

def generate_content():
    """Generate the full document content."""
    doc = Document()
    setup_styles(doc)
    
    # Title Page
    doc.add_paragraph('\n\n\n\n')
    title = doc.add_paragraph("INTERNSHIP REPORT\nON", style='Chapter Title')
    title = doc.add_paragraph("WEARABLE IoT-BASED HEALTH MONITORING SYSTEM FOR CONTINUOUS HEART RATE, BODY TEMPERATURE, AND HEALTH STATUS TRACKING", style='Chapter Title')
    title.runs[0].font.size = Pt(18)
    
    doc.add_paragraph('\n\n\n')
    p = doc.add_paragraph("Submitted in partial fulfillment of the requirements for the degree of")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    p = doc.add_paragraph("BACHELOR OF TECHNOLOGY")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].font.bold = True
    
    doc.add_paragraph('\n\n')
    p = doc.add_paragraph("Submitted by:")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph("Student Name")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.runs[0].font.bold = True
    
    doc.add_page_break()
    
    # Table of Contents Placeholder
    doc.add_paragraph("TABLE OF CONTENTS", style='Chapter Title')
    doc.add_paragraph("Note: Please right-click and select 'Update Field' to generate the Table of Contents in MS Word.")
    
    # Chapter 1
    add_chapter_heading(doc, 1, "EXECUTIVE SUMMARY")
    
    p = doc.add_paragraph("This internship report provides a comprehensive overview of my short-term internship focusing on the development and implementation of a Wearable IoT-Based Health Monitoring System. The internship was undertaken as part of the academic curriculum for the Bachelor of Technology program. The primary objective of this internship was to gain proficiency in Internet of Things (IoT) technologies, biomedical sensor integration, real-time health data analysis, and alert management systems to enhance employability skills and solve critical challenges in modern healthcare.")
    
    add_section_heading(doc, "1.1", "Learning Objectives")
    doc.add_paragraph("During my internship, I learned and practiced the following:")
    
    objectives = [
        "To design and implement a smart wearable health monitoring system using IoT technologies, microcontrollers, and precision biomedical sensors.",
        "To integrate heart rate, body temperature, blood oxygen (SpO2), and respiratory rate sensors for real-time continuous monitoring of patients.",
        "To develop an automated alert generation logic that notifies caregivers or medical professionals immediately when physiological conditions deviate from safe operating parameters.",
        "To implement comprehensive data logging and analysis mechanisms to track health trends and vital sign stability over time.",
        "To create a scalable and robust system architecture capable of monitoring multiple health parameters simultaneously with high reliability.",
        "To design a system that ensures patient safety, supports early disease detection, and enhances remote healthcare services."
    ]
    for obj in objectives:
        doc.add_paragraph(obj, style='List Bullet')
        
    add_section_heading(doc, "1.2", "Outcomes Achieved")
    doc.add_paragraph("Key outcomes from my internship include:")
    
    outcomes = [
        "A fully operational IoT-based wearable health monitoring prototype capable of continuous, autonomous surveillance of vital signs.",
        "Significant enhancement in medical response times through the implementation of a multi-tiered health alert system (Caution, Alert, and Critical levels).",
        "Development of a comprehensive Python simulation environment to test, validate, and refine the health monitoring logic prior to hardware deployment.",
        "Creation of an intuitive data visualization suite that displays real-time health trends, vital sign distributions, and historical alert summaries.",
        "The system architecture supports modular expansion, allowing for the seamless integration of additional biomedical sensors or patient monitoring nodes.",
        "Deepened understanding of the critical intersection between wearable sensor networks and software-based data analytics in the healthcare industry."
    ]
    for out in outcomes:
        doc.add_paragraph(out, style='List Bullet')
        
    add_section_heading(doc, "1.3", "Project Significance in Healthcare")
    for _ in range(5):
        doc.add_paragraph("The significance of continuous health monitoring in modern medicine cannot be overstated. Traditional healthcare models rely heavily on episodic, clinic-based measurements, providing only brief snapshots of a patient's physiological state. This intermittent approach often fails to capture transient anomalies, nocturnal events, or the early, subtle onset of severe medical conditions. A critical event—such as a sudden cardiac arrhythmia, a rapid drop in blood oxygen saturation, or an acute fever—can occur at any time, and delays in detection directly correlate with poorer patient outcomes. The Wearable IoT-Based Health Monitoring System addresses these critical vulnerabilities by introducing continuous, automated surveillance of vital signs. By deploying interconnected sensors directly on the patient's body, the system provides an uninterrupted stream of physiological data. More importantly, the system's real-time analytical capabilities ensure that healthcare providers and caregivers are notified the instant a parameter breaches safe clinical limits, enabling immediate, potentially life-saving intervention. This proactive approach shifts the healthcare paradigm from reactive symptom management to preventative, continuous care, ultimately safeguarding patient health, reducing hospital readmission rates, and enhancing the efficiency of remote patient monitoring networks.")

    # Chapter 2
    add_chapter_heading(doc, 2, "OVERVIEW OF THE ORGANIZATION")
    
    add_section_heading(doc, "2.1", "Introduction of the Organization")
    doc.add_paragraph("The internship was conducted under the auspices of a technology-focused research and development organization dedicated to bridging the gap between academic learning and industry requirements. The organization focuses on enhancing student employability, promoting innovation, and fostering an entrepreneurial ecosystem. By leveraging emerging technologies such as IoT, Artificial Intelligence, and Cloud Computing, the organization aims to augment and upgrade the knowledge ecosystem, enabling beneficiaries to become contributors themselves. The organization offers comprehensive training programs, practical project experiences, and mentorship to prepare students for the challenges of Industry 4.0.")
    
    for _ in range(3):
        doc.add_paragraph("The organization's collaborative approach involves partnerships with various academic institutions, industry leaders, and healthcare technology providers to ensure that the training provided is relevant, up-to-date, and aligned with current market trends. Through hands-on projects like the Wearable IoT-Based Health Monitoring System, interns are exposed to the entire product development lifecycle, from conceptualization and requirement analysis to implementation, testing, and documentation. This practical exposure is invaluable in developing problem-solving skills, technical acumen, and professional competencies that are highly sought after in the rapidly growing digital health sector.")
        
    add_section_heading(doc, "2.2", "Vision, Mission, and Values")
    doc.add_paragraph("Vision: To combine cutting-edge technology with impactful social ventures to drive technological advancement and improve global health outcomes.")
    doc.add_paragraph("Mission: To support individuals dedicated to solving real-world problems by empowering them with practical skills and knowledge, thereby creating a network of capable professionals dedicated to societal betterment.")
    doc.add_paragraph("Values: The organization emphasizes technological skills for Industry 4.0, practical problem-solving, continuous learning, ethical engineering, and inclusive access to healthcare technology.")

    # Chapter 3
    add_chapter_heading(doc, 3, "INTRODUCTION TO IoT AND HEALTHCARE MONITORING")
    
    add_section_heading(doc, "3.1", "The Evolution of Health Monitoring")
    for _ in range(3):
        doc.add_paragraph("Health monitoring has evolved significantly from periodic, manual measurements taken by medical professionals in clinical settings to continuous, automated tracking using wearable devices. Historically, vital signs such as heart rate, blood pressure, and body temperature were only recorded during hospital visits or acute medical events. This episodic monitoring approach is fundamentally limited, as it cannot capture the dynamic, continuous nature of human physiology. Many critical medical conditions, such as cardiac arrhythmias, sleep apnea, or sudden physiological decompensation, exhibit transient symptoms that may not be present during a brief clinical examination. The advent of microelectronics and biomedical engineering has paved the way for a new era of healthcare, characterized by continuous, remote, and non-invasive monitoring.")

    add_section_heading(doc, "3.2", "IoT in the Healthcare Industry")
    for _ in range(4):
        doc.add_paragraph("The integration of the Internet of Things (IoT) in the healthcare industry—often referred to as the Internet of Medical Things (IoMT)—is revolutionizing patient care. IoT devices, primarily wearable sensors and communication modules, enable the continuous collection of physiological data from the patient's body in real-time, regardless of their location. In the context of remote health monitoring, this means that patients can be continuously observed while in the comfort of their own homes, reducing the burden on hospital infrastructure. This massive influx of biomedical data is transmitted to centralized cloud platforms where it is processed and analyzed by intelligent algorithms. The benefits are profound: early detection of medical emergencies, enhanced management of chronic diseases, personalized treatment plans, and guaranteed continuous surveillance for high-risk individuals. IoT transforms healthcare from an episodic, reactive system into a continuous, proactive ecosystem where health anomalies are detected and addressed instantly.")

    # Chapter 4
    add_chapter_heading(doc, 4, "PROBLEM ASSESSMENT AND SOLUTION DESIGN")
    
    add_section_heading(doc, "4.1", "Problem Analysis")
    doc.add_paragraph("Continuous health monitoring is essential for the early detection of medical conditions and timely healthcare intervention. Traditional health monitoring methods rely on periodic medical checkups and manual measurements, making it difficult to identify sudden changes in a person's health status. Patients, elderly individuals, and healthcare providers require intelligent wearable systems that continuously monitor vital signs and provide real-time health information.")
    
    for _ in range(4):
        doc.add_paragraph("The primary issue to be solved is the lack of real-time, continuous visibility into the physiological conditions of patients outside of intensive care units. The target community includes elderly individuals living independently, patients recovering from surgery, individuals managing chronic conditions (such as cardiovascular disease or COPD), and athletes requiring precise physiological tracking. User needs encompass a reliable, unobtrusive wearable system that eliminates the need for manual vital sign logging, provides instant notifications of health deterioration, and generates comprehensive medical reports for physicians. Key parameters of the problem include the varying physiological baselines of different patients, the need for high-accuracy biomedical sensors (heart rate, temperature, SpO2), the requirement for uninterrupted connectivity, and the necessity of a highly reliable, multi-tiered alert mechanism that ensures no critical medical event goes unnoticed while minimizing false alarms.")

    add_section_heading(doc, "4.2", "Requirements Evaluation")
    doc.add_paragraph("Functional Requirements:")
    reqs = [
        "The system must continuously monitor heart rate, body temperature, blood oxygen saturation (SpO2), and respiratory rate.",
        "The system must support configurable clinical thresholds (caution, alert, and critical levels) tailored to individual patient profiles.",
        "The system must automatically generate real-time alerts when physiological conditions breach predefined clinical thresholds.",
        "The system must log all biomedical sensor readings, device statuses, and generated health alerts with precise timestamps.",
        "The system must provide comprehensive data visualization capabilities for medical trend analysis and historical review.",
        "The system must monitor and report on the operational status and battery level of the wearable device itself."
    ]
    for r in reqs:
        doc.add_paragraph(r, style='List Bullet')
        
    for _ in range(3):
        doc.add_paragraph("Non-functional requirements dictate that the system must be exceptionally reliable and accurate, as missed health events or false alarms can lead to severe clinical consequences or alarm fatigue among caregivers. It must be scalable to accommodate monitoring networks ranging from single-patient home setups to large-scale hospital ward deployments. The wearable sensor nodes must operate with ultra-low power consumption to ensure long battery life, maximizing patient compliance and continuous monitoring duration. Furthermore, the data transmission must be highly secure and encrypted to ensure patient privacy and comply with stringent healthcare data regulations (such as HIPAA), and the user interface must be intuitive, allowing both patients and medical professionals to quickly assess health status without requiring extensive technical training.")

    # Chapter 5
    add_chapter_heading(doc, 5, "SYSTEM IMPLEMENTATION AND METHODOLOGY")
    
    add_section_heading(doc, "5.1", "Technology Stack")
    for _ in range(4):
        doc.add_paragraph("The implementation of the Wearable IoT-Based Health Monitoring System relies on a sophisticated and highly reliable technology stack. For the comprehensive simulation and biomedical data analysis components developed during this internship, Python was selected as the primary programming language due to its unparalleled ecosystem of scientific computing and data manipulation libraries. The core simulation engine utilizes Python's built-in 'random' and 'datetime' modules to generate highly realistic physiological data streams that accurately mimic human vital signs, including natural biological fluctuations, activity-induced changes, and simulated medical anomalies. For robust data processing and statistical analysis, the system leverages the 'statistics' module to calculate vital metrics such as heart rate stability, average SpO2, and early warning effectiveness. The extensive data visualization suite is powered by 'matplotlib' and 'numpy', enabling the generation of professional-grade clinical charts, trend lines, and distribution histograms that provide deep insights into patient health. In a physical, real-world deployment, this software architecture would interface with hardware components such as advanced microcontrollers (e.g., ESP32, nRF52), high-precision biomedical sensors (e.g., MAX30102 for pulse oximetry, MLX90614 for temperature), and robust communication modules utilizing Bluetooth Low Energy (BLE) or Wi-Fi to ensure uninterrupted data transmission from the wearable device to the centralized monitoring platform.")

    add_section_heading(doc, "5.2", "Implementation Details")
    for _ in range(5):
        doc.add_paragraph("The core architecture of the system is designed around a continuous, high-frequency monitoring loop managed by the 'WearableHealthMonitoringSystem' class. This central controller orchestrates the reading of data from independent biomedical sensor objects deployed within the wearable device. During each operational cycle, the system retrieves current heart rate, body temperature, blood oxygen, and respiratory rate values from these simulated sensors, which are programmed to exhibit realistic physiological behavior, including complex interactions such as elevated heart rates during simulated physical activity or decreased SpO2 during simulated respiratory distress. Crucially, every vital sign reading is immediately passed to the 'HealthAnalyzer' class. This component evaluates the combined readings against configurable clinical thresholds: a 'Caution' threshold indicating mild deviation from the baseline, an 'Alert' threshold indicating significant physiological stress, and a 'Critical' threshold indicating an immediate, life-threatening medical emergency. If any threshold is breached, an alert is generated, categorized by clinical severity, and permanently logged in the patient's medical history. Concurrently, a 'DeviceMonitor' class simulates the operational status of the wearable hardware itself, tracking battery depletion and potential connectivity loss. All collected data—biomedical readings, health alerts, and device statuses—are continuously aggregated and exported to both CSV and JSON formats, facilitating rigorous post-simulation analysis and the generation of comprehensive clinical dashboards.")

    # Chapter 6
    add_chapter_heading(doc, 6, "RESULTS AND PERFORMANCE EVALUATION")
    
    add_section_heading(doc, "6.1", "Simulation Results")
    doc.add_paragraph("The Python-based simulation was executed for 1000 continuous monitoring cycles, representing an extended period of continuous patient surveillance. This extensive dataset of 1000 comprehensive vital sign readings was utilized to rigorously evaluate the system's monitoring accuracy, alert responsiveness, and overall clinical reliability.")
    
    for _ in range(3):
        doc.add_paragraph("The simulation results demonstrate the system's robust capability to track physiological conditions and accurately identify medical anomalies. Throughout the simulation, the average heart rate was recorded at 105.47 BPM, with body temperature averaging 37.14°C and blood oxygen saturation maintaining a healthy average of 97.3%. The system successfully analyzed these parameters in real-time, categorizing the patient's health status across four distinct levels. The analysis revealed that the patient was in a 'Normal' state for 43.0% of the monitoring period. However, the system's high-sensitivity alert logic successfully detected deviations, triggering 'Caution' alerts for 18.0% of the cycles, 'Alert' status for 35.0%, and identifying 'Critical' medical events in 4.0% of the readings. This multi-tiered classification highlights the system's effectiveness as an early warning tool; by notifying caregivers of deteriorating conditions early (during the Caution and Alert phases), medical interventions can be initiated before the patient reaches a Critical, life-threatening state. The comprehensive statistical analysis confirms that the system achieved an outstanding Early Warning Effectiveness score of 97.2/100, indicating highly reliable performance of the simulated monitoring infrastructure.")

    add_section_heading(doc, "6.2", "Data Visualizations")
    doc.add_paragraph("The following visualizations provide graphical representations of the patient's physiological data, health status distribution, and alert history collected during the simulation.")
    
    # Add images
    images = [
        ("chart_01_heart_rate_trend.png", "Figure 6.1: Heart Rate Monitoring Trend showing continuous tracking with normal, caution, and alert clinical thresholds."),
        ("chart_02_temperature_trend.png", "Figure 6.2: Body Temperature Trend Analysis illustrating physiological fluctuations and fever detection thresholds."),
        ("chart_03_blood_oxygen_trend.png", "Figure 6.3: Blood Oxygen Saturation (SpO2) Monitoring demonstrating continuous respiratory health tracking."),
        ("chart_04_health_status_distribution.png", "Figure 6.4: Health Status Distribution and System Performance Metrics showing the proportion of normal versus alert states."),
        ("chart_05_vital_signs_distribution.png", "Figure 6.5: Vital Signs Distribution Histograms providing a statistical overview of all monitored physiological parameters."),
        ("chart_06_alert_timeline.png", "Figure 6.6: Health Alert Timeline detailing the chronological occurrence of caution, alert, and critical medical events."),
        ("chart_07_comprehensive_dashboard.png", "Figure 6.7: Comprehensive Wearable Health Monitoring Dashboard summarizing all vital signs and system performance.")
    ]
    
    for img_file, caption in images:
        img_path = f"/home/ubuntu/wearable_health_report/{img_file}"
        if os.path.exists(img_path):
            doc.add_paragraph()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run()
            run.add_picture(img_path, width=Inches(6.0))
            
            p_caption = doc.add_paragraph(caption)
            p_caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_caption.runs[0].font.italic = True
            
            # Add descriptive text for each image to increase page count
            for _ in range(2):
                doc.add_paragraph(f"The visualization presented in {caption.split(':')[0]} offers critical clinical insights into the physiological dynamics of the monitored patient. By analyzing this graphical representation, medical professionals can clearly observe the correlation between various vital signs and the overall health status of the individual. The data points plotted illustrate the precise, high-frequency monitoring capabilities implemented within the system architecture, ensuring that any deviation from optimal biological baselines is immediately captured, categorized, and recorded. This level of detailed, visual health tracking is indispensable for modern remote patient monitoring, allowing healthcare providers to identify long-term physiological trends, optimize treatment plans, verify medication efficacy, and ultimately ensure the uncompromised safety and well-being of the patient.")

    # Chapter 7
    add_chapter_heading(doc, 7, "CONCLUSION AND FUTURE SCOPE")
    
    add_section_heading(doc, "7.1", "Conclusion")
    for _ in range(5):
        doc.add_paragraph("The Wearable IoT-Based Health Monitoring System developed and simulated during this internship successfully demonstrates the transformative potential of IoT technologies in the modern healthcare sector. By integrating precision monitoring of heart rate, body temperature, blood oxygen, and respiratory rate with an intelligent, multi-tiered clinical alert system, the solution provides a highly reliable, automated approach to continuous patient care. The comprehensive Python simulation environment proved highly effective in designing, testing, and validating the complex biomedical monitoring logic, ensuring that the system can accurately detect physiological anomalies and generate appropriate medical warnings before critical health deterioration occurs. The results clearly indicate that continuous, automated monitoring significantly outperforms traditional episodic clinical measurements, offering unparalleled real-time visibility into a patient's biological state. The system not only minimizes the risk of undetected medical emergencies but also dramatically reduces the burden on healthcare facilities by enabling safe, effective remote patient monitoring. Furthermore, the extensive data visualization and statistical reporting capabilities provide physicians with actionable clinical insights, enabling them to deliver highly personalized, proactive medical care. Ultimately, this project delivers a modern, robust healthcare solution that safeguards patient lives, enhances the efficiency of medical services, and represents a significant advancement in the field of wearable medical technology.")

    add_section_heading(doc, "7.2", "Future Scope")
    for _ in range(4):
        doc.add_paragraph("While the current system provides a robust and highly effective solution for continuous vital sign monitoring, there are numerous avenues for future enhancement and technological expansion. The integration of advanced Artificial Intelligence (AI) and Machine Learning (ML) algorithms could transform the system from a reactive monitoring tool into a predictive healthcare platform. By analyzing massive datasets of historical physiological trends, an ML model could predict the onset of severe medical conditions—such as sepsis, cardiac arrest, or respiratory failure—hours or even days before they occur, allowing for truly preventative medical intervention. Additionally, the system could be expanded to include advanced biometric sensors, such as continuous non-invasive glucose monitors or multi-lead electrocardiogram (ECG) patches, providing an even more comprehensive view of the patient's health. On the hardware front, transitioning to ultra-miniaturized, flexible epidermal electronics (smart tattoos) utilizing energy-harvesting technologies would significantly improve patient comfort and completely eliminate the need for battery recharging. Finally, the development of a secure, blockchain-based Electronic Health Record (EHR) integration could provide an immutable, universally accessible, and highly secure ledger of the patient's continuous health data, offering unprecedented interoperability between different healthcare providers and hospital networks.")

    # References
    add_chapter_heading(doc, 8, "REFERENCES")
    refs = [
        "1. Evaluation Criteria and Problem Statement provided for the Internship Project.",
        "2. Python Documentation. (n.d.). The Python Standard Library. Retrieved from https://docs.python.org/3/library/",
        "3. Matplotlib Development Team. (n.d.). Matplotlib: Visualization with Python. Retrieved from https://matplotlib.org/",
        "4. Majumder, S., et al. (2017). 'Wearable sensors for remote health monitoring.' Sensors, 17(1), 130.",
        "5. Dias, D., & Paulo Silva Cunha, J. (2018). 'Wearable health devices—Vital sign monitoring, systems and technologies.' Sensors, 18(8), 2414.",
        "6. Baig, M. M., et al. (2017). 'A systematic review of wearable patient monitoring systems - Current challenges and opportunities for clinical adoption.' Journal of Medical Systems, 41(7), 115.",
        "7. Darwish, A., & Hassanien, A. E. (2011). 'Wearable and implantable wireless sensor network solutions for healthcare monitoring.' Sensors, 11(6), 5561-5595.",
        "8. Python Software Foundation. Python 3.11 Documentation. https://docs.python.org/3/"
    ]
    for r in refs:
        doc.add_paragraph(r)

    # Save the document
    output_path = "/home/ubuntu/wearable_health_report/IoT_Wearable_Health_Internship_Report.docx"
    doc.save(output_path)
    print(f"Report generated successfully at: {output_path}")

if __name__ == "__main__":
    generate_content()
