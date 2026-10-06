"""
Wearable IoT-Based Health Monitoring System
Continuous tracking of heart rate, body temperature, and health status

This module simulates a comprehensive wearable health monitoring system that continuously
tracks vital signs and provides real-time health analysis and alerts.
"""

import random
import datetime
import json
import csv
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import statistics
from enum import Enum


class HealthStatus(Enum):
    """Health status classification."""
    NORMAL = "NORMAL"
    CAUTION = "CAUTION"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"


@dataclass
class VitalSignReading:
    """Represents a vital sign reading from the wearable sensor."""
    timestamp: str
    heart_rate: int          # BPM (beats per minute)
    body_temperature: float  # Celsius
    blood_oxygen: float      # SpO2 percentage (95-100%)
    respiratory_rate: int    # breaths per minute
    health_status: str       # NORMAL, CAUTION, ALERT, CRITICAL
    alert_message: str
    device_status: str       # ACTIVE, LOW_BATTERY, DISCONNECTED


class HeartRateSensor:
    """Simulates a heart rate sensor with realistic readings."""
    
    def __init__(self, baseline_hr: int = 72):
        """
        Initialize the heart rate sensor.
        
        Args:
            baseline_hr: Baseline heart rate in BPM (default: 72)
        """
        self.baseline_hr = baseline_hr
        self.last_reading = None
        self.activity_level = 0  # 0-10 scale
    
    def read_heart_rate(self) -> int:
        """
        Read heart rate with realistic variations based on activity.
        
        Returns:
            Heart rate in BPM
        """
        # Simulate activity level changes (0-10 scale)
        activity_change = random.uniform(-1, 1)
        self.activity_level = max(0, min(10, self.activity_level + activity_change))
        
        # Calculate heart rate based on activity
        activity_effect = self.activity_level * 8  # Up to 80 BPM increase
        
        if self.last_reading is None:
            reading = self.baseline_hr + activity_effect + random.uniform(-5, 5)
        else:
            # Smooth transition between readings
            reading = self.last_reading * 0.7 + (self.baseline_hr + activity_effect) * 0.3
            reading += random.uniform(-2, 2)
        
        reading = int(max(40, min(200, reading)))  # Clamp between 40-200 BPM
        self.last_reading = reading
        return reading


class TemperatureSensor:
    """Simulates a body temperature sensor."""
    
    def __init__(self, baseline_temp: float = 37.0):
        """
        Initialize the temperature sensor.
        
        Args:
            baseline_temp: Baseline body temperature in Celsius
        """
        self.baseline_temp = baseline_temp
        self.last_reading = None
    
    def read_temperature(self) -> float:
        """
        Read body temperature with realistic variations.
        
        Returns:
            Body temperature in Celsius
        """
        # Simulate occasional fever or hypothermia (5% chance)
        anomaly_chance = random.random()
        
        if anomaly_chance < 0.03:  # 3% chance of fever
            fluctuation = random.uniform(0.5, 2.5)
        elif anomaly_chance < 0.05:  # 2% chance of hypothermia
            fluctuation = random.uniform(-1.5, -0.5)
        else:  # 95% normal variation
            fluctuation = random.uniform(-0.3, 0.3)
        
        if self.last_reading is None:
            reading = self.baseline_temp + fluctuation
        else:
            reading = self.last_reading * 0.8 + self.baseline_temp * 0.2 + fluctuation
        
        self.last_reading = round(reading, 2)
        return self.last_reading


class BloodOxygenSensor:
    """Simulates a blood oxygen saturation (SpO2) sensor."""
    
    def __init__(self, baseline_spo2: float = 98.0):
        """
        Initialize the blood oxygen sensor.
        
        Args:
            baseline_spo2: Baseline SpO2 percentage
        """
        self.baseline_spo2 = baseline_spo2
        self.last_reading = None
    
    def read_blood_oxygen(self) -> float:
        """
        Read blood oxygen saturation.
        
        Returns:
            SpO2 percentage (95-100%)
        """
        # Simulate occasional oxygen drops (3% chance)
        if random.random() < 0.03:
            fluctuation = random.uniform(-3, -1)
        else:
            fluctuation = random.uniform(-0.5, 0.5)
        
        if self.last_reading is None:
            reading = self.baseline_spo2 + fluctuation
        else:
            reading = self.last_reading * 0.9 + self.baseline_spo2 * 0.1 + fluctuation
        
        reading = max(94, min(100, round(reading, 1)))
        self.last_reading = reading
        return reading


class RespiratoryRateSensor:
    """Simulates a respiratory rate sensor."""
    
    def __init__(self, baseline_rr: int = 16):
        """
        Initialize the respiratory rate sensor.
        
        Args:
            baseline_rr: Baseline respiratory rate in breaths per minute
        """
        self.baseline_rr = baseline_rr
        self.last_reading = None
    
    def read_respiratory_rate(self) -> int:
        """
        Read respiratory rate.
        
        Returns:
            Respiratory rate in breaths per minute
        """
        if self.last_reading is None:
            reading = self.baseline_rr + random.uniform(-2, 2)
        else:
            reading = self.last_reading * 0.8 + self.baseline_rr * 0.2
            reading += random.uniform(-1, 1)
        
        reading = int(max(10, min(40, reading)))
        self.last_reading = reading
        return reading


class HealthAnalyzer:
    """Analyzes vital signs and generates health status alerts."""
    
    def __init__(self,
                 hr_caution_low: int = 50,
                 hr_caution_high: int = 100,
                 hr_alert_low: int = 40,
                 hr_alert_high: int = 120,
                 temp_caution_high: float = 38.5,
                 temp_alert_high: float = 39.5,
                 temp_alert_low: float = 35.5,
                 spo2_caution: float = 95.0,
                 spo2_alert: float = 93.0):
        """
        Initialize the health analyzer with thresholds.
        
        Args:
            hr_caution_low/high: Caution level heart rate thresholds
            hr_alert_low/high: Alert level heart rate thresholds
            temp_caution_high: Caution level temperature threshold
            temp_alert_high: Alert level high temperature threshold
            temp_alert_low: Alert level low temperature threshold
            spo2_caution: Caution level SpO2 threshold
            spo2_alert: Alert level SpO2 threshold
        """
        self.hr_caution_low = hr_caution_low
        self.hr_caution_high = hr_caution_high
        self.hr_alert_low = hr_alert_low
        self.hr_alert_high = hr_alert_high
        self.temp_caution_high = temp_caution_high
        self.temp_alert_high = temp_alert_high
        self.temp_alert_low = temp_alert_low
        self.spo2_caution = spo2_caution
        self.spo2_alert = spo2_alert
        self.alert_history = []
    
    def analyze_vital_signs(self, 
                           heart_rate: int,
                           temperature: float,
                           blood_oxygen: float,
                           respiratory_rate: int) -> Tuple[HealthStatus, str]:
        """
        Analyze vital signs and determine health status.
        
        Returns:
            Tuple of (HealthStatus, alert_message)
        """
        alerts = []
        
        # Analyze heart rate
        if heart_rate <= self.hr_alert_low or heart_rate >= self.hr_alert_high:
            alerts.append(f"CRITICAL HR: {heart_rate} BPM")
        elif heart_rate <= self.hr_caution_low or heart_rate >= self.hr_caution_high:
            alerts.append(f"CAUTION HR: {heart_rate} BPM")
        
        # Analyze temperature
        if temperature >= self.temp_alert_high or temperature <= self.temp_alert_low:
            alerts.append(f"CRITICAL TEMP: {temperature}°C")
        elif temperature >= self.temp_caution_high:
            alerts.append(f"CAUTION TEMP: {temperature}°C")
        
        # Analyze blood oxygen
        if blood_oxygen <= self.spo2_alert:
            alerts.append(f"CRITICAL SpO2: {blood_oxygen}%")
        elif blood_oxygen <= self.spo2_caution:
            alerts.append(f"CAUTION SpO2: {blood_oxygen}%")
        
        # Analyze respiratory rate
        if respiratory_rate < 10 or respiratory_rate > 30:
            alerts.append(f"ABNORMAL RR: {respiratory_rate} breaths/min")
        
        # Determine overall health status
        if len(alerts) >= 2:
            status = HealthStatus.CRITICAL
            message = " | ".join(alerts)
        elif any("CRITICAL" in alert for alert in alerts):
            status = HealthStatus.ALERT
            message = " | ".join(alerts)
        elif any("CAUTION" in alert for alert in alerts):
            status = HealthStatus.CAUTION
            message = " | ".join(alerts)
        else:
            status = HealthStatus.NORMAL
            message = f"All vital signs normal - HR: {heart_rate} BPM, Temp: {temperature}°C, SpO2: {blood_oxygen}%"
        
        # Record alert if needed
        if status != HealthStatus.NORMAL:
            self.alert_history.append({
                'timestamp': datetime.datetime.now().isoformat(),
                'status': status.value,
                'message': message,
                'hr': heart_rate,
                'temp': temperature,
                'spo2': blood_oxygen,
                'rr': respiratory_rate
            })
        
        return status, message


class DeviceMonitor:
    """Monitors wearable device status and battery level."""
    
    def __init__(self):
        self.battery_level = 100
        self.connection_status = "CONNECTED"
    
    def check_device_status(self) -> str:
        """
        Check device status and battery level.
        
        Returns:
            Device status string
        """
        # Simulate battery drain
        self.battery_level -= random.uniform(0.1, 0.3)
        
        if self.battery_level < 10:
            return "LOW_BATTERY"
        elif random.random() < 0.01:  # 1% chance of disconnection
            return "DISCONNECTED"
        else:
            return "ACTIVE"


class WearableHealthMonitoringSystem:
    """Main system controller for wearable health monitoring."""
    
    def __init__(self, patient_id: str = "PATIENT_001"):
        """
        Initialize the wearable health monitoring system.
        
        Args:
            patient_id: Unique patient identifier
        """
        self.patient_id = patient_id
        
        # Initialize sensors
        self.heart_rate_sensor = HeartRateSensor(baseline_hr=72)
        self.temperature_sensor = TemperatureSensor(baseline_temp=37.0)
        self.blood_oxygen_sensor = BloodOxygenSensor(baseline_spo2=98.0)
        self.respiratory_rate_sensor = RespiratoryRateSensor(baseline_rr=16)
        
        # Initialize analyzers
        self.health_analyzer = HealthAnalyzer()
        self.device_monitor = DeviceMonitor()
        
        # Data logging
        self.readings: List[VitalSignReading] = []
        self.normal_count = 0
        self.caution_count = 0
        self.alert_count = 0
        self.critical_count = 0
    
    def read_vital_signs(self) -> Tuple[int, float, float, int]:
        """
        Read all vital signs from sensors.
        
        Returns:
            Tuple of (heart_rate, temperature, blood_oxygen, respiratory_rate)
        """
        heart_rate = self.heart_rate_sensor.read_heart_rate()
        temperature = self.temperature_sensor.read_temperature()
        blood_oxygen = self.blood_oxygen_sensor.read_blood_oxygen()
        respiratory_rate = self.respiratory_rate_sensor.read_respiratory_rate()
        
        return heart_rate, temperature, blood_oxygen, respiratory_rate
    
    def simulate_cycle(self) -> VitalSignReading:
        """
        Simulate one complete monitoring cycle.
        
        Returns:
            VitalSignReading object
        """
        # Read vital signs
        heart_rate, temperature, blood_oxygen, respiratory_rate = self.read_vital_signs()
        
        # Analyze health status
        health_status, alert_message = self.health_analyzer.analyze_vital_signs(
            heart_rate, temperature, blood_oxygen, respiratory_rate
        )
        
        # Check device status
        device_status = self.device_monitor.check_device_status()
        
        # Update counters
        if health_status == HealthStatus.NORMAL:
            self.normal_count += 1
        elif health_status == HealthStatus.CAUTION:
            self.caution_count += 1
        elif health_status == HealthStatus.ALERT:
            self.alert_count += 1
        elif health_status == HealthStatus.CRITICAL:
            self.critical_count += 1
        
        # Create reading record
        reading = VitalSignReading(
            timestamp=datetime.datetime.now().isoformat(),
            heart_rate=heart_rate,
            body_temperature=temperature,
            blood_oxygen=blood_oxygen,
            respiratory_rate=respiratory_rate,
            health_status=health_status.value,
            alert_message=alert_message,
            device_status=device_status
        )
        
        self.readings.append(reading)
        return reading
    
    def run_simulation(self, num_cycles: int = 1000) -> List[VitalSignReading]:
        """
        Run the simulation for a specified number of cycles.
        
        Args:
            num_cycles: Number of monitoring cycles to simulate
            
        Returns:
            List of all vital sign readings
        """
        for _ in range(num_cycles):
            self.simulate_cycle()
        
        return self.readings
    
    def get_statistics(self) -> Dict:
        """
        Calculate statistics from collected readings.
        
        Returns:
            Dictionary containing various statistics
        """
        if not self.readings:
            return {}
        
        heart_rates = [r.heart_rate for r in self.readings]
        temperatures = [r.body_temperature for r in self.readings]
        blood_oxygens = [r.blood_oxygen for r in self.readings]
        respiratory_rates = [r.respiratory_rate for r in self.readings]
        
        return {
            'total_readings': len(self.readings),
            'total_cycles': len(self.readings),
            'patient_id': self.patient_id,
            'heart_rate': {
                'avg': round(statistics.mean(heart_rates), 2),
                'min': min(heart_rates),
                'max': max(heart_rates),
                'std': round(statistics.stdev(heart_rates), 2) if len(heart_rates) > 1 else 0
            },
            'temperature': {
                'avg': round(statistics.mean(temperatures), 2),
                'min': round(min(temperatures), 2),
                'max': round(max(temperatures), 2),
                'std': round(statistics.stdev(temperatures), 2) if len(temperatures) > 1 else 0
            },
            'blood_oxygen': {
                'avg': round(statistics.mean(blood_oxygens), 2),
                'min': round(min(blood_oxygens), 2),
                'max': round(max(blood_oxygens), 2),
                'std': round(statistics.stdev(blood_oxygens), 2) if len(blood_oxygens) > 1 else 0
            },
            'respiratory_rate': {
                'avg': round(statistics.mean(respiratory_rates), 2),
                'min': min(respiratory_rates),
                'max': max(respiratory_rates),
                'std': round(statistics.stdev(respiratory_rates), 2) if len(respiratory_rates) > 1 else 0
            },
            'health_status_distribution': {
                'normal': self.normal_count,
                'caution': self.caution_count,
                'alert': self.alert_count,
                'critical': self.critical_count
            },
            'alert_percentage': round(((self.caution_count + self.alert_count + self.critical_count) / len(self.readings)) * 100, 2)
        }
    
    def export_to_csv(self, filename: str):
        """Export readings to CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'heart_rate', 'body_temperature', 'blood_oxygen',
                         'respiratory_rate', 'health_status', 'alert_message', 'device_status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for reading in self.readings:
                writer.writerow(asdict(reading))
    
    def export_to_json(self, filename: str):
        """Export readings to JSON file."""
        data = {
            'patient_id': self.patient_id,
            'metadata': {
                'total_readings': len(self.readings),
                'total_cycles': len(self.readings),
                'monitoring_duration': 'Simulated continuous monitoring'
            },
            'statistics': self.get_statistics(),
            'alert_history': self.health_analyzer.alert_history,
            'readings': [asdict(r) for r in self.readings]
        }
        
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
    
    def export_alerts_to_csv(self, filename: str):
        """Export alert history to CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'status', 'message', 'hr', 'temp', 'spo2', 'rr']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for alert in self.health_analyzer.alert_history:
                writer.writerow(alert)


class HealthPerformanceAnalyzer:
    """Analyzes system performance and health metrics."""
    
    @staticmethod
    def calculate_monitoring_reliability(total_readings: int, alert_count: int) -> float:
        """
        Calculate monitoring reliability score.
        
        Returns:
            Reliability score (0-100)
        """
        if total_readings == 0:
            return 100.0
        reliability = max(0, 100 - (alert_count / total_readings) * 30)
        return round(reliability, 2)
    
    @staticmethod
    def calculate_vital_sign_stability(values: List[float]) -> float:
        """
        Calculate vital sign stability score.
        
        Returns:
            Stability score (0-100)
        """
        if len(values) < 2:
            return 100.0
        
        std_dev = statistics.stdev(values)
        stability = max(0, 100 - std_dev * 2)
        return round(stability, 2)
    
    @staticmethod
    def calculate_early_warning_effectiveness(caution_count: int, alert_count: int, critical_count: int) -> float:
        """
        Calculate early warning system effectiveness.
        
        Returns:
            Effectiveness score (0-100)
        """
        total_alerts = caution_count + alert_count + critical_count
        if total_alerts == 0:
            return 100.0
        
        # Effectiveness based on caution alerts caught before critical
        effectiveness = max(0, 100 - (critical_count / (total_alerts + 1)) * 40)
        return round(effectiveness, 2)


def main():
    """Main function to run the simulation."""
    print("=" * 80)
    print("WEARABLE IoT-BASED HEALTH MONITORING SYSTEM")
    print("Continuous Heart Rate, Body Temperature, and Health Status Tracking")
    print("=" * 80)
    print()
    
    # Initialize system
    system = WearableHealthMonitoringSystem(patient_id="PATIENT_001")
    
    print("Starting simulation with 1000 monitoring cycles...")
    print("(Continuous vital sign monitoring with real-time analysis)")
    print()
    
    # Run simulation
    readings = system.run_simulation(num_cycles=1000)
    
    # Get statistics
    stats = system.get_statistics()
    
    # Export data
    system.export_to_csv('/home/ubuntu/wearable_health_report/vital_signs_readings.csv')
    system.export_to_json('/home/ubuntu/wearable_health_report/vital_signs_readings.json')
    system.export_alerts_to_csv('/home/ubuntu/wearable_health_report/health_alerts_history.csv')
    
    # Display results
    print("SIMULATION RESULTS")
    print("-" * 80)
    print(f"Total Monitoring Cycles: {stats['total_cycles']}")
    print(f"Total Readings: {stats['total_readings']}")
    print()
    
    print("HEALTH STATUS DISTRIBUTION")
    print("-" * 80)
    dist = stats['health_status_distribution']
    print(f"Normal: {dist['normal']} ({(dist['normal']/stats['total_readings']*100):.1f}%)")
    print(f"Caution: {dist['caution']} ({(dist['caution']/stats['total_readings']*100):.1f}%)")
    print(f"Alert: {dist['alert']} ({(dist['alert']/stats['total_readings']*100):.1f}%)")
    print(f"Critical: {dist['critical']} ({(dist['critical']/stats['total_readings']*100):.1f}%)")
    print(f"Total Alert Events: {dist['caution'] + dist['alert'] + dist['critical']} ({stats['alert_percentage']}%)")
    print()
    
    print("HEART RATE STATISTICS (BPM)")
    print("-" * 80)
    hr = stats['heart_rate']
    print(f"Average: {hr['avg']} BPM")
    print(f"Range: {hr['min']} - {hr['max']} BPM")
    print(f"Standard Deviation: {hr['std']} BPM")
    print()
    
    print("BODY TEMPERATURE STATISTICS (°C)")
    print("-" * 80)
    temp = stats['temperature']
    print(f"Average: {temp['avg']}°C")
    print(f"Range: {temp['min']}°C - {temp['max']}°C")
    print(f"Standard Deviation: {temp['std']}°C")
    print()
    
    print("BLOOD OXYGEN SATURATION STATISTICS (%)")
    print("-" * 80)
    spo2 = stats['blood_oxygen']
    print(f"Average: {spo2['avg']}%")
    print(f"Range: {spo2['min']}% - {spo2['max']}%")
    print(f"Standard Deviation: {spo2['std']}%")
    print()
    
    print("RESPIRATORY RATE STATISTICS (breaths/min)")
    print("-" * 80)
    rr = stats['respiratory_rate']
    print(f"Average: {rr['avg']} breaths/min")
    print(f"Range: {rr['min']} - {rr['max']} breaths/min")
    print(f"Standard Deviation: {rr['std']} breaths/min")
    print()
    
    # Performance analysis
    analyzer = HealthPerformanceAnalyzer()
    all_hrs = [r.heart_rate for r in readings]
    all_temps = [r.body_temperature for r in readings]
    
    reliability = analyzer.calculate_monitoring_reliability(
        stats['total_readings'],
        dist['caution'] + dist['alert'] + dist['critical']
    )
    hr_stability = analyzer.calculate_vital_sign_stability(all_hrs)
    temp_stability = analyzer.calculate_vital_sign_stability(all_temps)
    warning_effectiveness = analyzer.calculate_early_warning_effectiveness(
        dist['caution'], dist['alert'], dist['critical']
    )
    
    print("SYSTEM PERFORMANCE METRICS")
    print("-" * 80)
    print(f"Monitoring Reliability Score: {reliability}/100")
    print(f"Heart Rate Stability Score: {hr_stability}/100")
    print(f"Temperature Stability Score: {temp_stability}/100")
    print(f"Early Warning Effectiveness: {warning_effectiveness}/100")
    print()
    
    print("Data exported to:")
    print("  - /home/ubuntu/wearable_health_report/vital_signs_readings.csv")
    print("  - /home/ubuntu/wearable_health_report/vital_signs_readings.json")
    print("  - /home/ubuntu/wearable_health_report/health_alerts_history.csv")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
