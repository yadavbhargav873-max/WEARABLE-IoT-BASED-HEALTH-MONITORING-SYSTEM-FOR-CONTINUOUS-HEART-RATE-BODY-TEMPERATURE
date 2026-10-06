# Wearable IoT-Based Health Monitoring System

## Project Overview

This project implements a comprehensive **Wearable IoT-Based Health Monitoring System** for continuous tracking of heart rate, body temperature, blood oxygen saturation (SpO2), and respiratory rate. The system provides real-time health analysis, automated alert generation, and comprehensive data visualization for remote patient monitoring and early disease detection.

## Project Objectives

- Design and implement a smart wearable health monitoring system using IoT technologies
- Integrate multiple biomedical sensors for real-time vital sign monitoring
- Develop automated alert generation logic for health anomaly detection
- Create comprehensive data logging and analysis mechanisms
- Implement scalable system architecture for multi-parameter monitoring
- Support early disease detection and enhance remote healthcare services

## System Features

### Core Monitoring Capabilities
- **Heart Rate Monitoring**: Continuous BPM tracking with activity-based fluctuations (40-200 BPM range)
- **Body Temperature Monitoring**: Real-time temperature tracking with fever/hypothermia detection (34-41°C range)
- **Blood Oxygen Saturation (SpO2)**: Continuous oxygen level monitoring (94-100% range)
- **Respiratory Rate Monitoring**: Breathing rate tracking (10-40 breaths/min range)

### Health Status Classification
- **NORMAL**: All vital signs within safe operating parameters
- **CAUTION**: Mild deviation from baseline, requires monitoring
- **ALERT**: Significant physiological stress, immediate notification
- **CRITICAL**: Life-threatening medical emergency, urgent intervention required

### System Components
- **HeartRateSensor**: Simulates realistic heart rate variations based on activity levels
- **TemperatureSensor**: Generates physiologically accurate temperature readings with anomaly injection
- **BloodOxygenSensor**: Simulates SpO2 levels with occasional oxygen drops
- **RespiratoryRateSensor**: Tracks breathing rate with natural variations
- **HealthAnalyzer**: Evaluates vital signs against clinical thresholds and generates alerts
- **DeviceMonitor**: Tracks wearable device status and battery level
- **WearableHealthMonitoringSystem**: Central controller orchestrating all components

### Performance Metrics
- **Monitoring Reliability Score**: 82.9/100
- **Heart Rate Stability Score**: 47.48/100
- **Temperature Stability Score**: 98.83/100
- **Early Warning Effectiveness**: 97.2/100

## Simulation Results

### Monitoring Statistics (1000 Cycles)
- **Total Readings**: 1000
- **Average Heart Rate**: 105.47 BPM (Range: 69-151 BPM)
- **Average Temperature**: 37.14°C (Range: 35.05-39.84°C)
- **Average SpO2**: 97.3% (Range: 94-99.6%)
- **Average Respiratory Rate**: 13.4 breaths/min (Range: 11-16)

### Health Status Distribution
- **Normal**: 430 readings (43.0%)
- **Caution**: 180 readings (18.0%)
- **Alert**: 350 readings (35.0%)
- **Critical**: 40 readings (4.0%)
- **Total Alert Events**: 570 (57.0%)

## File Structure

```
wearable_health_report/
├── wearable_health_monitoring.py      # Main simulation engine (600+ lines)
├── generate_visualizations.py         # Chart generation script (500+ lines)
├── generate_report.py                 # Word document generator (400+ lines)
├── vital_signs_readings.csv           # Simulation data (CSV format)
├── vital_signs_readings.json          # Simulation data (JSON format)
├── health_alerts_history.csv          # Alert event log
├── chart_01_heart_rate_trend.png      # Heart rate visualization
├── chart_02_temperature_trend.png     # Temperature visualization
├── chart_03_blood_oxygen_trend.png    # SpO2 visualization
├── chart_04_health_status_distribution.png  # Status distribution chart
├── chart_05_vital_signs_distribution.png    # Distribution histograms
├── chart_06_alert_timeline.png        # Alert timeline visualization
├── chart_07_comprehensive_dashboard.png     # Complete dashboard
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── IoT_Wearable_Health_Internship_Report.docx  # Final report (30+ pages)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Extract the project files**:
   ```bash
   unzip iot_wearable_health_code.zip
   cd wearable_health_report
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install python-docx matplotlib numpy
   ```

## Usage

### Run the Complete Simulation

Execute the main simulation to generate vital sign data:
```bash
python3 wearable_health_monitoring.py
```

This will:
- Run 1000 monitoring cycles
- Generate 1000 vital sign readings
- Create health alerts based on clinical thresholds
- Export data to CSV and JSON formats
- Display comprehensive statistics

### Generate Visualizations

Create professional charts from the simulation data:
```bash
python3 generate_visualizations.py
```

This will generate 7 high-resolution visualization files:
1. Heart Rate Trend Chart
2. Temperature Trend Chart
3. Blood Oxygen Trend Chart
4. Health Status Distribution
5. Vital Signs Distribution Histograms
6. Alert Timeline
7. Comprehensive Dashboard

### Generate the Report

Create the final Word document report:
```bash
python3 generate_report.py
```

This will generate `IoT_Wearable_Health_Internship_Report.docx` containing:
- Executive Summary
- Organization Overview
- IoT and Healthcare Introduction
- Problem Assessment
- System Implementation Details
- Results and Performance Evaluation
- Conclusion and Future Scope
- All 7 embedded visualizations
- References

## System Architecture

### Monitoring Loop
```
Read Sensors → Analyze Health Status → Generate Alerts → Log Data → Export Results
```

### Data Flow
```
Wearable Sensors → HealthAnalyzer → Alert Generator → Data Logger → Visualization
```

### Alert Mechanism
```
Vital Signs → Clinical Thresholds → Multi-tier Classification → Notification System
```

## Clinical Thresholds

### Heart Rate (BPM)
- Normal: 60-100 BPM
- Caution: 50-60 or 100-120 BPM
- Alert: <40 or >120 BPM
- Critical: <40 or >150 BPM

### Body Temperature (°C)
- Normal: 36.5-37.5°C
- Caution: 37.5-38.5°C
- Alert: >38.5°C or <35.5°C
- Critical: >39.5°C or <35°C

### Blood Oxygen (%)
- Normal: ≥95%
- Caution: 93-95%
- Alert: <93%
- Critical: <90%

### Respiratory Rate (breaths/min)
- Normal: 12-20 breaths/min
- Abnormal: <10 or >30 breaths/min

## Configuration

### Modifying Clinical Thresholds

Edit `wearable_health_monitoring.py` to adjust alert thresholds:

```python
analyzer = HealthAnalyzer(
    hr_caution_low=50,
    hr_caution_high=100,
    hr_alert_low=40,
    hr_alert_high=120,
    temp_caution_high=38.5,
    temp_alert_high=39.5,
    temp_alert_low=35.5,
    spo2_caution=95.0,
    spo2_alert=93.0
)
```

### Adjusting Simulation Parameters

Modify the number of monitoring cycles:

```python
system = WearableHealthMonitoringSystem(patient_id="PATIENT_001")
readings = system.run_simulation(num_cycles=2000)  # Change cycle count
```

## Output Files

### Data Files
- **vital_signs_readings.csv**: All vital sign readings with timestamps and health status
- **vital_signs_readings.json**: Complete simulation data with statistics and alert history
- **health_alerts_history.csv**: Detailed log of all generated health alerts

### Visualization Files
- **chart_*.png**: High-resolution (300 DPI) professional charts suitable for reports and presentations

### Report File
- **IoT_Wearable_Health_Internship_Report.docx**: Comprehensive 30+ page internship report

## Performance Metrics Explained

### Monitoring Reliability Score (82.9/100)
Measures the system's ability to maintain normal health status. Calculated as:
```
Reliability = 100 - (Alert_Count / Total_Readings) × 30
```

### Heart Rate Stability Score (47.48/100)
Evaluates the consistency of heart rate readings:
```
Stability = 100 - (Standard_Deviation × 2)
```

### Temperature Stability Score (98.83/100)
Measures temperature consistency (typically very high):
```
Stability = 100 - (Standard_Deviation × 2)
```

### Early Warning Effectiveness (97.2/100)
Assesses the system's ability to catch issues early:
```
Effectiveness = 100 - (Critical_Count / Total_Alerts × 40)
```

## Real-World Deployment Considerations

### Hardware Integration
- **Microcontroller**: ESP32 or nRF52 for processing and connectivity
- **Sensors**: MAX30102 (heart rate/SpO2), MLX90614 (temperature), accelerometer for activity
- **Communication**: Bluetooth Low Energy (BLE) for power efficiency
- **Power**: Rechargeable battery with 7-14 day autonomy

### Cloud Platform
- Real-time data ingestion via MQTT or REST APIs
- Secure data storage with encryption (HIPAA compliant)
- Machine learning for predictive health analytics
- Mobile and web dashboards for patients and physicians

### Security Measures
- End-to-end encryption for all data transmission
- Secure authentication and authorization
- Regular security audits and penetration testing
- Compliance with healthcare regulations (HIPAA, GDPR)

## Future Enhancements

1. **Artificial Intelligence Integration**: Predictive health analytics using machine learning
2. **Advanced Sensors**: ECG, continuous glucose monitoring, blood pressure
3. **Flexible Electronics**: Epidermal sensors and energy-harvesting technologies
4. **Blockchain Integration**: Immutable health records and multi-provider access
5. **Mobile Applications**: Native iOS and Android apps for patient engagement
6. **Telemedicine Integration**: Direct communication with healthcare providers
7. **Wearable Diversity**: Support for smartwatches, fitness bands, medical patches

## Troubleshooting

### Issue: ImportError for matplotlib or numpy
**Solution**: Install missing packages:
```bash
pip install matplotlib numpy python-docx
```

### Issue: CSV or JSON files not found
**Solution**: Ensure you've run the main simulation first:
```bash
python3 wearable_health_monitoring.py
```

### Issue: Charts not generating
**Solution**: Verify matplotlib installation and check file permissions:
```bash
pip install --upgrade matplotlib
```

## Performance Optimization Tips

1. **For Large Datasets**: Increase simulation cycles for more comprehensive analysis
2. **For Real-time Processing**: Implement streaming data processing with Kafka or RabbitMQ
3. **For Cloud Deployment**: Use containerization (Docker) and orchestration (Kubernetes)
4. **For ML Integration**: Prepare data in batches for model training

## References

- Python Documentation: https://docs.python.org/3/
- Matplotlib Documentation: https://matplotlib.org/
- IoT in Healthcare: Dias & Silva Cunha (2018)
- Wearable Sensors: Majumder et al. (2017)
- Real-time Health Monitoring: Baig et al. (2017)

## Support and Contact

For questions, issues, or suggestions regarding this project, please refer to the comprehensive documentation in the internship report or contact the development team.

## License

This project is provided for educational and research purposes as part of an internship program.

## Acknowledgments

This project was developed as part of an internship program focused on IoT technologies and healthcare applications. The work demonstrates the practical application of IoT principles in solving real-world healthcare challenges.

---

**Project Status**: Completed ✓
**Last Updated**: July 13, 2024
**Version**: 1.0
