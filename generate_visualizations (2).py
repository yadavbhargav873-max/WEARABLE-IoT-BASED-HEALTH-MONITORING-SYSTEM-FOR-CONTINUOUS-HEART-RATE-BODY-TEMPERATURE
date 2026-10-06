"""
Generate visualizations for the Wearable Health Monitoring System report.
Creates professional charts showing vital signs and health monitoring data.
"""

import json
import csv
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict


def load_sensor_data(json_file: str) -> Dict:
    """Load sensor data from JSON file."""
    with open(json_file, 'r') as f:
        return json.load(f)


def load_csv_data(csv_file: str) -> List[Dict]:
    """Load sensor data from CSV file."""
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def create_heart_rate_trend_chart(csv_file: str, output_file: str):
    """Create heart rate trend chart."""
    data = load_csv_data(csv_file)
    
    heart_rates = [int(row['heart_rate']) for row in data]
    indices = list(range(len(heart_rates)))
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot heart rate
    ax.plot(indices, heart_rates, linewidth=2, color='#d62728', alpha=0.8, label='Heart Rate')
    
    # Add threshold lines
    ax.axhline(y=60, color='#2ca02c', linestyle='--', linewidth=2, label='Normal Low (60 BPM)', alpha=0.7)
    ax.axhline(y=100, color='#ff7f0e', linestyle='--', linewidth=2, label='Caution High (100 BPM)', alpha=0.7)
    ax.axhline(y=120, color='#d62728', linestyle='--', linewidth=2, label='Alert High (120 BPM)', alpha=0.7)
    
    # Shade normal zone
    ax.fill_between(indices, 60, 100, alpha=0.1, color='green', label='Normal Range')
    
    # Formatting
    ax.set_xlabel('Monitoring Cycle', fontsize=12, fontweight='bold')
    ax.set_ylabel('Heart Rate (BPM)', fontsize=12, fontweight='bold')
    ax.set_title('Heart Rate Monitoring Over Time', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='best', fontsize=10)
    ax.set_ylim(40, 160)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_temperature_chart(csv_file: str, output_file: str):
    """Create body temperature trend chart."""
    data = load_csv_data(csv_file)
    
    temperatures = [float(row['body_temperature']) for row in data]
    indices = list(range(len(temperatures)))
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot temperature
    ax.plot(indices, temperatures, linewidth=2, color='#1f77b4', alpha=0.8, label='Body Temperature')
    
    # Add threshold lines
    ax.axhline(y=36.5, color='#2ca02c', linestyle='--', linewidth=2, label='Normal Low (36.5°C)', alpha=0.7)
    ax.axhline(y=37.5, color='#2ca02c', linestyle='--', linewidth=2, label='Normal High (37.5°C)', alpha=0.7)
    ax.axhline(y=38.5, color='#ff7f0e', linestyle='--', linewidth=2, label='Caution (38.5°C)', alpha=0.7)
    ax.axhline(y=39.5, color='#d62728', linestyle='--', linewidth=2, label='Alert (39.5°C)', alpha=0.7)
    
    # Shade normal zone
    ax.fill_between(indices, 36.5, 37.5, alpha=0.1, color='green', label='Normal Range')
    
    # Formatting
    ax.set_xlabel('Monitoring Cycle', fontsize=12, fontweight='bold')
    ax.set_ylabel('Body Temperature (°C)', fontsize=12, fontweight='bold')
    ax.set_title('Body Temperature Monitoring Over Time', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='best', fontsize=10)
    ax.set_ylim(34, 41)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_blood_oxygen_chart(csv_file: str, output_file: str):
    """Create blood oxygen saturation chart."""
    data = load_csv_data(csv_file)
    
    spo2_values = [float(row['blood_oxygen']) for row in data]
    indices = list(range(len(spo2_values)))
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Plot SpO2
    ax.plot(indices, spo2_values, linewidth=2, color='#2ca02c', alpha=0.8, label='Blood Oxygen (SpO2)')
    
    # Add threshold lines
    ax.axhline(y=95, color='#2ca02c', linestyle='--', linewidth=2, label='Normal (95%)', alpha=0.7)
    ax.axhline(y=93, color='#ff7f0e', linestyle='--', linewidth=2, label='Caution (93%)', alpha=0.7)
    ax.axhline(y=90, color='#d62728', linestyle='--', linewidth=2, label='Alert (90%)', alpha=0.7)
    
    # Shade normal zone
    ax.fill_between(indices, 95, 100, alpha=0.1, color='green', label='Normal Range')
    
    # Formatting
    ax.set_xlabel('Monitoring Cycle', fontsize=12, fontweight='bold')
    ax.set_ylabel('Blood Oxygen Saturation (%)', fontsize=12, fontweight='bold')
    ax.set_title('Blood Oxygen Saturation (SpO2) Monitoring', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='best', fontsize=10)
    ax.set_ylim(88, 101)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_health_status_distribution_chart(json_file: str, output_file: str):
    """Create health status distribution chart."""
    data = load_sensor_data(json_file)
    stats = data['statistics']
    dist = stats['health_status_distribution']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Health Status Distribution and System Performance', fontsize=14, fontweight='bold')
    
    # Health status pie chart
    status_data = [dist['normal'], dist['caution'], dist['alert'], dist['critical']]
    status_labels = [f'Normal\n({dist["normal"]})', f'Caution\n({dist["caution"]})', 
                    f'Alert\n({dist["alert"]})', f'Critical\n({dist["critical"]})']
    colors_pie = ['#2ca02c', '#ff7f0e', '#d62728', '#9467bd']
    
    ax1.pie(status_data, labels=status_labels, colors=colors_pie, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 10, 'fontweight': 'bold'})
    ax1.set_title('Health Status Distribution', fontsize=12, fontweight='bold')
    
    # Performance metrics bar chart
    metrics = ['Reliability', 'HR Stability', 'Temp Stability', 'Warning Effectiveness']
    scores = [82.9, 47.48, 98.83, 97.2]
    colors_bar = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    bars = ax2.bar(metrics, scores, color=colors_bar, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Score', fontsize=11, fontweight='bold')
    ax2.set_ylim(0, 100)
    ax2.grid(True, alpha=0.3, axis='y', linestyle=':')
    ax2.set_title('System Performance Metrics', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='x', labelsize=9)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_vital_signs_distribution_chart(csv_file: str, output_file: str):
    """Create vital signs distribution histograms."""
    data = load_csv_data(csv_file)
    
    heart_rates = [int(row['heart_rate']) for row in data]
    temperatures = [float(row['body_temperature']) for row in data]
    spo2_values = [float(row['blood_oxygen']) for row in data]
    rr_values = [int(row['respiratory_rate']) for row in data]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Vital Signs Distribution Analysis', fontsize=14, fontweight='bold')
    
    # Heart rate histogram
    axes[0, 0].hist(heart_rates, bins=30, color='#d62728', alpha=0.7, edgecolor='black')
    axes[0, 0].axvline(np.mean(heart_rates), color='darkred', linestyle='--', linewidth=2,
                      label=f'Mean: {np.mean(heart_rates):.1f} BPM')
    axes[0, 0].set_xlabel('Heart Rate (BPM)', fontsize=10, fontweight='bold')
    axes[0, 0].set_ylabel('Frequency', fontsize=10, fontweight='bold')
    axes[0, 0].set_title('Heart Rate Distribution', fontsize=11, fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3, axis='y', linestyle=':')
    
    # Temperature histogram
    axes[0, 1].hist(temperatures, bins=30, color='#1f77b4', alpha=0.7, edgecolor='black')
    axes[0, 1].axvline(np.mean(temperatures), color='darkblue', linestyle='--', linewidth=2,
                      label=f'Mean: {np.mean(temperatures):.2f}°C')
    axes[0, 1].set_xlabel('Body Temperature (°C)', fontsize=10, fontweight='bold')
    axes[0, 1].set_ylabel('Frequency', fontsize=10, fontweight='bold')
    axes[0, 1].set_title('Temperature Distribution', fontsize=11, fontweight='bold')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3, axis='y', linestyle=':')
    
    # SpO2 histogram
    axes[1, 0].hist(spo2_values, bins=20, color='#2ca02c', alpha=0.7, edgecolor='black')
    axes[1, 0].axvline(np.mean(spo2_values), color='darkgreen', linestyle='--', linewidth=2,
                      label=f'Mean: {np.mean(spo2_values):.2f}%')
    axes[1, 0].set_xlabel('Blood Oxygen (%)', fontsize=10, fontweight='bold')
    axes[1, 0].set_ylabel('Frequency', fontsize=10, fontweight='bold')
    axes[1, 0].set_title('Blood Oxygen Distribution', fontsize=11, fontweight='bold')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3, axis='y', linestyle=':')
    
    # Respiratory rate histogram
    axes[1, 1].hist(rr_values, bins=15, color='#ff7f0e', alpha=0.7, edgecolor='black')
    axes[1, 1].axvline(np.mean(rr_values), color='darkorange', linestyle='--', linewidth=2,
                      label=f'Mean: {np.mean(rr_values):.1f} breaths/min')
    axes[1, 1].set_xlabel('Respiratory Rate (breaths/min)', fontsize=10, fontweight='bold')
    axes[1, 1].set_ylabel('Frequency', fontsize=10, fontweight='bold')
    axes[1, 1].set_title('Respiratory Rate Distribution', fontsize=11, fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3, axis='y', linestyle=':')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_alert_timeline_chart(csv_file: str, output_file: str):
    """Create alert timeline visualization."""
    data = load_csv_data(csv_file)
    
    caution_indices = []
    alert_indices = []
    critical_indices = []
    
    for idx, row in enumerate(data):
        status = row['health_status']
        if status == 'CRITICAL':
            critical_indices.append(idx)
        elif status == 'ALERT':
            alert_indices.append(idx)
        elif status == 'CAUTION':
            caution_indices.append(idx)
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Plot alert occurrences
    if critical_indices:
        ax.scatter(critical_indices, [3]*len(critical_indices), color='#9467bd', s=150, 
                  alpha=0.7, label=f'Critical ({len(critical_indices)})', marker='*')
    if alert_indices:
        ax.scatter(alert_indices, [2]*len(alert_indices), color='#d62728', s=100, 
                  alpha=0.6, label=f'Alert ({len(alert_indices)})', marker='X')
    if caution_indices:
        ax.scatter(caution_indices, [1]*len(caution_indices), color='#ff7f0e', s=80, 
                  alpha=0.6, label=f'Caution ({len(caution_indices)})', marker='o')
    
    # Formatting
    ax.set_xlabel('Monitoring Cycle', fontsize=12, fontweight='bold')
    ax.set_ylabel('Alert Type', fontsize=12, fontweight='bold')
    ax.set_title('Health Alert Timeline Throughout Monitoring Period', fontsize=14, fontweight='bold', pad=20)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['Caution', 'Alert', 'Critical'])
    ax.set_ylim(0.5, 3.5)
    ax.grid(True, alpha=0.3, linestyle=':', axis='x')
    ax.legend(loc='best', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def create_comprehensive_dashboard(json_file: str, output_file: str):
    """Create comprehensive health monitoring dashboard."""
    data = load_sensor_data(json_file)
    stats = data['statistics']
    dist = stats['health_status_distribution']
    
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(4, 3, hspace=0.4, wspace=0.3)
    
    fig.suptitle('Wearable Health Monitoring System - Comprehensive Dashboard', 
                fontsize=16, fontweight='bold', y=0.98)
    
    # 1. Heart Rate Statistics
    ax1 = fig.add_subplot(gs[0, 0])
    hr_data = [stats['heart_rate']['min'], stats['heart_rate']['avg'], stats['heart_rate']['max']]
    hr_labels = ['Min', 'Avg', 'Max']
    colors1 = ['#1f77b4', '#2ca02c', '#d62728']
    bars1 = ax1.bar(hr_labels, hr_data, color=colors1, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('BPM', fontsize=10, fontweight='bold')
    ax1.set_title('Heart Rate Statistics', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y', linestyle=':')
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 2. Temperature Statistics
    ax2 = fig.add_subplot(gs[0, 1])
    temp_data = [stats['temperature']['min'], stats['temperature']['avg'], stats['temperature']['max']]
    temp_labels = ['Min', 'Avg', 'Max']
    colors2 = ['#1f77b4', '#2ca02c', '#d62728']
    bars2 = ax2.bar(temp_labels, temp_data, color=colors2, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('°C', fontsize=10, fontweight='bold')
    ax2.set_title('Temperature Statistics', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y', linestyle=':')
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 3. Blood Oxygen Statistics
    ax3 = fig.add_subplot(gs[0, 2])
    spo2_data = [stats['blood_oxygen']['min'], stats['blood_oxygen']['avg'], stats['blood_oxygen']['max']]
    spo2_labels = ['Min', 'Avg', 'Max']
    colors3 = ['#1f77b4', '#2ca02c', '#d62728']
    bars3 = ax3.bar(spo2_labels, spo2_data, color=colors3, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax3.set_ylabel('%', fontsize=10, fontweight='bold')
    ax3.set_title('Blood Oxygen Statistics', fontsize=11, fontweight='bold')
    ax3.set_ylim(90, 100)
    ax3.grid(True, alpha=0.3, axis='y', linestyle=':')
    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 4. Health Status Distribution
    ax4 = fig.add_subplot(gs[1, :2])
    status_data = [dist['normal'], dist['caution'], dist['alert'], dist['critical']]
    status_labels = ['Normal', 'Caution', 'Alert', 'Critical']
    colors_status = ['#2ca02c', '#ff7f0e', '#d62728', '#9467bd']
    bars4 = ax4.bar(status_labels, status_data, color=colors_status, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax4.set_ylabel('Count', fontsize=10, fontweight='bold')
    ax4.set_title('Health Status Distribution', fontsize=11, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y', linestyle=':')
    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # 5. Alert Percentage
    ax5 = fig.add_subplot(gs[1, 2])
    alert_pct = stats['alert_percentage']
    normal_pct = 100 - alert_pct
    pie_data = [normal_pct, alert_pct]
    pie_labels = [f'Normal\n({normal_pct:.1f}%)', f'Alert Events\n({alert_pct:.1f}%)']
    colors_pie = ['#2ca02c', '#d62728']
    ax5.pie(pie_data, labels=pie_labels, colors=colors_pie, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 9, 'fontweight': 'bold'})
    ax5.set_title('Alert Event Percentage', fontsize=11, fontweight='bold')
    
    # 6-9. Summary metrics
    ax_summary = fig.add_subplot(gs[2:, :])
    ax_summary.axis('off')
    
    summary_text = f"""
VITAL SIGNS SUMMARY

Total Monitoring Cycles: {stats['total_cycles']}
Total Readings: {stats['total_readings']}
Patient ID: {stats['patient_id']}

HEART RATE ANALYSIS:
  • Average: {stats['heart_rate']['avg']} BPM  |  Range: {stats['heart_rate']['min']} - {stats['heart_rate']['max']} BPM
  • Standard Deviation: {stats['heart_rate']['std']} BPM  |  Stability Score: 47.48/100

BODY TEMPERATURE ANALYSIS:
  • Average: {stats['temperature']['avg']}°C  |  Range: {stats['temperature']['min']}°C - {stats['temperature']['max']}°C
  • Standard Deviation: {stats['temperature']['std']}°C  |  Stability Score: 98.83/100

BLOOD OXYGEN SATURATION (SpO2) ANALYSIS:
  • Average: {stats['blood_oxygen']['avg']}%  |  Range: {stats['blood_oxygen']['min']}% - {stats['blood_oxygen']['max']}%
  • Standard Deviation: {stats['blood_oxygen']['std']}%

RESPIRATORY RATE ANALYSIS:
  • Average: {stats['respiratory_rate']['avg']} breaths/min  |  Range: {stats['respiratory_rate']['min']} - {stats['respiratory_rate']['max']} breaths/min
  • Standard Deviation: {stats['respiratory_rate']['std']} breaths/min

HEALTH STATUS DISTRIBUTION:
  • Normal: {dist['normal']} ({(dist['normal']/stats['total_readings']*100):.1f}%)  |  Caution: {dist['caution']} ({(dist['caution']/stats['total_readings']*100):.1f}%)
  • Alert: {dist['alert']} ({(dist['alert']/stats['total_readings']*100):.1f}%)  |  Critical: {dist['critical']} ({(dist['critical']/stats['total_readings']*100):.1f}%)
  • Total Alert Events: {dist['caution'] + dist['alert'] + dist['critical']} ({stats['alert_percentage']}%)

SYSTEM PERFORMANCE:
  • Monitoring Reliability Score: 82.9/100  |  Early Warning Effectiveness: 97.2/100
  • Device Status: ACTIVE  |  Data Integrity: 100%  |  Alert Response: Real-time
    """
    
    ax_summary.text(0.05, 0.95, summary_text, transform=ax_summary.transAxes,
                   fontsize=9, verticalalignment='top', fontfamily='monospace',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Saved: {output_file}")


def main():
    """Generate all visualizations."""
    print("\n" + "="*80)
    print("GENERATING VISUALIZATIONS FOR WEARABLE HEALTH MONITORING SYSTEM REPORT")
    print("="*80 + "\n")
    
    base_path = '/home/ubuntu/wearable_health_report'
    csv_file = f'{base_path}/vital_signs_readings.csv'
    json_file = f'{base_path}/vital_signs_readings.json'
    
    print("Creating visualizations...\n")
    
    # Generate all charts
    create_heart_rate_trend_chart(csv_file, f'{base_path}/chart_01_heart_rate_trend.png')
    create_temperature_chart(csv_file, f'{base_path}/chart_02_temperature_trend.png')
    create_blood_oxygen_chart(csv_file, f'{base_path}/chart_03_blood_oxygen_trend.png')
    create_health_status_distribution_chart(json_file, f'{base_path}/chart_04_health_status_distribution.png')
    create_vital_signs_distribution_chart(csv_file, f'{base_path}/chart_05_vital_signs_distribution.png')
    create_alert_timeline_chart(csv_file, f'{base_path}/chart_06_alert_timeline.png')
    create_comprehensive_dashboard(json_file, f'{base_path}/chart_07_comprehensive_dashboard.png')
    
    print("\n" + "="*80)
    print("All visualizations generated successfully!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
